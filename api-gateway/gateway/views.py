import os  # <-- THÊM DÒNG NÀY
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

# ----- CẤU HÌNH SERVICE URLs (DÙNG BIẾN MÔI TRƯỜNG) -----
STUDENT_SERVICE = os.getenv('STUDENT_SERVICE_URL', 'http://localhost:8001/api/')
EXAM_SERVICE = os.getenv('EXAM_SERVICE_URL', 'http://localhost:8002/api/')
CERT_SERVICE = os.getenv('CERTIFICATE_SERVICE_URL', 'http://localhost:8003/api/')
TRAINING_SERVICE = os.getenv('TRAINING_SERVICE_URL', 'http://localhost:8004/api/')
NOTIFICATION_SERVICE = os.getenv('NOTIFICATION_SERVICE_URL', 'http://localhost:8005/api/')
CMS_SERVICE = os.getenv('CMS_SERVICE_URL', 'http://localhost:8006/api/')
REPORT_SERVICE = os.getenv('REPORT_SERVICE_URL', 'http://localhost:8007/api/')


# ----- HÀM GỌI API CHUNG -----
def call_api(request, method, url, data=None, files=None, params=None):
    """Gọi API qua Gateway với token và xử lý lỗi"""
    token = request.session.get('access_token')
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    
    try:
        if method.upper() == 'GET':
            resp = requests.get(url, headers=headers, params=params, timeout=10)
        elif method.upper() == 'POST':
            if files:
                # Upload file: không set Content-Type
                headers.pop('Content-Type', None)
                resp = requests.post(url, headers=headers, data=data, files=files, timeout=30)
            else:
                resp = requests.post(url, headers=headers, json=data, timeout=10)
        elif method.upper() == 'PUT':
            resp = requests.put(url, headers=headers, json=data, timeout=10)
        elif method.upper() == 'PATCH':
            resp = requests.patch(url, headers=headers, json=data, timeout=10)
        elif method.upper() == 'DELETE':
            resp = requests.delete(url, headers=headers, timeout=10)
        else:
            return None
        return resp
    except requests.exceptions.RequestException as e:
        return None


# ================================================================
# VIEWS CHO ADMIN (namespace: admin_mofi)
# ================================================================

# ----- DASHBOARD ----- (đã có)

# ----- QUẢN LÝ KHOA -----
@login_required
def khoa_list(request):
    """Danh sách khoa"""
    resp = call_api(request, 'GET', STUDENT_SERVICE + 'khoa/')
    khoas = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin_mofi/system/khoa_list.html', {'danh_sach_khoa': khoas})

@login_required
def khoa_create(request):
    if request.method == 'POST':
        data = {
            'ma_khoa': request.POST.get('ma_khoa'),
            'ten_khoa': request.POST.get('ten_khoa'),
        }
        resp = call_api(request, 'POST', STUDENT_SERVICE + 'khoa/', data=data)
        if resp and resp.status_code == 201:
            messages.success(request, 'Thêm khoa thành công!')
            return redirect('admin_mofi:khoa_list')
        else:
            messages.error(request, 'Thêm khoa thất bại!')
    return render(request, 'admin_mofi/system/khoa_form.html', {'instance': None})

@login_required
def khoa_edit(request, pk):
    if request.method == 'POST':
        data = {
            'ma_khoa': request.POST.get('ma_khoa'),
            'ten_khoa': request.POST.get('ten_khoa'),
        }
        resp = call_api(request, 'PUT', STUDENT_SERVICE + f'khoa/{pk}/', data=data)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật khoa thành công!')
            return redirect('admin_mofi:khoa_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', STUDENT_SERVICE + f'khoa/{pk}/')
    khoa = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin_mofi/system/khoa_form.html', {'instance': khoa})

@login_required
def khoa_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', STUDENT_SERVICE + f'khoa/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa khoa thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('admin_mofi:khoa_list')


# ----- QUẢN LÝ NGÀNH ĐÀO TẠO -----
@login_required
def nganh_list(request):
    resp = call_api(request, 'GET', STUDENT_SERVICE + 'nganh/')
    ds_nganh = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin_mofi/system/nganh_list.html', {'ds_nganh': ds_nganh})

@login_required
def nganh_create(request):
    khoa_resp = call_api(request, 'GET', STUDENT_SERVICE + 'khoa/')
    khoas = khoa_resp.json() if khoa_resp and khoa_resp.status_code == 200 else []
    if request.method == 'POST':
        data = {
            'ma_nganh': request.POST.get('ma_nganh'),
            'ten_nganh': request.POST.get('ten_nganh'),
            'khoa': request.POST.get('khoa'),
            'loai_nganh': request.POST.get('loai_nganh'),
            'thoi_gian_dao_tao_nam': request.POST.get('thoi_gian_dao_tao_nam'),
            'is_active': request.POST.get('is_active') == 'on',
        }
        resp = call_api(request, 'POST', STUDENT_SERVICE + 'nganh/', data=data)
        if resp and resp.status_code == 201:
            messages.success(request, 'Thêm ngành thành công!')
            return redirect('admin_mofi:nganh_list')
        else:
            messages.error(request, 'Thêm ngành thất bại!')
    return render(request, 'admin_mofi/system/nganh_form.html', {'instance': None, 'khoas': khoas})

@login_required
def nganh_edit(request, pk):
    khoa_resp = call_api(request, 'GET', STUDENT_SERVICE + 'khoa/')
    khoas = khoa_resp.json() if khoa_resp and khoa_resp.status_code == 200 else []
    if request.method == 'POST':
        data = {
            'ma_nganh': request.POST.get('ma_nganh'),
            'ten_nganh': request.POST.get('ten_nganh'),
            'khoa': request.POST.get('khoa'),
            'loai_nganh': request.POST.get('loai_nganh'),
            'thoi_gian_dao_tao_nam': request.POST.get('thoi_gian_dao_tao_nam'),
            'is_active': request.POST.get('is_active') == 'on',
        }
        resp = call_api(request, 'PUT', STUDENT_SERVICE + f'nganh/{pk}/', data=data)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật ngành thành công!')
            return redirect('admin_mofi:nganh_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', STUDENT_SERVICE + f'nganh/{pk}/')
    nganh = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin_mofi/system/nganh_form.html', {'instance': nganh, 'khoas': khoas})

@login_required
def nganh_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', STUDENT_SERVICE + f'nganh/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa ngành thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('admin_mofi:nganh_list')


# ----- QUẢN LÝ DANH MỤC CHỨNG CHỈ -----
@login_required
def chungchi_list(request):
    resp = call_api(request, 'GET', CERT_SERVICE + 'danhmuc/')
    danh_sach = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin_mofi/certificates/chungchi_list.html', {'danh_sach': danh_sach})

@login_required
def chungchi_create(request):
    if request.method == 'POST':
        data = {
            'ten_chung_chi': request.POST.get('ten_chung_chi'),
            'loai': request.POST.get('loai'),
            'mo_ta': request.POST.get('mo_ta', ''),
        }
        resp = call_api(request, 'POST', CERT_SERVICE + 'danhmuc/', data=data)
        if resp and resp.status_code == 201:
            messages.success(request, 'Thêm danh mục chứng chỉ thành công!')
            return redirect('admin_mofi:chungchi_list')
        else:
            messages.error(request, 'Thêm thất bại!')
    return render(request, 'admin_mofi/certificates/chungchi_form.html', {'instance': None})

@login_required
def chungchi_edit(request, pk):
    if request.method == 'POST':
        data = {
            'ten_chung_chi': request.POST.get('ten_chung_chi'),
            'loai': request.POST.get('loai'),
            'mo_ta': request.POST.get('mo_ta', ''),
        }
        resp = call_api(request, 'PUT', CERT_SERVICE + f'danhmuc/{pk}/', data=data)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật thành công!')
            return redirect('admin_mofi:chungchi_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', CERT_SERVICE + f'danhmuc/{pk}/')
    instance = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin_mofi/certificates/chungchi_form.html', {'instance': instance})

@login_required
def chungchi_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', CERT_SERVICE + f'danhmuc/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('admin_mofi:chungchi_list')


# ----- TIÊU CHÍ CĐR -----
@login_required
def tieu_chi_list(request):
    # Giả sử có endpoint /api/tieu-chi/ trong Student Service hoặc Report
    resp = call_api(request, 'GET', STUDENT_SERVICE + 'tieu-chi/')
    tieu_chi_list = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin_mofi/system/tieu_chi_list.html', {'tieu_chi_list': tieu_chi_list, 'tong': len(tieu_chi_list)})


