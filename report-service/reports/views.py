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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def thong_ke_tien_do_cdr(request):
    """
    Thống kê tiến độ hoàn thành CĐR theo khoa, ngành, khóa
    Query params: khoa_id, nganh_id, khoa_hoc, loai (ngoai_ngu / tin_hoc)
    """
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    students = get_students(token)
    exams = get_exam_records(token)
    
    khoa_id = request.GET.get('khoa_id')
    nganh_id = request.GET.get('nganh_id')
    khoa_hoc = request.GET.get('khoa_hoc')
    loai = request.GET.get('loai', 'all')  # all, ngoai_ngu, tin_hoc
    
    result = []
    for sv in students:
        # Áp dụng filter
        if khoa_id and sv.get('khoa_id') != int(khoa_id):
            continue
        if nganh_id and sv.get('nganh_id') != int(nganh_id):
            continue
        if khoa_hoc and sv.get('khoa_hoc') != khoa_hoc:
            continue
        
        sv_exams = [e for e in exams if e.get('sinh_vien_id') == sv.get('id')]
        nn_pass = any(e.get('mon_thi') == 'CDR_NGOAI_NGU' and e.get('ket_qua_dat') for e in sv_exams)
        th_pass = any(e.get('mon_thi') == 'CDR_TIN_HOC' and e.get('ket_qua_dat') for e in sv_exams)
        
        # Lọc theo loại
        if loai == 'ngoai_ngu' and nn_pass:
            continue
        if loai == 'tin_hoc' and th_pass:
            continue
        
        result.append({
            'ma_sv': sv.get('ma_sv'),
            'ho_ten': sv.get('ho_ten'),
            'khoa': sv.get('khoa', {}).get('ten_khoa') if isinstance(sv.get('khoa'), dict) else '',
            'nganh': sv.get('nganh', {}).get('ten_nganh') if isinstance(sv.get('nganh'), dict) else '',
            'khoa_hoc': sv.get('khoa_hoc'),
            'dat_ngoai_ngu': nn_pass,
            'dat_tin_hoc': th_pass,
            'dat_chuan': nn_pass and th_pass
        })
    
    # Tính % đạt
    tong = len(result)
    dat = sum(1 for r in result if r['dat_chuan'])
    ti_le = round(dat / tong * 100, 2) if tong > 0 else 0
    
    return Response({
        'tong': tong,
        'da_dat': dat,
        'ti_le': ti_le,
        'chi_tiet': result
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def thong_ke_diem_theo_thoi_gian(request):
    """
    Thống kê điểm thi theo thời gian (kỳ, năm)
    Query params: mon_thi (CDR_NGOAI_NGU / CDR_TIN_HOC), nam_hoc
    """
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    exams = get_exam_records(token)
    dot_this = get_dot_thi(token)
    
    mon_thi = request.GET.get('mon_thi', 'CDR_NGOAI_NGU')
    nam_hoc = request.GET.get('nam_hoc')
    
    # Tạo map dot_thi
    dot_map = {d.get('id'): d for d in dot_this}
    
    # Nhóm theo kỳ (dựa trên thời gian bắt đầu)
    data_by_period = {}
    for exam in exams:
        if exam.get('mon_thi') != mon_thi:
            continue
        dot_id = exam.get('dot_thi')
        dot = dot_map.get(dot_id, {})
        thoi_gian = dot.get('thoi_gian_bat_dau', '')
        if not thoi_gian:
            continue
        # Lấy năm hoặc kỳ (VD: "Học kỳ 1 2025-2026")
        period = dot.get('ten_dot', '').split()[0] if dot.get('ten_dot') else 'Khác'
        if nam_hoc and nam_hoc not in dot.get('ten_dot', ''):
            continue
        
        if period not in data_by_period:
            data_by_period[period] = {'tong': 0, 'dat': 0, 'diem_list': []}
        data_by_period[period]['tong'] += 1
        data_by_period[period]['diem_list'].append(exam.get('diem_tong', 0))
        if exam.get('ket_qua_dat'):
            data_by_period[period]['dat'] += 1
    
    # Tính trung bình và tỉ lệ
    result = []
    for period, data in data_by_period.items():
        diem_avg = round(sum(data['diem_list']) / len(data['diem_list']), 2) if data['diem_list'] else 0
        result.append({
            'period': period,
            'tong_so_luot_thi': data['tong'],
            'so_luot_dat': data['dat'],
            'ti_le_dat': round(data['dat'] / data['tong'] * 100, 2) if data['tong'] > 0 else 0,
            'diem_trung_binh': diem_avg
        })
    
    return Response({
        'mon_thi': mon_thi,
        'data': sorted(result, key=lambda x: x['period'])
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def thong_ke_sv_theo_nhom(request):
    """
    Thống kê số lượng sinh viên theo nhóm: đạt/chưa đạt, theo khoa, ngành, khóa
    """
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    students = get_students(token)
    exams = get_exam_records(token)
    
    # Nhóm theo khoa
    khoa_stats = {}
    for sv in students:
        sv_exams = [e for e in exams if e.get('sinh_vien_id') == sv.get('id')]
        nn_pass = any(e.get('mon_thi') == 'CDR_NGOAI_NGU' and e.get('ket_qua_dat') for e in sv_exams)
        th_pass = any(e.get('mon_thi') == 'CDR_TIN_HOC' and e.get('ket_qua_dat') for e in sv_exams)
        dat = nn_pass and th_pass
        
        khoa_name = sv.get('khoa', {}).get('ten_khoa') if isinstance(sv.get('khoa'), dict) else 'Chưa phân'
        if khoa_name not in khoa_stats:
            khoa_stats[khoa_name] = {'tong': 0, 'dat': 0, 'chua_dat': 0}
        khoa_stats[khoa_name]['tong'] += 1
        if dat:
            khoa_stats[khoa_name]['dat'] += 1
        else:
            khoa_stats[khoa_name]['chua_dat'] += 1
    
    result = []
    for ten_khoa, stats in khoa_stats.items():
        result.append({
            'ten_khoa': ten_khoa,
            'tong': stats['tong'],
            'dat': stats['dat'],
            'chua_dat': stats['chua_dat'],
            'ti_le_dat': round(stats['dat'] / stats['tong'] * 100, 2) if stats['tong'] > 0 else 0
        })
    
    return Response({
        'theo_khoa': sorted(result, key=lambda x: -x['ti_le_dat'])
    })
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def thong_ke_bao_luu(request):
    """
    Thống kê tỉ lệ sinh viên có bảo lưu điểm
    """
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    
    # Lấy danh sách sinh viên
    students = get_students(token)
    
    # Lấy danh sách bảo lưu từ Exam Service
    try:
        headers = {'Authorization': f'Bearer {token}'}
        resp = requests.get('http://localhost:8002/api/baoluudiem/', headers=headers, timeout=5)
        if resp.status_code == 200:
            bao_luu_list = resp.json()
        else:
            bao_luu_list = []
    except Exception as e:
        bao_luu_list = []
    
    tong = len(students)
    
    # Đếm số sinh viên có ít nhất 1 bảo lưu
    sv_with_bao_luu = set()
    for bl in bao_luu_list:
        sv_with_bao_luu.add(bl.get('sinh_vien_id'))
    co_bao_luu = len(sv_with_bao_luu)
    tong_bao_luu = len(bao_luu_list)
    
    return Response({
        'tong_sinh_vien': tong,
        'co_bao_luu': co_bao_luu,
        'ti_le_bao_luu': round(co_bao_luu / tong * 100, 2) if tong > 0 else 0,
        'tong_ban_ghi_bao_luu': tong_bao_luu
    })
