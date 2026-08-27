from rest_framework import viewsets
from .models import Khoa, NganhDaoTao, SinhVien
from .serializers import KhoaSerializer, NganhDaoTaoSerializer, SinhVienSerializer
from .utils.import_utils import (
    read_excel_with_smart_header,
    ensure_student,
    clean_excel_val,
    extract_mssv,
)
from .utils.import_utils import normalize_key

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .utils.import_utils import read_excel_with_smart_header, ensure_student, clean_excel_val, extract_mssv



class KhoaViewSet(viewsets.ModelViewSet):
    queryset = Khoa.objects.all()
    serializer_class = KhoaSerializer

class NganhDaoTaoViewSet(viewsets.ModelViewSet):
    queryset = NganhDaoTao.objects.all()
    serializer_class = NganhDaoTaoSerializer

class SinhVienViewSet(viewsets.ModelViewSet):
    queryset = SinhVien.objects.all()
    serializer_class = SinhVienSerializer

# students/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .utils.import_utils import read_excel_with_smart_header, ensure_student, clean_excel_val, extract_mssv
import pandas as pd

@api_view(['POST'])
@permission_classes([IsAuthenticated])   # <-- THÊM DÒNG NÀY
def import_students(request):
    """
    Import danh sách sinh viên từ file Excel.
    Yêu cầu: file có cột MSSV (hoặc MaSV), Họ tên (hoặc HoTen), Email (hoặc EmailTruong), Lớp, Ngành.
    """
    if 'file' not in request.FILES:
        return Response({'error': 'Vui lòng chọn file Excel'}, status=400)

    excel_file = request.FILES['file']
    try:
        df = read_excel_with_smart_header(excel_file)
    except Exception as e:
        return Response({'error': f'Không đọc được file: {str(e)}'}, status=400)

    created_count = 0
    updated_count = 0
    errors = []

    # Chuẩn hóa tên cột
    df.columns = [normalize_key(c) for c in df.columns]

    for idx, row in df.iterrows():
        mssv = extract_mssv(row.get('mssv') or row.get('masv') or row.get('ma_sinh_vien') or '')
        if not mssv:
            errors.append(f"Dòng {idx+2}: Thiếu MSSV")
            continue

        ho_ten = clean_excel_val(row.get('hoten') or row.get('ho_ten') or row.get('hovaten') or '')
        email = clean_excel_val(row.get('email') or row.get('email_truong') or row.get('emailtruong') or '')
        lop = clean_excel_val(row.get('lop') or row.get('lop_sinh_hoat') or '')
        phone = clean_excel_val(row.get('sdt') or row.get('so_dien_thoai') or row.get('sodienthoai') or '')
        ten_nganh = clean_excel_val(row.get('nganh') or row.get('nganh_dao_tao') or row.get('ten_nganh') or '')
        ma_lop = clean_excel_val(row.get('ma_lop') or row.get('malop') or '')

        sv = ensure_student(
            mssv=mssv,
            ho_ten=ho_ten,
            lop=lop,
            email=email,
            phone=phone,
            ten_nganh=ten_nganh,
            ma_lop=ma_lop
        )
        if sv:
            if SinhVien.objects.filter(mssv=mssv).exists():
                updated_count += 1
            else:
                created_count += 1
        else:
            errors.append(f"Dòng {idx+2}: Không thể tạo sinh viên")

    return Response({
        'message': 'Import hoàn tất',
        'created': created_count,
        'updated': updated_count,
        'errors': errors[:50]  # chỉ trả về tối đa 50 lỗi
    })

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import SinhVien

@api_view(['GET'])

def student_cdr_status(request, student_id):
    """Lấy trạng thái CĐR của một sinh viên"""
    try:
        sv = SinhVien.objects.get(id=student_id)
        return Response({
            'id': sv.id,
            'mssv': sv.mssv,
            'ho_ten': sv.ho_ten,
            'check_dat_ngoai_ngu': sv.check_dat_ngoai_ngu,
            'check_dat_tin_hoc': sv.check_dat_tin_hoc,
            'dat_chuan_dau_ra': sv.dat_chuan_dau_ra,
        })
    except SinhVien.DoesNotExist:
        return Response({'error': 'Sinh viên không tồn tại'}, status=404)
    
@api_view(['GET'])
def bulk_cdr_status(request):
    """
    Lấy trạng thái CĐR của tất cả sinh viên (có filter)
    Query params:
        - khoa_id: int (lọc theo khoa)
        - khoa_hoc: str (lọc theo khóa học, VD: K70)
        - dat_chuan: boolean (true/false)
    """
    queryset = SinhVien.objects.select_related('khoa', 'nganh').all()
    
    # Lọc
    khoa_id = request.GET.get('khoa_id')
    if khoa_id:
        queryset = queryset.filter(khoa_id=khoa_id)
    
    khoa_hoc = request.GET.get('khoa_hoc')
    if khoa_hoc:
        queryset = queryset.filter(khoa_hoc=khoa_hoc)
    
    dat_chuan = request.GET.get('dat_chuan')
    if dat_chuan is not None:
        dat_chuan = dat_chuan.lower() == 'true'
        # Lọc sau khi tính (dùng list comprehension vì property không filter được qua ORM)
    
    # Lấy dữ liệu
    result = []
    for sv in queryset:
        item = {
            'id': sv.id,
            'ma_sv': sv.ma_sv,
            'ho_ten': sv.ho_ten,
            'khoa': sv.khoa.ten_khoa if sv.khoa else None,
            'khoa_hoc': sv.khoa_hoc,
            'da_mien_cdr': sv.da_mien_cdr,
            'check_dat_ngoai_ngu': sv.check_dat_ngoai_ngu,
            'check_dat_tin_hoc': sv.check_dat_tin_hoc,
            'dat_chuan_dau_ra': sv.dat_chuan_dau_ra,
        }
        # Áp dụng filter dat_chuan nếu có
        if dat_chuan is not None:
            if dat_chuan and not sv.dat_chuan_dau_ra:
                continue
            if not dat_chuan and sv.dat_chuan_dau_ra:
                continue
        result.append(item)
    
    return Response({
        'count': len(result),
        'results': result
    })