# ----- QUẢN LÝ ĐỢT THI -----
@login_required
def dot_thi_list(request):
    resp = call_api(request, 'GET', EXAM_SERVICE + 'dotthi/')
    dot_this = resp.json() if resp and resp.status_code == 200 else []
    # Thêm trạng thái
    for dt in dot_this:
        now = datetime.now().isoformat()
        if dt.get('thoi_gian_bat_dau') <= now <= dt.get('thoi_gian_ket_thuc'):
            dt['trang_thai_hien_tai'] = 1  # Đang diễn ra
        elif dt.get('thoi_gian_bat_dau') > now:
            dt['trang_thai_hien_tai'] = 2  # Sắp diễn ra
        else:
            dt['trang_thai_hien_tai'] = 0  # Kết thúc
    return render(request, 'admin_mofi/exams/dot_thi_list.html', {'dot_this': dot_this})

@login_required
def dot_thi_create(request):
    if request.method == 'POST':
        data = {
            'ma_dot': request.POST.get('ma_dot'),
            'ten_dot': request.POST.get('ten_dot'),
            'thoi_gian_bat_dau': request.POST.get('thoi_gian_bat_dau'),
            'thoi_gian_ket_thuc': request.POST.get('thoi_gian_ket_thuc'),
            'diem_chuan_ngoai_ngu': float(request.POST.get('diem_chuan_ngoai_ngu', 50)),
            'diem_liet_ngoai_ngu': float(request.POST.get('diem_liet_ngoai_ngu', 0)),
            'diem_chuan_tin_hoc': float(request.POST.get('diem_chuan_tin_hoc', 50)),
            'diem_liet_tin_hoc': float(request.POST.get('diem_liet_tin_hoc', 0)),
        }
        resp = call_api(request, 'POST', EXAM_SERVICE + 'dotthi/', data=data)
        if resp and resp.status_code == 201:
            messages.success(request, 'Tạo đợt thi thành công!')
            return redirect('admin_mofi:dot_thi_list')
        else:
            messages.error(request, 'Tạo đợt thi thất bại!')
    return redirect('admin_mofi:dot_thi_list')

@login_required
def dot_thi_detail(request, pk):
    resp = call_api(request, 'GET', EXAM_SERVICE + f'dotthi/{pk}/')
    dot_thi = resp.json() if resp and resp.status_code == 200 else None
    if not dot_thi:
        messages.error(request, 'Không tìm thấy đợt thi!')
        return redirect('admin_mofi:dot_thi_list')
    
    # Lấy danh sách lịch sử thi theo đợt (có thể filter)
    # Ta sẽ lấy tất cả và phân loại theo tab
    resp_lich = call_api(request, 'GET', EXAM_SERVICE + f'lichsuthi/?dot_thi_id={pk}')
    lich_su = resp_lich.json() if resp_lich and resp_lich.status_code == 200 else []
    
    # Phân loại theo mon_thi
    tdnn = [l for l in lich_su if l.get('mon_thi') == 'TA_DAU_VAO']
    cdr_nn = [l for l in lich_su if l.get('mon_thi') == 'CDR_NGOAI_NGU']
    cdr_tin = [l for l in lich_su if l.get('mon_thi') == 'CDR_TIN_HOC']
    
    # Phân trang đơn giản (có thể tách riêng)
    paginator = Paginator(tdnn, 20)
    page_tdnn = paginator.get_page(request.GET.get('p_tdnn', 1))
    paginator = Paginator(cdr_nn, 20)
    page_cdr_nn = paginator.get_page(request.GET.get('p_cdr_nn', 1))
    paginator = Paginator(cdr_tin, 20)
    page_cdr_tin = paginator.get_page(request.GET.get('p_cdr_tin', 1))
    
    context = {
        'dot_thi': dot_thi,
        'page_tdnn': page_tdnn,
        'page_cdr_nn': page_cdr_nn,
        'page_cdr_tin': page_cdr_tin,
        'active_tab': request.GET.get('tab', 'tdnn'),
        'search_query': request.GET.get('q', ''),
        'sort_by': request.GET.get('sort', 'sbd'),
    }
    return render(request, 'admin_mofi/exams/dot_thi_detail.html', context)


# ----- IMPORT DỮ LIỆU (Excel) -----
@login_required
def import_excel_student(request):
    if request.method == 'POST':
        if 'excel_file' not in request.FILES:
            messages.error(request, 'Vui lòng chọn file!')
            return redirect('admin_mofi:import_excel_student')
        file = request.FILES['excel_file']
        files = {'file': file}
        resp = call_api(request, 'POST', STUDENT_SERVICE + 'import-students/', files=files)
        if resp and resp.status_code == 200:
            data = resp.json()
            messages.success(request, f"Import thành công! Tạo mới: {data.get('created',0)}, Cập nhật: {data.get('updated',0)}")
        else:
            messages.error(request, 'Import thất bại!')
        return redirect('admin_mofi:student_list')
    return render(request, 'admin_mofi/students/import_excel.html')


@login_required
def import_exam_data(request, loai):
    """Import lịch thi hoặc điểm thi (loai: lich_thi_tdnn, diem_tdnn, ...)"""
    # Lấy danh sách đợt thi để hiển thị dropdown
    resp_dot = call_api(request, 'GET', EXAM_SERVICE + 'dotthi/')
    dot_this = resp_dot.json() if resp_dot and resp_dot.status_code == 200 else []
    
    if request.method == 'POST':
        dot_thi_id = request.POST.get('dot_thi')
        if not dot_thi_id:
            messages.error(request, 'Vui lòng chọn đợt thi!')
            return redirect(request.path)
        file = request.FILES.get('excel_file')
        if not file:
            messages.error(request, 'Vui lòng chọn file!')
            return redirect(request.path)
        
        # Map loại sang endpoint và param
        mapping = {
            'lich_thi_tdnn': ('import-exam-schedule/', {'mon_thi': 'TA_DAU_VAO'}),
            'lich_thi_nn': ('import-exam-schedule/', {'mon_thi': 'CDR_NGOAI_NGU'}),
            'lich_thi_cntt': ('import-exam-schedule/', {'mon_thi': 'CDR_TIN_HOC'}),
            'diem_tdnn': ('import-exam-scores/', {'loai': 'tdnn'}),
            'diem_cdr_nn': ('import-exam-scores/', {'loai': 'cdr_nn'}),
            'diem_cntt': ('import-exam-scores/', {'loai': 'cntt'}),
        }
        endpoint, params = mapping.get(loai, (None, {}))
        if not endpoint:
            messages.error(request, 'Loại import không hợp lệ!')
            return redirect('admin_mofi:dot_thi_list')
        
        files = {'file': file}
        data = {'dot_thi_id': dot_thi_id, **params}
        resp = call_api(request, 'POST', EXAM_SERVICE + endpoint, data=data, files=files)
        if resp and resp.status_code == 200:
            messages.success(request, f"Import thành công! {resp.json().get('message', '')}")
        else:
            messages.error(request, 'Import thất bại!')
        return redirect('admin_mofi:dot_thi_detail', pk=dot_thi_id)
    
    template_map = {
        'lich_thi_tdnn': 'admin_mofi/exams/import_lich_thi_tdnn.html',
        'lich_thi_nn': 'admin_mofi/exams/import_lich_thi_nn.html',
        'lich_thi_cntt': 'admin_mofi/exams/import_lich_thi_cntt.html',
        'diem_tdnn': 'admin_mofi/exams/import_diem_tdnn.html',
        'diem_cdr_nn': 'admin_mofi/exams/import_diem_cdr_nn.html',
        'diem_cntt': 'admin_mofi/exams/import_diem_cntt.html',
    }
    template = template_map.get(loai, 'admin_mofi/exams/import_lich_thi.html')
    return render(request, template, {'dot_this': dot_this})


# ----- QUẢN LÝ LỚP BỒI DƯỠNG -----
@login_required
def class_list(request):
    resp = call_api(request, 'GET', TRAINING_SERVICE + 'lop/')
    classes = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin_mofi/classes/class_list.html', {'classes': classes})

