import requests
import json
from django.http import HttpResponse
from django.views import View
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from users.permissions import IsAdmin, IsTeacher, IsStudent
import os


class ProxyView(View):
    service_map = {
        'students':      os.getenv('STUDENT_SERVICE_URL',      'http://localhost:8001/api/'),
        'exams':         os.getenv('EXAM_SERVICE_URL',         'http://localhost:8003/api/'),
        'certificates':  os.getenv('CERTIFICATE_SERVICE_URL',  'http://localhost:8004/api/'),
        'training':      os.getenv('TRAINING_SERVICE_URL',     'http://localhost:8002/api/'),
        'notifications': os.getenv('NOTIFICATION_SERVICE_URL', 'http://localhost:8005/api/'),
        'cms':           os.getenv('CMS_SERVICE_URL',          'http://localhost:8006/api/'),
        'reports':       os.getenv('REPORT_SERVICE_URL',       'http://localhost:8007/api/'),
    }

    def _authenticate_request(self, request):
        """Xác thực JWT (từ header) HOẶC session cookie (fallback)."""
        auth = JWTAuthentication()

        # 1. Thử JWT từ Authorization header
        try:
            result = auth.authenticate(request)
            if result is not None:
                user, token = result
                request.user = user
                request.jwt_token = str(token)
                return True
        except (InvalidToken, TokenError):
            pass

        # 2. Fallback: Django session
        if hasattr(request, 'user') and request.user.is_authenticated:
            token = request.session.get('access_token')
            if not token:
                # Không có JWT trong session → tạo mới từ user
                try:
                    refresh = RefreshToken.for_user(request.user)
                    token = str(refresh.access_token)
                    request.session['access_token'] = token
                except Exception:
                    return False
            request.jwt_token = token
            return True

        return False

    def _check_permission(self, request, service):
        if not request.user.is_authenticated:
            return False, "Authentication required"

        # Admin có toàn quyền
        if IsAdmin().has_permission(request, self):
            return True, None

        # Teacher: students, exams, training, reports
        if service in ['students', 'exams', 'training', 'reports']:
            if IsTeacher().has_permission(request, self):
                return True, None
            # Student: chỉ GET
            if IsStudent().has_permission(request, self) and request.method == 'GET':
                return True, None
            return False, "Permission denied"

        # Certificates / notifications / cms: chỉ admin ghi, các role khác đọc
        if service in ['certificates', 'notifications', 'cms']:
            if IsAdmin().has_permission(request, self):
                return True, None
            if IsTeacher().has_permission(request, self) or IsStudent().has_permission(request, self):
                if request.method == 'GET':
                    return True, None
            return False, "Admin only for write on this service"

        return False, "Access denied"

    def dispatch(self, request, service, path):
        # 1. Xác thực
        if not self._authenticate_request(request):
            return HttpResponse(
                json.dumps({'error': 'Authentication required'}),
                status=401,
                content_type='application/json'
            )

        # 2. Kiểm tra quyền
        allowed, error_msg = self._check_permission(request, service)
        if not allowed:
            return HttpResponse(
                json.dumps({'error': error_msg}),
                status=403,
                content_type='application/json'
            )

        # 3. Tìm upstream
        target_url = self.service_map.get(service)
        if not target_url:
            return HttpResponse(
                json.dumps({'error': f'Service not found: {service}'}),
                status=404,
                content_type='application/json'
            )

        full_url = f"{target_url}{path}"
        if request.GET:
            full_url += '?' + request.GET.urlencode()

        method = request.method.lower()

        # 4. Build headers — KHÔNG forward Cookie, Host, Authorization cũ
        skip_headers = {'host', 'cookie', 'authorization', 'content-length'}
        headers = {k: v for k, v in request.headers.items() if k.lower() not in skip_headers}

        # Inject JWT vào Authorization
        if getattr(request, 'jwt_token', None):
            headers['Authorization'] = f'Bearer {request.jwt_token}'

        # Body
        data = request.body if request.body else None

        # 5. Gọi upstream
        try:
            if method == 'get':
                resp = requests.get(full_url, headers=headers, timeout=30)
            elif method == 'post':
                resp = requests.post(full_url, headers=headers, data=data, timeout=30)
            elif method == 'put':
                resp = requests.put(full_url, headers=headers, data=data, timeout=30)
            elif method == 'patch':
                resp = requests.patch(full_url, headers=headers, data=data, timeout=30)
            elif method == 'delete':
                resp = requests.delete(full_url, headers=headers, timeout=30)
            else:
                return HttpResponse(
                    json.dumps({'error': 'Method not allowed'}),
                    status=405,
                    content_type='application/json'
                )

            return HttpResponse(
                resp.content,
                status=resp.status_code,
                content_type=resp.headers.get('Content-Type', 'application/json')
            )

        except requests.exceptions.Timeout:
            return HttpResponse(
                json.dumps({'error': 'Upstream timeout'}),
                status=504,
                content_type='application/json'
            )
        except requests.exceptions.ConnectionError:
            return HttpResponse(
                json.dumps({'error': 'Service unavailable'}),
                status=503,
                content_type='application/json'
            )