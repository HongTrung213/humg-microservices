# reports/views.py
import io
import requests
import pandas as pd
from datetime import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# ---------- HÀM GỌI API TỪ CÁC SERVICE ----------
def get_students(token):
    """Lấy danh sách sinh viên từ Student Service"""
    try:
        headers = {'Authorization': f'Bearer {token}'}
        resp = requests.get('http://localhost:8001/api/sinhvien/', headers=headers, timeout=5)
        if resp.status_code == 200:
            return resp.json()
    except:
        pass
    return []

def get_exam_records(token):
    """Lấy lịch sử thi từ Exam Service"""
    try:
        headers = {'Authorization': f'Bearer {token}'}
        resp = requests.get('http://localhost:8002/api/lichsuthi/', headers=headers, timeout=5)
        if resp.status_code == 200:
            return resp.json()
    except:
        pass
    return []

def get_certificates(token):
    """Lấy chứng chỉ từ Certificate Service"""
    try:
        headers = {'Authorization': f'Bearer {token}'}
        resp = requests.get('http://localhost:8003/api/chungchi/', headers=headers, timeout=5)
        if resp.status_code == 200:
            return resp.json()
    except:
        pass
    return []

def get_dot_thi(token):
    """Lấy danh sách đợt thi từ Exam Service"""
    try:
        headers = {'Authorization': f'Bearer {token}'}
        resp = requests.get('http://localhost:8002/api/dotthi/', headers=headers, timeout=5)
        if resp.status_code == 200:
            return resp.json()
    except:
        pass
    return []