@login_required
def class_create(request):
    if request.method == 'POST':
        data = {
            'ma_lop': request.POST.get('ma_lop'),
            'ten_lop': request.POST.get('ten_lop'),
            'loai': request.POST.get('loai'),
            'so_luong_toi_da': request.POST.get('so_luong_toi_da'),
            'bat_dau': request.POST.get('bat_dau'),
            'ket_thuc': request.POST.get('ket_thuc'),
            'trang_thai': request.POST.get('trang_thai', 'OPEN'),
        }
        resp = call_api(request, 'POST', TRAINING_SERVICE + 'lop/', data=data)
        if resp and resp.status_code == 201:
            messages.success(request, 'Tạo lớp thành công!')
            return redirect('admin_mofi:class_list')
        else:
            messages.error(request, 'Tạo lớp thất bại!')
    return render(request, 'admin_mofi/classes/class_form.html', {'instance': None})

@login_required
def class_edit(request, pk):
    if request.method == 'POST':
        data = {
            'ma_lop': request.POST.get('ma_lop'),
            'ten_lop': request.POST.get('ten_lop'),
            'loai': request.POST.get('loai'),
            'so_luong_toi_da': request.POST.get('so_luong_toi_da'),
            'bat_dau': request.POST.get('bat_dau'),
            'ket_thuc': request.POST.get('ket_thuc'),
            'trang_thai': request.POST.get('trang_thai', 'OPEN'),
        }
        resp = call_api(request, 'PUT', TRAINING_SERVICE + f'lop/{pk}/', data=data)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật lớp thành công!')
            return redirect('admin_mofi:class_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', TRAINING_SERVICE + f'lop/{pk}/')
    instance = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin_mofi/classes/class_form.html', {'instance': instance})

@login_required
def class_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', TRAINING_SERVICE + f'lop/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa lớp thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('admin_mofi:class_list')


@login_required
def import_class_list(request):
    if request.method == 'POST':
        lop_id = request.POST.get('lop_id')
        if not lop_id:
            messages.error(request, 'Vui lòng chọn lớp!')
            return redirect('admin_mofi:import_class_list')
        file = request.FILES.get('excel_file')
        if not file:
            messages.error(request, 'Vui lòng chọn file!')
            return redirect('admin_mofi:import_class_list')
        files = {'file': file}
        data = {'lop_id': lop_id}
        resp = call_api(request, 'POST', TRAINING_SERVICE + f'lop/{lop_id}/import-students/', data=data, files=files)
        if resp and resp.status_code == 200:
            messages.success(request, 'Import danh sách lớp thành công!')
        else:
            messages.error(request, 'Import thất bại!')
        return redirect('admin_mofi:class_list')
    # Lấy danh sách lớp để dropdown
    resp = call_api(request, 'GET', TRAINING_SERVICE + 'lop/')
    lops = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin_mofi/classes/import_class_list.html', {'lops': lops})


# ----- QUẢN LÝ BÀI VIẾT (CMS) -----
@login_required
def post_list(request):
    resp = call_api(request, 'GET', CMS_SERVICE + 'baiviet/')
    posts = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin_mofi/cms/post_list.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        data = {
            'tieu_de': request.POST.get('tieu_de'),
            'noi_dung': request.POST.get('noi_dung'),
            'slug': request.POST.get('slug'),
            'category': request.POST.get('category'),
            'is_published': request.POST.get('is_published') == 'on',
            'image': request.FILES.get('image') if 'image' in request.FILES else None,
        }
        # Xử lý file upload
        files = None
        if 'image' in request.FILES:
            files = {'image': request.FILES['image']}
        resp = call_api(request, 'POST', CMS_SERVICE + 'baiviet/', data=data, files=files)
        if resp and resp.status_code == 201:
            messages.success(request, 'Thêm bài viết thành công!')
            return redirect('admin_mofi:post_list')
        else:
            messages.error(request, 'Thêm thất bại!')
    # Lấy danh mục cho dropdown
    resp_cat = call_api(request, 'GET', CMS_SERVICE + 'danhmuc/')
    categories = resp_cat.json() if resp_cat and resp_cat.status_code == 200 else []
    return render(request, 'admin_mofi/cms/post_form.html', {'instance': None, 'categories': categories})

@login_required
def post_edit(request, pk):
    if request.method == 'POST':
        data = {
            'tieu_de': request.POST.get('tieu_de'),
            'noi_dung': request.POST.get('noi_dung'),
            'slug': request.POST.get('slug'),
            'category': request.POST.get('category'),
            'is_published': request.POST.get('is_published') == 'on',
        }
        files = None
        if 'image' in request.FILES:
            files = {'image': request.FILES['image']}
        resp = call_api(request, 'PUT', CMS_SERVICE + f'baiviet/{pk}/', data=data, files=files)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật thành công!')
            return redirect('admin_mofi:post_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', CMS_SERVICE + f'baiviet/{pk}/')
    instance = resp.json() if resp and resp.status_code == 200 else None
    resp_cat = call_api(request, 'GET', CMS_SERVICE + 'danhmuc/')
    categories = resp_cat.json() if resp_cat and resp_cat.status_code == 200 else []
    return render(request, 'admin_mofi/cms/post_form.html', {'instance': instance, 'categories': categories})

@login_required
def post_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', CMS_SERVICE + f'baiviet/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('admin_mofi:post_list')


# ----- QUẢN LÝ DANH MỤC BÀI VIẾT (CMS) -----
@login_required
def category_list(request):
    resp = call_api(request, 'GET', CMS_SERVICE + 'danhmuc/')
    categories = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin_mofi/cms/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'slug': request.POST.get('slug'),
            'description': request.POST.get('description'),
            'show_on_navbar': request.POST.get('show_on_navbar') == 'on',
            'show_on_homepage': request.POST.get('show_on_homepage') == 'on',
            'is_active': request.POST.get('is_active') == 'on',
        }
        resp = call_api(request, 'POST', CMS_SERVICE + 'danhmuc/', data=data)
        if resp and resp.status_code == 201:
            messages.success(request, 'Thêm danh mục thành công!')
            return redirect('admin_mofi:category_list')
        else:
            messages.error(request, 'Thêm thất bại!')
    return render(request, 'admin_mofi/cms/category_form.html', {'instance': None})

@login_required
def category_edit(request, pk):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'slug': request.POST.get('slug'),
            'description': request.POST.get('description'),
            'show_on_navbar': request.POST.get('show_on_navbar') == 'on',
            'show_on_homepage': request.POST.get('show_on_homepage') == 'on',
            'is_active': request.POST.get('is_active') == 'on',
        }
        resp = call_api(request, 'PUT', CMS_SERVICE + f'danhmuc/{pk}/', data=data)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật thành công!')
            return redirect('admin_mofi:category_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', CMS_SERVICE + f'danhmuc/{pk}/')
    instance = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin_mofi/cms/category_form.html', {'instance': instance})

@login_required
def category_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', CMS_SERVICE + f'danhmuc/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('admin_mofi:category_list')


# ----- QUẢN LÝ SLIDER -----
@login_required
def slider_list(request):
    resp = call_api(request, 'GET', CMS_SERVICE + 'slider/')
    sliders = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin_mofi/cms/slider_list.html', {'sliders': sliders})

@login_required
def slider_create(request):
    if request.method == 'POST':
        data = {
            'title': request.POST.get('title'),
            'link_url': request.POST.get('link_url'),
            'order': request.POST.get('order'),
            'is_active': request.POST.get('is_active') == 'on',
        }
        files = None
        if 'image' in request.FILES:
            files = {'image': request.FILES['image']}
        resp = call_api(request, 'POST', CMS_SERVICE + 'slider/', data=data, files=files)
        if resp and resp.status_code == 201:
            messages.success(request, 'Thêm slider thành công!')
            return redirect('admin_mofi:slider_list')
        else:
            messages.error(request, 'Thêm thất bại!')
    return render(request, 'admin_mofi/cms/slider_form.html', {'instance': None})

@login_required
def slider_edit(request, pk):
    if request.method == 'POST':
        data = {
            'title': request.POST.get('title'),
            'link_url': request.POST.get('link_url'),
            'order': request.POST.get('order'),
            'is_active': request.POST.get('is_active') == 'on',
        }
        files = None
        if 'image' in request.FILES:
            files = {'image': request.FILES['image']}
        resp = call_api(request, 'PUT', CMS_SERVICE + f'slider/{pk}/', data=data, files=files)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật thành công!')
            return redirect('admin_mofi:slider_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', CMS_SERVICE + f'slider/{pk}/')
    instance = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin_mofi/cms/slider_form.html', {'instance': instance})

@login_required
def slider_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', CMS_SERVICE + f'slider/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('admin_mofi:slider_list')


