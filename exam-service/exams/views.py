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


class LichSuThiViewSet(viewsets.ModelViewSet):
    queryset = LichSuThi.objects.all()
    serializer_class = LichSuThiSerializer


class BaoLuuDiemViewSet(viewsets.ModelViewSet):
    queryset = BaoLuuDiem.objects.all()
    serializer_class = BaoLuuDiemSerializer


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
    errors = []

    for idx, row in df.iterrows():
        parsed = parse_func(row)
        if not parsed:
            errors.append(f"Dòng {idx+2}: Không parse được dữ liệu")
            continue

        mssv = parsed.get('mssv')
        if not mssv:
            errors.append(f"Dòng {idx+2}: Thiếu MSSV")
            continue

        # Lấy sinh viên từ Student Service (dùng ma_sv)
        try:
            resp = requests.get(f'http://localhost:8001/api/sinhvien/?ma_sv={mssv}', timeout=5)
            if resp.status_code != 200 or not resp.json():
                errors.append(f"Dòng {idx+2}: Không tìm thấy SV {mssv}")
                continue
            sinh_vien_data = resp.json()[0]
            sinh_vien_id = sinh_vien_data['id']
        except Exception:
            errors.append(f"Dòng {idx+2}: Lỗi kết nối Student Service")
            continue

        diem_tong = parsed.get('diem_tong')
        if mon_thi in ['TA_DAU_VAO', 'CDR_NGOAI_NGU']:
            diem_chuan = dot_thi.diem_chuan_ngoai_ngu
        else:
            diem_chuan = dot_thi.diem_chuan_tin_hoc

        ket_qua_dat = diem_tong is not None and diem_tong >= diem_chuan

        # Lưu LichSuThi
        try:
            lich_su, created = LichSuThi.objects.update_or_create(
                sinh_vien_id=sinh_vien_id,
                dot_thi=dot_thi,
                mon_thi=mon_thi,
                defaults={
                    'sbd': parsed.get('sbd', ''),
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
            )
            created_count += 1

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
            errors.append(f"Dòng {idx+2}: Lỗi lưu - {str(e)}")

    return Response({
        'message': f'Import {loai} hoàn tất',
        'created': created_count,
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
    created_count = 0
    updated_count = 0
    errors = []

    for idx, row in df.iterrows():
        mssv = extract_mssv(get_first(row, ['mssv', 'ma sinh vien', 'masinhvien']))
        if not mssv:
            errors.append(f"Dòng {idx+2}: Thiếu MSSV")
            continue

        try:
            resp = requests.get(f'http://localhost:8001/api/sinhvien/?ma_sv={mssv}', timeout=5)
            if resp.status_code != 200 or not resp.json():
                errors.append(f"Dòng {idx+2}: Không tìm thấy SV {mssv}")
                continue
            sinh_vien_id = resp.json()[0]['id']
        except Exception:
            errors.append(f"Dòng {idx+2}: Lỗi kết nối Student Service")
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
            errors.append(f"Dòng {idx+2}: Lỗi lưu lịch thi - {str(e)}")

    return Response({
        'message': 'Import lịch thi hoàn tất',
        'created': created_count,
        'updated': updated_count,
        'errors': errors[:50]
    })