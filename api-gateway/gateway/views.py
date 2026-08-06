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

# ----- CẤU HÌNH SERVICE URLs -----
STUDENT_SERVICE = 'http://localhost:8001/api/'
EXAM_SERVICE = 'http://localhost:8002/api/'
CERT_SERVICE = 'http://localhost:8003/api/'
TRAINING_SERVICE = 'http://localhost:8004/api/'
NOTIFICATION_SERVICE = 'http://localhost:8005/api/'
CMS_SERVICE = 'http://localhost:8006/api/'
REPORT_SERVICE = 'http://localhost:8007/api/'


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
    """Trang chủ portal"""
    # Lấy danh sách bài viết, slider, quicklink từ CMS
    # Gọi API từ CMS service
    return render(request, 'students/home.html')


def student_dashboard(request):
    """Dashboard sinh viên"""
    # Lấy thông tin sinh viên đang đăng nhập
    return render(request, 'students/dashboard.html')


def tra_cuu(request):
    """Tra cứu kết quả"""
    return render(request, 'students/tra_cuu.html')


def dang_nhap(request):
    """Đăng nhập"""
    # Xử lý đăng nhập
    return render(request, 'students/login.html')


def dang_xuat(request):
    """Đăng xuất"""
    logout(request)
    return redirect('students:home')

def quy_che_list(request):
    """
    Danh sách các văn bản quy chế
    """
    token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {token}'} if token else {}
    
    try:
        resp = requests.get(
            f'{CMS_SERVICE}van-ban/',
            headers=headers,
            timeout=5
        )
        if resp.status_code == 200:
            van_ban_list = resp.json()
        else:
            van_ban_list = []
    except Exception:
        van_ban_list = []
    
    # Lọc theo loại nếu có
    loai = request.GET.get('loai')
    if loai:
        van_ban_list = [vb for vb in van_ban_list if vb.get('loai') == loai]
    
    context = {
        'van_ban_list': van_ban_list,
        'loai_hien_tai': loai,
        'loai_choices': VanBanQuyChe.LOAI_CHOICES,
    }
    return render(request, 'students/quy_che_list.html', context)


def quy_che_detail(request, slug):
    """
    Chi tiết một văn bản quy chế
    """
    token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {token}'} if token else {}
    
    try:
        resp = requests.get(
            f'{CMS_SERVICE}van-ban/?slug={slug}',
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