# ----- QUẢN LÝ QUICKLINK -----
@login_required
def quicklink_list(request):
    resp = call_api(request, 'GET', CMS_SERVICE + 'quicklink/')
    quicklinks = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin_mofi/cms/quicklink_list.html', {'quicklinks': quicklinks})

@login_required
def quicklink_create(request):
    if request.method == 'POST':
        data = {
            'title': request.POST.get('title'),
            'url': request.POST.get('url'),
            'order': request.POST.get('order'),
            'is_active': request.POST.get('is_active') == 'on',
        }
        files = None
        if 'image' in request.FILES:
            files = {'image': request.FILES['image']}
        resp = call_api(request, 'POST', CMS_SERVICE + 'quicklink/', data=data, files=files)
        if resp and resp.status_code == 201:
            messages.success(request, 'Thêm quicklink thành công!')
            return redirect('admin_mofi:quicklink_list')
        else:
            messages.error(request, 'Thêm thất bại!')
    return render(request, 'admin_mofi/cms/quicklink_form.html', {'instance': None})

@login_required
def quicklink_edit(request, pk):
    if request.method == 'POST':
        data = {
            'title': request.POST.get('title'),
            'url': request.POST.get('url'),
            'order': request.POST.get('order'),
            'is_active': request.POST.get('is_active') == 'on',
        }
        files = None
        if 'image' in request.FILES:
            files = {'image': request.FILES['image']}
        resp = call_api(request, 'PUT', CMS_SERVICE + f'quicklink/{pk}/', data=data, files=files)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật thành công!')
            return redirect('admin_mofi:quicklink_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', CMS_SERVICE + f'quicklink/{pk}/')
    instance = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin_mofi/cms/quicklink_form.html', {'instance': instance})

@login_required
def quicklink_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', CMS_SERVICE + f'quicklink/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('admin_mofi:quicklink_list')


# ----- QUẢN LÝ THÔNG BÁO (đã có trong reports? nhưng tách riêng) -----
@login_required
def thongbao_list(request):
    resp = call_api(request, 'GET', NOTIFICATION_SERVICE + 'thongbao/')
    thong_baos = resp.json() if resp and resp.status_code == 200 else []
    # Thêm thống kê
    context = {
        'thong_baos': thong_baos,
        'tong_thong_bao': len(thong_baos),
        'dang_hien_thi': sum(1 for tb in thong_baos if tb.get('is_active')),
        'tong_sv_chua_dat_nn': 0,  # Lấy từ report
        'tong_sv_chua_dat_th': 0,
    }
    return render(request, 'admin_mofi/reports/thongbao_list.html', context)

@login_required
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
            return redirect('admin_mofi:thongbao_list')
        else:
            messages.error(request, 'Tạo thất bại!')
    return render(request, 'admin_mofi/reports/thongbao_form.html', {'instance': None})

@login_required
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
            return redirect('admin_mofi:thongbao_list')
        else:
            messages.error(request, 'Cập nhật thất bại!')
    resp = call_api(request, 'GET', NOTIFICATION_SERVICE + f'thongbao/{pk}/')
    instance = resp.json() if resp and resp.status_code == 200 else None
    return render(request, 'admin_mofi/reports/thongbao_form.html', {'instance': instance})

@login_required
def thongbao_delete(request, pk):
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', NOTIFICATION_SERVICE + f'thongbao/{pk}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('admin_mofi:thongbao_list')


# ----- QUẢN LÝ TÀI KHOẢN VÀ NHÓM QUYỀN (Django Auth) -----
@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'admin_mofi/system/user_list.html', {'users': users})

