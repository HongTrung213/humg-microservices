# -*- coding: utf-8 -*-
import os
import time
import logging
import requests
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout, login as auth_login
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
import base64
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from django.views.decorators.http import require_POST

from functools import wraps

logger = logging.getLogger('gateway')
from django.core.exceptions import PermissionDenied


def admin_required(view_func):
    """Chỉ cho phép user có profile.role == 'admin'."""
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("students:dang_nhap")
        profile = getattr(request.user, "profile", None)
        if not profile or profile.role != "admin":
            raise PermissionDenied("Chỉ admin được truy cập")
        return view_func(request, *args, **kwargs)
    return _wrapped


def teacher_required(view_func):
    """Cho phép admin hoặc teacher."""
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("students:dang_nhap")
        profile = getattr(request.user, "profile", None)
        if not profile or profile.role not in ("admin", "teacher"):
            raise PermissionDenied("Chỉ admin/giảng viên được truy cập")
        return view_func(request, *args, **kwargs)
    return _wrapped


# ----- CẤU HÌNH SERVICE URLs (DÙNG BIẾN MÔI TRƯỜNG) -----
STUDENT_SERVICE = os.getenv('STUDENT_SERVICE_URL', 'http://127.0.0.1:8001/api/')
EXAM_SERVICE = os.getenv('EXAM_SERVICE_URL', 'http://127.0.0.1:8003/api/')
CERT_SERVICE = os.getenv('CERTIFICATE_SERVICE_URL', 'http://127.0.0.1:8004/api/')
TRAINING_SERVICE = os.getenv('TRAINING_SERVICE_URL', 'http://127.0.0.1:8002/api/')
NOTIFICATION_SERVICE = os.getenv('NOTIFICATION_SERVICE_URL', 'http://127.0.0.1:8005/api/')
CMS_SERVICE = os.getenv('CMS_SERVICE_URL', 'http://127.0.0.1:8006/api/')
REPORT_SERVICE = os.getenv('REPORT_SERVICE_URL', 'http://127.0.0.1:8007/api/')

# ===== PERFORMANCE HELPERS (parallel + cache) =====
from concurrent.futures import ThreadPoolExecutor, as_completed as _as_completed
from django.core.cache import cache as _cache

def _cached_get_json(url, ttl=60, timeout=8):
    """GET API + cache trong ttl giay."""
    key = f"api_cache:{url}"
    val = _cache.get(key)
    if val is not None:
        return val
    try:
        r = requests.get(url, timeout=timeout)
        val = r.json() if r.status_code == 200 else None
    except Exception:
        val = None
    _cache.set(key, val, ttl)
    return val


def parallel_get_json(urls, ttl=60, timeout=8):
    """GET nhieu URL song song + cache. Return {url: data}."""
    results = {}
    to_fetch = []
    for url in urls:
        key = f"api_cache:{url}"
        cached = _cache.get(key)
        if cached is not None:
            results[url] = cached
        else:
            to_fetch.append(url)
    if to_fetch:
        with ThreadPoolExecutor(max_workers=min(8, len(to_fetch))) as ex:
            futures = {ex.submit(requests.get, u, timeout=timeout): u for u in to_fetch}
            for fu in _as_completed(futures):
                u = futures[fu]
                try:
                    r = fu.result()
                    data = r.json() if r.status_code == 200 else None
                except Exception:
                    data = None
                _cache.set(f"api_cache:{u}", data, ttl)
                results[u] = data
    return results


def parallel_api_get(request, urls, ttl=60, timeout=8):
    """Parallel API GET co JWT auth (cho admin views). Return {url: data}."""
    results = {}
    to_fetch = []
    for url in urls:
        key = f"api_cache:{url}"
        cached = _cache.get(key)
        if cached is not None:
            results[url] = cached
        else:
            to_fetch.append(url)

    def _fetch(url_list, headers):
        status = {}
        with ThreadPoolExecutor(max_workers=min(8, len(url_list))) as ex:
            futures = {ex.submit(requests.get, u, headers=headers, timeout=timeout): u for u in url_list}
            for fu in _as_completed(futures):
                u = futures[fu]
                try:
                    r = fu.result()
                    status[u] = r.status_code
                    data = r.json() if r.status_code == 200 else None
                except Exception:
                    status[u] = None
                    data = None
                if data is not None:          # không cache lỗi -> lần sau gọi lại được ngay
                    _cache.set(f"api_cache:{u}", data, ttl)
                results[u] = data
        return [u for u, st in status.items() if st == 401]

    if to_fetch:
        bi_tu_choi = _fetch(to_fetch, _auth_headers(request))
        if bi_tu_choi and request.user.is_authenticated:
            bi_tu_choi = _fetch(bi_tu_choi, _auth_headers(request, force=True))
        if bi_tu_choi:
            logger.warning('Service từ chối JWT cho %d URL – kiểm tra JWT_SIGNING_KEY.', len(bi_tu_choi))
            _fetch(bi_tu_choi, {})
    return results

# ===== END PERFORMANCE HELPERS =====




# ----- HÀM GỌI API CHUNG -----
def _jwt_payload(token):
    try:
        part = token.split('.')[1]
        return json.loads(base64.urlsafe_b64decode(part + '=' * (-len(part) % 4)))
    except Exception:
        return {}


def get_access_token(request, force=False):
    """
    Token JWT hợp lệ cho người dùng đang đăng nhập.
    Tự cấp lại khi thiếu, sắp hết hạn (< 60 giây), không khớp người dùng hoặc khi force=True.
    Khách chưa đăng nhập -> None (không gửi token cũ, tránh bị service trả 401).
    """
    user = getattr(request, 'user', None)
    if not (user and user.is_authenticated):
        return None
    token = request.session.get('access_token')
    payload = _jwt_payload(token) if token else {}
    het_han = payload.get('exp', 0) - 60 < time.time()
    sai_user = str(payload.get('user_id')) != str(user.pk)
    if force or not token or het_han or sai_user:
        try:
            from rest_framework_simplejwt.tokens import RefreshToken
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)
            request.session['access_token'] = token
            request.session['refresh_token'] = str(refresh)
            request.session['token_obtained_at'] = datetime.now().isoformat()
        except Exception as exc:
            logger.warning('Không cấp được JWT cho %s: %s', user, exc)
    return token


def _auth_headers(request, force=False):
    token = get_access_token(request, force=force)
    return {'Authorization': f'Bearer {token}'} if token else {}


def _rewind_files(files):
    for value in (files or {}).values():
        obj = value[1] if isinstance(value, (tuple, list)) and len(value) > 1 else value
        if hasattr(obj, 'seek'):
            try:
                obj.seek(0)
            except Exception:
                pass


def call_api(request, method, url, data=None, files=None, params=None):
    """Gọi API service kèm JWT của phiên đăng nhập.
    Token hết hạn/không hợp lệ (401) -> cấp token mới và gọi lại 1 lần;
    GET vẫn bị 401 (các service khác JWT_SIGNING_KEY) -> gọi lại không kèm token để vẫn đọc được dữ liệu công khai."""
    method = method.upper()

    def _send(headers):
        headers = dict(headers)
        if method == 'GET':
            return requests.get(url, headers=headers, params=params, timeout=10)
        if method == 'DELETE':
            return requests.delete(url, headers=headers, timeout=10)
        fn = {'POST': requests.post, 'PUT': requests.put, 'PATCH': requests.patch}.get(method)
        if fn is None:
            return None
        if files:
            _rewind_files(files)
            return fn(url, headers=headers, data=data, files=files, timeout=300)
        headers['Content-Type'] = 'application/json'
        return fn(url, headers=headers, json=data, timeout=10)

    try:
        resp = _send(_auth_headers(request))
        if resp is not None and resp.status_code == 401 and request.user.is_authenticated:
            resp = _send(_auth_headers(request, force=True))
            if resp is not None and resp.status_code == 401:
                logger.warning('Service từ chối JWT (%s). Kiểm tra JWT_SIGNING_KEY giống nhau ở mọi service.', url)
                if method == 'GET':
                    resp = _send({})
        return resp
    except requests.exceptions.RequestException:
        return None


# ================================================================
# VIEWS CHO ADMIN (namespace: admin_mofi)
# ================================================================

def _as_list_of(data, sinh_vien_id=None):
    """Chuẩn hoá dữ liệu API thành list; nếu có sinh_vien_id thì CHỈ giữ bản ghi của sinh viên đó.
    Lớp bảo vệ thêm ở gateway: không để sinh viên thấy dữ liệu của người khác
    kể cả khi service phía sau bỏ qua tham số lọc."""
    if isinstance(data, dict):
        data = data.get('results', [])
    if not isinstance(data, list):
        return []
    if sinh_vien_id is None:
        return data
    return [x for x in data if str(x.get('sinh_vien_id')) == str(sinh_vien_id)]


# ----- ĐĂNG KÝ LỚP: chuẩn hoá dữ liệu từ training-service để hiển thị -----
TRANG_THAI_DANG_KY = {
    'PENDING': ('Chờ duyệt', 'warning'),
    'DA_DUYET': ('Đã duyệt', 'success'),
    'APPROVED': ('Đã duyệt', 'success'),
    'TU_CHOI': ('Từ chối', 'danger'),
    'REJECTED': ('Từ chối', 'danger'),
}


def _enrich_registrations(request, registrations, lops=None):
    """Gắn tên sinh viên, tên lớp, nhãn trạng thái cho danh sách DangKyLop (API chỉ trả id)."""
    registrations = registrations or []
    if not registrations:
        return []
    urls = [STUDENT_SERVICE + 'sinhvien/']
    if lops is None:
        urls.append(TRAINING_SERVICE + 'lop/')
    res = parallel_api_get(request, urls, ttl=120)

    def _lst(data):
        if isinstance(data, dict):
            data = data.get('results', [])
        return data if isinstance(data, list) else []

    sv_map = {sv.get('id'): sv for sv in _lst(res.get(urls[0]))}
    if lops is None:
        lops = _lst(res.get(urls[1]))
    lop_map = {l.get('id'): l for l in lops}

    out = []
    for dk in registrations:
        sv = sv_map.get(dk.get('sinh_vien_id')) or {}
        lop = lop_map.get(dk.get('lop')) or {}
        label, tone = TRANG_THAI_DANG_KY.get(dk.get('trang_thai'), (dk.get('trang_thai') or '-', 'secondary'))
        out.append({
            'id': dk.get('id'),
            'sinh_vien': {
                'ho_ten': sv.get('ho_ten') or f"SV #{dk.get('sinh_vien_id', '')}",
                'ma_sv': sv.get('ma_sv', ''),
            },
            'lop_hoc': {'id': dk.get('lop'), 'ten_lop': lop.get('ten_lop') or f"Lớp #{dk.get('lop', '')}",
                        'ma_lop': lop.get('ma_lop', '')},
            'hanh_dong': 'Đăng ký lớp',
            'thoi_gian': dk.get('ngay_dang_ky'),
            'thoi_gian_dk': dk.get('ngay_dang_ky'),
            'trang_thai': dk.get('trang_thai'),
            'trang_thai_label': label,
            'trang_thai_tone': tone,
        })
    return out


# ----- DASHBOARD -----
@admin_required
def admin_mofi_dashboard(request):
    """Admin dashboard - parallel + cache."""
    urls = [
        REPORT_SERVICE + 'dashboard/',
        REPORT_SERVICE + 'chua-dat-chuan/?loai=all&limit=10',
        REPORT_SERVICE + 'thong-ke-theo-khoa/',
        TRAINING_SERVICE + 'dangky/',
        TRAINING_SERVICE + 'lop/',
        CERT_SERVICE + 'chungchi/',
        EXAM_SERVICE + 'dotthi/',
    ]
    res = parallel_api_get(request, urls, ttl=60)

    def _as_list(data):
        if isinstance(data, dict):
            data = data.get('results', [])
        return data if isinstance(data, list) else []

    dash_data = res.get(urls[0]) or {}
    total_students = dash_data.get('tong_sinh_vien', 0) if isinstance(dash_data, dict) else 0

    canh_bao_data = res.get(urls[1]) or {}
    if isinstance(canh_bao_data, dict):
        top_canh_bao = canh_bao_data.get('results', [])[:10]
        so_luong_canh_bao = canh_bao_data.get('count', 0)
    else:
        top_canh_bao = []
        so_luong_canh_bao = 0

    thong_ke_khoa = res.get(urls[2]) or []
    if not isinstance(thong_ke_khoa, list):
        thong_ke_khoa = []

    chart_data = {'labels': [], 'cdr_nn': {'da_dat': [], 'chua_dat': []}, 'cdr_th': {'da_dat': [], 'chua_dat': []}}
    chart_data['labels'] = [item.get('ten_khoa', '') for item in thong_ke_khoa]
    chart_data['cdr_nn']['da_dat']   = [item.get('dat_ngoai_ngu', 0) for item in thong_ke_khoa]
    chart_data['cdr_nn']['chua_dat'] = [item.get('tong_sv', 0) - item.get('dat_ngoai_ngu', 0) for item in thong_ke_khoa]
    chart_data['cdr_th']['da_dat']   = [item.get('dat_tin_hoc', 0) for item in thong_ke_khoa]
    chart_data['cdr_th']['chua_dat'] = [item.get('tong_sv', 0) - item.get('dat_tin_hoc', 0) for item in thong_ke_khoa]

    # --- Đăng ký lớp / lớp / chứng chỉ: số liệu thật thay cho số 0 cố định ---
    dang_ky = _as_list(res.get(urls[3]))
    lops = _as_list(res.get(urls[4]))
    chung_chi = _as_list(res.get(urls[5]))

    active_classes = sum(1 for l in lops if str(l.get('trang_thai', '')).upper() in ('OPEN', 'MO', 'DANG_MO'))
    pending = [dk for dk in dang_ky if dk.get('trang_thai') == 'PENDING']

    dang_ky_sorted = sorted(dang_ky, key=lambda dk: dk.get('ngay_dang_ky') or '', reverse=True)
    recent = dang_ky_sorted[:10]
    pending_recent = [dk for dk in dang_ky_sorted if dk.get('trang_thai') == 'PENDING'][:5]

    recent_activities = _enrich_registrations(request, recent, lops)
    pending_registrations_list = _enrich_registrations(request, pending_recent, lops)

    # --- Đợt thi: chia "Sắp diễn ra" / "Gần đây" như khối Sự kiện của humg.edu.vn ---
    today_iso = datetime.now().date().isoformat()
    dot_sap_toi, dot_gan_day, dot_dang_dien_ra = [], [], []
    for d in _as_list(res.get(urls[6])):
        start = (d.get('ngay_bat_dau') or '')[:10]
        end = (d.get('ngay_ket_thuc') or start)[:10]
        d['loai_display'] = LOAI_DOT_NGAN.get(d.get('loai'), d.get('loai') or '')
        d['ngay'] = start[8:10] if len(start) == 10 else '--'
        d['thang'] = str(int(start[5:7])) if len(start) == 10 else ''
        if start and start <= today_iso <= end:
            d['trang_thai_label'], d['trang_thai_tone'] = 'Đang diễn ra', 'success'
            dot_dang_dien_ra.append(d)
            dot_sap_toi.append(d)
        elif start and start > today_iso:
            d['trang_thai_label'], d['trang_thai_tone'] = 'Sắp diễn ra', 'warning'
            dot_sap_toi.append(d)
        else:
            d['trang_thai_label'], d['trang_thai_tone'] = 'Đã kết thúc', 'secondary'
            dot_gan_day.append(d)
    dot_sap_toi.sort(key=lambda d: d.get('ngay_bat_dau') or '')
    dot_gan_day.sort(key=lambda d: d.get('ngay_bat_dau') or '', reverse=True)

    tong_khoa = len(thong_ke_khoa)
    tong_dat = sum(int(k.get('dat_chuan_dau_ra') or 0) for k in thong_ke_khoa)
    tong_sv_khoa = sum(int(k.get('tong_sv') or 0) for k in thong_ke_khoa)
    ti_le_dat_chung = round(tong_dat * 100 / tong_sv_khoa, 1) if tong_sv_khoa else 0

    context = {
        'total_students': total_students,
        'active_classes': active_classes,
        'pending_registrations': len(pending),
        'certificates_issued': len(chung_chi),
        'top_canh_bao': top_canh_bao,
        'so_luong_canh_bao': so_luong_canh_bao,
        'recent_activities': recent_activities,
        'pending_registrations_list': pending_registrations_list,
        'thong_ke_khoa': thong_ke_khoa,
        'chart_data': chart_data,
        'dot_sap_toi': dot_sap_toi[:5],
        'dot_gan_day': dot_gan_day[:5],
        'so_dot_sap_toi': len(dot_sap_toi),
        'so_dot_gan_day': len(dot_gan_day),
        'dot_dang_dien_ra': dot_dang_dien_ra,
        'tong_khoa': tong_khoa,
        'ti_le_dat_chung': ti_le_dat_chung,
        'tong_dat_cdr': tong_dat,
    }
    return render(request, 'admin/admin_dashboard.html', context)


