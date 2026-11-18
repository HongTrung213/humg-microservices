from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import DotThi, LichSuThi, BaoLuuDiem
from .serializers import DotThiSerializer, LichSuThiSerializer, BaoLuuDiemSerializer
from .utils.import_utils import (
    read_excel_with_smart_header,
    parse_tdnn_row,
    parse_cdr_nn_row,
    parse_cntt_row,
    extract_mssv,
    clean_excel_val,
    to_float,
    get_first
)
from .utils.bao_luu_utils import tao_bao_luu_tu_lich_su_thi
import requests


class DotThiViewSet(viewsets.ModelViewSet):
    queryset = DotThi.objects.all()
    serializer_class = DotThiSerializer


def _int_param(request, *names):
    """Đọc tham số số nguyên đầu tiên có trong query string (bỏ qua giá trị rỗng/không hợp lệ)."""
    for name in names:
        value = request.query_params.get(name)
        if value not in (None, ''):
            try:
                return int(value)
            except (TypeError, ValueError):
                return -1  # giá trị sai -> không trả bản ghi nào
    return None


class LichSuThiViewSet(viewsets.ModelViewSet):
    """
    Lịch sử / lịch thi. Hỗ trợ lọc: ?sinh_vien_id=, ?dot_thi_id= (hoặc ?dot_thi=), ?mon_thi=, ?sbd=
    Trước đây không lọc nên mọi sinh viên / mọi đợt thi đều nhận về toàn bộ dữ liệu
    (lộ điểm của nhau và làm sai kết quả xét CĐR).
    """
    queryset = LichSuThi.objects.all()
    serializer_class = LichSuThiSerializer

    def get_queryset(self):
        qs = super().get_queryset().select_related('dot_thi')
        sinh_vien_id = _int_param(self.request, 'sinh_vien_id')
        if sinh_vien_id is not None:
            qs = qs.filter(sinh_vien_id=sinh_vien_id)
        dot_thi_id = _int_param(self.request, 'dot_thi_id', 'dot_thi')
        if dot_thi_id is not None:
            qs = qs.filter(dot_thi_id=dot_thi_id)
        mon_thi = self.request.query_params.get('mon_thi')
        if mon_thi:
            qs = qs.filter(mon_thi=mon_thi)
        sbd = self.request.query_params.get('sbd')
        if sbd:
            qs = qs.filter(sbd=sbd.strip())
        return qs.order_by('dot_thi_id', 'mon_thi', 'sbd', 'id')


class BaoLuuDiemViewSet(viewsets.ModelViewSet):
    """Bảo lưu điểm. Hỗ trợ lọc: ?sinh_vien_id=, ?dot_thi_id=, ?loai="""
    queryset = BaoLuuDiem.objects.all()
    serializer_class = BaoLuuDiemSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        sinh_vien_id = _int_param(self.request, 'sinh_vien_id')
        if sinh_vien_id is not None:
            qs = qs.filter(sinh_vien_id=sinh_vien_id)
        dot_thi_id = _int_param(self.request, 'dot_thi_id', 'dot_thi')
        if dot_thi_id is not None:
            qs = qs.filter(dot_thi_id=dot_thi_id)
        loai = self.request.query_params.get('loai')
        if loai:
            qs = qs.filter(loai=loai)
        return qs


STUDENT_API = 'http://127.0.0.1:8001/api/'


def _build_mssv_map():
    """Lấy toàn bộ MSSV -> id sinh viên trong MỘT lần gọi (thay vì gọi lại cho từng dòng Excel)."""
    try:
        resp = requests.get(STUDENT_API + 'sinhvien/', timeout=30)
        if resp.status_code == 200:
            data = resp.json()
            if isinstance(data, dict):
                data = data.get('results', [])
            return {str(sv.get('ma_sv')): sv.get('id') for sv in data if sv.get('ma_sv')}
    except Exception:
        pass
    return {}