@login_required
def user_create(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = 'Humg@123456'  # Mặc định
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        is_active = request.POST.get('is_active') == 'on'
        groups = request.POST.getlist('groups')
        user = User.objects.create_user(username=username, password=password, email=email,
                                        first_name=first_name, last_name=last_name, is_active=is_active)
        if groups:
            user.groups.set(groups)
        messages.success(request, f'Tạo tài khoản {username} thành công! Mật khẩu mặc định: Humg@123456')
        return redirect('admin_mofi:user_list')
    groups = Group.objects.all()
    return render(request, 'admin_mofi/system/user_form.html', {'instance': None, 'groups': groups})

@login_required
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
        return redirect('admin_mofi:user_list')
    groups = Group.objects.all()
    return render(request, 'admin_mofi/system/user_form.html', {'instance': user, 'groups': groups})

@login_required
def group_list(request):
    groups = Group.objects.all()
    return render(request, 'admin_mofi/system/group_list.html', {'groups': groups})

@login_required
def group_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        group = Group.objects.create(name=name)
        group.permissions.set(request.POST.getlist('permissions'))
        messages.success(request, 'Tạo nhóm quyền thành công!')
        return redirect('admin_mofi:group_list')
    from django.contrib.auth.models import Permission
    permissions = Permission.objects.all()
    return render(request, 'admin_mofi/system/group_form.html', {'instance': None, 'permissions': permissions})

@login_required
def group_edit(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.name = request.POST.get('name')
        group.permissions.set(request.POST.getlist('permissions'))
        group.save()
        messages.success(request, 'Cập nhật nhóm quyền thành công!')
        return redirect('admin_mofi:group_list')
    from django.contrib.auth.models import Permission
    permissions = Permission.objects.all()
    return render(request, 'admin_mofi/system/group_form.html', {'instance': group, 'permissions': permissions})


# ================================================================
# VIEWS CHO PORTAL (students/)
# ================================================================

def home(request):
    """
    Trang chủ portal: hiển thị slider, quick links, bài viết mới nhất,
    và các chuyên mục tin tức.
    """
    # Lấy slider
    try:
        resp_slider = requests.get(CMS_SERVICE + 'slider/', timeout=5)
        sliders = resp_slider.json() if resp_slider.status_code == 200 else []
    except:
        sliders = []

    # Lấy quick links
    try:
        resp_quick = requests.get(CMS_SERVICE + 'quicklink/', timeout=5)
        quick_links = resp_quick.json() if resp_quick.status_code == 200 else []
    except:
        quick_links = []

    # Lấy danh sách bài viết mới nhất (giới hạn 10)
    try:
        resp_posts = requests.get(CMS_SERVICE + 'baiviet/?limit=10', timeout=5)
        latest_posts = resp_posts.json() if resp_posts.status_code == 200 else []
    except:
        latest_posts = []

    # Lấy danh mục bài viết để hiển thị block chuyên mục
    try:
        resp_cats = requests.get(CMS_SERVICE + 'danhmuc/?show_on_homepage=true', timeout=5)
        categories = resp_cats.json() if resp_cats.status_code == 200 else []
    except:
        categories = []

    # Xây dựng home_blocks: mỗi block gồm category và danh sách bài viết thuộc category đó
    home_blocks = []
    for cat in categories:
        try:
            resp_posts_cat = requests.get(
                CMS_SERVICE + f'baiviet/?category={cat.get("id")}&limit=4',
                timeout=5
            )
            posts = resp_posts_cat.json() if resp_posts_cat.status_code == 200 else []
        except:
            posts = []
        home_blocks.append({
            'category': cat,
            'posts': posts
        })

    context = {
        'slider_posts': sliders,
        'quick_links': quick_links,
        'latest_posts': latest_posts,
        'home_blocks': home_blocks,
    }
    return render(request, 'students/home.html', context)


@login_required
def student_dashboard(request):
    """
    Dashboard sinh viên: hiển thị thông tin cá nhân, tiến độ CĐR,
    lịch thi sắp tới, kết quả thi, chứng chỉ, lớp học, thông báo.
    """
    # Lấy thông tin sinh viên từ Student Service
    # Giả sử username là MSSV (hoặc có thể lấy từ session)
    username = request.user.username
    try:
        resp_student = requests.get(
            STUDENT_SERVICE + f'sinhvien/?ma_sv={username}',
            timeout=5
        )
        if resp_student.status_code == 200:
            students = resp_student.json()
            sinh_vien = students[0] if students else None
        else:
            sinh_vien = None
    except:
        sinh_vien = None

    if not sinh_vien:
        messages.warning(request, 'Không tìm thấy thông tin sinh viên. Vui lòng liên hệ quản trị viên.')
        # Vẫn render dashboard nhưng thiếu dữ liệu
        sinh_vien = {}

    # Lấy danh sách kết quả thi
    sinh_vien_id = sinh_vien.get('id')
    lich_su_thi = []
    if sinh_vien_id:
        try:
            resp_exam = requests.get(
                EXAM_SERVICE + f'lichsuthi/?sinh_vien_id={sinh_vien_id}',
                timeout=5
            )
            lich_su_thi = resp_exam.json() if resp_exam.status_code == 200 else []
        except:
            pass

    # Lấy danh sách chứng chỉ
    chung_chi = []
    if sinh_vien_id:
        try:
            resp_cert = requests.get(
                CERT_SERVICE + f'chungchi/?sinh_vien_id={sinh_vien_id}',
                timeout=5
            )
            chung_chi = resp_cert.json() if resp_cert.status_code == 200 else []
        except:
            pass

    # Lấy danh sách đăng ký lớp
    dang_ky_lop = []
    if sinh_vien_id:
        try:
            resp_reg = requests.get(
                TRAINING_SERVICE + f'dangky/?sinh_vien_id={sinh_vien_id}',
                timeout=5
            )
            dang_ky_lop = resp_reg.json() if resp_reg.status_code == 200 else []
        except:
            pass

    # Lấy thông báo mới (cho sinh viên)
    thong_bao_moi = []
    if sinh_vien_id:
        try:
            resp_noti = requests.get(
                NOTIFICATION_SERVICE + f'thongbao/?sinh_vien_id={sinh_vien_id}&is_active=true',
                timeout=5
            )
            thong_bao_moi = resp_noti.json() if resp_noti.status_code == 200 else []
        except:
            pass

    # Lấy lịch thi sắp tới (lọc từ lich_su_thi, chọn ngày thi trong tương lai)
    from datetime import datetime
    today = datetime.now().date()
    lich_thi_sap_toi = []
    for item in lich_su_thi:
        ngay_thi = item.get('ngay_thi')
        if ngay_thi:
            try:
                ngay_thi_date = datetime.strptime(ngay_thi, '%d/%m/%Y').date()
                if ngay_thi_date >= today:
                    lich_thi_sap_toi.append(item)
            except:
                pass

    context = {
        'sinh_vien': sinh_vien,
        'lich_su_thi': lich_su_thi,
        'chung_chi': chung_chi,
        'dang_ky_lop': dang_ky_lop,
        'thong_bao_moi': thong_bao_moi,
        'lich_thi_sap_toi': lich_thi_sap_toi,
    }
    return render(request, 'students/dashboard.html', context)


def tra_cuu(request):
    """
    Tra cứu kết quả sinh viên theo MSSV.
    Nếu có MSSV, gọi API từ Student Service, Exam Service, Certificate Service
    để hiển thị thông tin chi tiết.
    """
    mssv = request.GET.get('mssv')
    sinh_vien = None
    lich_su_thi = []
    chung_chi = []
    lich_thi_sap_toi = []
    thong_bao = None

    if mssv:
        # Lấy thông tin sinh viên
        try:
            resp = requests.get(
                STUDENT_SERVICE + f'sinhvien/?ma_sv={mssv}',
                timeout=5
            )
            if resp.status_code == 200:
                results = resp.json()
                if results:
                    sinh_vien = results[0]
                    sinh_vien_id = sinh_vien.get('id')
                else:
                    thong_bao = 'Không tìm thấy sinh viên với MSSV này.'
            else:
                thong_bao = 'Lỗi kết nối đến hệ thống.'
        except:
            thong_bao = 'Lỗi kết nối đến hệ thống.'

        if sinh_vien and sinh_vien.get('id'):
            sinh_vien_id = sinh_vien['id']
            # Lấy lịch sử thi
            try:
                resp_exam = requests.get(
                    EXAM_SERVICE + f'lichsuthi/?sinh_vien_id={sinh_vien_id}',
                    timeout=5
                )
                if resp_exam.status_code == 200:
                    lich_su_thi = resp_exam.json()
            except:
                pass

            # Lấy chứng chỉ
            try:
                resp_cert = requests.get(
                    CERT_SERVICE + f'chungchi/?sinh_vien_id={sinh_vien_id}',
                    timeout=5
                )
                if resp_cert.status_code == 200:
                    chung_chi = resp_cert.json()
            except:
                pass

            # Lọc lịch thi sắp tới
            from datetime import datetime
            today = datetime.now().date()
            for item in lich_su_thi:
                ngay_thi = item.get('ngay_thi')
                if ngay_thi:
                    try:
                        ngay_thi_date = datetime.strptime(ngay_thi, '%d/%m/%Y').date()
                        if ngay_thi_date >= today:
                            lich_thi_sap_toi.append(item)
                    except:
                        pass

    context = {
        'sinh_vien': sinh_vien,
        'lich_su_thi': lich_su_thi,
        'chung_chi': chung_chi,
        'lich_thi_sap_toi': lich_thi_sap_toi,
        'query_mssv': mssv,
        'thong_bao': thong_bao,
    }
    return render(request, 'students/tra_cuu.html', context)


def dang_nhap(request):
    """
    Đăng nhập hệ thống (hỗ trợ username/password).
    """
    if request.method == 'POST':
        username = request.POST.get('mssv')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Chào mừng {user.get_full_name() or user.username}!')
            return redirect('students:dashboard')
        else:
            messages.error(request, 'Sai tài khoản hoặc mật khẩu. Vui lòng thử lại.')
    
    return render(request, 'students/login.html')


def dang_xuat(request):
    """Đăng xuất và chuyển hướng về trang chủ."""
    logout(request)
    messages.info(request, 'Bạn đã đăng xuất thành công.')
    return redirect('students:home')


def quy_che_list(request):
    """
    Danh sách các văn bản quy chế (lấy từ CMS service).
    Hỗ trợ lọc theo loại văn bản.
    """
    token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {token}'} if token else {}
    
    try:
        resp = requests.get(CMS_SERVICE + 'van-ban/', headers=headers, timeout=5)
        if resp.status_code == 200:
            van_ban_list = resp.json()
        else:
            van_ban_list = []
    except Exception:
        van_ban_list = []
    
    loai = request.GET.get('loai')
    if loai:
        van_ban_list = [vb for vb in van_ban_list if vb.get('loai') == loai]
    
    context = {
        'van_ban_list': van_ban_list,
        'loai_hien_tai': loai,
    }
    return render(request, 'students/quy_che_list.html', context)


def quy_che_detail(request, slug):
    """
    Chi tiết một văn bản quy chế dựa trên slug.
    """
    token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {token}'} if token else {}
    
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
    
    context = {'van_ban': van_ban}
    return render(request, 'students/quy_che_detail.html', context)


# ====== ADMIN: IMPORT SINH VIÊN VÀO LỚP ======
@login_required
def import_class_students(request, pk):
    """Import danh sách sinh viên vào lớp từ Excel"""
    if request.method == 'POST':
        lop_id = pk
        file = request.FILES.get('excel_file')
        if not file:
            messages.error(request, 'Vui lòng chọn file Excel!')
            return redirect('admin_mofi:class_list')
        
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
        return redirect('admin_mofi:class_list')
    
    # GET: Hiển thị form import
    resp = call_api(request, 'GET', TRAINING_SERVICE + f'lop/{pk}/')
    lop = resp.json() if resp and resp.status_code == 200 else None
    if not lop:
        messages.error(request, 'Không tìm thấy lớp học!')
        return redirect('admin_mofi:class_list')
    
    return render(request, 'admin_mofi/classes/import_students.html', {'lop': lop})


# ====== ADMIN: IMPORT LỊCH HỌC ======
@login_required
def import_class_schedule(request):
    """Import lịch học từ Excel (hỗ trợ merge cells)"""
    if request.method == 'POST':
        file = request.FILES.get('excel_file')
        if not file:
            messages.error(request, 'Vui lòng chọn file Excel!')
            return redirect('admin_mofi:import_schedule')
        
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
        return redirect('admin_mofi:class_list')
    
    # GET: Hiển thị form
    return render(request, 'admin_mofi/classes/import_schedule.html')


# ================================================================
# DASHBOARD ADMIN
# ================================================================
@login_required
def admin_mofi_dashboard(request):
    """Trang dashboard dành cho admin (Mofi) - lấy dữ liệu từ Report Service"""
    
    token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {token}'} if token else {}
    
    # ====== 1. LẤY DỮ LIỆU THỐNG KÊ TỔNG QUAN ======
    total_students = 0
    active_classes = 0
    pending_registrations = 0
    certificates_issued = 0
    top_canh_bao = []
    so_luong_canh_bao = 0
    recent_activities = []
    thong_ke_khoa = []
    chart_data = {'labels': [], 'cdr_nn': {'da_dat': [], 'chua_dat': []}, 'cdr_th': {'da_dat': [], 'chua_dat': []}}
    
    try:
        resp = requests.get(
            'http://localhost:8007/api/dashboard/',
            headers=headers,
            timeout=5
        )
        if resp.status_code == 200:
            data = resp.json()
            total_students = data.get('tong_sinh_vien', 0)
            # Các thông số khác có thể lấy từ dashboard_stats
            # Lưu ý: report-service hiện chưa trả active_classes, pending_registrations, certificates_issued
            # Nên tạm tính hoặc gọi thêm API khác
    except:
        pass
    
    # ====== 2. LẤY DANH SÁCH CẢNH BÁO TỪ REPORT ======
    try:
        resp = requests.get(
            'http://localhost:8007/api/chua-dat-chuan/?loai=all&limit=10',
            headers=headers,
            timeout=5
        )
        if resp.status_code == 200:
            data = resp.json()
            # Chuyển đổi format để phù hợp với template
            top_canh_bao = data.get('results', [])[:10]
            so_luong_canh_bao = data.get('count', 0)
    except:
        pass
    
    # ====== 3. LẤY THỐNG KÊ THEO KHOA (CHO BIỂU ĐỒ) ======
    try:
        resp = requests.get(
            'http://localhost:8007/api/thong-ke-theo-khoa/',
            headers=headers,
            timeout=5
        )
        if resp.status_code == 200:
            thong_ke_khoa = resp.json()
            # Xây dựng chart_data
            chart_data['labels'] = [item['ten_khoa'] for item in thong_ke_khoa]
            chart_data['cdr_nn']['da_dat'] = [item['dat_ngoai_ngu'] for item in thong_ke_khoa]
            chart_data['cdr_nn']['chua_dat'] = [item['tong_sv'] - item['dat_ngoai_ngu'] for item in thong_ke_khoa]
            chart_data['cdr_th']['da_dat'] = [item['dat_tin_hoc'] for item in thong_ke_khoa]
            chart_data['cdr_th']['chua_dat'] = [item['tong_sv'] - item['dat_tin_hoc'] for item in thong_ke_khoa]
    except:
        pass
    
    # ====== 4. LẤY ĐĂNG KÝ GẦN ĐÂY TỪ TRAINING SERVICE ======
    try:
        resp = requests.get(
            'http://localhost:8004/api/dangky/?limit=10',
            headers=headers,
            timeout=5
        )
        if resp.status_code == 200:
            # Lấy danh sách đăng ký và enrich thông tin (giả định)
            recent_activities = resp.json()
            # Thêm thông tin sinh viên và lớp (nếu cần)
    except:
        pass

    context = {
        'total_students': total_students,
        'active_classes': active_classes or 0,   # Tạm thời để 0, sau này lấy từ training
        'pending_registrations': pending_registrations or 0,
        'certificates_issued': certificates_issued or 0,
        'top_canh_bao': top_canh_bao,
        'so_luong_canh_bao': so_luong_canh_bao,
        'recent_activities': recent_activities,
        'thong_ke_khoa': thong_ke_khoa,
        'chart_data': chart_data,
    }
    return render(request, 'admin_mofi/admin_dashboard.html', context)



# ========== QUẢN LÝ SINH VIÊN (ADMIN) ==========

@login_required
def student_list(request):
    """Danh sách sinh viên (có phân trang và tìm kiếm)"""
    search = request.GET.get('q', '')
    page = request.GET.get('page', 1)
    
    params = {}
    if search:
        params['search'] = search
    
    resp = call_api(request, 'GET', STUDENT_SERVICE + 'sinhvien/', params=params)
    if resp and resp.status_code == 200:
        students = resp.json()
        # Nếu API trả về danh sách, có thể phân trang ở đây hoặc dùng DataTable client-side
    else:
        students = []
    
    # Phân trang đơn giản (nếu API không hỗ trợ)
    paginator = Paginator(students, 20)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    return render(request, 'admin_mofi/students/student_list.html', {
        'sinhviens': page_obj,
        'search': search,
    })

@login_required
def student_detail(request, student_id):
    """Chi tiết sinh viên"""
    resp = call_api(request, 'GET', STUDENT_SERVICE + f'sinhvien/{student_id}/')
    if resp and resp.status_code == 200:
        student = resp.json()
    else:
        messages.error(request, 'Không tìm thấy sinh viên')
        return redirect('admin_mofi:student_list')
    
    # Lấy danh mục chứng chỉ cho modal
    cert_resp = call_api(request, 'GET', CERT_SERVICE + 'danhmuc/')
    danh_muc_cc = cert_resp.json() if cert_resp and cert_resp.status_code == 200 else []
    
    # Lấy danh sách đăng ký lớp
    reg_resp = call_api(request, 'GET', TRAINING_SERVICE + 'dangky/?sinh_vien_id=' + str(student_id))
    ds_dang_ky = reg_resp.json() if reg_resp and reg_resp.status_code == 200 else []
    
    # Lấy lịch sử thi
    exam_resp = call_api(request, 'GET', EXAM_SERVICE + 'lichsuthi/?sinh_vien_id=' + str(student_id))
    lich_su_thi = exam_resp.json() if exam_resp and exam_resp.status_code == 200 else []
    
    return render(request, 'admin_mofi/students/student_detail.html', {
        'student': student,
        'danh_muc_cc': danh_muc_cc,
        'ds_dang_ky': ds_dang_ky,
        'lich_su_thi': lich_su_thi,
    })

@login_required
def student_create(request):
    """Thêm sinh viên mới"""
    # Lấy danh sách khoa cho dropdown
    khoa_resp = call_api(request, 'GET', STUDENT_SERVICE + 'khoa/')
    khoas = khoa_resp.json() if khoa_resp and khoa_resp.status_code == 200 else []
    
    if request.method == 'POST':
        data = {
            'ma_sv': request.POST.get('mssv'),
            'ho_ten': request.POST.get('ho_ten'),
            'khoa': request.POST.get('khoa'),
            'lop': request.POST.get('lop'),
            'email_truong': request.POST.get('email_truong'),
            'so_dien_thoai': request.POST.get('so_dien_thoai'),
            'email_ca_nhan': request.POST.get('email_ca_nhan'),
            'khoa_hoc': request.POST.get('khoa_hoc'),
            'nam_nhap_hoc': request.POST.get('nam_nhap_hoc'),
        }
        resp = call_api(request, 'POST', STUDENT_SERVICE + 'sinhvien/', data=data)
        if resp and resp.status_code in [200, 201]:
            messages.success(request, 'Thêm sinh viên thành công!')
            return redirect('admin_mofi:student_list')
        else:
            messages.error(request, 'Thêm sinh viên thất bại!')
    
    return render(request, 'admin_mofi/students/student_form.html', {
        'student': None,
        'khoas': khoas,
    })

@login_required
def student_edit(request, student_id):
    """Chỉnh sửa sinh viên"""
    # Lấy danh sách khoa
    khoa_resp = call_api(request, 'GET', STUDENT_SERVICE + 'khoa/')
    khoas = khoa_resp.json() if khoa_resp and khoa_resp.status_code == 200 else []
    
    # Lấy thông tin hiện tại
    resp = call_api(request, 'GET', STUDENT_SERVICE + f'sinhvien/{student_id}/')
    if resp and resp.status_code == 200:
        student = resp.json()
    else:
        messages.error(request, 'Không tìm thấy sinh viên')
        return redirect('admin_mofi:student_list')
    
    if request.method == 'POST':
        data = {
            'ma_sv': request.POST.get('mssv'),
            'ho_ten': request.POST.get('ho_ten'),
            'khoa': request.POST.get('khoa'),
            'lop': request.POST.get('lop'),
            'email_truong': request.POST.get('email_truong'),
            'so_dien_thoai': request.POST.get('so_dien_thoai'),
            'email_ca_nhan': request.POST.get('email_ca_nhan'),
            'khoa_hoc': request.POST.get('khoa_hoc'),
            'nam_nhap_hoc': request.POST.get('nam_nhap_hoc'),
        }
        # Xử lý upload avatar nếu có
        files = None
        if 'anh_dai_dien' in request.FILES:
            files = {'anh_dai_dien': request.FILES['anh_dai_dien']}
        
        resp = call_api(request, 'PUT', STUDENT_SERVICE + f'sinhvien/{student_id}/', data=data, files=files)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật thành công!')
            return redirect('admin_mofi:student_detail', student_id=student_id)
        else:
            messages.error(request, 'Cập nhật thất bại!')
    
    return render(request, 'admin_mofi/students/student_form.html', {
        'student': student,
        'khoas': khoas,
    })

@login_required
def student_delete(request, student_id):
    """Xóa sinh viên"""
    if request.method == 'POST':
        resp = call_api(request, 'DELETE', STUDENT_SERVICE + f'sinhvien/{student_id}/')
        if resp and resp.status_code == 204:
            messages.success(request, 'Xóa sinh viên thành công!')
        else:
            messages.error(request, 'Xóa thất bại!')
    return redirect('admin_mofi:student_list')

@login_required
def cap_nhat_ho_so(request):
    """Cập nhật thông tin cá nhân của sinh viên (avatar, số điện thoại, email cá nhân)"""
    if request.method == 'POST':
        # Lấy thông tin sinh viên từ Student Service
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
        # Chuẩn bị dữ liệu cập nhật
        data = {
            'so_dien_thoai': request.POST.get('so_dien_thoai', ''),
            'email_ca_nhan': request.POST.get('email_ca_nhan', ''),
        }
        files = None
        if 'anh_dai_dien' in request.FILES:
            files = {'anh_dai_dien': request.FILES['anh_dai_dien']}

        # Gọi API update
        resp = call_api(request, 'PUT', STUDENT_SERVICE + f'sinhvien/{student_id}/', data=data, files=files)
        if resp and resp.status_code == 200:
            messages.success(request, 'Cập nhật thông tin thành công!')
        else:
            messages.error(request, 'Cập nhật thất bại. Vui lòng thử lại.')
        return redirect('students:dashboard')

    # Nếu là GET, chuyển hướng về dashboard
    return redirect('students:dashboard')


# ================================================================
# VIEWS CHO CHỨC NĂNG BỔ SUNG (CERT, BẢO LƯU, EXPORT)
# ================================================================

@login_required
def cert_list(request):
    """Danh sách chứng chỉ chờ duyệt"""
    resp = call_api(request, 'GET', CERT_SERVICE + 'chungchi/?trang_thai=CHO')
    certs = resp.json() if resp and resp.status_code == 200 else []
    # Thêm thông tin sinh viên (nếu cần) - có thể gọi student service để lấy thêm
    total_pending = len(certs)
    return render(request, 'admin_mofi/certificates/cert_list.html', {
        'pending_certs': certs,
        'total_pending': total_pending,
        'search_query': request.GET.get('q', '')
    })

@login_required
def bao_luu_diem_list(request):
    """Danh sách bảo lưu điểm"""
    resp = call_api(request, 'GET', EXAM_SERVICE + 'baoluudiem/')
    bao_luus = resp.json() if resp and resp.status_code == 200 else []
    # Lấy thông tin sinh viên cho mỗi bảo lưu (có thể làm sau)
    return render(request, 'admin_mofi/reports/bao_luu_diem_list.html', {
        'bao_luus': bao_luus,
        'tong': len(bao_luus)
    })

@login_required
def export_chua_dat_chuan(request):
    """Xuất Excel danh sách sinh viên chưa đạt CĐR"""
    token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {token}'} if token else {}
    try:
        resp = requests.get(REPORT_SERVICE + 'export-chua-dat-chuan/', headers=headers, timeout=30)
        if resp.status_code == 200:
            response = HttpResponse(resp.content, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="danh_sach_chua_dat_chuan.xlsx"'
            return response
        else:
            messages.error(request, 'Không thể xuất danh sách. Vui lòng thử lại.')
    except Exception as e:
        messages.error(request, f'Lỗi kết nối: {str(e)}')
    return redirect('admin_mofi:admin_mofi_dashboard')

@login_required
def registration_list(request):
    """Danh sách đăng ký lớp (dành cho admin)"""
    resp = call_api(request, 'GET', TRAINING_SERVICE + 'dangky/')
    registrations = resp.json() if resp and resp.status_code == 200 else []
    return render(request, 'admin_mofi/classes/registration_list.html', {
        'registrations': registrations
    })


# ========== PHÂN LOẠI SINH VIÊN ==========
@login_required
def phan_loai_sinh_vien(request):
    """
    Phân loại sinh viên theo trạng thái: đạt/chưa đạt, năm cuối.
    Hỗ trợ lọc theo khoa, khóa, loại.
    """
    token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {token}'} if token else {}

    loai = request.GET.get('loai', 'tat_ca')
    khoa_id = request.GET.get('khoa_id')
    khoa_hoc = request.GET.get('khoa_hoc')
    search = request.GET.get('search', '')

    # Lấy tất cả sinh viên từ student-service
    students = []
    try:
        resp = requests.get('http://localhost:8001/api/sinhvien/', headers=headers, timeout=5)
        if resp.status_code == 200:
            students = resp.json()
    except:
        pass

    # Lấy trạng thái CĐR từ report-service
    chua_dat_list = []
    try:
        resp = requests.get('http://localhost:8007/api/chua-dat-chuan/?loai=all', headers=headers, timeout=5)
        if resp.status_code == 200:
            chua_dat_list = resp.json().get('results', [])
    except:
        pass

    # Tạo dict để tra cứu nhanh
    cdr_status = {}
    for sv in chua_dat_list:
        cdr_status[sv.get('ma_sv')] = {
            'dat_ngoai_ngu': sv.get('dat_ngoai_ngu', False),
            'dat_tin_hoc': sv.get('dat_tin_hoc', False),
            'dat_chuan_dau_ra': sv.get('dat_chuan_dau_ra', False)
        }

    # Lọc và enrich
    filtered = []
    for sv in students:
        ma_sv = sv.get('ma_sv')
        status = cdr_status.get(ma_sv, {'dat_ngoai_ngu': False, 'dat_tin_hoc': False, 'dat_chuan_dau_ra': False})
        sv['dat_ngoai_ngu'] = status['dat_ngoai_ngu']
        sv['dat_tin_hoc'] = status['dat_tin_hoc']
        sv['dat_chuan_dau_ra'] = status['dat_chuan_dau_ra']

        # Áp dụng filter
        if search and search.lower() not in sv.get('ho_ten', '').lower() and search not in ma_sv:
            continue
        if khoa_id and str(sv.get('khoa', {}).get('id')) != khoa_id:
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

    # Thống kê nhanh
    dat = sum(1 for sv in filtered if sv['dat_chuan_dau_ra'])
    chua_dat = len(filtered) - dat
    canh_bao = sum(1 for sv in filtered if sv.get('khoa_hoc', '') in ['K63', 'K64', 'K65'] and not sv['dat_chuan_dau_ra'])

    # Lấy danh sách khoa để dropdown
    khoas = []
    try:
        resp = requests.get('http://localhost:8001/api/khoa/', headers=headers, timeout=5)
        if resp.status_code == 200:
            khoas = resp.json()
    except:
        pass

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
    return render(request, 'admin_mofi/reports/phan_loai_sv.html', context)


# ========== DANH SÁCH CẢNH BÁO ==========
@login_required
def danh_sach_canh_bao(request):
    """
    Hiển thị danh sách sinh viên cần cảnh báo (năm cuối chưa đạt CĐR)
    """
    token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {token}'} if token else {}

    students = []
    try:
        resp = requests.get('http://localhost:8007/api/chua-dat-chuan/?loai=all', headers=headers, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            all_results = data.get('results', [])
            # Lọc năm cuối (K63, K64, K65) - tùy chỉnh theo thực tế
            final_year_codes = ['K63', 'K64', 'K65']
            students = [sv for sv in all_results if sv.get('khoa_hoc', '') in final_year_codes]
    except:
        pass

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
    return render(request, 'admin_mofi/reports/danh_sach_canh_bao.html', context)


# ========== GỬI CẢNH BÁO ==========
@login_required
def gui_canh_bao(request):
    """
    Form gửi cảnh báo đến sinh viên.
    """
    token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {token}'} if token else {}

    stats = {'tat_ca': 0, 'nam_cuoi': 0, 'chua_dat_nn': 0, 'chua_dat_th': 0}
    try:
        # Lấy tổng số sinh viên chưa đạt từ report
        resp = requests.get('http://localhost:8007/api/chua-dat-chuan/?loai=all', headers=headers, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            all_results = data.get('results', [])
            stats['tat_ca'] = len(all_results)
            stats['chua_dat_nn'] = sum(1 for sv in all_results if not sv.get('dat_ngoai_ngu', False))
            stats['chua_dat_th'] = sum(1 for sv in all_results if not sv.get('dat_tin_hoc', False))
            final_year_codes = ['K63', 'K64', 'K65']
            stats['nam_cuoi'] = sum(1 for sv in all_results if sv.get('khoa_hoc', '') in final_year_codes and not sv.get('dat_chuan_dau_ra', False))
    except:
        pass

    if request.method == 'POST':
        loai_canh_bao = request.POST.get('loai_canh_bao')
        noi_dung = request.POST.get('noi_dung')
        gui_email = request.POST.get('gui_email') == 'on'

        if not loai_canh_bao or not noi_dung:
            messages.error(request, 'Vui lòng chọn đối tượng và nhập nội dung')
            return redirect('gui_canh_bao')

        # Lấy danh sách sinh viên theo loại
        students_to_notify = []
        if loai_canh_bao == 'tat_ca':
            resp = requests.get('http://localhost:8007/api/chua-dat-chuan/?loai=all', headers=headers, timeout=5)
            if resp.status_code == 200:
                students_to_notify = resp.json().get('results', [])
        elif loai_canh_bao == 'nam_cuoi':
            resp = requests.get('http://localhost:8007/api/chua-dat-chuan/?loai=all', headers=headers, timeout=5)
            if resp.status_code == 200:
                all_results = resp.json().get('results', [])
                final_year_codes = ['K63', 'K64', 'K65']
                students_to_notify = [sv for sv in all_results if sv.get('khoa_hoc', '') in final_year_codes and not sv.get('dat_chuan_dau_ra', False)]
        elif loai_canh_bao == 'chua_dat_nn':
            resp = requests.get('http://localhost:8007/api/chua-dat-chuan/?loai=nn', headers=headers, timeout=5)
            if resp.status_code == 200:
                students_to_notify = resp.json().get('results', [])
        elif loai_canh_bao == 'chua_dat_th':
            resp = requests.get('http://localhost:8007/api/chua-dat-chuan/?loai=th', headers=headers, timeout=5)
            if resp.status_code == 200:
                students_to_notify = resp.json().get('results', [])

        # Tạo cảnh báo trong notification-service
        created = 0
        for sv in students_to_notify:
            data = {
                'sinh_vien_id': sv.get('id'),
                'tieu_de': 'Cảnh báo chưa đạt Chuẩn đầu ra',
                'noi_dung': noi_dung,
                'muc_do': 'HIGH'
            }
            try:
                resp = requests.post('http://localhost:8005/api/canhbao/', json=data, headers=headers, timeout=5)
                if resp.status_code in [200, 201]:
                    created += 1
            except:
                pass

        messages.success(request, f'Đã gửi cảnh báo đến {created} sinh viên')
        return redirect('danh_sach_canh_bao')

    context = {'stats': stats}
    return render(request, 'admin_mofi/reports/gui_canh_bao.html', context)


# ========== BÁO CÁO DASHBOARD RIÊNG ==========
@login_required
def report_dashboard(request):
    """
    Trang báo cáo thống kê chi tiết với biểu đồ và bảng dữ liệu.
    Lấy dữ liệu từ report-service.
    """
    token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {token}'} if token else {}
    
    # Lấy filter từ request
    khoa_filter = request.GET.get('khoa', '')
    khoa_tsv_filter = request.GET.get('khoa_tsv', '')
    
    # ====== 1. THỐNG KÊ NHANH ======
    tong_sinh_vien = 0
    co_email = 0
    khong_email = 0
    co_nganh = 0
    khong_nganh = 0
    
    try:
        resp = requests.get('http://localhost:8007/api/dashboard/', headers=headers, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            tong_sinh_vien = data.get('tong_sinh_vien', 0)
            # Các số liệu này có thể lấy từ API khác nếu cần
            # Tạm thời để 0
    except:
        pass
    
    # Lấy danh sách sinh viên để tính email và ngành
    try:
        resp = requests.get('http://localhost:8001/api/sinhvien/', headers=headers, timeout=5)
        if resp.status_code == 200:
            students = resp.json()
            for sv in students:
                if sv.get('email_truong') or sv.get('email_ca_nhan'):
                    co_email += 1
                else:
                    khong_email += 1
                if sv.get('nganh_dao_tao') or sv.get('nganh'):
                    co_nganh += 1
                else:
                    khong_nganh += 1
    except:
        pass
    
    # ====== 2. LẤY DỮ LIỆU CHO BIỂU ĐỒ ======
    theo_khoa = []
    try:
        resp = requests.get('http://localhost:8007/api/thong-ke-theo-khoa/', headers=headers, timeout=5)
        if resp.status_code == 200:
            theo_khoa = resp.json()
    except:
        pass
    
    # ====== 3. LẤY DỮ LIỆU NGÀNH ======
    theo_nganh = []
    try:
        # Gọi student-service để lấy danh sách sinh viên và nhóm theo ngành
        resp = requests.get('http://localhost:8001/api/sinhvien/', headers=headers, timeout=5)
        if resp.status_code == 200:
            students = resp.json()
            # Nhóm theo ngành
            nganh_count = {}
            for sv in students:
                nganh = sv.get('nganh_dao_tao', {})
                if isinstance(nganh, dict):
                    ten_nganh = nganh.get('ten_nganh', 'Chưa xác định')
                else:
                    ten_nganh = 'Chưa xác định'
                nganh_count[ten_nganh] = nganh_count.get(ten_nganh, 0) + 1
            theo_nganh = [{'nganh_dao_tao__ten_nganh': k, 'total': v} for k, v in nganh_count.items()]
            # Sắp xếp giảm dần
            theo_nganh.sort(key=lambda x: x['total'], reverse=True)
    except:
        pass
    
    # ====== 4. LẤY DỮ LIỆU KHÓA TUYỂN SINH ======
    theo_khoa_tuyen_sinh = []
    try:
        resp = requests.get('http://localhost:8001/api/sinhvien/', headers=headers, timeout=5)
        if resp.status_code == 200:
            students = resp.json()
            khoa_ts_count = {}
            for sv in students:
                khoa_ts = sv.get('khoa_hoc', 'Không xác định')
                khoa_ts_count[khoa_ts] = khoa_ts_count.get(khoa_ts, 0) + 1
            theo_khoa_tuyen_sinh = [{'khoa_tuyen_sinh': k, 'total': v} for k, v in khoa_ts_count.items()]
            theo_khoa_tuyen_sinh.sort(key=lambda x: x['khoa_tuyen_sinh'] if str(x['khoa_tuyen_sinh']).isdigit() else 0)
    except:
        pass
    
    # ====== 5. CHI TIẾT KHOA + KHÓA ======
    theo_khoa_va_khoa = []
    try:
        resp = requests.get('http://localhost:8001/api/sinhvien/', headers=headers, timeout=5)
        if resp.status_code == 200:
            students = resp.json()
            # Nhóm theo khoa và khóa
            combined = {}
            for sv in students:
                khoa = sv.get('khoa', {})
                if isinstance(khoa, dict):
                    ten_khoa = khoa.get('ten_khoa', 'Chưa phân')
                else:
                    ten_khoa = 'Chưa phân'
                khoa_hoc = sv.get('khoa_hoc', '?')
                key = f"{ten_khoa}_{khoa_hoc}"
                combined[key] = combined.get(key, 0) + 1
            # Chuyển đổi format
            for key, count in combined.items():
                parts = key.split('_')
                theo_khoa_va_khoa.append({
                    'khoa__ten_khoa': parts[0],
                    'khoa_tuyen_sinh': parts[1] if len(parts) > 1 else '?',
                    'total': count
                })
    except:
        pass
    
    context = {
        'pham_vi_vai_tro': 'Toàn hệ thống',
        'khoa_filter': khoa_filter,
        'khoa_tsv_filter': khoa_tsv_filter,
        'tong_sinh_vien': tong_sinh_vien,
        'co_email': co_email,
        'khong_email': khong_email,
        'co_nganh': co_nganh,
        'khong_nganh': khong_nganh,
        'theo_khoa': theo_khoa,
        'theo_nganh': theo_nganh,
        'theo_khoa_tuyen_sinh': theo_khoa_tuyen_sinh,
        'theo_khoa_va_khoa': theo_khoa_va_khoa,
    }
    return render(request, 'admin_mofi/report_dashboard.html', context)