# ---------- API DASHBOARD THỐNG KÊ ----------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    """
    Dashboard tổng hợp:
    - Tổng số sinh viên
    - Phân loại theo khoa
    - Phân loại theo khóa học
    - Tỉ lệ đạt CĐR
    - Danh sách cảnh báo (năm cuối chưa đạt)
    """
    token = request.auth.token if hasattr(request.auth, 'token') else request.headers.get('Authorization', '').replace('Bearer ', '')
    
    students = get_students(token)
    exams = get_exam_records(token)
    
    tong_sv = len(students)
    
    # Thống kê theo khoa
    khoa_stats = {}
    for sv in students:
        khoa = sv.get('khoa', {})
        khoa_name = khoa.get('ten_khoa', 'Không xác định') if isinstance(khoa, dict) else str(khoa)
        khoa_stats[khoa_name] = khoa_stats.get(khoa_name, 0) + 1
    
    # Thống kê theo khóa học
    khoa_hoc_stats = {}
    for sv in students:
        khoa_hoc = sv.get('khoa_hoc', 'Không xác định')
        khoa_hoc_stats[khoa_hoc] = khoa_hoc_stats.get(khoa_hoc, 0) + 1
    
    # Tính CĐR (gọi từng sinh viên)
    dat_nn = 0
    dat_th = 0
    dat_cdr = 0
    canh_bao = []
    
    for sv in students:
        sv_id = sv.get('id')
        ma_sv = sv.get('ma_sv')
        ho_ten = sv.get('ho_ten')
        khoa_hoc = sv.get('khoa_hoc', '')
        
        # Kiểm tra CĐR từ lịch sử thi
        sv_exams = [e for e in exams if e.get('sinh_vien_id') == sv_id]
        
        nn_pass = any(e.get('mon_thi') == 'CDR_NGOAI_NGU' and e.get('ket_qua_dat') for e in sv_exams)
        th_pass = any(e.get('mon_thi') == 'CDR_TIN_HOC' and e.get('ket_qua_dat') for e in sv_exams)
        
        # Nếu có chứng chỉ (sẽ gọi certificate service sau, tạm bỏ qua)
        
        if nn_pass:
            dat_nn += 1
        if th_pass:
            dat_th += 1
        if nn_pass and th_pass:
            dat_cdr += 1
        
        # Cảnh báo năm cuối (K63, K64)
        if khoa_hoc in ['K63', 'K64', 'K65'] and not (nn_pass and th_pass):
            canh_bao.append({
                'id': sv_id,
                'ma_sv': ma_sv,
                'ho_ten': ho_ten,
                'khoa_hoc': khoa_hoc,
                'dat_nn': nn_pass,
                'dat_th': th_pass,
            })
    
    return Response({
        'tong_sinh_vien': tong_sv,
        'dat_ngoai_ngu': dat_nn,
        'dat_tin_hoc': dat_th,
        'dat_chuan_dau_ra': dat_cdr,
        'ti_le_dat_cdr': round(dat_cdr / tong_sv * 100, 2) if tong_sv > 0 else 0,
        'theo_khoa': [{'ten_khoa': k, 'so_luong': v} for k, v in khoa_stats.items()],
        'theo_khoa_hoc': [{'khoa_hoc': k, 'so_luong': v} for k, v in khoa_hoc_stats.items()],
        'canh_bao': canh_bao[:20],  # chỉ lấy 20 sinh viên đầu
        'so_luong_canh_bao': len(canh_bao),
        'updated_at': datetime.now().isoformat(),
    })


# ---------- API DANH SÁCH SINH VIÊN CHƯA ĐẠT CĐR ----------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chua_dat_chuan(request):
    """Danh sách sinh viên chưa đạt CĐR (có filter)"""
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    khoa_id = request.GET.get('khoa_id')
    khoa_hoc = request.GET.get('khoa_hoc')
    loai = request.GET.get('loai', 'all')  # all, nn, th
    
    students = get_students(token)
    exams = get_exam_records(token)
    
    result = []
    for sv in students:
        sv_id = sv.get('id')
        sv_khoa_id = sv.get('khoa_id')
        sv_khoa_hoc = sv.get('khoa_hoc', '')
        
        # Filter
        if khoa_id and sv_khoa_id != int(khoa_id):
            continue
        if khoa_hoc and sv_khoa_hoc != khoa_hoc:
            continue
        
        sv_exams = [e for e in exams if e.get('sinh_vien_id') == sv_id]
        nn_pass = any(e.get('mon_thi') == 'CDR_NGOAI_NGU' and e.get('ket_qua_dat') for e in sv_exams)
        th_pass = any(e.get('mon_thi') == 'CDR_TIN_HOC' and e.get('ket_qua_dat') for e in sv_exams)
        
        if loai == 'nn' and nn_pass:
            continue
        if loai == 'th' and th_pass:
            continue
        if loai == 'all' and (nn_pass and th_pass):
            continue
        
        # Lấy khoa name
        khoa = sv.get('khoa', {})
        khoa_name = khoa.get('ten_khoa', '') if isinstance(khoa, dict) else ''
        
        result.append({
            'id': sv_id,
            'ma_sv': sv.get('ma_sv'),
            'ho_ten': sv.get('ho_ten'),
            'email': sv.get('email'),
            'khoa': khoa_name,
            'khoa_hoc': sv_khoa_hoc,
            'dat_ngoai_ngu': nn_pass,
            'dat_tin_hoc': th_pass,
            'dat_chuan_dau_ra': nn_pass and th_pass,
            'ly_do': 'Chưa đạt ngoại ngữ' if not nn_pass else 'Chưa đạt tin học' if not th_pass else 'Chưa đạt cả hai'
        })
    
    return Response({
        'count': len(result),
        'results': result
    })


# ---------- API EXPORT EXCEL ----------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def export_chua_dat_chuan(request):
    """
    Xuất Excel danh sách sinh viên chưa đạt CĐR
    """
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    
    students = get_students(token)
    exams = get_exam_records(token)
    
    rows = []
    for sv in students:
        sv_id = sv.get('id')
        sv_exams = [e for e in exams if e.get('sinh_vien_id') == sv_id]
        nn_pass = any(e.get('mon_thi') == 'CDR_NGOAI_NGU' and e.get('ket_qua_dat') for e in sv_exams)
        th_pass = any(e.get('mon_thi') == 'CDR_TIN_HOC' and e.get('ket_qua_dat') for e in sv_exams)
        
        if nn_pass and th_pass:
            continue
        
        khoa = sv.get('khoa', {})
        khoa_name = khoa.get('ten_khoa', '') if isinstance(khoa, dict) else ''
        
        ly_do = []
        if not nn_pass:
            ly_do.append('Chưa đạt Ngoại ngữ')
        if not th_pass:
            ly_do.append('Chưa đạt Tin học')
        
        rows.append({
            'STT': len(rows) + 1,
            'MSSV': sv.get('ma_sv', ''),
            'Họ và tên': sv.get('ho_ten', ''),
            'Email': sv.get('email', ''),
            'Số điện thoại': sv.get('so_dien_thoai', ''),
            'Khoa': khoa_name,
            'Khóa học': sv.get('khoa_hoc', ''),
            'Ngoại ngữ': 'Đạt' if nn_pass else 'Chưa đạt',
            'Tin học': 'Đạt' if th_pass else 'Chưa đạt',
            'Nội dung cần chăm sóc': '; '.join(ly_do),
        })
    
    # Tạo DataFrame
    df = pd.DataFrame(rows)
    if df.empty:
        df = pd.DataFrame(columns=['STT', 'MSSV', 'Họ và tên', 'Email', 'Số điện thoại', 'Khoa', 'Khóa học', 'Ngoại ngữ', 'Tin học', 'Nội dung cần chăm sóc'])
    
    # Tạo response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    filename = f"danh_sach_chua_dat_chuan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Chua dat CDR')
        ws = writer.sheets['Chua dat CDR']
        # Tự động điều chỉnh độ rộng cột
        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            ws.column_dimensions[col[0].column_letter].width = min(max_len + 2, 40)
    
    return response


# ---------- API THỐNG KÊ THEO KHOA ----------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def thong_ke_theo_khoa(request):
    """Thống kê CĐR theo từng khoa"""
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    
    students = get_students(token)
    exams = get_exam_records(token)
    
    khoa_data = {}
    for sv in students:
        sv_id = sv.get('id')
        khoa = sv.get('khoa', {})
        khoa_name = khoa.get('ten_khoa', 'Không xác định') if isinstance(khoa, dict) else 'Không xác định'
        
        if khoa_name not in khoa_data:
            khoa_data[khoa_name] = {'tong': 0, 'dat_nn': 0, 'dat_th': 0, 'dat_cdr': 0}
        khoa_data[khoa_name]['tong'] += 1
        
        sv_exams = [e for e in exams if e.get('sinh_vien_id') == sv_id]
        nn_pass = any(e.get('mon_thi') == 'CDR_NGOAI_NGU' and e.get('ket_qua_dat') for e in sv_exams)
        th_pass = any(e.get('mon_thi') == 'CDR_TIN_HOC' and e.get('ket_qua_dat') for e in sv_exams)
        
        if nn_pass:
            khoa_data[khoa_name]['dat_nn'] += 1
        if th_pass:
            khoa_data[khoa_name]['dat_th'] += 1
        if nn_pass and th_pass:
            khoa_data[khoa_name]['dat_cdr'] += 1
    
    result = []
    for ten_khoa, data in khoa_data.items():
        result.append({
            'ten_khoa': ten_khoa,
            'tong_sv': data['tong'],
            'dat_ngoai_ngu': data['dat_nn'],
            'dat_tin_hoc': data['dat_th'],
            'dat_chuan_dau_ra': data['dat_cdr'],
            'ti_le_dat_cdr': round(data['dat_cdr'] / data['tong'] * 100, 2) if data['tong'] > 0 else 0,
        })
    
    return Response(result)


# ---------- API LỊCH SỬ THI CỦA SINH VIÊN ----------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lich_su_thi_sinh_vien(request, sinh_vien_id):
    """Lấy lịch sử thi của một sinh viên cụ thể"""
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    
    exams = get_exam_records(token)
    students = get_students(token)
    
    # Tìm sinh viên
    sv = next((s for s in students if s.get('id') == sinh_vien_id), None)
    if not sv:
        return Response({'error': 'Không tìm thấy sinh viên'}, status=404)
    
    # Lọc lịch sử thi
    sv_exams = [e for e in exams if e.get('sinh_vien_id') == sinh_vien_id]
    
    # Lấy thông tin đợt thi
    dot_this = get_dot_thi(token)
    dot_map = {d.get('id'): d for d in dot_this}
    
    result = []
    for exam in sv_exams:
        dot_id = exam.get('dot_thi')
        dot = dot_map.get(dot_id, {})
        result.append({
            'id': exam.get('id'),
            'mon_thi': exam.get('mon_thi'),
            'ten_dot_thi': dot.get('ten_dot', ''),
            'ngay_thi': exam.get('ngay_thi'),
            'ca_thi': exam.get('ca_thi'),
            'phong_thi': exam.get('phong_thi'),
            'diem_tong': exam.get('diem_tong'),
            'xep_loai': exam.get('xep_loai'),
            'ket_qua_dat': exam.get('ket_qua_dat'),
            'ghi_chu': exam.get('ghi_chu'),
            'co_bao_luu': exam.get('co_bao_luu', False),
        })
    
    return Response({
        'sinh_vien': {
            'ma_sv': sv.get('ma_sv'),
            'ho_ten': sv.get('ho_ten'),
            'khoa': sv.get('khoa', {}).get('ten_khoa', ''),
            'khoa_hoc': sv.get('khoa_hoc', ''),
        },
        'lich_su_thi': result
    })