@admin_required
def report_dashboard(request):
    """Trang báo cáo thống kê chi tiết"""
    import json as _json
    khoa_filter = request.GET.get('khoa', '')
    khoa_tsv_filter = request.GET.get('khoa_tsv', '')
    report_type = request.GET.get('report_type', 'tong_quan')

    # 1. Dashboard stats tu report-service
    dashboard_data = {}
    resp = call_api(request, 'GET', REPORT_SERVICE + 'dashboard/')
    if resp and resp.status_code == 200:
        dashboard_data = resp.json() or {}

    tong_sinh_vien = dashboard_data.get('tong_sinh_vien', 0)
    dat_ngoai_ngu = dashboard_data.get('dat_ngoai_ngu', 0)
    dat_tin_hoc = dashboard_data.get('dat_tin_hoc', 0)
    dat_chuan_dau_ra = dashboard_data.get('dat_chuan_dau_ra', 0)
    ti_le_dat_cdr = dashboard_data.get('ti_le_dat_cdr', 0)
    chua_dat_cdr = tong_sinh_vien - dat_chuan_dau_ra

    # 2. Students
    students = []
    resp = call_api(request, 'GET', STUDENT_SERVICE + 'sinhvien/')
    if resp and resp.status_code == 200:
        raw = resp.json()
        if isinstance(raw, dict):
            raw = raw.get('results', [])
        students = raw or []

    co_email = 0; khong_email = 0; co_nganh = 0; khong_nganh = 0
    for sv in students:
        if sv.get('email_truong') or sv.get('email_ca_nhan'):
            co_email += 1
        else:
            khong_email += 1
        if sv.get('nganh_info') or sv.get('nganh'):
            co_nganh += 1
        else:
            khong_nganh += 1

    # 3. Thong ke theo khoa (transform sang fields template can)
    theo_khoa_raw = []
    resp = call_api(request, 'GET', REPORT_SERVICE + 'thong-ke-theo-khoa/')
    if resp and resp.status_code == 200:
        theo_khoa_raw = resp.json() or []
        if isinstance(theo_khoa_raw, dict):
            theo_khoa_raw = theo_khoa_raw.get('results', [])

    thong_ke_khoa = []
    for x in theo_khoa_raw:
        thong_ke_khoa.append({
            'ten_khoa': x.get('ten_khoa', ''),
            'tong_sv': x.get('tong_sv', 0),
            'da_dat_nn': x.get('dat_ngoai_ngu', 0),
            'da_dat_th': x.get('dat_tin_hoc', 0),
            'da_dat_ca_2': x.get('dat_chuan_dau_ra', 0),
            'ty_le': x.get('ti_le_dat_cdr', 0),
        })

    # 4. Theo nganh
    nganh_count = {}
    for sv in students:
        nganh = sv.get('nganh_info') or sv.get('nganh') or {}
        ten_nganh = nganh.get('ten_nganh', 'Chưa xác định') if isinstance(nganh, dict) else 'Chưa xác định'
        nganh_count[ten_nganh] = nganh_count.get(ten_nganh, 0) + 1
    theo_nganh = [{'nganh_dao_tao__ten_nganh': k, 'total': v} for k, v in nganh_count.items()]
    theo_nganh.sort(key=lambda x: x['total'], reverse=True)

    # 5. Khoa tuyen sinh
    khoa_ts_count = {}
    for sv in students:
        khoa_ts = sv.get('khoa_hoc', 'Không xác định')
        khoa_ts_count[khoa_ts] = khoa_ts_count.get(khoa_ts, 0) + 1
    theo_khoa_tuyen_sinh = [{'khoa_tuyen_sinh': k, 'total': v} for k, v in khoa_ts_count.items()]

    # 6. DS khoa cho filter dropdown
    ds_khoa = []
    resp_k = call_api(request, 'GET', STUDENT_SERVICE + 'khoa/')
    if resp_k and resp_k.status_code == 200:
        ds_khoa = resp_k.json() or []
        if isinstance(ds_khoa, dict):
            ds_khoa = ds_khoa.get('results', [])

    # 7. Chart JSON
    cdr_nganh_chart = None
    if theo_nganh:
        cdr_nganh_chart = {
            'labels': [str(x.get('nganh_dao_tao__ten_nganh', ''))[:25] for x in theo_nganh[:10]],
            'values': [x.get('total', 0) for x in theo_nganh[:10]]
        }

    tien_do_khoa_chart = None
    if thong_ke_khoa:
        tien_do_khoa_chart = {
            'labels': [str(x.get('ten_khoa', ''))[:20] for x in thong_ke_khoa[:15]],
            'values': [x.get('ty_le', 0) for x in thong_ke_khoa[:15]]
        }

    so_sanh_khoa_chart = None
    if thong_ke_khoa:
        so_sanh_khoa_chart = {
            'labels': [str(x.get('ten_khoa', ''))[:20] for x in thong_ke_khoa[:15]],
            'nn': [x.get('da_dat_nn', 0) for x in thong_ke_khoa[:15]],
            'th': [x.get('da_dat_th', 0) for x in thong_ke_khoa[:15]]
        }

    context = {
        'pham_vi_vai_tro': 'Toàn hệ thống',
        'khoa_filter': khoa_filter,
        'khoa_tsv_filter': khoa_tsv_filter,
        'report_type': report_type,
        'tong_sinh_vien': tong_sinh_vien,
        'dat_ngoai_ngu': dat_ngoai_ngu,
        'dat_tin_hoc': dat_tin_hoc,
        'dat_chuan_dau_ra': dat_chuan_dau_ra,
        'da_dat_cdr': dat_chuan_dau_ra,
        'chua_dat_cdr': chua_dat_cdr,
        'ti_le_dat_cdr': ti_le_dat_cdr,
        'ty_le_tot_nghiep': ti_le_dat_cdr,
        'co_email': co_email,
        'khong_email': khong_email,
        'co_nganh': co_nganh,
        'khong_nganh': khong_nganh,
        'theo_khoa': theo_khoa_raw,
        'thong_ke_khoa': thong_ke_khoa,
        'ds_khoa': ds_khoa,
        'theo_nganh': theo_nganh,
        'theo_khoa_tuyen_sinh': theo_khoa_tuyen_sinh,
        'theo_khoa_va_khoa': [],
        'top_sinh_vien': [],
        'recent_activities': [],
        'cdr_nganh_data': _json.dumps(cdr_nganh_chart) if cdr_nganh_chart else 'null',
        'ket_qua_dot_thi_data': 'null',
        'tien_do_khoa_data': _json.dumps(tien_do_khoa_chart) if tien_do_khoa_chart else 'null',
        'so_sanh_khoa_data': _json.dumps(so_sanh_khoa_chart) if so_sanh_khoa_chart else 'null',
    }
    return render(request, 'admin/reports/report_dashboard.html', context)

@admin_required
def khoa_list(request):
    resp = call_api(request, 'GET', STUDENT_SERVICE + 'khoa/')
    khoas = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin/system/khoa_list.html', {'danh_sach_khoa': khoas})

@admin_required
def khoa_create(request):
    if request.method == 'POST':
        data = {
            'ma_khoa': request.POST.get('ma_khoa'),
            'ten_khoa': request.POST.get('ten_khoa'),
        }
        resp = call_api(request, 'POST', STUDENT_SERVICE + 'khoa/', data=data)
        if resp and resp.status_code == 201:
            messages.success(request, 'Thêm khoa thành công!')
            return redirect('khoa_list')
        else:
            messages.error(request, 'Thêm khoa thất bại!')
    return render(request, 'admin/system/khoa_form.html', {'instance': None})

@admin_required
def khoa_edit(request, pk):
    if request.method == 'POST':
        data = {
            'ma_khoa': request.POST.get('ma_khoa'),
            'ten_khoa': request.POST.get('ten_khoa'),
        }
        resp = call_api(request, 'PUT', STUDENT_SERVICE + f'khoa/{pk}/', data=data)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật khoa thành công!')
            return redirect('khoa_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', STUDENT_SERVICE + f'khoa/{pk}/')
    khoa = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin/system/khoa_form.html', {'instance': khoa})

@admin_required
def khoa_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', STUDENT_SERVICE + f'khoa/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa khoa thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('khoa_list')


# ----- QUẢN LÝ NGÀNH ĐÀO TẠO -----
@admin_required
def nganh_list(request):
    resp = call_api(request, 'GET', STUDENT_SERVICE + 'nganh/')
    ds_nganh = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin/system/nganh_list.html', {'ds_nganh': ds_nganh})

@admin_required
def nganh_create(request):
    khoa_resp = call_api(request, 'GET', STUDENT_SERVICE + 'khoa/')
    khoas = khoa_resp.json() if khoa_resp and khoa_resp.status_code == 200 else []
    if request.method == 'POST':
        data = {
            'ma_nganh': request.POST.get('ma_nganh'),
            'ten_nganh': request.POST.get('ten_nganh'),
            'khoa': request.POST.get('khoa') or None,
            'khoa_id': request.POST.get('khoa') or None,
            'loai_nganh': request.POST.get('loai_nganh') or 'THUONG',
            'thoi_gian_dao_tao_nam': request.POST.get('thoi_gian_dao_tao_nam') or 4,
            'is_active': request.POST.get('is_active') == 'on',
        }
        resp = call_api(request, 'POST', STUDENT_SERVICE + 'nganh/', data=data)
        if resp and resp.status_code == 201:
            messages.success(request, 'Thêm ngành thành công!')
            return redirect('nganh_list')
        else:
            messages.error(request, 'Thêm ngành thất bại!')
    return render(request, 'admin/system/nganh_form.html', {'instance': None, 'khoas': khoas})

@admin_required
def nganh_edit(request, pk):
    khoa_resp = call_api(request, 'GET', STUDENT_SERVICE + 'khoa/')
    khoas = khoa_resp.json() if khoa_resp and khoa_resp.status_code == 200 else []
    if request.method == 'POST':
        data = {
            'ma_nganh': request.POST.get('ma_nganh'),
            'ten_nganh': request.POST.get('ten_nganh'),
            'khoa': request.POST.get('khoa') or None,
            'khoa_id': request.POST.get('khoa') or None,
            'loai_nganh': request.POST.get('loai_nganh') or 'THUONG',
            'thoi_gian_dao_tao_nam': request.POST.get('thoi_gian_dao_tao_nam') or 4,
            'is_active': request.POST.get('is_active') == 'on',
        }
        resp = call_api(request, 'PUT', STUDENT_SERVICE + f'nganh/{pk}/', data=data)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật ngành thành công!')
            return redirect('nganh_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', STUDENT_SERVICE + f'nganh/{pk}/')
    nganh = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin/system/nganh_form.html', {'instance': nganh, 'khoas': khoas})

@admin_required
def nganh_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', STUDENT_SERVICE + f'nganh/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa ngành thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('nganh_list')


# ----- QUẢN LÝ DANH MỤC CHỨNG CHỈ -----
@admin_required
def chungchi_list(request):
    resp = call_api(request, 'GET', CERT_SERVICE + 'danhmuc/')
    danh_sach = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin/certificates/chungchi_list.html', {'danh_sach': danh_sach})

@admin_required
def chungchi_create(request):
    if request.method == 'POST':
        # Khớp model DanhMucChungChi của certificate-service
        data = {
            'ma_danh_muc': (request.POST.get('ma_danh_muc') or '').strip(),
            'ten_danh_muc': (request.POST.get('ten_danh_muc') or '').strip(),
            'loai': request.POST.get('loai') or 'NGOAI_NGU',
            'bac': request.POST.get('bac') or 1,
        }
        resp = call_api(request, 'POST', CERT_SERVICE + 'danhmuc/', data=data)
        if resp and resp.status_code == 201:
            messages.success(request, 'Thêm danh mục chứng chỉ thành công!')
            return redirect('chungchi_list')
        else:
            messages.error(request, 'Thêm thất bại!')
    return render(request, 'admin/certificates/chungchi_form.html', {'instance': None})

@admin_required
def chungchi_edit(request, pk):
    if request.method == 'POST':
        # Khớp model DanhMucChungChi của certificate-service
        data = {
            'ma_danh_muc': (request.POST.get('ma_danh_muc') or '').strip(),
            'ten_danh_muc': (request.POST.get('ten_danh_muc') or '').strip(),
            'loai': request.POST.get('loai') or 'NGOAI_NGU',
            'bac': request.POST.get('bac') or 1,
        }
        resp = call_api(request, 'PUT', CERT_SERVICE + f'danhmuc/{pk}/', data=data)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật thành công!')
            return redirect('chungchi_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', CERT_SERVICE + f'danhmuc/{pk}/')
    instance = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin/certificates/chungchi_form.html', {'instance': instance})

@admin_required
def chungchi_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', CERT_SERVICE + f'danhmuc/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('chungchi_list')


# ----- TIÊU CHÍ CĐR -----
@admin_required
def tieu_chi_list(request):
    resp = call_api(request, 'GET', STUDENT_SERVICE + 'tieu-chi/')
    tieu_chi_list = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin/system/tieu_chi_list.html', {'tieu_chi_list': tieu_chi_list, 'tong': len(tieu_chi_list)})


# ----- QUẢN LÝ ĐỢT THI -----
@admin_required
def dot_thi_list(request):
    resp = call_api(request, 'GET', EXAM_SERVICE + 'dotthi/')
    dot_this = resp.json() if resp is not None and resp.status_code == 200 else []
    if isinstance(dot_this, dict):
        dot_this = dot_this.get('results', [])
    for dt in dot_this:
        _gan_trang_thai_dot(dt)
    dot_this.sort(key=lambda d: (d.get('ngay_bat_dau') or '', d.get('id') or 0), reverse=True)

    mon = request.GET.get('mon') or ''
    dem = {k: sum(1 for d in dot_this if d['loai'] == k) for k in LOAI_DOT}
    if mon in LOAI_DOT:
        dot_this = [d for d in dot_this if d['loai'] == mon]

    nam = _nam_hoc_hien_tai()
    return render(request, 'admin/exams/dot_thi_list.html', {
        'dot_this': dot_this,
        'loai_choices': list(LOAI_DOT.items()),
        'loai_ma': LOAI_DOT_MA,
        'mon_loc': mon,
        'dem_theo_mon': [(k, LOAI_DOT_NGAN[k], dem[k]) for k in LOAI_DOT],
        'tong_dot': sum(dem.values()),
        'today': datetime.now().date().isoformat(),
        'nam_hoc_choices': [f'{y}-{y + 1}' for y in range(nam - 2, nam + 2)],
        'nam_hoc_mac_dinh': f'{nam}-{nam + 1}',
        'mo_form': request.GET.get('tao') == '1',
        'dot_so_choices': list(enumerate(['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'], start=1)),
    })


@admin_required
def dot_thi_create(request):
    """Tạo đợt thi cho MỘT môn: mã đợt, tên đợt, môn thi, ngày bắt đầu, ngày kết thúc."""
    if request.method != 'POST':
        return redirect('dot_thi_list')
    loai = request.POST.get('loai') or ''
    ma_dot = (request.POST.get('ma_dot') or '').strip().upper()
    ten_dot = (request.POST.get('ten_dot') or '').strip()
    today = datetime.now().date().isoformat()
    ngay_bd = request.POST.get('ngay_bat_dau') or today
    ngay_kt = request.POST.get('ngay_ket_thuc') or ngay_bd

    loi = []
    if loai not in LOAI_DOT:
        loi.append('Chọn môn thi')
    if not ma_dot:
        loi.append('Nhập mã đợt')
    if not ten_dot:
        loi.append('Nhập tên đợt')
    if ngay_kt < ngay_bd:
        loi.append('Ngày kết thúc phải sau hoặc bằng ngày bắt đầu')
    if loi:
        messages.error(request, 'Chưa tạo được đợt thi: ' + '; '.join(loi) + '.')
        return redirect(f"{reverse('dot_thi_list')}?tao=1")

    data = {
        'ma_dot': ma_dot[:20],
        'ten_dot': ten_dot[:200],
        'loai': loai,
        'ngay_bat_dau': ngay_bd,
        'ngay_ket_thuc': ngay_kt,
        # Điểm đạt cố định theo quy định (TĐNN 50, CĐR NN 90, CĐR Tin học 50) – lưu kèm để tham chiếu
        'diem_chuan_ngoai_ngu': DIEM_DAT['TA_DAU_VAO'] if loai == 'TDNN' else DIEM_DAT['CDR_NGOAI_NGU'],
        'diem_liet_ngoai_ngu': 0,
        'diem_chuan_tin_hoc': DIEM_DAT['CDR_TIN_HOC'],
        'diem_liet_tin_hoc': 0,
    }
    resp = call_api(request, 'POST', EXAM_SERVICE + 'dotthi/', data=data)
    if resp is not None and resp.status_code == 201:
        dot = resp.json()
        messages.success(request, f"Đã tạo đợt “{ten_dot}” ({LOAI_DOT[loai]}). Bước tiếp theo: import file Excel lịch thi.")
        return redirect('dot_thi_detail', pk=dot.get('id'))
    try:
        body = resp.json() if resp is not None else {}
    except ValueError:
        body = {}
    if isinstance(body, dict) and body.get('ma_dot'):
        messages.error(request, f'Mã đợt “{ma_dot}” đã tồn tại, vui lòng chọn mã khác.')
    else:
        messages.error(request, 'Tạo đợt thi thất bại! Kiểm tra mã đợt (không trùng) và ngày thi.')
    return redirect(f"{reverse('dot_thi_list')}?tao=1")


