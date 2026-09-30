from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import pandas as pd

from .models import Khoa, NganhDaoTao, SinhVien
from .serializers import KhoaSerializer, NganhDaoTaoSerializer, SinhVienSerializer
from .utils.import_utils import (
    read_excel_with_smart_header,
    ensure_student,
    clean_excel_val,
    extract_mssv,
    normalize_key,
)


class KhoaViewSet(viewsets.ModelViewSet):
    queryset = Khoa.objects.all()
    serializer_class = KhoaSerializer


class NganhDaoTaoViewSet(viewsets.ModelViewSet):
    queryset = NganhDaoTao.objects.all()
    serializer_class = NganhDaoTaoSerializer


class SinhVienViewSet(viewsets.ModelViewSet):
    """
    FIX BUG #9: Filter theo query params.
    Hỗ trợ: ?ma_sv=, ?khoa=, ?nganh=, ?khoa_hoc=, ?search=
    """
    # ✅ Cần queryset cho DRF router
    queryset = SinhVien.objects.all()
    serializer_class = SinhVienSerializer

    def get_queryset(self):
        qs = SinhVien.objects.select_related('khoa', 'nganh').all()

        ma_sv = self.request.query_params.get('ma_sv')
        if ma_sv:
            qs = qs.filter(ma_sv=ma_sv.strip())

        ma_sv_like = self.request.query_params.get('ma_sv__icontains')
        if ma_sv_like:
            qs = qs.filter(ma_sv__icontains=ma_sv_like.strip())

        khoa_id = self.request.query_params.get('khoa')
        if khoa_id:
            qs = qs.filter(khoa_id=khoa_id)

        nganh_id = self.request.query_params.get('nganh')
        if nganh_id:
            qs = qs.filter(nganh_id=nganh_id)

        khoa_hoc = self.request.query_params.get('khoa_hoc')
        if khoa_hoc:
            qs = qs.filter(khoa_hoc=khoa_hoc.strip())

        lop = self.request.query_params.get('lop')
        if lop:
            qs = qs.filter(lop__icontains=lop.strip())

        search = self.request.query_params.get('search')
        if search:
            from django.db.models import Q
            search = search.strip()
            qs = qs.filter(
                Q(ma_sv__icontains=search) |
                Q(ho_ten__icontains=search) |
                Q(email_truong__icontains=search)
            )

        return qs.order_by('ma_sv')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def import_students(request):
    """Import danh sách sinh viên từ file Excel."""
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

    df.columns = [normalize_key(c) for c in df.columns]

    for idx, row in df.iterrows():
        mssv = extract_mssv(
            row.get('mssv') or row.get('masv') or row.get('masinhvien') or ''
        )
        if not mssv:
            errors.append(f"Dòng {idx+2}: Thiếu MSSV")
            continue

        ho_ten = clean_excel_val(row.get('hoten') or row.get('hovaten') or '')
        email = clean_excel_val(row.get('email') or row.get('emailtruong') or '')
        lop = clean_excel_val(row.get('lop') or row.get('lopsinhhoat') or '')
        phone = clean_excel_val(row.get('sdt') or row.get('sodienthoai') or '')
        ten_nganh = clean_excel_val(row.get('nganh') or row.get('tennganh') or '')
        ma_lop = clean_excel_val(row.get('malop') or '')

        existed = SinhVien.objects.filter(ma_sv=mssv).exists()

        sv = ensure_student(
            mssv=mssv, ho_ten=ho_ten, lop=lop, email=email,
            phone=phone, ten_nganh=ten_nganh, ma_lop=ma_lop,
        )

        if sv:
            if existed:
                updated_count += 1
            else:
                created_count += 1
        else:
            errors.append(f"Dòng {idx+2}: Không thể tạo sinh viên")

    return Response({
        'message': 'Import hoàn tất',
        'created': created_count,
        'updated': updated_count,
        'errors': errors[:50],
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_cdr_status(request, student_id):
    """Lấy trạng thái CĐR của một sinh viên."""
    try:
        sv = SinhVien.objects.get(id=student_id)
        return Response({
            'id': sv.id,
            'ma_sv': sv.ma_sv,
            'ho_ten': sv.ho_ten,
            'check_dat_ngoai_ngu': sv.check_dat_ngoai_ngu,
            'check_dat_tin_hoc': sv.check_dat_tin_hoc,
            'dat_chuan_dau_ra': sv.dat_chuan_dau_ra,
        })
    except SinhVien.DoesNotExist:
        return Response({'error': 'Sinh viên không tồn tại'}, status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bulk_cdr_status(request):
    """Lấy trạng thái CĐR của tất cả sinh viên (có filter)."""
    queryset = SinhVien.objects.select_related('khoa', 'nganh').all()

    khoa_id = request.GET.get('khoa_id')
    if khoa_id:
        queryset = queryset.filter(khoa_id=khoa_id)

    khoa_hoc = request.GET.get('khoa_hoc')
    if khoa_hoc:
        queryset = queryset.filter(khoa_hoc=khoa_hoc)

    dat_chuan = request.GET.get('dat_chuan')
    if dat_chuan is not None:
        dat_chuan = dat_chuan.lower() == 'true'

    result = []
    for sv in queryset:
        item = {
            'id': sv.id,
            'ma_sv': sv.ma_sv,
            'ho_ten': sv.ho_ten,
            'email_truong': sv.email_truong,
            'email_ca_nhan': sv.email_ca_nhan,
            'khoa': sv.khoa.ten_khoa if sv.khoa else None,
            'khoa_id': sv.khoa_id,
            'khoa_hoc': sv.khoa_hoc,
            'da_mien_cdr': sv.da_mien_cdr,
            'check_dat_ngoai_ngu': sv.check_dat_ngoai_ngu,
            'check_dat_tin_hoc': sv.check_dat_tin_hoc,
            'dat_chuan_dau_ra': sv.dat_chuan_dau_ra,
        }
        if dat_chuan is not None:
            if dat_chuan and not sv.dat_chuan_dau_ra:
                continue
            if not dat_chuan and sv.dat_chuan_dau_ra:
                continue
        result.append(item)

    return Response({
        'count': len(result),
        'results': result,
    })