def _find_sinh_vien_id(mssv, mssv_map):
    """Tra id sinh viên theo MSSV: ưu tiên bảng đã nạp sẵn, nếu thiếu thì hỏi lại Student Service."""
    if mssv in mssv_map:
        return mssv_map[mssv], None
    try:
        resp = requests.get(STUDENT_API + 'sinhvien/', params={'ma_sv': mssv}, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            if isinstance(data, dict):
                data = data.get('results', [])
            for sv in data:
                if str(sv.get('ma_sv')) == mssv:
                    mssv_map[mssv] = sv['id']
                    return sv['id'], None
        return None, f"Không tìm thấy SV {mssv}"
    except Exception:
        return None, "Lỗi kết nối Student Service"


# ---------- IMPORT ĐIỂM (hỗ trợ 3 loại: tdnn, cdr_nn, cntt) ----------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def import_exam_scores(request):
    dot_thi_id = request.data.get('dot_thi_id')
    loai = request.data.get('loai', 'tdnn')
    if not dot_thi_id:
        return Response({'error': 'Vui lòng cung cấp dot_thi_id'}, status=400)

    dot_thi = DotThi.objects.filter(id=dot_thi_id).first()
    if not dot_thi:
        return Response({'error': 'Đợt thi không tồn tại'}, status=404)

    if 'file' not in request.FILES:
        return Response({'error': 'Vui lòng chọn file Excel'}, status=400)

    excel_file = request.FILES['file']
    try:
        df = read_excel_with_smart_header(excel_file)
    except Exception as e:
        return Response({'error': f'Không đọc được file: {str(e)}'}, status=400)

    if loai == 'tdnn':
        parse_func = parse_tdnn_row
        mon_thi = 'TA_DAU_VAO'
    elif loai == 'cdr_nn':
        parse_func = parse_cdr_nn_row
        mon_thi = 'CDR_NGOAI_NGU'
    elif loai == 'cntt':
        parse_func = parse_cntt_row
        mon_thi = 'CDR_TIN_HOC'
    else:
        return Response({'error': 'Loại không hợp lệ. Chọn: tdnn, cdr_nn, cntt'}, status=400)

    created_count = 0
    updated_count = 0
    errors = []
    mssv_map = _build_mssv_map()

    # idx là chỉ số dòng gốc trong file (0-based) -> số dòng Excel = idx + 1
    for idx, row in df.iterrows():
        parsed = parse_func(row)
        if not parsed:
            errors.append(f"Dòng {idx+1}: Không parse được dữ liệu")
            continue

        mssv = parsed.get('mssv')
        if not mssv:
            errors.append(f"Dòng {idx+1}: Thiếu MSSV")
            continue

        # Lấy sinh viên từ Student Service (dùng ma_sv, khớp chính xác)
        sinh_vien_id, err = _find_sinh_vien_id(mssv, mssv_map)
        if not sinh_vien_id:
            errors.append(f"Dòng {idx+1}: {err}")
            continue

        diem_tong = parsed.get('diem_tong')
        if mon_thi in ['TA_DAU_VAO', 'CDR_NGOAI_NGU']:
            diem_chuan = dot_thi.diem_chuan_ngoai_ngu
        else:
            diem_chuan = dot_thi.diem_chuan_tin_hoc

        # FIX BUG #8: Check điểm chuẩn + điểm liệt
        if mon_thi in ['TA_DAU_VAO', 'CDR_NGOAI_NGU']:
            diem_liet = dot_thi.diem_liet_ngoai_ngu
        else:
            diem_liet = dot_thi.diem_liet_tin_hoc

        diem_thanh_phan = [parsed.get(f'd{i}') for i in (1, 2, 3, 4)]
        diem_thanh_phan = [d for d in diem_thanh_phan if d is not None]

        co_diem_liet = False
        if diem_liet and diem_liet > 0 and diem_thanh_phan:
            co_diem_liet = any(d < diem_liet for d in diem_thanh_phan)

        ket_qua_dat = (
            diem_tong is not None
            and diem_tong >= diem_chuan
            and not co_diem_liet
        )

        # Lưu LichSuThi
        try:
            defaults = {
                    'diem_thanh_phan_1': parsed.get('d1'),
                    'diem_thanh_phan_2': parsed.get('d2'),
                    'diem_thanh_phan_3': parsed.get('d3'),
                    'diem_thanh_phan_4': parsed.get('d4'),
                    'diem_tong': diem_tong,
                    'xep_loai': parsed.get('xep_loai'),
                    'ghi_chu': parsed.get('ghi_chu'),
                    'ket_qua_dat': ket_qua_dat,
                    'co_bao_luu': parsed.get('co_bao_luu', False),
            }
            # Chỉ ghi SBD khi file điểm có cột SBD -> không xoá SBD đã import từ lịch thi
            if parsed.get('sbd'):
                defaults['sbd'] = parsed['sbd']
            lich_su, created = LichSuThi.objects.update_or_create(
                sinh_vien_id=sinh_vien_id,
                dot_thi=dot_thi,
                mon_thi=mon_thi,
                defaults=defaults,
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

            # === TỰ ĐỘNG BẢO LƯU ĐIỂM ===
            if loai == 'cdr_nn':
                # Ngoại ngữ
                bao_luu = tao_bao_luu_tu_lich_su_thi(
                    sinh_vien_id=sinh_vien_id,
                    dot_thi=dot_thi,
                    loai='NN',
                    diem_1=parsed.get('d1'),  # Nghe
                    diem_2=parsed.get('d2'),  # Đọc
                    diem_3=parsed.get('d3'),  # Viết
                    diem_4=parsed.get('d4'),  # Nói
                    nguong=25  # Có thể lấy từ dot_thi.nguong_bao_luu nếu có
                )
            elif loai == 'cntt':
                # Tin học
                bao_luu = tao_bao_luu_tu_lich_su_thi(
                    sinh_vien_id=sinh_vien_id,
                    dot_thi=dot_thi,
                    loai='TH',
                    diem_1=parsed.get('d1'),  # Trắc nghiệm
                    diem_2=parsed.get('d2'),  # Word
                    diem_3=parsed.get('d3'),  # Excel
                    diem_4=parsed.get('d4'),  # PowerPoint
                    nguong=25
                )
            else:
                bao_luu = None

            if bao_luu:
                lich_su.co_bao_luu = True
                lich_su.so_lan_bao_luu = (lich_su.so_lan_bao_luu or 0) + 1
                lich_su.save(update_fields=['co_bao_luu', 'so_lan_bao_luu'])

        except Exception as e:
            errors.append(f"Dòng {idx+1}: Lỗi lưu - {str(e)}")

    return Response({
        'message': f'Import {loai} hoàn tất',
        'created': created_count,
        'updated': updated_count,
        'errors': errors[:50]
    })


# ---------- IMPORT LỊCH THI ----------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def import_exam_schedule(request):
    dot_thi_id = request.data.get('dot_thi_id')
    if not dot_thi_id:
        return Response({'error': 'Vui lòng cung cấp dot_thi_id'}, status=400)

    dot_thi = DotThi.objects.filter(id=dot_thi_id).first()
    if not dot_thi:
        return Response({'error': 'Đợt thi không tồn tại'}, status=404)

    if 'file' not in request.FILES:
        return Response({'error': 'Vui lòng chọn file Excel'}, status=400)

    excel_file = request.FILES['file']
    try:
        df = read_excel_with_smart_header(excel_file)
    except Exception as e:
        return Response({'error': f'Không đọc được file: {str(e)}'}, status=400)

    mon_thi = request.data.get('mon_thi', 'CDR_NGOAI_NGU')
    if mon_thi not in dict(LichSuThi.MON_THI_CHOICES):
        return Response({'error': 'Môn thi không hợp lệ'}, status=400)
    created_count = 0
    updated_count = 0
    errors = []
    mssv_map = _build_mssv_map()

    for idx, row in df.iterrows():
        mssv = extract_mssv(get_first(row, ['mssv', 'ma sinh vien', 'masinhvien']))
        if not mssv:
            errors.append(f"Dòng {idx+1}: Thiếu MSSV")
            continue

        sinh_vien_id, err = _find_sinh_vien_id(mssv, mssv_map)
        if not sinh_vien_id:
            errors.append(f"Dòng {idx+1}: {err}")
            continue

        sbd = clean_excel_val(get_first(row, ['sbd', 'so bao danh', 'sobaodanh']))
        ngay_thi = clean_excel_val(get_first(row, ['ngaythi', 'ngay thi', 'ngay thi 1']))
        ca_thi = clean_excel_val(get_first(row, ['cathi', 'ca thi', 'ca thi 1']))
        phong_thi = clean_excel_val(get_first(row, ['phongthi', 'phong thi', 'phong thi 1']))
        ngay_thi_2 = clean_excel_val(get_first(row, ['ngaythi2', 'ngay thi 2', 'ngaynoi']))
        ca_thi_2 = clean_excel_val(get_first(row, ['cathi2', 'ca thi 2', 'canoi']))
        phong_thi_2 = clean_excel_val(get_first(row, ['phongthi2', 'phong thi 2', 'phongnoi']))
        ghi_chu = clean_excel_val(get_first(row, ['ghichu', 'ghi chu']))

        try:
            obj, created = LichSuThi.objects.update_or_create(
                sinh_vien_id=sinh_vien_id,
                dot_thi=dot_thi,
                mon_thi=mon_thi,
                defaults={
                    'sbd': sbd,
                    'ngay_thi': ngay_thi,
                    'ca_thi': ca_thi,
                    'phong_thi': phong_thi,
                    'ngay_thi_2': ngay_thi_2,
                    'ca_thi_2': ca_thi_2,
                    'phong_thi_2': phong_thi_2,
                    'ghi_chu': ghi_chu,
                }
            )
            if created:
                created_count += 1
            else:
                updated_count += 1
        except Exception as e:
            errors.append(f"Dòng {idx+1}: Lỗi lưu lịch thi - {str(e)}")

    return Response({
        'message': 'Import lịch thi hoàn tất',
        'created': created_count,
        'updated': updated_count,
        'errors': errors[:50]
    })