@admin_required
def dot_thi_detail(request, pk):
    resp = call_api(request, 'GET', EXAM_SERVICE + f'dotthi/{pk}/')
    dot_thi = resp.json() if resp is not None and resp.status_code == 200 else None
    if not dot_thi:
        messages.error(request, 'Không tìm thấy đợt thi!')
        return redirect('dot_thi_list')
    _gan_trang_thai_dot(dot_thi)

    resp_lich = call_api(request, 'GET', EXAM_SERVICE + f'lichsuthi/?dot_thi_id={pk}')
    lich_su = resp_lich.json() if resp_lich is not None and resp_lich.status_code == 200 else []
    if isinstance(lich_su, dict):
        lich_su = lich_su.get('results', [])
    # Chỉ giữ thí sinh của ĐÚNG đợt này (không lẫn sinh viên của đợt khác)
    lich_su = [l for l in lich_su if str(l.get('dot_thi')) == str(pk)]

    # Gắn MSSV / họ tên (API chỉ trả sinh_vien_id)
    sv_res = parallel_api_get(request, [STUDENT_SERVICE + 'sinhvien/'], ttl=120)
    sv_list = sv_res.get(STUDENT_SERVICE + 'sinhvien/') or []
    if isinstance(sv_list, dict):
        sv_list = sv_list.get('results', [])
    sv_map = {sv.get('id'): sv for sv in sv_list}
    if any(l.get('sinh_vien_id') not in sv_map for l in lich_su):
        # Danh sách SV trong cache đã cũ (vd. vừa tự thêm SV khi import) -> lấy lại
        _cache.delete(f"api_cache:{STUDENT_SERVICE}sinhvien/")
        sv_res = parallel_api_get(request, [STUDENT_SERVICE + 'sinhvien/'], ttl=120)
        sv_list = sv_res.get(STUDENT_SERVICE + 'sinhvien/') or []
        if isinstance(sv_list, dict):
            sv_list = sv_list.get('results', [])
        sv_map = {sv.get('id'): sv for sv in sv_list}
    for l in lich_su:
        sv = sv_map.get(l.get('sinh_vien_id')) or {}
        l['ma_sv'] = sv.get('ma_sv', '')
        l['ho_ten'] = sv.get('ho_ten') or f"SV #{l.get('sinh_vien_id', '')}"
        l['co_lich'] = bool(l.get('ngay_thi') or l.get('phong_thi') or l.get('ngay_thi_2'))
        l['co_diem'] = l.get('diem_tong') is not None or bool(l.get('xep_loai'))

    thong_ke = {
        'tong': len(lich_su),
        'co_lich': sum(1 for l in lich_su if l['co_lich']),
        'co_diem': sum(1 for l in lich_su if l['co_diem']),
        'dat': sum(1 for l in lich_su if l.get('ket_qua_dat')),
        'phong': len({l.get('phong_thi') for l in lich_su if l.get('phong_thi')}),
    }

    q = (request.GET.get('q') or '').strip().lower()
    phong = request.GET.get('phong') or ''
    if q:
        lich_su = [l for l in lich_su if q in l['ma_sv'].lower() or q in l['ho_ten'].lower()
                   or q in str(l.get('sbd') or '').lower() or q in str(l.get('phong_thi') or '').lower()]
    if phong:
        lich_su = [l for l in lich_su if (l.get('phong_thi') or '') == phong]

    sort = request.GET.get('sort') or 'ten'
    if sort == 'phong':
        lich_su.sort(key=lambda l: (str(l.get('ngay_thi') or ''), str(l.get('ca_thi') or ''), str(l.get('phong_thi') or ''), l['ho_ten'].split()[-1:] if l['ho_ten'] else ''))
    elif sort == 'mssv':
        lich_su.sort(key=lambda l: l['ma_sv'])
    else:
        lich_su.sort(key=lambda l: (l['ho_ten'].split()[-1:] if l['ho_ten'] else [''], l['ho_ten']))

    page = Paginator(lich_su, 25).get_page(request.GET.get('p', 1))
    from urllib.parse import urlencode as _urlencode
    qs_params = {k: v for k, v in (('q', request.GET.get('q', '')), ('phong', phong), ('sort', sort)) if v}
    qs = ('&' + _urlencode(qs_params)) if qs_params else ''
    phong_list = sorted({l.get('phong_thi') for l in lich_su if l.get('phong_thi')} | ({phong} if phong else set()))
    return render(request, 'admin/exams/dot_thi_detail.html', {
        'dot_thi': dot_thi,
        'mon_thi': LOAI_SANG_MON.get(dot_thi['loai']),
        'page': page,
        'thong_ke': thong_ke,
        'phong_list': phong_list,
        'phong': phong,
        'tong_luot_thi': thong_ke['tong'],
        'search_query': request.GET.get('q', ''),
        'sort_by': sort,
        'qs': qs,
        'diem_dat': DIEM_DAT.get(LOAI_SANG_MON.get(dot_thi['loai']), 50),
    })


# ----- IMPORT DỮ LIỆU (Excel) -----
@admin_required
def import_excel_student(request):
    if request.method == 'POST':
        # Form gửi trường "file" (bản cũ dùng "excel_file") -> nhận cả hai
        file = request.FILES.get('excel_file') or request.FILES.get('file')
        if not file:
            messages.error(request, 'Vui lòng chọn file!')
            return redirect('import_excel_student')
        if not file.name.lower().endswith(('.xlsx', '.xls')):
            messages.error(request, 'File phải có định dạng .xlsx hoặc .xls')
            return redirect('import_excel_student')
        files = {'file': (file.name, file.read(), file.content_type or 'application/octet-stream')}
        payload = {'sheet_name': request.POST.get('sheet_name', '').strip()} if request.POST.get('sheet_name', '').strip() else None
        resp = call_api(request, 'POST', STUDENT_SERVICE + 'import-students/', data=payload, files=files)
        try:
            data = resp.json() if resp is not None else {}
        except ValueError:
            data = {}
        if resp is not None and resp.status_code == 200:
            messages.success(request, f"Import xong: {data.get('created', 0)} sinh viên mới, {data.get('updated', 0)} cập nhật.")
            errs = data.get('errors') or []
            if errs:
                messages.warning(request, f"{len(errs)} dòng bị bỏ qua, ví dụ: " + '; '.join(errs[:3]))
        elif resp is None:
            messages.error(request, 'Không kết nối được Student Service hoặc quá thời gian xử lý.')
        else:
            messages.error(request, f"Import thất bại: {data.get('error') or data.get('detail') or resp.status_code}")
        return redirect('student_list')
    return render(request, 'admin/students/import_excel.html')

# Điểm đạt (thang 100) – khớp exams.models.DIEM_DAT của exam-service
DIEM_DAT = {'TA_DAU_VAO': 50, 'CDR_NGOAI_NGU': 90, 'CDR_TIN_HOC': 50}
DIEM_DAT_LOAI = {'tdnn': 50, 'cdr_nn': 90, 'cntt': 50}


@admin_required
@require_POST
def dot_thi_tinh_lai(request, pk):
    """Tính lại Đạt/Chưa đạt của cả đợt theo điểm đạt hiện hành."""
    resp = call_api(request, 'POST', EXAM_SERVICE + f'dotthi/{pk}/tinh-lai-ket-qua/')
    try:
        body = resp.json() if resp is not None else {}
    except ValueError:
        body = {}
    if resp is not None and resp.status_code == 200:
        messages.success(request, f"Đã tính lại {body.get('tong', 0)} kết quả ({body.get('thay_doi', 0)} thay đổi) theo điểm đạt TĐNN 50 · CĐR NN 90 · CĐR Tin học 50.")
    else:
        messages.error(request, 'Không tính lại được kết quả của đợt thi.')
    return redirect('dot_thi_detail', pk=pk)


# Mỗi đợt thi là MỘT môn -> cấu hình import theo (loại đợt, lịch thi/kết quả)
LOAI_DOT = {
    'CDR_TH': 'Chuẩn đầu ra Công nghệ thông tin',
    'CDR_NN': 'Chuẩn đầu ra Ngoại ngữ',
    'TDNN': 'Trình độ ngoại ngữ',
}
LOAI_DOT_NGAN = {'CDR_TH': 'CĐR CNTT', 'CDR_NN': 'CĐR Ngoại ngữ', 'TDNN': 'TĐNN', 'TIN_CHI': 'TĐNN'}
LOAI_DOT_TONE = {'CDR_TH': 'info', 'CDR_NN': 'primary', 'TDNN': 'warning', 'TIN_CHI': 'warning'}
LOAI_DOT_MA = {'CDR_TH': 'CNTT', 'CDR_NN': 'CDRNN', 'TDNN': 'TDNN'}
LOAI_SANG_MON = {'CDR_TH': 'CDR_TIN_HOC', 'CDR_NN': 'CDR_NGOAI_NGU', 'TDNN': 'TA_DAU_VAO', 'TIN_CHI': 'TA_DAU_VAO'}
MON_THI_LABEL = {
    'CDR_TIN_HOC': 'Chuẩn đầu ra Công nghệ thông tin',
    'CDR_NGOAI_NGU': 'Chuẩn đầu ra Ngoại ngữ',
    'TA_DAU_VAO': 'Trình độ ngoại ngữ',
}

_COT_LICH = {
    'CDR_TH': (['Mã sinh viên', 'Họ đệm + Tên', 'Ngày thi', 'Ca', 'Thời gian', 'Phòng thi'],
               ['Ghi chú/Đợt BL', 'Phần bảo lưu',
                'Thi thử trực tuyến: Tên phòng thi trên Microsoft Teams, Ngày thi thử, Thời gian đăng nhập (thiết bị 1, 2)']),
    'CDR_NN': (['MSV / Mã sinh viên', 'Họ đệm + Tên', 'NGÀY KT', 'CA KT', 'PHÒNG THI'],
               ['Lịch thi vấn đáp (NGÀY KT / CA KT / Phòng tập trung)', 'Đợt bảo lưu', 'Phần bảo lưu',
                'Thi thử trực tuyến: Ngày thi thử, Phòng thi thử, Thời gian đăng nhập Ms TEAMS / SEB']),
    'TDNN': (['MSV / Mã sinh viên', 'Họ đệm + Tên', 'NGÀY KT', 'CA KT', 'PHÒNG THI'],
             ['Lịch thi vấn đáp (NGÀY KT / CA KT / Phòng tập trung)', 'Ghi chú']),
}
_COT_DIEM = {
    'CDR_TH': (['Mã sinh viên', 'Họ và tên', 'Trắc nghiệm', 'Thực hành', 'Điểm đánh giá'], ['Xếp loại', 'Ghi chú', 'Bảo lưu']),
    'CDR_NN': (['Mã sinh viên', 'Họ và tên', 'Nghe', 'Đọc', 'Viết', 'Nói', 'Điểm đánh giá'], ['Xếp loại', 'Ghi chú', 'Bảo lưu']),
    'TDNN': (['Mã sinh viên', 'Họ và tên', 'Nghe', 'Đọc', 'Viết', 'Nói', 'Điểm đánh giá'], ['Xếp loại', 'Ghi chú', 'Khóa']),
}
_LOAI_DIEM = {'CDR_TH': 'cntt', 'CDR_NN': 'cdr_nn', 'TDNN': 'tdnn', 'TIN_CHI': 'tdnn'}


def _loai_dot(dot):
    loai = (dot or {}).get('loai') or ''
    return 'TDNN' if loai == 'TIN_CHI' else loai


def _import_cfg(dot, kind):
    loai = _loai_dot(dot)
    if loai not in LOAI_DOT:
        return None
    cot = (_COT_LICH if kind == 'lich' else _COT_DIEM)[loai]
    return {
        'kind': kind,
        'title': ('Import lịch thi' if kind == 'lich' else 'Import kết quả thi'),
        'mon': LOAI_DOT[loai],
        'mon_ngan': LOAI_DOT_NGAN[loai],
        'endpoint': 'import-exam-schedule/' if kind == 'lich' else 'import-exam-scores/',
        'params': {'mon_thi': LOAI_SANG_MON[loai]} if kind == 'lich' else {'loai': _LOAI_DIEM[loai]},
        'columns': cot[0],
        'optional': cot[1],
    }


def _gan_trang_thai_dot(dot):
    """Bổ sung nhãn môn thi / trạng thái thời gian cho một đợt thi (dict từ exam-service)."""
    today = datetime.now().date().isoformat()
    loai = _loai_dot(dot)
    dot['loai'] = loai
    dot['loai_display'] = LOAI_DOT.get(loai, loai)
    dot['loai_ngan'] = LOAI_DOT_NGAN.get(loai, loai)
    dot['loai_tone'] = LOAI_DOT_TONE.get(loai, 'secondary')
    start, end = (dot.get('ngay_bat_dau') or '')[:10], (dot.get('ngay_ket_thuc') or '')[:10]
    if start and end and start <= today <= end:
        dot['trang_thai_hien_tai'], dot['trang_thai_label'], dot['trang_thai_tone'] = 1, 'Đang diễn ra', 'success'
    elif start and start > today:
        dot['trang_thai_hien_tai'], dot['trang_thai_label'], dot['trang_thai_tone'] = 2, 'Sắp diễn ra', 'warning'
    else:
        dot['trang_thai_hien_tai'], dot['trang_thai_label'], dot['trang_thai_tone'] = 0, 'Đã kết thúc', 'secondary'
    return dot


def _parse_ngay_vn(value):
    for fmt in ('%d/%m/%Y', '%Y-%m-%d', '%d-%m-%Y', '%d/%m/%y'):
        try:
            return datetime.strptime(str(value).strip()[:10], fmt).date()
        except (TypeError, ValueError):
            continue
    return None


def _chia_lich_thi(lich_su, dot_map):
    """Lịch thi của một thí sinh -> (sắp thi, đã thi). Bỏ bản ghi chưa có lịch.
    Ngày thi máy tính và ngày vấn đáp có thể khác nhau -> lấy ngày gần nhất chưa qua."""
    today = datetime.now().date()
    sap_toi, da_qua = [], []
    for item in lich_su:
        if not (item.get('ngay_thi') or item.get('phong_thi') or item.get('ngay_thi_2')):
            continue
        dot = dot_map.get(item.get('dot_thi')) if not isinstance(item.get('dot_thi'), dict) else item['dot_thi']
        dot = dot or {}
        item['dot_thi_ten'] = dot.get('ten_dot', '')
        item['dot_ma'] = dot.get('ma_dot', '')
        item['mon_thi_display'] = MON_THI_LABEL.get(item.get('mon_thi'), item.get('mon_thi') or '')
        item['truc_tuyen'] = 'trực tuyến' in str(item.get('ghi_chu') or '').lower()
        ngays = sorted(n for n in (_parse_ngay_vn(item.get('ngay_thi')), _parse_ngay_vn(item.get('ngay_thi_2'))) if n)
        con = [n for n in ngays if n >= today]
        if con:
            item['ngay_gan_nhat'] = con[0]
            item['con_ngay'] = (con[0] - today).days
            sap_toi.append(item)
        else:
            item['ngay_gan_nhat'] = ngays[-1] if ngays else None
            item['con_ngay'] = None
            da_qua.append(item)
    sap_toi.sort(key=lambda x: x['ngay_gan_nhat'])
    da_qua.sort(key=lambda x: x['ngay_gan_nhat'] or datetime.min.date(), reverse=True)
    return sap_toi, da_qua


def _nam_hoc_hien_tai(today=None):
    today = today or datetime.now().date()
    y = today.year if today.month >= 8 else today.year - 1
    return y


import tempfile as _tempfile
IMPORT_TMP_DIR = os.path.join(_tempfile.gettempdir(), 'humg_import_tmp')


def _import_tmp_save(request, upload):
    """Lưu file tạm cho bước xem trước -> xác nhận. Chỉ token lưu trong session mới mở lại được."""
    import uuid
    os.makedirs(IMPORT_TMP_DIR, exist_ok=True)
    token = uuid.uuid4().hex
    ext = '.xls' if upload.name.lower().endswith('.xls') else '.xlsx'
    path = os.path.join(IMPORT_TMP_DIR, token + ext)
    with open(path, 'wb') as fh:
        for chunk in upload.chunks():
            fh.write(chunk)
    store = request.session.get('import_tmp') or {}
    # giữ tối đa 5 file gần nhất của phiên
    for old in list(store)[:-4]:
        try:
            os.remove(store[old]['path'])
        except (OSError, KeyError, TypeError):
            pass
        store.pop(old, None)
    store[token] = {'path': path, 'name': upload.name}
    request.session['import_tmp'] = store
    return token


