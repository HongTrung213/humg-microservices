import requests
import json
from django.http import HttpResponse
from django.views import View
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from users.permissions import IsAdmin, IsTeacher, IsStudent
import os

class ProxyView(View):
    service_map = {
        'students': os.getenv('STUDENT_SERVICE_URL', 'http://localhost:8001/api/'),
        'exams': os.getenv('EXAM_SERVICE_URL', 'http://localhost:8003/api/'),
        'certificates': os.getenv('CERTIFICATE_SERVICE_URL', 'http://localhost:8004/api/'),  # ✅ SỬA
        'training': os.getenv('TRAINING_SERVICE_URL', 'http://localhost:8002/api/'),         # ✅ SỬA (8002)
        'notifications': os.getenv('NOTIFICATION_SERVICE_URL', 'http://localhost:8005/api/'),
        'cms': os.getenv('CMS_SERVICE_URL', 'http://localhost:8006/api/'),
        'reports': os.getenv('REPORT_SERVICE_URL', 'http://localhost:8007/api/'),
    }

    def _authenticate_request(self, request):
        """Xác thực JWT token từ header Authorization"""
        auth = JWTAuthentication()
        try:
            user, token = auth.authenticate(request)
            if user is not None:
                request.user = user
                return True
        except (InvalidToken, TokenError):
            pass
        return False

    def _check_permission(self, request, service):
        if not request.user.is_authenticated:
            return False, "Authentication required"

        # Admin có toàn quyền
        if IsAdmin().has_permission(request, self):
            return True, None

        # Teacher được truy cập students, exams, training, reports
        if service in ['students', 'exams', 'training', 'reports']:
            if IsTeacher().has_permission(request, self):
                return True, None
            # 🟢 CHO PHÉP SINH VIÊN (chỉ GET)
            if IsStudent().has_permission(request, self) and request.method == 'GET':
                return True, None
            return False, "Permission denied"

        if service in ['certificates', 'notifications', 'cms']:
            return False, "Admin only for this service"

        return False, "Access denied"

    def dispatch(self, request, service, path):
        # Xác thực JWT
        if not self._authenticate_request(request):
            return HttpResponse(
                json.dumps({'error': 'Authentication required'}),
                status=401,
                content_type='application/json'
            )

        # Kiểm tra quyền
        allowed, error_msg = self._check_permission(request, service)
        if not allowed:
            return HttpResponse(
                json.dumps({'error': error_msg}),
                status=403,
                content_type='application/json'
            )

        # Tiếp tục proxy
        target_url = self.service_map.get(service)
        if not target_url:
            return HttpResponse(json.dumps({'error': 'Service not found'}), status=404, content_type='application/json')

        full_url = f"{target_url}{path}"
        if request.GET:
            full_url += '?' + request.GET.urlencode()

        method = request.method.lower()
        headers = {k: v for k, v in request.headers.items() if k.lower() != 'host'}
        
        # Chuyển token (nếu có)
        auth_header = request.headers.get('Authorization')
        if auth_header:
            headers['Authorization'] = auth_header

        data = request.body if request.body else None

        try:
            if method == 'get':
                resp = requests.get(full_url, headers=headers)
            elif method == 'post':
                resp = requests.post(full_url, headers=headers, data=data)
            elif method == 'put':
                resp = requests.put(full_url, headers=headers, data=data)
            elif method == 'patch':
                resp = requests.patch(full_url, headers=headers, data=data)
            elif method == 'delete':
                resp = requests.delete(full_url, headers=headers)
            else:
                return HttpResponse(json.dumps({'error': 'Method not allowed'}), status=405, content_type='application/json')

            return HttpResponse(resp.content, status=resp.status_code, content_type=resp.headers.get('Content-Type', 'application/json'))
        except requests.exceptions.ConnectionError:
            return HttpResponse(json.dumps({'error': 'Service unavailable'}), status=503, content_type='application/json')