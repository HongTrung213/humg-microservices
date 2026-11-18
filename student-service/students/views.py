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
    sheet_name = (request.data.get('sheet_name') or '').strip() or 0
    try:
        df = read_excel_with_smart_header(excel_file, sheet_name=sheet_name)
    except ValueError as e:
        if sheet_name != 0:
            return Response({'error': f'Không có sheet "{sheet_name}" trong file'}, status=400)
        return Response({'error': f'Không đọc được file: {str(e)}'}, status=400)
    except Exception as e:
        return Response({'error': f'Không đọc được file: {str(e)}'}, status=400)
    if 'mssv' not in df.columns:
        return Response({'error': 'Không tìm thấy cột Mã sinh viên / MSSV / MSV trong file'}, status=400)

    created_count = 0
    updated_count = 0
    errors = []

    for idx, row in df.iterrows():
        mssv = extract_mssv(
            row.get('mssv') or row.get('msv') or row.get('masv') or row.get('masinhvien') or ''
        )
        co_ten = any(clean_excel_val(row.get(k)) for k in ('hoten', 'hovaten', 'hodem', 'ten'))
        if not mssv:
            if co_ten:                      # bỏ qua dòng trống / chữ ký cuối trang
                errors.append(f"Dòng {idx+1}: Thiếu MSSV")
            continue
        if len(mssv) != 10:
            errors.append(f"Dòng {idx+1}: MSSV \"{mssv}\" không hợp lệ (cần 10 chữ số)")
            continue

        ho_ten = clean_excel_val(row.get('hoten')) or clean_excel_val(row.get('hovaten'))
        if ho_ten:
            ho_ten = f"{ho_ten} {clean_excel_val(row.get('tenghep'))}".strip()
        else:
            ho_ten = f"{clean_excel_val(row.get('hodem'))} {clean_excel_val(row.get('ten'))}".strip()
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
            errors.append(f"Dòng {idx+1}: Không thể tạo sinh viên")

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
        sv = SinhVien.objects.select_related('nganh').get(id=student_id)
        dat_nn = sv.check_dat_ngoai_ngu
        dat_th = sv.check_dat_tin_hoc
        return Response({
            'id': sv.id,
            'ma_sv': sv.ma_sv,
            'ho_ten': sv.ho_ten,
            'check_dat_ngoai_ngu': dat_nn,
            'check_dat_tin_hoc': dat_th,
            'dat_chuan_dau_ra': bool(sv.da_mien_cdr or (dat_nn and dat_th)),
            'da_mien_cdr': sv.da_mien_cdr,
            'bac_yeu_cau_ngoai_ngu': sv.get_required_foreign_language_level(),
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ensure_students(request):
    """
    Thêm hàng loạt sinh viên còn thiếu khi import danh sách thi.
    Body: {"students": [{"ma_sv": "2121050001", "ho_ten": "Nguyễn Văn A"}, ...]}
    Trả về {"created": n, "map": {"2121050001": 15, ...}}
    """
    items = request.data.get('students') or []
    if not isinstance(items, list):
        return Response({'error': 'students phải là danh sách'}, status=400)
    result, created = {}, 0
    for item in items[:5000]:
        mssv = extract_mssv((item or {}).get('ma_sv'))
        if not mssv or len(mssv) != 10:
            continue
        existed = SinhVien.objects.filter(ma_sv=mssv).exists()
        sv = ensure_student(mssv=mssv, ho_ten=(item or {}).get('ho_ten') or '')
        if sv:
            result[mssv] = sv.id
            if not existed:
                created += 1
    return Response({'created': created, 'map': result})