def _import_tmp_get(request, token):
    info = (request.session.get('import_tmp') or {}).get(token or '')
    if info and os.path.isfile(info.get('path', '')):
        return info
    return None


def _import_tmp_drop(request, token):
    store = request.session.get('import_tmp') or {}
    info = store.pop(token, None)
    request.session['import_tmp'] = store
    if info:
        try:
            os.remove(info['path'])
        except OSError:
            pass


@admin_required
def import_exam_data(request, loai):
    """Đường dẫn import cũ (theo môn): nay mỗi đợt là một môn -> chuyển sang trang import của đợt."""
    kind = 'lich' if loai.startswith('lich') else 'diem'
    dot_id = request.GET.get('dot')
    if dot_id and str(dot_id).isdigit():
        return redirect('dot_thi_import', pk=int(dot_id), kind='lich-thi' if kind == 'lich' else 'ket-qua')
    messages.info(request, 'Chọn đợt thi rồi bấm “Import lịch thi” / “Import kết quả” trong trang chi tiết đợt.')
    return redirect('dot_thi_list')


@admin_required
def dot_thi_import(request, pk, kind):
    """Import lịch thi / kết quả thi cho MỘT đợt (môn thi lấy theo đợt).
    2 bước: tải file -> xem trước (chọn sheet) -> xác nhận ghi dữ liệu."""
    kind = 'lich' if kind in ('lich', 'lich-thi') else 'diem'
    resp_dot = call_api(request, 'GET', EXAM_SERVICE + f'dotthi/{pk}/')
    dot_chon = resp_dot.json() if resp_dot is not None and resp_dot.status_code == 200 else None
    if not dot_chon:
        messages.error(request, 'Không tìm thấy đợt thi!')
        return redirect('dot_thi_list')
    _gan_trang_thai_dot(dot_chon)
    cfg = _import_cfg(dot_chon, kind)
    if not cfg:
        messages.error(request, 'Đợt thi chưa có môn thi hợp lệ.')
        return redirect('dot_thi_detail', pk=pk)

    selected = str(pk)
    preview = import_result = None
    token = request.POST.get('token') or ''
    file_name = ''
    sheet = request.POST.get('sheet') or ''
    tao_sv_moi = request.POST.get('tao_sv_moi') == '1'

    if request.method == 'POST':
        action = request.POST.get('action') or 'preview'
        upload = request.FILES.get('excel_file')
        info = None
        if upload:
            if not upload.name.lower().endswith(('.xlsx', '.xls')):
                messages.error(request, 'File phải có định dạng .xlsx hoặc .xls')
            else:
                if token:
                    _import_tmp_drop(request, token)
                token = _import_tmp_save(request, upload)
                info = _import_tmp_get(request, token)
                sheet = ''                       # file mới -> để hệ thống tự chọn sheet
                action = 'preview'
        elif token:
            info = _import_tmp_get(request, token)
            if not info:
                messages.error(request, 'File tạm đã hết hạn, vui lòng chọn lại file Excel.')
                token = ''
        else:
            messages.error(request, 'Vui lòng chọn file Excel!')

        if info:
            file_name = info['name']
            with open(info['path'], 'rb') as fh:
                content = fh.read()
            files = {'file': (info['name'], content, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')}
            data = {'dot_thi_id': selected, **cfg['params']}
            if sheet:
                data['sheet'] = sheet
            if action == 'preview':
                data['dry_run'] = '1'
            elif tao_sv_moi:
                data['tao_sv_moi'] = '1'
            resp = call_api(request, 'POST', EXAM_SERVICE + cfg['endpoint'], data=data, files=files)
            try:
                body = resp.json() if resp is not None else {}
            except ValueError:
                body = {}

            if resp is None:
                messages.error(request, 'Không kết nối được Exam Service hoặc quá thời gian xử lý.')
            elif resp.status_code != 200:
                messages.error(request, f"Không đọc được file: {body.get('error') or body.get('detail') or resp.status_code}")
                if body.get('sheets'):
                    preview = {'sheets': body['sheets'], 'invalid': True}
            elif action == 'preview':
                preview = body
                sheet = body.get('sheet') or sheet
            else:
                import_result = {
                    'created': body.get('created', 0),
                    'updated': body.get('updated', 0),
                    'sv_moi': body.get('sv_moi', 0),
                    'skipped': body.get('skipped', []) or [],
                    'errors': body.get('errors', []) or [],
                    'sheet': body.get('sheet') or sheet,
                    'file_name': file_name,
                    'dot_thi_id': selected,
                }
                _import_tmp_drop(request, token)
                token = ''
                if import_result['sv_moi']:
                    _cache.delete(f"api_cache:{STUDENT_SERVICE}sinhvien/")
                total = import_result['created'] + import_result['updated']
                if total:
                    messages.success(request, f"Đã import {total} thí sinh vào đợt {dot_chon.get('ma_dot')}: {import_result['created']} thêm mới, {import_result['updated']} cập nhật.")
                else:
                    messages.warning(request, 'Không có dòng nào được ghi — xem chi tiết bên dưới.')

    return render(request, 'admin/exams/import_exam.html', {
        'cfg': cfg,
        'kind_url': 'lich-thi' if kind == 'lich' else 'ket-qua',
        'diem_dat': DIEM_DAT.get(LOAI_SANG_MON.get(dot_chon['loai'])) if kind == 'diem' else None,
        'dot_chon': dot_chon,
        'selected': selected,
        'preview': preview,
        'import_result': import_result,
        'token': token,
        'file_name': file_name,
        'sheet': sheet,
        'tao_sv_moi': tao_sv_moi,
    })


# ----- QUẢN LÝ LỚP BỒI DƯỠNG -----
@admin_required
def class_list(request):
    resp = call_api(request, 'GET', TRAINING_SERVICE + 'lop/')
    classes = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin/classes/class_list.html', {'classes': classes})

@admin_required
def class_create(request):
    if request.method == 'POST':
        data = {
            'ma_lop': request.POST.get('ma_lop'),
            'ten_lop': request.POST.get('ten_lop'),
            'loai': request.POST.get('loai'),
            'so_luong_toi_da': request.POST.get('so_luong_toi_da') or 30,
            'bat_dau': request.POST.get('bat_dau'),
            'ket_thuc': request.POST.get('ket_thuc'),
            'trang_thai': request.POST.get('trang_thai', 'OPEN'),
        }
        resp = call_api(request, 'POST', TRAINING_SERVICE + 'lop/', data=data)
        if resp and resp.status_code == 201:
            messages.success(request, 'Tạo lớp thành công!')
            return redirect('class_list')
        else:
            messages.error(request, 'Tạo lớp thất bại!')
    return render(request, 'admin/classes/class_form.html', {'instance': None})

@admin_required
def class_edit(request, pk):
    if request.method == 'POST':
        data = {
            'ma_lop': request.POST.get('ma_lop'),
            'ten_lop': request.POST.get('ten_lop'),
            'loai': request.POST.get('loai'),
            'so_luong_toi_da': request.POST.get('so_luong_toi_da') or 30,
            'bat_dau': request.POST.get('bat_dau'),
            'ket_thuc': request.POST.get('ket_thuc'),
            'trang_thai': request.POST.get('trang_thai', 'OPEN'),
        }
        resp = call_api(request, 'PUT', TRAINING_SERVICE + f'lop/{pk}/', data=data)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật lớp thành công!')
            return redirect('class_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', TRAINING_SERVICE + f'lop/{pk}/')
    instance = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin/classes/class_form.html', {'instance': instance})

@admin_required
def class_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', TRAINING_SERVICE + f'lop/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa lớp thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('class_list')

@admin_required
def import_class_list(request):
    if request.method == 'POST':
        lop_id = request.POST.get('lop_id')
        if not lop_id:
            messages.error(request, 'Vui lòng chọn lớp!')
            return redirect('import_class_list')
        file = request.FILES.get('excel_file')
        if not file:
            messages.error(request, 'Vui lòng chọn file!')
            return redirect('import_class_list')
        files = {'file': file}
        data = {'lop_id': lop_id}
        resp = call_api(request, 'POST', TRAINING_SERVICE + f'lop/{lop_id}/import-students/', data=data, files=files)
        if resp and resp.status_code == 200:
            messages.success(request, 'Import danh sách lớp thành công!')
        else:
            messages.error(request, 'Import thất bại!')
        return redirect('class_list')
    resp = call_api(request, 'GET', TRAINING_SERVICE + 'lop/')
    lops = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin/classes/import_class_list.html', {'lops': lops})


# ----- QUẢN LÝ BÀI VIẾT (CMS) -----
@login_required
def danh_sach_lop(request):
    """Danh sach lop boi duong."""
    lops = []
    da_dang_ky_ids = []

    # Thu import model tu cac app khac nhau
    LopHoc = None
    for mod_path in ('proxy.models', 'users.models', 'gateway.models'):
        try:
            mod = __import__(mod_path, fromlist=['LopHoc'])
            LopHoc = getattr(mod, 'LopHoc', None)
            if LopHoc:
                break
        except Exception:
            continue

    if LopHoc is not None:
        try:
            lops = list(LopHoc.objects.all().order_by('-id'))
        except Exception:
            lops = []

    # Lay danh sach lop user da dang ky (neu co model DangKy)
    if request.user.is_authenticated:
        for cls_name in ('DangKyLop', 'DangKy', 'Registration'):
            try:
                mod = __import__('proxy.models', fromlist=[cls_name])
                DangKy = getattr(mod, cls_name, None)
                if DangKy is None:
                    continue
                qs = DangKy.objects.filter(user=request.user)
                da_dang_ky_ids = list(qs.values_list('lop_id', flat=True))
                break
            except Exception:
                continue

    return render(request, 'students/danh_sach_lop.html', {
        'lops': lops,
        'da_dang_ky_ids': da_dang_ky_ids,
    })


@admin_required
def post_list(request):
    """Admin: danh sách bài viết (CMS)."""
    resp = call_api(request, 'GET', CMS_SERVICE + 'baiviet/')
    posts = resp.json() if resp and resp.status_code == 200 else []
    if isinstance(posts, dict):
        posts = posts.get('results', [])
    return render(request, 'admin/cms/post_list.html', {'posts': posts})


# ============================================
# PORTAL VIEWS - Bài viết cho sinh viên
# ============================================
def post_list_portal(request):
    """Portal: danh sách bài viết cho sinh viên (có search + sidebar danh mục)."""
    query = (request.GET.get('q') or '').strip()

    # --- Lấy bài viết ---
    posts = []
    try:
        url = CMS_SERVICE + 'baiviet/'
        params = {}
        if query:
            params['search'] = query
        resp = requests.get(url, params=params, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            posts = data if isinstance(data, list) else data.get('results', [])
    except Exception:
        posts = []

    # --- Lấy danh mục cho sidebar ---
    categories = []
    try:
        resp_cat = requests.get(CMS_SERVICE + 'danhmuc/?is_active=true', timeout=5)
        if resp_cat.status_code == 200:
            data_cat = resp_cat.json()
            categories = data_cat if isinstance(data_cat, list) else data_cat.get('results', [])
    except Exception:
        categories = []

    context = {
        'posts': posts,
        'categories': categories,
        'query': query,
        'category': None,
    }
    return render(request, 'students/post_list.html', context)


def post_detail(request, slug):
    """Portal: chi tiết bài viết."""
    try:
        resp = requests.get(CMS_SERVICE + f'baiviet/?slug={slug}', timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            posts = data if isinstance(data, list) else data.get('results', [])
            post = posts[0] if posts else None
        else:
            post = None
    except Exception:
        post = None

    if not post:
        raise Http404("Không tìm thấy bài viết")

    # Lấy bài viết liên quan (5 bài mới nhất khác slug)
    try:
        resp2 = requests.get(CMS_SERVICE + 'baiviet/', timeout=5)
        if resp2.status_code == 200:
            data2 = resp2.json()
            all_posts = data2 if isinstance(data2, list) else data2.get('results', [])
            related = [p for p in all_posts if p.get('slug') != slug][:5]
        else:
            related = []
    except Exception:
        related = []

    # Quick links sidebar
    try:
        resp3 = requests.get(CMS_SERVICE + 'quicklink/', timeout=5)
        quick_links = resp3.json() if resp3.status_code == 200 else []
    except Exception:
        quick_links = []

    context = {
        'post': post,
        'related_posts': related,
        'quick_links': quick_links,
    }
    return render(request, 'students/post_detail.html', context)


def post_list_by_category(request, slug):
    """Portal: bài viết theo danh mục (slug)."""
    # --- Lấy thông tin danh mục ---
    category = None
    try:
        resp_cat = requests.get(CMS_SERVICE + f'danhmuc/?slug={slug}', timeout=5)
        if resp_cat.status_code == 200:
            data_cat = resp_cat.json()
            cat_list = data_cat if isinstance(data_cat, list) else data_cat.get('results', [])
            category = cat_list[0] if cat_list else None
    except Exception:
        category = None

    # --- Lấy bài viết theo danh mục ---
    posts = []
    if category:
        try:
            resp = requests.get(
                CMS_SERVICE + f'baiviet/?category__slug={slug}',
                timeout=5,
            )
            if resp.status_code == 200:
                data = resp.json()
                posts = data if isinstance(data, list) else data.get('results', [])
        except Exception:
            posts = []

    # --- Lấy tất cả danh mục cho sidebar ---
    categories = []
    try:
        resp_cat2 = requests.get(CMS_SERVICE + 'danhmuc/?is_active=true', timeout=5)
        if resp_cat2.status_code == 200:
            data_cat2 = resp_cat2.json()
            categories = data_cat2 if isinstance(data_cat2, list) else data_cat2.get('results', [])
    except Exception:
        categories = []

    context = {
        'posts': posts,
        'categories': categories,
        'category': category,
        'query': '',
    }
    return render(request, 'students/post_list.html', context)

@admin_required
def post_create(request):
    if request.method == 'POST':
        data = {
            'tieu_de': request.POST.get('tieu_de') or request.POST.get('title') or '',
            'noi_dung': request.POST.get('noi_dung') or request.POST.get('content') or '',
            'slug': request.POST.get('slug') or '',
            'hinh_anh': request.POST.get('hinh_anh') or request.POST.get('image') or '',
            'summary': request.POST.get('summary') or '',
            'category_id': request.POST.get('category') or None,
            'is_published': request.POST.get('is_published') == 'on',
        }
        files = None
        if 'image' in request.FILES:
            files = {'image': request.FILES['image']}
        resp = call_api(request, 'POST', CMS_SERVICE + 'baiviet/', data=data, files=files)
        if resp and resp.status_code == 201:
            messages.success(request, 'Thêm bài viết thành công!')
            return redirect('post_list')
        else:
            messages.error(request, 'Thêm thất bại!')
    resp_cat = call_api(request, 'GET', CMS_SERVICE + 'danhmuc/')
    categories = resp_cat.json() if resp_cat and resp_cat.status_code == 200 else []
    return render(request, 'admin/cms/post_form.html', {'instance': None, 'categories': categories})

@admin_required
def post_edit(request, pk):
    if request.method == 'POST':
        data = {
            'tieu_de': request.POST.get('tieu_de') or request.POST.get('title') or '',
            'noi_dung': request.POST.get('noi_dung') or request.POST.get('content') or '',
            'slug': request.POST.get('slug') or '',
            'hinh_anh': request.POST.get('hinh_anh') or request.POST.get('image') or '',
            'summary': request.POST.get('summary') or '',
            'category_id': request.POST.get('category') or None,
            'is_published': request.POST.get('is_published') == 'on',
        }
        files = None
        if 'image' in request.FILES:
            files = {'image': request.FILES['image']}
        resp = call_api(request, 'PUT', CMS_SERVICE + f'baiviet/{pk}/', data=data, files=files)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật thành công!')
            return redirect('post_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', CMS_SERVICE + f'baiviet/{pk}/')
    instance = resp.json() if resp and resp.status_code == 200 else None
    resp_cat = call_api(request, 'GET', CMS_SERVICE + 'danhmuc/')
    categories = resp_cat.json() if resp_cat and resp_cat.status_code == 200 else []
    return render(request, 'admin/cms/post_form.html', {'instance': instance, 'categories': categories})

@admin_required
def post_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', CMS_SERVICE + f'baiviet/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('post_list')


# ----- QUẢN LÝ DANH MỤC BÀI VIẾT (CMS) -----
@admin_required
def category_list(request):
    resp = call_api(request, 'GET', CMS_SERVICE + 'danhmuc/')
    categories = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin/cms/category_list.html', {'categories': categories})

@admin_required
def category_create(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name') or '',
            'slug': request.POST.get('slug') or '',
            'description': request.POST.get('description') or '',
            'show_on_navbar': request.POST.get('show_on_navbar') == 'on',
            'show_on_homepage': request.POST.get('show_on_homepage') == 'on',
            'is_active': request.POST.get('is_active') == 'on',
            'thu_tu': int(request.POST.get('thu_tu') or 0),
        }
        resp = call_api(request, 'POST', CMS_SERVICE + 'danhmuc/', data=data)
        if resp and resp.status_code == 201:
            messages.success(request, 'Thêm danh mục thành công!')
            return redirect('category_list')
        else:
            messages.error(request, 'Thêm thất bại!')
    return render(request, 'admin/cms/category_form.html', {'instance': None})

@admin_required
def category_edit(request, pk):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name') or '',
            'slug': request.POST.get('slug') or '',
            'description': request.POST.get('description') or '',
            'show_on_navbar': request.POST.get('show_on_navbar') == 'on',
            'show_on_homepage': request.POST.get('show_on_homepage') == 'on',
            'is_active': request.POST.get('is_active') == 'on',
            'thu_tu': int(request.POST.get('thu_tu') or 0),
        }
        resp = call_api(request, 'PUT', CMS_SERVICE + f'danhmuc/{pk}/', data=data)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật thành công!')
            return redirect('category_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', CMS_SERVICE + f'danhmuc/{pk}/')
    instance = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin/cms/category_form.html', {'instance': instance})

@admin_required
def category_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', CMS_SERVICE + f'danhmuc/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('category_list')


# ----- QUẢN LÝ SLIDER -----
@admin_required
def slider_list(request):
    resp = call_api(request, 'GET', CMS_SERVICE + 'slider/')
    sliders = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin/cms/slider_list.html', {'sliders': sliders})

@admin_required
def slider_create(request):
    if request.method == 'POST':
        data = {
            'tieu_de': request.POST.get('title') or request.POST.get('tieu_de') or '',
            'duong_dan': request.POST.get('link_url') or request.POST.get('duong_dan') or '',
            'thu_tu': int(request.POST.get('order') or request.POST.get('thu_tu') or 0),
            'is_active': request.POST.get('is_active') == 'on',
        }
        files = None
        if 'image' in request.FILES:
            files = {'image': request.FILES['image']}
        resp = call_api(request, 'POST', CMS_SERVICE + 'slider/', data=data, files=files)
        if resp and resp.status_code == 201:
            messages.success(request, 'Thêm slider thành công!')
            return redirect('slider_list')
        else:
            messages.error(request, 'Thêm thất bại!')
    return render(request, 'admin/cms/slider_form.html', {'instance': None})

@admin_required
def slider_edit(request, pk):
    if request.method == 'POST':
        data = {
            'tieu_de': request.POST.get('title') or request.POST.get('tieu_de') or '',
            'duong_dan': request.POST.get('link_url') or request.POST.get('duong_dan') or '',
            'thu_tu': int(request.POST.get('order') or request.POST.get('thu_tu') or 0),
            'is_active': request.POST.get('is_active') == 'on',
        }
        files = None
        if 'image' in request.FILES:
            files = {'image': request.FILES['image']}
        resp = call_api(request, 'PUT', CMS_SERVICE + f'slider/{pk}/', data=data, files=files)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật thành công!')
            return redirect('slider_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', CMS_SERVICE + f'slider/{pk}/')
    instance = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin/cms/slider_form.html', {'instance': instance})

@admin_required
def slider_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', CMS_SERVICE + f'slider/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('slider_list')


# ----- QUẢN LÝ QUICKLINK -----
@admin_required
def quicklink_list(request):
    resp = call_api(request, 'GET', CMS_SERVICE + 'quicklink/')
    quicklinks = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin/cms/quicklink_list.html', {'quicklinks': quicklinks})

@admin_required
def quicklink_create(request):
    if request.method == 'POST':
        data = {
            'ten': request.POST.get('title') or request.POST.get('ten') or '',
            'duong_dan': request.POST.get('url') or request.POST.get('duong_dan') or '',
            'thu_tu': int(request.POST.get('order') or request.POST.get('thu_tu') or 0),
            'is_active': request.POST.get('is_active') == 'on',
        }
        files = None
        if 'image' in request.FILES:
            files = {'image': request.FILES['image']}
        resp = call_api(request, 'POST', CMS_SERVICE + 'quicklink/', data=data, files=files)
        if resp and resp.status_code == 201:
            messages.success(request, 'Thêm quicklink thành công!')
            return redirect('quicklink_list')
        else:
            messages.error(request, 'Thêm thất bại!')
    return render(request, 'admin/cms/quicklink_form.html', {'instance': None})

@admin_required
def quicklink_edit(request, pk):
    if request.method == 'POST':
        data = {
            'ten': request.POST.get('title') or request.POST.get('ten') or '',
            'duong_dan': request.POST.get('url') or request.POST.get('duong_dan') or '',
            'thu_tu': int(request.POST.get('order') or request.POST.get('thu_tu') or 0),
            'is_active': request.POST.get('is_active') == 'on',
        }
        files = None
        if 'image' in request.FILES:
            files = {'image': request.FILES['image']}
        resp = call_api(request, 'PUT', CMS_SERVICE + f'quicklink/{pk}/', data=data, files=files)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật thành công!')
            return redirect('quicklink_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', CMS_SERVICE + f'quicklink/{pk}/')
    instance = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin/cms/quicklink_form.html', {'instance': instance})

@admin_required
def quicklink_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', CMS_SERVICE + f'quicklink/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('quicklink_list')


# ----- QUẢN LÝ THÔNG BÁO -----
@admin_required
def thongbao_list(request):
    resp = call_api(request, 'GET', NOTIFICATION_SERVICE + 'thongbao/')
    thong_baos = resp.json() if resp and resp.status_code == 200 else []
    context = {
        'thong_baos': thong_baos,
        'tong_thong_bao': len(thong_baos),
        'dang_hien_thi': sum(1 for tb in thong_baos if tb.get('is_active')),
        'tong_sv_chua_dat_nn': 0,
        'tong_sv_chua_dat_th': 0,
    }
    return render(request, 'admin/reports/thongbao_list.html', context)

@admin_required
def thongbao_create(request):
    if request.method == 'POST':
        data = {
            'tieu_de': request.POST.get('tieu_de'),
            'noi_dung': request.POST.get('noi_dung'),
            'loai': request.POST.get('loai'),
            'doi_tuong': request.POST.get('doi_tuong'),
            'ngay_bat_dau': request.POST.get('ngay_bat_dau'),
            'ngay_ket_thuc': request.POST.get('ngay_ket_thuc'),
            'is_active': request.POST.get('is_active') == 'on',
        }
        resp = call_api(request, 'POST', NOTIFICATION_SERVICE + 'thongbao/', data=data)
        if resp and resp.status_code == 201:
            messages.success(request, 'Tạo thông báo thành công!')
            return redirect('thongbao_list')
        else:
            messages.error(request, 'Tạo thất bại!')
    return render(request, 'admin/reports/thongbao_form.html', {'instance': None})

@admin_required
def thongbao_edit(request, pk):
    if request.method == 'POST':
        data = {
            'tieu_de': request.POST.get('tieu_de'),
            'noi_dung': request.POST.get('noi_dung'),
            'loai': request.POST.get('loai'),
            'doi_tuong': request.POST.get('doi_tuong'),
            'ngay_bat_dau': request.POST.get('ngay_bat_dau'),
            'ngay_ket_thuc': request.POST.get('ngay_ket_thuc'),
            'is_active': request.POST.get('is_active') == 'on',
        }
        resp = call_api(request, 'PUT', NOTIFICATION_SERVICE + f'thongbao/{pk}/', data=data)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật thành công!')
            return redirect('thongbao_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', NOTIFICATION_SERVICE + f'thongbao/{pk}/')
    instance = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin/reports/thongbao_form.html', {'instance': instance})

@admin_required
def thongbao_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', NOTIFICATION_SERVICE + f'thongbao/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('thongbao_list')


# ----- QUẢN LÝ TÀI KHOẢN VÀ NHÓM QUYỀN -----
@admin_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'admin/system/user_list.html', {'users': users})

@admin_required
def user_create(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = 'Humg@123456'
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        is_active = request.POST.get('is_active') == 'on'
        groups = request.POST.getlist('groups')
        username = (username or '').strip()
        if not username:
            messages.error(request, 'Vui lòng nhập tên đăng nhập.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, f'Tên đăng nhập "{username}" đã tồn tại.')
        else:
            user = User.objects.create_user(username=username, password=password, email=email,
                                            first_name=first_name, last_name=last_name, is_active=is_active)
            if groups:
                user.groups.set(groups)
            messages.success(request, f'Tạo tài khoản {username} thành công! Mật khẩu mặc định: Humg@123456')
            return redirect('user_list')
    groups = Group.objects.all()
    return render(request, 'admin/system/user_form.html', {'instance': None, 'groups': groups})

@admin_required
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.is_active = request.POST.get('is_active') == 'on'
        user.groups.set(request.POST.getlist('groups'))
        user.save()
        messages.success(request, 'Cập nhật tài khoản thành công!')
        return redirect('user_list')
    groups = Group.objects.all()
    return render(request, 'admin/system/user_form.html', {
        'instance': user, 'groups': groups,
        'selected_group_ids': list(user.groups.values_list('id', flat=True)),
    })

@admin_required
def group_list(request):
    groups = Group.objects.all()
    return render(request, 'admin/system/group_list.html', {'groups': groups})

@admin_required
def group_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        group = Group.objects.create(name=name)
        group.permissions.set(request.POST.getlist('permissions'))
        messages.success(request, 'Tạo nhóm quyền thành công!')
        return redirect('group_list')
    from django.contrib.auth.models import Permission
    permissions = Permission.objects.select_related('content_type').all()
    return render(request, 'admin/system/group_form.html', {'instance': None, 'permissions': permissions})

@admin_required
def group_edit(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.name = request.POST.get('name')
        group.permissions.set(request.POST.getlist('permissions'))
        group.save()
        messages.success(request, 'Cập nhật nhóm quyền thành công!')
        return redirect('group_list')
    from django.contrib.auth.models import Permission
    permissions = Permission.objects.select_related('content_type').all()
    return render(request, 'admin/system/group_form.html', {
        'instance': group, 'permissions': permissions,
        'selected_perm_ids': list(group.permissions.values_list('id', flat=True)),
    })


# ================================================================
# VIEWS CHO PORTAL (students/)
# ================================================================

def home(request):
    """Trang chu portal - parallel + cache."""
    urls = [
        CMS_SERVICE + 'slider/',
        CMS_SERVICE + 'quicklink/',
        CMS_SERVICE + 'baiviet/?limit=10',
        CMS_SERVICE + 'danhmuc/?show_on_homepage=true',
        EXAM_SERVICE + 'dotthi/',
    ]
    results = parallel_get_json(urls, ttl=60)

    def _lst(v):
        if isinstance(v, dict):
            v = v.get('results', [])
        return v if isinstance(v, list) else []

    sliders = [x for x in _lst(results.get(urls[0])) if x.get('is_active', True)]
    quick_links = [x for x in _lst(results.get(urls[1])) if x.get('is_active', True)]
    latest_posts = _lst(results.get(urls[2]))
    categories = _lst(results.get(urls[3]))

    # Biểu tượng cho liên kết nhanh theo tên
    QL_ICONS = (('lich', 'fa-regular fa-calendar-check'), ('diem', 'fa-solid fa-magnifying-glass-chart'),
                ('tracuu', 'fa-solid fa-magnifying-glass'), ('dangky', 'fa-solid fa-chalkboard-user'),
                ('lop', 'fa-solid fa-chalkboard-user'), ('quyche', 'fa-regular fa-file-lines'),
                ('vanban', 'fa-regular fa-file-lines'), ('chungchi', 'fa-solid fa-certificate'),
                ('tintuc', 'fa-regular fa-newspaper'), ('lienhe', 'fa-solid fa-headset'))
    import unicodedata as _ud
    for ql in quick_links:
        key = _ud.normalize('NFD', (ql.get('ten') or '').lower().replace('đ', 'd'))
        key = ''.join(c for c in key if c.isalnum() and _ud.category(c) != 'Mn')
        ql['icon'] = next((ic for k, ic in QL_ICONS if k in key), 'fa-solid fa-arrow-up-right-from-square')
        ql['noi_bo'] = str(ql.get('duong_dan') or '').startswith('/')

    # Đợt thi sắp tới / đang diễn ra (hiển thị kiểu "sự kiện" như humg.edu.vn)
    from datetime import date as _date
    today_iso = _date.today().isoformat()
    dot_sap_toi = []
    for d in _lst(results.get(urls[4])):
        if (d.get('ngay_ket_thuc') or d.get('ngay_bat_dau') or '') >= today_iso:
            d['loai_display'] = LOAI_DOT.get(_loai_dot(d), d.get('loai') or '')
            d['dang_dien_ra'] = (d.get('ngay_bat_dau') or '') <= today_iso
            dot_sap_toi.append(d)
    dot_sap_toi.sort(key=lambda d: d.get('ngay_bat_dau') or '')

    home_blocks = []
    if categories:
        cat_urls = [CMS_SERVICE + f'baiviet/?category={cat.get("id")}&limit=4' for cat in categories]
        cat_results = parallel_get_json(cat_urls, ttl=60)
        for cat, url in zip(categories, cat_urls):
            home_blocks.append({
                'category': cat,
                'posts': cat_results.get(url) or [],
            })

    context = {
        'slider_posts': sliders,
        'slider_images': [x for x in sliders if x.get('hinh_anh')],
        'quick_links': quick_links,
        'latest_posts': latest_posts,
        'home_blocks': home_blocks,
        'dot_sap_toi': dot_sap_toi[:4],
    }
    return render(request, 'students/home.html', context)


@login_required
def student_dashboard(request):
    """Dashboard sinh vien - parallel + cache."""
    from datetime import datetime as dt, date as date_cls

    def parse_ngay(s):
        if not s:
            return None
        if isinstance(s, date_cls):
            return s
        s = str(s).strip()
        for fmt in ('%d/%m/%Y', '%Y-%m-%d', '%d-%m-%Y', '%m/%d/%Y', '%d/%m/%y'):
            try:
                return dt.strptime(s, fmt).date()
            except ValueError:
                continue
        return None

    MON_THI_DISPLAY = MON_THI_LABEL
    THU_DISPLAY = {2: 'T2', 3: 'T3', 4: 'T4', 5: 'T5', 6: 'T6', 7: 'T7', 8: 'CN'}

    username = request.user.username

    sv_data = _cached_get_json(STUDENT_SERVICE + f'sinhvien/?ma_sv={username}', ttl=120)
    sinh_vien = None
    if sv_data:
        if isinstance(sv_data, dict):
            sv_data = sv_data.get('results', [])
        sinh_vien = sv_data[0] if sv_data else None

    if not sinh_vien:
        messages.warning(request, 'Không tìm thấy thông tin sinh viên.')
        return render(request, 'students/dashboard.html', {
            'sinh_vien': {}, 'khong_co_ho_so': True, 'ten_goi': username,
            'lich_su_thi': [], 'ket_qua_thi': [], 'chung_chi': [], 'cc_cho_duyet': [],
            'dang_ky_lop': [], 'lop_dang_hoc': [], 'lop_cho_duyet': [],
            'thong_bao_moi': [], 'lich_thi_sap_toi': [], 'danh_muc_cc': [],
            'check_dat_ngoai_ngu': False, 'check_dat_tin_hoc': False,
            'dat_chuan_dau_ra': False, 'bac_yeu_cau_nn': 3,
        })

    sinh_vien_id = sinh_vien.get('id')

    urls = {
        'cdr':       STUDENT_SERVICE + f'sinhvien/{sinh_vien_id}/cdr-status/',
        'lichsuthi': EXAM_SERVICE + f'lichsuthi/?sinh_vien_id={sinh_vien_id}',
        'dotthi':    EXAM_SERVICE + 'dotthi/',
        'chungchi':  CERT_SERVICE + f'chungchi/?sinh_vien_id={sinh_vien_id}',
        'danhmuc':   CERT_SERVICE + 'danhmuc/',
        'dangky':    TRAINING_SERVICE + f'dangky/?sinh_vien_id={sinh_vien_id}',
        'lop':       TRAINING_SERVICE + 'lop/',
        'lichhoc':   TRAINING_SERVICE + 'lich-hoc/',
        'thongbao':  NOTIFICATION_SERVICE + f'thongbao/?sinh_vien_id={sinh_vien_id}&is_active=true',
    }
    res = parallel_get_json(list(urls.values()), ttl=60)
    d = {k: res.get(v) for k, v in urls.items()}
    if not d['cdr']:
        # cdr-status của student-service yêu cầu JWT -> gọi lại kèm token phiên đăng nhập
        d['cdr'] = parallel_api_get(request, [urls['cdr']], ttl=60).get(urls['cdr'])

    cdr = d['cdr'] or {}
    check_nn  = cdr.get('check_dat_ngoai_ngu', False)
    check_th  = cdr.get('check_dat_tin_hoc', False)
    check_cdr = cdr.get('dat_chuan_dau_ra', False)

    lich_su_thi = _as_list_of(d['lichsuthi'], sinh_vien_id)

    dot_map = {}
    dots = d['dotthi'] or []
    if isinstance(dots, dict):
        dots = dots.get('results', [])
    for dd in dots:
        dot_map[dd.get('id')] = dd

    for item in lich_su_thi:
        dot_id = item.get('dot_thi')
        item['dot_thi_ten'] = dot_map.get(dot_id, {}).get('ten_dot', '') if dot_id else ''
        item['mon_thi_display'] = MON_THI_DISPLAY.get(item.get('mon_thi'), item.get('mon_thi', ''))

    chung_chi = _as_list_of(d['chungchi'], sinh_vien_id)

    danh_muc_cc = d['danhmuc'] or []
    if isinstance(danh_muc_cc, dict):
        danh_muc_cc = danh_muc_cc.get('results', [])

    dang_ky_lop = _as_list_of(d['dangky'], sinh_vien_id)

    lop_map = {}
    lops = d['lop'] or []
    if isinstance(lops, dict):
        lops = lops.get('results', [])
    for l in lops:
        lop_map[l.get('id')] = l

    lich_hoc_map = {}
    lhs = d['lichhoc'] or []
    if isinstance(lhs, dict):
        lhs = lhs.get('results', [])
    for lh in lhs:
        lop_id = lh.get('lop')
        if lop_id:
            lich_hoc_map.setdefault(lop_id, []).append(lh)

    for dk in dang_ky_lop:
        lop_id = dk.get('lop')
        lop = lop_map.get(lop_id, {})
        dk['lop_ten'] = lop.get('ten_lop') or f'Lớp ID {lop_id}'
        dk['lop_loai_display'] = 'Ngoại ngữ' if lop.get('loai') == 'NN' else 'Tin học'
        dk['lop_ngay_khai_giang'] = lop.get('bat_dau', '')

        lhs_lop = lich_hoc_map.get(lop_id, [])
        if lhs_lop:
            thu_list, phong_list = [], []
            for lh in lhs_lop:
                thu = lh.get('thu')
                thu_str = THU_DISPLAY.get(thu, f'T{thu}')
                thu_list.append(f"{thu_str} tiết {lh.get('tiet_bat_dau','')}-{lh.get('tiet_ket_thuc','')}")
                if lh.get('phong_hoc'):
                    phong_list.append(lh['phong_hoc'])
            dk['lop_lich_hoc'] = '; '.join(thu_list)
            dk['lop_phong_hoc'] = ', '.join(sorted(set(phong_list)))
        else:
            dk['lop_lich_hoc'] = ''
            dk['lop_phong_hoc'] = ''

    thong_bao_moi = d['thongbao'] or []
    if isinstance(thong_bao_moi, dict):
        thong_bao_moi = thong_bao_moi.get('results', [])

    today = dt.now().date()
    for item in lich_su_thi:
        item['co_ket_qua'] = item.get('diem_tong') is not None or bool(item.get('xep_loai'))
    # Lịch thi của tôi: sắp thi (kể cả hôm nay) + các lịch đã thi gần nhất
    lich_thi_sap_toi, lich_thi_da_qua = _chia_lich_thi(lich_su_thi, dot_map)
    ket_qua_thi = [x for x in lich_su_thi if x.get('co_ket_qua')]
    ket_qua_thi.sort(key=lambda x: x.get('dot_thi') or 0, reverse=True)

    lop_dang_hoc = [dk for dk in dang_ky_lop if dk.get('trang_thai') in ('DA_DUYET', 'APPROVED')]
    lop_cho_duyet = [dk for dk in dang_ky_lop if dk.get('trang_thai') in ('PENDING', 'CHO_DUYET', 'CHO')]
    cc_cho_duyet = [cc for cc in chung_chi if cc.get('trang_thai') == 'CHO']

    ten = (sinh_vien.get('ho_ten') or '').split()
    context = {
        'sinh_vien': sinh_vien,
        'ten_goi': ten[-1] if ten else username,
        'lich_su_thi': lich_su_thi,
        'ket_qua_thi': ket_qua_thi,
        'chung_chi': chung_chi,
        'cc_cho_duyet': cc_cho_duyet,
        'dang_ky_lop': dang_ky_lop,
        'lop_dang_hoc': lop_dang_hoc,
        'lop_cho_duyet': lop_cho_duyet,
        'thong_bao_moi': thong_bao_moi[:5],
        'lich_thi_sap_toi': lich_thi_sap_toi,
        'lich_thi_da_qua': lich_thi_da_qua[:4],
        'danh_muc_cc': danh_muc_cc,
        'check_dat_ngoai_ngu': check_nn,
        'check_dat_tin_hoc': check_th,
        'dat_chuan_dau_ra': check_cdr,
        'da_mien_cdr': cdr.get('da_mien_cdr', False),
        'bac_yeu_cau_nn': cdr.get('bac_yeu_cau_ngoai_ngu') or 3,
        'today': today,
    }
    return render(request, 'students/dashboard.html', context)


@login_required
def tra_cuu(request):
    MON_THI = MON_THI_LABEL
    LOAI_CC = {'NGOAI_NGU': 'Ngoại ngữ', 'TIN_HOC': 'Tin học'}
    mssv = (request.GET.get('mssv') or '').strip()
    sinh_vien = None
    lich_su_thi, chung_chi, lich_thi_sap_toi, ket_qua_thi = [], [], [], []
    thong_bao = None

    # Sinh viên chỉ được tra cứu kết quả của CHÍNH MÌNH; admin tra cứu được mọi MSSV
    profile = getattr(request.user, 'profile', None)
    la_admin = request.user.is_superuser or bool(profile and profile.role == 'admin')
    if not la_admin:
        if mssv and mssv != request.user.username:
            thong_bao = 'Bạn chỉ được xem kết quả của chính mình. Đã hiển thị kết quả theo MSSV của bạn.'
        mssv = request.user.username

    def _lst(data):
        if isinstance(data, dict):
            data = data.get('results', [])
        return data if isinstance(data, list) else []

    if mssv:
        try:
            resp = requests.get(STUDENT_SERVICE + 'sinhvien/', params={'ma_sv': mssv}, timeout=5)
            if resp.status_code == 200:
                results = _lst(resp.json())
                # Lọc chính xác theo MSSV (phòng khi API bỏ qua tham số lọc)
                results = [sv for sv in results if sv.get('ma_sv') == mssv] or results[:0]
                if results:
                    sinh_vien = results[0]
                else:
                    thong_bao = 'Không tìm thấy sinh viên với MSSV này.'
            else:
                thong_bao = 'Lỗi kết nối đến hệ thống.'
        except requests.exceptions.RequestException:
            thong_bao = 'Lỗi kết nối đến hệ thống.'

    if sinh_vien and sinh_vien.get('id'):
        sv_id = sinh_vien['id']
        urls = {
            'lichsuthi': EXAM_SERVICE + f'lichsuthi/?sinh_vien_id={sv_id}',
            'dotthi': EXAM_SERVICE + 'dotthi/',
            'chungchi': CERT_SERVICE + f'chungchi/?sinh_vien_id={sv_id}',
            'cdr': STUDENT_SERVICE + f'sinhvien/{sv_id}/cdr-status/',
        }
        res = parallel_api_get(request, list(urls.values()), ttl=60)
        dot_map = {d.get('id'): d for d in _lst(res.get(urls['dotthi']))}
        lich_su_thi = _as_list_of(res.get(urls['lichsuthi']), sv_id)
        chung_chi = _as_list_of(res.get(urls['chungchi']), sv_id)
        cdr = res.get(urls['cdr']) or {}

        today = datetime.now().date()
        for item in lich_su_thi:
            item['dot_thi'] = dot_map.get(item.get('dot_thi')) or {'ten_dot': ''}
            item['get_mon_thi_display'] = MON_THI.get(item.get('mon_thi'), item.get('mon_thi') or '')
            try:
                if datetime.strptime(item.get('ngay_thi') or '', '%d/%m/%Y').date() >= today:
                    lich_thi_sap_toi.append(item)
            except ValueError:
                pass
            if item.get('diem_tong') is not None:
                ket_qua_thi.append(item)

        def _max(mon):
            diem = [l.get('diem_tong') or 0 for l in lich_su_thi if l.get('mon_thi') == mon]
            return max(diem) if diem else 0

        for c in chung_chi:
            dm = c.get('danh_muc') or {}
            dm['get_loai_display'] = LOAI_CC.get(dm.get('loai'), dm.get('loai') or '')
            dm['ten_chung_chi'] = dm.get('ten_danh_muc', '')
            c['so_hieu'] = c.get('so_chung_chi', '')
        cc_hop_le = [c for c in chung_chi if c.get('trang_thai') == 'DAT']

        khoa_info = sinh_vien.get('khoa_info') or {}
        sinh_vien.update({
            'mssv': sinh_vien.get('ma_sv', ''),
            'khoa': khoa_info.get('ten_khoa') or sinh_vien.get('khoa') or '',
            'max_diem_dau_vao': _max('TA_DAU_VAO'),
            'co_thi_dau_vao': any(l.get('mon_thi') == 'TA_DAU_VAO' and (l.get('diem_tong') is not None or l.get('xep_loai')) for l in lich_su_thi),
            'dat_dau_vao': any(l.get('mon_thi') == 'TA_DAU_VAO' and l.get('ket_qua_dat') for l in lich_su_thi),
            'max_diem_ngoai_ngu': _max('CDR_NGOAI_NGU'),
            'max_diem_tin_hoc': _max('CDR_TIN_HOC'),
            'has_valid_cert_ngoai_ngu': any((c.get('danh_muc') or {}).get('loai') == 'NGOAI_NGU' for c in cc_hop_le),
            'has_valid_cert_tin_hoc': any((c.get('danh_muc') or {}).get('loai') == 'TIN_HOC' for c in cc_hop_le),
            'check_dat_ngoai_ngu': cdr.get('check_dat_ngoai_ngu', False),
            'check_dat_tin_hoc': cdr.get('check_dat_tin_hoc', False),
            'dat_chuan_dau_ra': cdr.get('dat_chuan_dau_ra', False),
        })

    context = {
        'sinh_vien': sinh_vien,
        'lich_su_thi': lich_su_thi,
        'chung_chi': chung_chi,
        'lich_thi_sap_toi': lich_thi_sap_toi,
        'ket_qua_thi': ket_qua_thi,
        'query_mssv': mssv,
        'thong_bao': thong_bao,
        'la_admin': la_admin,
    }
    return render(request, 'students/tra_cuu.html', context)


def lich_thi(request):
    """Portal: lịch thi CỦA THÍ SINH đang đăng nhập (theo từng đợt) + các đợt thi của Trung tâm."""
    today = datetime.now().date()
    dots = _cached_get_json(EXAM_SERVICE + 'dotthi/', ttl=120) or []
    if isinstance(dots, dict):
        dots = dots.get('results', [])
    sap_toi, da_qua = [], []
    for d in dots:
        _gan_trang_thai_dot(d)
        ket_thuc = _parse_ngay_vn(d.get('ngay_ket_thuc')) or _parse_ngay_vn(d.get('ngay_bat_dau'))
        (da_qua if ket_thuc and ket_thuc < today else sap_toi).append(d)
    sap_toi.sort(key=lambda d: d.get('ngay_bat_dau') or '')
    da_qua.sort(key=lambda d: d.get('ngay_bat_dau') or '', reverse=True)
    dot_map = {d.get('id'): d for d in dots}

    lich_cua_toi, lich_da_thi, sinh_vien = [], [], None
    if request.user.is_authenticated:
        sv_data = _cached_get_json(STUDENT_SERVICE + f'sinhvien/?ma_sv={request.user.username}', ttl=120)
        if isinstance(sv_data, dict):
            sv_data = sv_data.get('results', [])
        sinh_vien = next((sv for sv in (sv_data or []) if sv.get('ma_sv') == request.user.username), None)
        if sinh_vien and sinh_vien.get('id'):
            lst = _as_list_of(_cached_get_json(EXAM_SERVICE + f"lichsuthi/?sinh_vien_id={sinh_vien['id']}", ttl=30),
                              sinh_vien['id'])
            lich_cua_toi, lich_da_thi = _chia_lich_thi(lst, dot_map)

    return render(request, 'students/lich_thi.html', {
        'dot_sap_toi': sap_toi,
        'dot_da_qua': da_qua[:6],
        'lich_cua_toi': lich_cua_toi,
        'lich_da_thi': lich_da_thi[:10],
        'sinh_vien': sinh_vien,
    })


def dang_nhap(request):
    if request.method == 'POST':
        username = request.POST.get('mssv')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Cấp JWT ngay trong phiên (không gọi HTTP vòng lại chính gateway)
            get_access_token(request, force=True)

            messages.success(request, f'Chào mừng {user.get_full_name() or user.username}!')
            _log_activity(request, 'login', 'Đăng nhập hệ thống')
            return redirect('students:dashboard')
        else:
            messages.error(request, 'Sai tài khoản hoặc mật khẩu. Vui lòng thử lại.')

    return render(request, 'students/login.html')


def dang_xuat(request):
    logout(request)
    messages.info(request, 'Bạn đã đăng xuất thành công.')
    return redirect('students:home')

def quy_che_list(request):
    headers = _auth_headers(request)
    
    try:
        resp = requests.get(CMS_SERVICE + 'van-ban/', headers=headers, timeout=5)
        if resp.status_code == 200:
            van_ban_list = resp.json()
        else:
            van_ban_list = []
    except Exception:
        van_ban_list = []
    
    LOAI_VAN_BAN = [('QUY_CHE', 'Quy chế'), ('BIEU_MAU', 'Biểu mẫu'), ('HUONG_DAN', 'Hướng dẫn'), ('VAN_BAN', 'Văn bản khác')]
    loai_map = dict(LOAI_VAN_BAN)
    if isinstance(van_ban_list, dict):
        van_ban_list = van_ban_list.get('results', [])
    for vb in van_ban_list:
        vb['get_loai_display'] = loai_map.get(vb.get('loai'), vb.get('loai') or '')

    loai = request.GET.get('loai')
    if loai:
        van_ban_list = [vb for vb in van_ban_list if vb.get('loai') == loai]
    
    context = {
        'van_ban_list': van_ban_list,
        'loai_hien_tai': loai,
        'loai_choices': LOAI_VAN_BAN,
    }
    return render(request, 'students/quy_che_list.html', context)


def quy_che_detail(request, slug):
    headers = _auth_headers(request)
    
    try:
        resp = requests.get(
            CMS_SERVICE + f'van-ban/?slug={slug}',
            headers=headers,
            timeout=5
        )
        if resp.status_code == 200:
            results = resp.json()
            van_ban = results[0] if results else None
        else:
            van_ban = None
    except Exception:
        van_ban = None
    
    if not van_ban:
        raise Http404("Không tìm thấy văn bản")
    van_ban['get_loai_display'] = dict([('QUY_CHE', 'Quy chế'), ('BIEU_MAU', 'Biểu mẫu'), ('HUONG_DAN', 'Hướng dẫn'), ('VAN_BAN', 'Văn bản khác')]).get(van_ban.get('loai'), van_ban.get('loai') or '')

    context = {'van_ban': van_ban}
    return render(request, 'students/quy_che_detail.html', context)


# ====== ADMIN: IMPORT SINH VIÊN VÀO LỚP ======
@admin_required
def import_class_students(request, pk):
    if request.method == 'POST':
        lop_id = pk
        file = request.FILES.get('excel_file')
        if not file:
            messages.error(request, 'Vui lòng chọn file Excel!')
            return redirect('class_list')
        
        files = {'file': file}
        resp = call_api(request, 'POST', TRAINING_SERVICE + f'lop/{lop_id}/import-students/', files=files)
        
        if resp and resp.status_code == 200:
            data = resp.json()
            msg = f"Import thành công! Thêm mới: {data.get('created', 0)}, Đã tồn tại: {data.get('existed', 0)}"
            if data.get('not_found'):
                msg += f", Không tìm thấy: {data.get('not_found')}"
            messages.success(request, msg)
            if data.get('errors'):
                for err in data['errors'][:5]:
                    messages.warning(request, err)
        else:
            messages.error(request, 'Import thất bại! Vui lòng kiểm tra file.')
        return redirect('class_list')
    
    resp = call_api(request, 'GET', TRAINING_SERVICE + f'lop/{pk}/')
    lop = resp.json() if resp and resp.status_code == 200 else None
    if not lop:
        messages.error(request, 'Không tìm thấy lớp học!')
        return redirect('class_list')
    
    return render(request, 'admin/classes/import_students.html', {'lop': lop})


# ====== ADMIN: IMPORT LỊCH HỌC ======
@admin_required
def import_class_schedule(request):
    if request.method == 'POST':
        file = request.FILES.get('excel_file')
        if not file:
            messages.error(request, 'Vui lòng chọn file Excel!')
            return redirect('import_class_schedule')
        
        files = {'file': file}
        resp = call_api(request, 'POST', TRAINING_SERVICE + 'lop/import-schedule/', files=files)
        
        if resp and resp.status_code == 200:
            data = resp.json()
            messages.success(request, f"Import lịch học thành công! {data.get('message', '')}")
            if data.get('errors'):
                for err in data['errors'][:5]:
                    messages.warning(request, err)
        else:
            messages.error(request, 'Import lịch học thất bại! Vui lòng kiểm tra file.')
        return redirect('class_list')
    
    return render(request, 'admin/classes/import_schedule.html')


# ========== QUẢN LÝ SINH VIÊN (ADMIN) ==========

@admin_required
def student_list(request):
    search = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    khoa_filter = request.GET.get('khoa', '')

    params = {}
    if search:
        params['search'] = search
    if khoa_filter:
        params['khoa'] = khoa_filter

    resp = call_api(request, 'GET', STUDENT_SERVICE + 'sinhvien/', params=params)
    if resp and resp.status_code == 200:
        students = resp.json()
        if isinstance(students, dict):
            students = students.get('results', [])
    else:
        students = []

    # Normalize: them full_name alias cho template
    for s in students:
        if 'ho_ten' in s and 'full_name' not in s:
            s['full_name'] = s['ho_ten']

    # Fetch list khoa cho filter dropdown
    list_khoa = []
    try:
        resp_k = call_api(request, 'GET', STUDENT_SERVICE + 'khoa/')
        if resp_k and resp_k.status_code == 200:
            list_khoa = resp_k.json()
            if isinstance(list_khoa, dict):
                list_khoa = list_khoa.get('results', [])
    except Exception:
        pass

    paginator = Paginator(students, 20)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'admin/students/student_list.html', {
        'sinhviens': page_obj,
        'students': page_obj,
        'list_khoa': list_khoa,
        'search': search,
        'khoa_filter': khoa_filter,
        'paginator': paginator,
    })

@admin_required
def student_detail(request, student_id):
    resp = call_api(request, 'GET', STUDENT_SERVICE + f'sinhvien/{student_id}/')
    if resp and resp.status_code == 200:
        student = resp.json()
    else:
        messages.error(request, 'Không tìm thấy sinh viên')
        return redirect('student_list')
    
    cert_resp = call_api(request, 'GET', CERT_SERVICE + 'danhmuc/')
    danh_muc_cc = cert_resp.json() if cert_resp and cert_resp.status_code == 200 else []
    
    reg_resp = call_api(request, 'GET', TRAINING_SERVICE + 'dangky/?sinh_vien_id=' + str(student_id))
    ds_dang_ky = _as_list_of(reg_resp.json() if reg_resp and reg_resp.status_code == 200 else [], student_id)
    
    exam_resp = call_api(request, 'GET', EXAM_SERVICE + 'lichsuthi/?sinh_vien_id=' + str(student_id))
    lich_su_thi = _as_list_of(exam_resp.json() if exam_resp and exam_resp.status_code == 200 else [], student_id)

    # Template dùng tên trường cũ -> ánh xạ từ dữ liệu API của student-service
    cdr_resp = call_api(request, 'GET', STUDENT_SERVICE + f'sinhvien/{student_id}/cdr-status/')
    cdr = cdr_resp.json() if cdr_resp and cdr_resp.status_code == 200 else {}
    student.update({
        'full_name': student.get('ho_ten', ''),
        'ma_sinh_vien': student.get('ma_sv', ''),
        'email': student.get('email_truong') or student.get('email_ca_nhan') or '',
        'sdt': student.get('so_dien_thoai', ''),
        'get_gioi_tinh_display': student.get('gioi_tinh', ''),
        'khoa': student.get('khoa_info') or {},
        'nganh': student.get('nganh_info') or {},
        'lop': {'ten_lop': student.get('lop') or ''},
        'dat_ngoai_ngu': cdr.get('check_dat_ngoai_ngu', student.get('dat_ngoai_ngu', False)),
        'dat_tin_hoc': cdr.get('check_dat_tin_hoc', student.get('dat_tin_hoc', False)),
        'dat_chuan_dau_ra': cdr.get('dat_chuan_dau_ra', student.get('dat_chuan_dau_ra', False)),
    })

    return render(request, 'admin/students/student_detail.html', {
        'student': student,
        'danh_muc_cc': danh_muc_cc,
        'ds_dang_ky': ds_dang_ky,
        'lich_su_thi': lich_su_thi,
    })

@admin_required
def student_create(request):
    from .forms import StudentForm

    # Load khoa + nganh từ API
    khoa_resp = call_api(request, 'GET', STUDENT_SERVICE + 'khoa/')
    khoas = khoa_resp.json() if khoa_resp and khoa_resp.status_code == 200 else []

    nganh_resp = call_api(request, 'GET', STUDENT_SERVICE + 'nganh/')
    nganhs = nganh_resp.json() if nganh_resp and nganh_resp.status_code == 200 else []

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, khoas=khoas, nganhs=nganhs)
        if form.is_valid():
            d = form.cleaned_data
            data = {
                'ma_sv': d['ma_sv'],
                'ho_ten': d['ho_ten'],
                'ngay_sinh': d.get('ngay_sinh').isoformat() if d.get('ngay_sinh') else None,
                'gioi_tinh': d.get('gioi_tinh') or '',
                'email_truong': d.get('email_truong') or None,
                'email_ca_nhan': d.get('email_ca_nhan') or None,
                'so_dien_thoai': d.get('so_dien_thoai') or '',
                'khoa': int(d['khoa']) if d.get('khoa') else None,
                'nganh': int(d['nganh']) if d.get('nganh') else None,
                'khoa_hoc': d.get('khoa_hoc') or '',
                'nam_nhap_hoc': d.get('nam_nhap_hoc') or None,
                'lop': d.get('lop') or '',
            }
            files = None
            if 'anh_dai_dien' in request.FILES:
                files = {'anh_dai_dien': request.FILES['anh_dai_dien']}

            resp = call_api(request, 'POST', STUDENT_SERVICE + 'sinhvien/', data=data, files=files)
            if resp and resp.status_code in [200, 201]:
                messages.success(request, 'Thêm sinh viên thành công!')
                return redirect('student_list')
            else:
                err = resp.text[:300] if resp else 'Không kết nối được service'
                messages.error(request, f'Thêm sinh viên thất bại: {err}')
        else:
            messages.error(request, 'Vui lòng kiểm tra lại các trường báo lỗi.')
    else:
        form = StudentForm(khoas=khoas, nganhs=nganhs)

    return render(request, 'admin/students/student_form.html', {
        'form': form,
        'khoas': khoas,
        'nganhs': nganhs,
        'student': None,
    })


@admin_required
def student_edit(request, student_id):
    from .forms import StudentForm

    khoa_resp = call_api(request, 'GET', STUDENT_SERVICE + 'khoa/')
    khoas = khoa_resp.json() if khoa_resp and khoa_resp.status_code == 200 else []

    nganh_resp = call_api(request, 'GET', STUDENT_SERVICE + 'nganh/')
    nganhs = nganh_resp.json() if nganh_resp and nganh_resp.status_code == 200 else []

    resp = call_api(request, 'GET', STUDENT_SERVICE + f'sinhvien/{student_id}/')
    if not (resp and resp.status_code == 200):
        messages.error(request, 'Không tìm thấy sinh viên')
        return redirect('student_list')
    student = resp.json()

    initial = {
        'ma_sv': student.get('ma_sv', ''),
        'ho_ten': student.get('ho_ten', ''),
        'ngay_sinh': student.get('ngay_sinh'),
        'gioi_tinh': student.get('gioi_tinh', ''),
        'email_truong': student.get('email_truong', ''),
        'email_ca_nhan': student.get('email_ca_nhan', ''),
        'so_dien_thoai': student.get('so_dien_thoai', ''),
        'khoa': str(student.get('khoa') or ''),
        'nganh': str(student.get('nganh') or ''),
        'khoa_hoc': student.get('khoa_hoc', ''),
        'nam_nhap_hoc': student.get('nam_nhap_hoc'),
        'lop': student.get('lop', ''),
        'khoa_id': student.get('khoa'),
        'nganh_id': student.get('nganh'),
    }

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, khoas=khoas, nganhs=nganhs)
        if form.is_valid():
            d = form.cleaned_data
            data = {
                'ma_sv': d['ma_sv'],
                'ho_ten': d['ho_ten'],
                'ngay_sinh': d.get('ngay_sinh').isoformat() if d.get('ngay_sinh') else None,
                'gioi_tinh': d.get('gioi_tinh') or '',
                'email_truong': d.get('email_truong') or None,
                'email_ca_nhan': d.get('email_ca_nhan') or None,
                'so_dien_thoai': d.get('so_dien_thoai') or '',
                'khoa': int(d['khoa']) if d.get('khoa') else None,
                'nganh': int(d['nganh']) if d.get('nganh') else None,
                'khoa_hoc': d.get('khoa_hoc') or '',
                'nam_nhap_hoc': d.get('nam_nhap_hoc') or None,
                'lop': d.get('lop') or '',
            }
            files = None
            if 'anh_dai_dien' in request.FILES:
                files = {'anh_dai_dien': request.FILES['anh_dai_dien']}

            r = call_api(request, 'PUT', STUDENT_SERVICE + f'sinhvien/{student_id}/', data=data, files=files)
            if r and r.status_code == 200:
                messages.success(request, 'Cập nhật thành công!')
                return redirect('student_detail', student_id=student_id)
            else:
                err = r.text[:300] if r else 'Không kết nối được service'
                messages.error(request, f'Cập nhật thất bại: {err}')
        else:
            messages.error(request, 'Vui lòng kiểm tra lại các trường báo lỗi.')
    else:
        form = StudentForm(initial=initial, khoas=khoas, nganhs=nganhs)

    return render(request, 'admin/students/student_form.html', {
        'form': form,
        'khoas': khoas,
        'nganhs': nganhs,
        'student': student,
    })
@admin_required
def student_delete(request, student_id):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', STUDENT_SERVICE + f'sinhvien/{student_id}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa sinh viên thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('student_list')


# ========== PHÂN LOẠI SINH VIÊN ==========
@admin_required
def phan_loai_sinh_vien(request):
    headers = _auth_headers(request)

    loai = request.GET.get('loai', 'tat_ca')
    khoa_id = request.GET.get('khoa_id')
    khoa_hoc = request.GET.get('khoa_hoc')
    search = request.GET.get('search', '')

    students = []
    resp = call_api(request, 'GET', STUDENT_SERVICE + 'sinhvien/')
    if resp and resp.status_code == 200:
        students = resp.json()

    chua_dat_list = []
    resp2 = call_api(request, 'GET', REPORT_SERVICE + 'chua-dat-chuan/?loai=all')
    if resp2 and resp2.status_code == 200:
        chua_dat_list = resp2.json().get('results', [])

    cdr_status = {}
    for sv in chua_dat_list:
        cdr_status[sv.get('ma_sv')] = {
            'dat_ngoai_ngu': sv.get('dat_ngoai_ngu', False),
            'dat_tin_hoc': sv.get('dat_tin_hoc', False),
            'dat_chuan_dau_ra': sv.get('dat_chuan_dau_ra', False)
        }

    filtered = []
    for sv in students:
        ma_sv = sv.get('ma_sv')
        status = cdr_status.get(ma_sv, {'dat_ngoai_ngu': False, 'dat_tin_hoc': False, 'dat_chuan_dau_ra': False})
        sv['dat_ngoai_ngu'] = status['dat_ngoai_ngu']
        sv['dat_tin_hoc'] = status['dat_tin_hoc']
        sv['dat_chuan_dau_ra'] = status['dat_chuan_dau_ra']

        if search and search.lower() not in sv.get('ho_ten', '').lower() and search not in ma_sv:
            continue
        if khoa_id and str(sv.get('khoa_info', {}).get('id')) != khoa_id:
            continue
        if khoa_hoc and sv.get('khoa_hoc') != khoa_hoc:
            continue
        if loai == 'da_dat' and not sv['dat_chuan_dau_ra']:
            continue
        if loai == 'chua_dat' and sv['dat_chuan_dau_ra']:
            continue
        if loai == 'canh_bao' and (sv['dat_chuan_dau_ra'] or sv.get('khoa_hoc', '') not in ['K63', 'K64', 'K65']):
            continue

        filtered.append(sv)

    dat = sum(1 for sv in filtered if sv['dat_chuan_dau_ra'])
    chua_dat = len(filtered) - dat
    canh_bao = sum(1 for sv in filtered if sv.get('khoa_hoc', '') in ['K63', 'K64', 'K65'] and not sv['dat_chuan_dau_ra'])

    khoas = []
    resp3 = call_api(request, 'GET', STUDENT_SERVICE + 'khoa/')
    if resp3 and resp3.status_code == 200:
        khoas = resp3.json()

    context = {
        'students': filtered,
        'tong': len(filtered),
        'dat': dat,
        'chua_dat': chua_dat,
        'canh_bao': canh_bao,
        'loai': loai,
        'khoa_id': khoa_id,
        'khoa_hoc': khoa_hoc,
        'search': search,
        'khoas': khoas,
    }
    return render(request, 'admin/reports/phan_loai_sv.html', context)


# ========== DANH SÁCH CẢNH BÁO ==========
@admin_required
def danh_sach_canh_bao(request):
    resp = call_api(request, 'GET', REPORT_SERVICE + 'chua-dat-chuan/?loai=all')
    students = []
    if resp and resp.status_code == 200:
        all_results = resp.json().get('results', [])
        final_year_codes = ['K63', 'K64', 'K65']
        students = [sv for sv in all_results if sv.get('khoa_hoc', '') in final_year_codes]

    tong = len(students)
    chua_dat_nn = sum(1 for sv in students if not sv.get('dat_ngoai_ngu', False))
    chua_dat_th = sum(1 for sv in students if not sv.get('dat_tin_hoc', False))
    chua_dat_ca_2 = sum(1 for sv in students if not sv.get('dat_ngoai_ngu', False) and not sv.get('dat_tin_hoc', False))

    context = {
        'students': students,
        'tong': tong,
        'chua_dat_nn': chua_dat_nn,
        'chua_dat_th': chua_dat_th,
        'chua_dat_ca_2': chua_dat_ca_2,
    }
    return render(request, 'admin/reports/danh_sach_canh_bao.html', context)


# ========== GỬI CẢNH BÁO ==========
@admin_required
def gui_canh_bao(request):
    stats = {'tat_ca': 0, 'nam_cuoi': 0, 'chua_dat_nn': 0, 'chua_dat_th': 0}
    resp = call_api(request, 'GET', REPORT_SERVICE + 'chua-dat-chuan/?loai=all')
    if resp and resp.status_code == 200:
        data = resp.json()
        all_results = data.get('results', [])
        stats['tat_ca'] = len(all_results)
        stats['chua_dat_nn'] = sum(1 for sv in all_results if not sv.get('dat_ngoai_ngu', False))
        stats['chua_dat_th'] = sum(1 for sv in all_results if not sv.get('dat_tin_hoc', False))
        final_year_codes = ['K63', 'K64', 'K65']
        stats['nam_cuoi'] = sum(1 for sv in all_results if sv.get('khoa_hoc', '') in final_year_codes and not sv.get('dat_chuan_dau_ra', False))

    if request.method == 'POST':
        loai_canh_bao = request.POST.get('loai_canh_bao')
        noi_dung = request.POST.get('noi_dung')
        gui_email = request.POST.get('gui_email') == 'on'

        if not loai_canh_bao or not noi_dung:
            messages.error(request, 'Vui lòng chọn đối tượng và nhập nội dung')
            return redirect('gui_canh_bao')

        students_to_notify = []
        if loai_canh_bao == 'tat_ca':
            resp = call_api(request, 'GET', REPORT_SERVICE + 'chua-dat-chuan/?loai=all')
            if resp and resp.status_code == 200:
                students_to_notify = resp.json().get('results', [])
        elif loai_canh_bao == 'nam_cuoi':
            resp = call_api(request, 'GET', REPORT_SERVICE + 'chua-dat-chuan/?loai=all')
            if resp and resp.status_code == 200:
                all_results = resp.json().get('results', [])
                final_year_codes = ['K63', 'K64', 'K65']
                students_to_notify = [sv for sv in all_results if sv.get('khoa_hoc', '') in final_year_codes and not sv.get('dat_chuan_dau_ra', False)]
        elif loai_canh_bao == 'chua_dat_nn':
            resp = call_api(request, 'GET', REPORT_SERVICE + 'chua-dat-chuan/?loai=nn')
            if resp and resp.status_code == 200:
                students_to_notify = resp.json().get('results', [])
        elif loai_canh_bao == 'chua_dat_th':
            resp = call_api(request, 'GET', REPORT_SERVICE + 'chua-dat-chuan/?loai=th')
            if resp and resp.status_code == 200:
                students_to_notify = resp.json().get('results', [])

        created = 0
        for sv in students_to_notify:
            data = {
                'sinh_vien_id': sv.get('id'),
                'tieu_de': 'Cảnh báo chưa đạt Chuẩn đầu ra',
                'noi_dung': noi_dung,
                'muc_do': 'HIGH'
            }
            try:
                resp = call_api(request, 'POST', NOTIFICATION_SERVICE + 'canhbao/', data=data)
                if resp and resp.status_code in [200, 201]:
                    created += 1
            except:
                pass

        messages.success(request, f'Đã gửi cảnh báo đến {created} sinh viên')
        return redirect('danh_sach_canh_bao')

    context = {'stats': stats}
    return render(request, 'admin/reports/gui_canh_bao.html', context)


# ========== VIEW CHO ADMIN: CÁC CHỨC NĂNG BỔ SUNG ==========

@admin_required
def cert_list(request):
    resp = call_api(request, 'GET', CERT_SERVICE + 'chungchi/?trang_thai=CHO')
    certs = resp.json() if resp and resp.status_code == 200 else []
    total_pending = len(certs)
    return render(request, 'admin/certificates/cert_list.html', {
        'pending_certs': certs,
        'total_pending': total_pending,
        'search_query': request.GET.get('q', '')
    })

@admin_required
def bao_luu_diem_list(request):
    resp = call_api(request, 'GET', EXAM_SERVICE + 'baoluudiem/')
    bao_luus = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin/reports/bao_luu_diem_list.html', {
        'bao_luus': bao_luus,
        'tong': len(bao_luus)
    })

@admin_required
def export_chua_dat_chuan(request):
    resp = call_api(request, 'GET', REPORT_SERVICE + 'export-chua-dat-chuan/')
    if resp and resp.status_code == 200:
        response = HttpResponse(resp.content, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="danh_sach_chua_dat_chuan.xlsx"'
        return response
    messages.error(request, 'Không thể xuất danh sách.')
    return redirect('admin_mofi_dashboard')

@admin_required
def registration_list(request):
    res = parallel_api_get(request, [TRAINING_SERVICE + 'dangky/', TRAINING_SERVICE + 'lop/'], ttl=30)
    regs = res.get(TRAINING_SERVICE + 'dangky/') or []
    lops = res.get(TRAINING_SERVICE + 'lop/') or []
    if isinstance(regs, dict):
        regs = regs.get('results', [])
    if isinstance(lops, dict):
        lops = lops.get('results', [])

    lop_filter = request.GET.get('lop', '')
    trang_thai = request.GET.get('trang_thai', 'PENDING')
    if lop_filter:
        regs = [r for r in regs if str(r.get('lop')) == lop_filter]
    so_cho_duyet = sum(1 for r in regs if r.get('trang_thai') == 'PENDING')
    if trang_thai and trang_thai != 'ALL':
        regs = [r for r in regs if r.get('trang_thai') == trang_thai]
    regs = sorted(regs, key=lambda r: r.get('ngay_dang_ky') or '', reverse=True)

    return render(request, 'admin/classes/registration_list.html', {
        'registrations': _enrich_registrations(request, regs, lops),
        'lops': lops,
        'lop_filter': lop_filter,
        'trang_thai': trang_thai,
        'so_cho_duyet': so_cho_duyet,
    })

@admin_required
def export_bang_diem(request, pk):
    dot_thi_id = pk
    try:
        resp = requests.get(EXAM_SERVICE + f'dotthi/{dot_thi_id}/export-scores/', timeout=120,
                            headers=_auth_headers(request))
    except requests.exceptions.RequestException:
        resp = None
    if resp is not None and resp.status_code == 200:
        response = HttpResponse(resp.content, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = resp.headers.get('Content-Disposition') or f'attachment; filename="bang_diem_{dot_thi_id}.xlsx"'
        return response
    messages.error(request, 'Xuất file thất bại.')
    return redirect('dot_thi_detail', pk=dot_thi_id)

@admin_required
def mofi_thongbao_send_email(request, pk):
    thongbao_id = pk
    if request.method == 'POST':
        resp = call_api(request, 'POST', NOTIFICATION_SERVICE + f'thongbao/{thongbao_id}/send-email/')
        if resp and resp.status_code == 200:
            messages.success(request, 'Đã gửi email thành công.')
        else:
            messages.error(request, 'Gửi email thất bại.')
    return redirect('thongbao_list')

@admin_required
def verify_certificate(request, pk):
    if request.method == 'POST':
        action = request.POST.get('action')
        ghi_chu = request.POST.get('ghi_chu', '')
        if action == 'approve':
            resp = call_api(request, 'PATCH', CERT_SERVICE + f'chungchi/{pk}/', data={'trang_thai': 'DAT', 'ghi_chu_xac_minh': ghi_chu})
        elif action == 'reject':
            resp = call_api(request, 'PATCH', CERT_SERVICE + f'chungchi/{pk}/', data={'trang_thai': 'TU_CHOI', 'ghi_chu_xac_minh': ghi_chu})
        elif action == 'delete':
            resp = call_api(request, 'DELETE', CERT_SERVICE + f'chungchi/{pk}/')
        else:
            messages.error(request, 'Hành động không hợp lệ.')
            return redirect('cert_list')
        
        if resp and resp.status_code in [200, 201, 204]:
            messages.success(request, 'Cập nhật chứng chỉ thành công.')
        else:
            messages.error(request, 'Thao tác thất bại.')
    return redirect('cert_list')

@admin_required
def registration_approve(request, pk):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            data = {'trang_thai': 'DA_DUYET'}
        elif action == 'reject':
            data = {'trang_thai': 'TU_CHOI'}
        else:
            messages.error(request, 'Hành động không hợp lệ.')
            return redirect('registration_list')
        
        # Ưu tiên action /approve/ của training-service (cập nhật luôn sĩ số lớp)
        resp = call_api(request, 'POST', TRAINING_SERVICE + f'dangky/{pk}/approve/', data={'action': action})
        if not resp or resp.status_code in (404, 405):
            resp = call_api(request, 'PATCH', TRAINING_SERVICE + f'dangky/{pk}/', data=data)
        if resp and resp.status_code == 200:
            messages.success(request, 'Đã duyệt đơn đăng ký.' if action == 'approve' else 'Đã từ chối đơn đăng ký.')
        else:
            messages.error(request, 'Thao tác thất bại.')
    return redirect('registration_list')


# ========== VIEW CHO PORTAL: NỘP CHỨNG CHỈ ==========
@login_required
def nop_chung_chi(request):
    if request.method == 'POST':
        username = request.user.username
        resp = call_api(request, 'GET', STUDENT_SERVICE + f'sinhvien/?ma_sv={username}')
        sinh_vien = None
        if resp and resp.status_code == 200:
            data = resp.json()
            sinh_vien = data[0] if data else None
        if not sinh_vien:
            messages.error(request, 'Không tìm thấy sinh viên.')
            return redirect('students:dashboard')
        
        data = {
            'sinh_vien_id': sinh_vien['id'],
            'danh_muc_id': request.POST.get('danh_muc_id'),
            'so_hieu': request.POST.get('so_hieu'),
            'ngay_cap': request.POST.get('ngay_cap'),
            'trang_thai': 'CHO',
        }
        files = None
        if 'file_minh_chung' in request.FILES:
            files = {'file_minh_chung': request.FILES['file_minh_chung']}
        
        resp = call_api(request, 'POST', CERT_SERVICE + 'chungchi/', data=data, files=files)
        if resp and resp.status_code in [200, 201]:
            messages.success(request, 'Nộp chứng chỉ thành công! Đang chờ xét duyệt.')
        else:
            messages.error(request, 'Nộp chứng chỉ thất bại.')
        return redirect('students:dashboard')
    
    resp = call_api(request, 'GET', CERT_SERVICE + 'danhmuc/')
    danh_muc_cc = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'students/nop_chung_chi.html', {'danh_muc_cc': danh_muc_cc})

@login_required
def quick_add_cert_portal(request):
    if request.method == 'POST':
        username = request.user.username
        resp = call_api(request, 'GET', STUDENT_SERVICE + f'sinhvien/?ma_sv={username}')
        sinh_vien = None
        if resp and resp.status_code == 200:
            data = resp.json()
            sinh_vien = data[0] if data else None
        if not sinh_vien:
            messages.error(request, 'Không tìm thấy sinh viên.')
            return redirect('students:dashboard')
        
        data = {
            'sinh_vien_id': sinh_vien['id'],
            'danh_muc_id': request.POST.get('danh_muc_id'),
            'so_hieu': request.POST.get('so_hieu'),
            'ngay_cap': request.POST.get('ngay_cap'),
            'trang_thai': 'CHO',
            'diem_so': request.POST.get('diem_so', 0),
            'hinh_thuc_thi': request.POST.get('hinh_thuc_thi', ''),
        }
        files = None
        if 'file_minh_chung' in request.FILES:
            files = {'file_minh_chung': request.FILES['file_minh_chung']}
        
        resp = call_api(request, 'POST', CERT_SERVICE + 'chungchi/', data=data, files=files)
        if resp and resp.status_code in [200, 201]:
            messages.success(request, 'Nộp chứng chỉ thành công! Đang chờ duyệt.')
        else:
            messages.error(request, 'Nộp thất bại.')
        return redirect('students:dashboard')
    
    return redirect('students:dashboard')

@login_required
def student_delete_cert(request, cert_id):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', CERT_SERVICE + f'chungchi/{cert_id}/')
        if resp and resp.status_code in [200, 204]:
            messages.success(request, 'Xóa chứng chỉ thành công.')
        else:
            messages.error(request, 'Xóa thất bại.')
    return redirect('students:dashboard')

@admin_required
def quick_add_chung_chi(request, student_id):
    if request.method == 'POST':
        data = {
            'sinh_vien_id': student_id,
            'danh_muc_id': request.POST.get('danh_muc_id'),
            'so_hieu': request.POST.get('so_hieu'),
            'ngay_cap': request.POST.get('ngay_cap'),
            'trang_thai': 'CHO',
        }
        files = None
        if 'file_minh_chung' in request.FILES:
            files = {'file_minh_chung': request.FILES['file_minh_chung']}
        
        resp = call_api(request, 'POST', CERT_SERVICE + 'chungchi/', data=data, files=files)
        if resp and resp.status_code in [200, 201]:
            messages.success(request, 'Đã thêm chứng chỉ.')
        else:
            messages.error(request, 'Thêm thất bại.')
    return redirect('student_detail', student_id=student_id)

@admin_required
def quick_add_diem(request, student_id):
    if request.method == 'POST':
        dot_thi_id = request.POST.get('dot_thi')
        mon_thi = request.POST.get('mon_thi')
        try:
            d1 = float(request.POST.get('diem_tp1') or 0)
            d2 = float(request.POST.get('diem_tp2') or 0)
        except ValueError:
            messages.error(request, 'Điểm không hợp lệ.')
            return redirect('student_detail', student_id=student_id)
        diem_tong = d1 + d2
        ket_qua_dat = diem_tong >= DIEM_DAT.get(mon_thi, 50)
        
        data = {
            'sinh_vien_id': student_id,
            'dot_thi': dot_thi_id,          # serializer LichSuThi dùng khoá "dot_thi"
            'mon_thi': mon_thi,
            'diem_thanh_phan_1': d1,
            'diem_thanh_phan_2': d2,
            'diem_tong': diem_tong,
            'ket_qua_dat': ket_qua_dat,
        }
        resp = call_api(request, 'POST', EXAM_SERVICE + 'lichsuthi/', data=data)
        if resp and resp.status_code in [200, 201]:
            messages.success(request, 'Đã thêm điểm thi.')
        else:
            messages.error(request, 'Thêm thất bại.')
    return redirect('student_detail', student_id=student_id)


@login_required
def cap_nhat_ho_so(request):
    if request.method == 'POST':
        username = request.user.username
        try:
            resp = requests.get(STUDENT_SERVICE + f'sinhvien/?ma_sv={username}', timeout=5)
            if resp.status_code == 200:
                students = resp.json()
                sinh_vien = students[0] if students else None
            else:
                sinh_vien = None
        except:
            sinh_vien = None

        if not sinh_vien:
            messages.error(request, 'Không tìm thấy sinh viên.')
            return redirect('students:dashboard')

        student_id = sinh_vien.get('id')
        data = {
            'so_dien_thoai': request.POST.get('so_dien_thoai', ''),
            'email_ca_nhan': request.POST.get('email_ca_nhan', ''),
        }
        files = None
        if 'anh_dai_dien' in request.FILES:
            files = {'anh_dai_dien': request.FILES['anh_dai_dien']}

        resp = call_api(request, 'PATCH', STUDENT_SERVICE + f'sinhvien/{student_id}/', data=data, files=files)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật thông tin thành công!')
        else:
            messages.error(request, 'Cập nhật thất bại. Vui lòng thử lại.')
        return redirect('students:dashboard')
    return redirect('students:dashboard')


# =========================================================
# PROFILE VIEWS (admin + sinh viên)
# =========================================================
from users.forms import (
    UserUpdateForm,
    UserProfileForm,
    AvatarUploadForm,
    CustomPasswordChangeForm,
)
from users.models import UserActivity, UserProfile as _UserProfile


def teacher_required(view_func):
    """Cho phép admin hoặc teacher."""
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("students:dang_nhap")
        profile = getattr(request.user, "profile", None)
        if not profile or profile.role not in ("admin", "teacher"):
            raise PermissionDenied("Chỉ admin/giảng viên được truy cập")
        return view_func(request, *args, **kwargs)
    return _wrapped




def _client_ip(request):
    xff = request.META.get('HTTP_X_FORWARDED_FOR')
    if xff:
        return xff.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


def _log_activity(request, action, description=''):
    """Ghi log hoạt động của user hiện tại."""
    try:
        if not request.user.is_authenticated:
            return
        UserActivity.objects.create(
            user=request.user,
            action=action,
            description=description[:255],
            ip_address=_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', '')[:255],
        )
    except Exception:
        pass


def _get_profile_context(request):
    """Build context chung cho trang profile."""
    user = request.user
    profile, _ = _UserProfile.objects.get_or_create(user=user)
    activities = UserActivity.objects.filter(user=user)[:30]
    return {
        'profile_user': user,
        'profile': profile,
        'activities': activities,
        'user_form': UserUpdateForm(instance=user),
        'profile_form': UserProfileForm(instance=profile),
        'password_form': CustomPasswordChangeForm(user=user),
        'avatar_form': AvatarUploadForm(instance=profile),
    }


def _redirect_target(request, default):
    """Chọn URL redirect theo 'next' hoặc default."""
    return request.POST.get('next') or default


def admin_profile(request):
    """Trang profile cho ADMIN — layout DreamLMS."""
    if not request.user.is_authenticated:
        return redirect('students:dang_nhap')
    profile = getattr(request.user, 'profile', None)
    if not profile or profile.role != 'admin':
        # Sinh viên/giảng viên dùng trang hồ sơ của cổng sinh viên
        return redirect('students:student_profile')
    context = _get_profile_context(request)
    return render(request, 'admin/profile/index.html', context)


def student_profile(request):
    """Trang profile cho SINH VIÊN — layout portal."""
    if not request.user.is_authenticated:
        return redirect('students:dang_nhap')
    context = _get_profile_context(request)
    return render(request, 'students/profile/index.html', context)


@require_POST
def profile_update(request):
    """POST: cập nhật thông tin User + Profile."""
    if not request.user.is_authenticated:
        return redirect('students:dang_nhap')

    profile, _ = _UserProfile.objects.get_or_create(user=request.user)
    uf = UserUpdateForm(request.POST, instance=request.user)
    pf = UserProfileForm(request.POST, instance=profile)

    if uf.is_valid() and pf.is_valid():
        uf.save()
        pf.save()
        _log_activity(request, 'update_profile', 'Cập nhật thông tin cá nhân')
        messages.success(request, 'Cập nhật thông tin thành công!')
    else:
        for form in (uf, pf):
            for field, errors in form.errors.items():
                for e in errors:
                    messages.error(request, f'{field}: {e}')

    return redirect(_redirect_target(request, 'students:dashboard'))


@require_POST
def profile_change_password(request):
    """POST: đổi mật khẩu."""
    if not request.user.is_authenticated:
        return redirect('students:dang_nhap')

    form = CustomPasswordChangeForm(request.user, request.POST)
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        _log_activity(request, 'change_password', 'Đổi mật khẩu thành công')
        messages.success(request, 'Đổi mật khẩu thành công!')
    else:
        for field, errors in form.errors.items():
            for e in errors:
                messages.error(request, e)

    return redirect(_redirect_target(request, 'students:dashboard'))


@require_POST
def profile_upload_avatar(request):
    """POST: upload ảnh đại diện."""
    if not request.user.is_authenticated:
        return redirect('students:dang_nhap')

    profile, _ = _UserProfile.objects.get_or_create(user=request.user)
    form = AvatarUploadForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
        form.save()
        _log_activity(request, 'upload_avatar', 'Cập nhật ảnh đại diện')
        messages.success(request, 'Cập nhật ảnh đại diện thành công!')
    else:
        for field, errors in form.errors.items():
            for e in errors:
                messages.error(request, e)

    return redirect(_redirect_target(request, 'students:dashboard'))
