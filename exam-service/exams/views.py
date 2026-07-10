from rest_framework import viewsets
from .models import DotThi, LichSuThi, BaoLuuDiem
from .serializers import DotThiSerializer, LichSuThiSerializer, BaoLuuDiemSerializer

class DotThiViewSet(viewsets.ModelViewSet):
    queryset = DotThi.objects.all()
    serializer_class = DotThiSerializer

class LichSuThiViewSet(viewsets.ModelViewSet):
    queryset = LichSuThi.objects.all()
    serializer_class = LichSuThiSerializer

class BaoLuuDiemViewSet(viewsets.ModelViewSet):
    queryset = BaoLuuDiem.objects.all()
    serializer_class = BaoLuuDiemSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .utils.import_utils import read_excel_with_smart_header, extract_mssv, to_float, clean_excel_val
import requests

@api_view(['POST'])

def import_exam_scores(request):
    """
    Import điểm thi cho một đợt thi cụ thể.
    Yêu cầu: file Excel có các cột: MSSV, DiemThanhPhan1, DiemThanhPhan2, ...
    """
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

    created_count = 0
    errors = []

    for idx, row in df.iterrows():
        mssv = extract_mssv(row.get('mssv') or row.get('masv') or '')
        if not mssv:
            errors.append(f"Dòng {idx+2}: Thiếu MSSV")
            continue

        # Tìm sinh viên (có thể gọi Student Service qua Gateway)
        try:
            resp = requests.get(f'http://localhost:8001/api/sinhvien/?mssv={mssv}')
            if resp.status_code != 200 or not resp.json():
                errors.append(f"Dòng {idx+2}: Không tìm thấy sinh viên MSSV {mssv}")
                continue
            sinh_vien_data = resp.json()[0]
        except Exception:
            errors.append(f"Dòng {idx+2}: Lỗi kết nối Student Service")
            continue

        # Lấy điểm
        d1 = to_float(row.get('diemthanhphan1') or row.get('diemtp1') or row.get('d1'))
        d2 = to_float(row.get('diemthanhphan2') or row.get('diemtp2') or row.get('d2'))
        d3 = to_float(row.get('diemthanhphan3') or row.get('diemtp3') or row.get('d3'))
        d4 = to_float(row.get('diemthanhphan4') or row.get('diemtp4') or row.get('d4'))
        diem_tong = to_float(row.get('diemtong') or row.get('tongdiem'))
        xep_loai = clean_excel_val(row.get('xeploai') or '')
        ghi_chu = clean_excel_val(row.get('ghichu') or '')

        # Lưu LichSuThi
        try:
            lich_su, created = LichSuThi.objects.update_or_create(
                sinh_vien_id=sinh_vien_data['id'],
                dot_thi=dot_thi,
                mon_thi=request.data.get('mon_thi', 'CDR_NGOAI_NGU'),
                defaults={
                    'diem_thanh_phan_1': d1,
                    'diem_thanh_phan_2': d2,
                    'diem_thanh_phan_3': d3,
                    'diem_thanh_phan_4': d4,
                    'diem_tong': diem_tong,
                    'xep_loai': xep_loai,
                    'ghi_chu': ghi_chu,
                    'ket_qua_dat': diem_tong is not None and diem_tong >= dot_thi.diem_chuan_ngoai_ngu if request.data.get('mon_thi') in ['TA_DAU_VAO', 'CDR_NGOAI_NGU'] else (diem_tong is not None and diem_tong >= dot_thi.diem_chuan_tin_hoc),
                }
            )
            created_count += 1
        except Exception as e:
            errors.append(f"Dòng {idx+2}: Lỗi lưu điểm - {str(e)}")

    return Response({
        'message': 'Import hoàn tất',
        'created': created_count,
        'errors': errors[:50]
    })


@api_view(['POST'])

def import_exam_schedule(request):
    """
    Import lịch thi từ file Excel.
    Yêu cầu: dot_thi_id và file Excel với các cột:
    MSSV, SBD, NgayThi, CaThi, PhongThi, NgayThi2, CaThi2, PhongThi2
    """
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

    created_count = 0
    updated_count = 0
    errors = []

    for idx, row in df.iterrows():
        mssv = extract_mssv(row.get('mssv') or row.get('masv') or '')
        if not mssv:
            errors.append(f"Dòng {idx+2}: Thiếu MSSV")
            continue

        # Tìm sinh viên từ Student Service
        try:
            resp = requests.get(f'http://localhost:8001/api/sinhvien/?mssv={mssv}', timeout=5)
            if resp.status_code != 200 or not resp.json():
                errors.append(f"Dòng {idx+2}: Không tìm thấy sinh viên MSSV {mssv}")
                continue
            sinh_vien_data = resp.json()[0]
            sinh_vien_id = sinh_vien_data['id']
        except Exception as e:
            errors.append(f"Dòng {idx+2}: Lỗi kết nối Student Service - {str(e)}")
            continue

        # Lấy thông tin lịch thi
        sbd = clean_excel_val(row.get('sbd') or row.get('sobaodanh') or '')
        ngay_thi = clean_excel_val(row.get('ngaythi') or row.get('ngay_thi') or '')
        ca_thi = clean_excel_val(row.get('cathi') or row.get('ca_thi') or '')
        phong_thi = clean_excel_val(row.get('phongthi') or row.get('phong_thi') or '')
        ngay_thi_2 = clean_excel_val(row.get('ngaythi2') or row.get('ngay_thi_2') or '')
        ca_thi_2 = clean_excel_val(row.get('cathi2') or row.get('ca_thi_2') or '')
        phong_thi_2 = clean_excel_val(row.get('phongthi2') or row.get('phong_thi_2') or '')
        ghi_chu = clean_excel_val(row.get('ghichu') or row.get('ghi_chu') or '')

        # Lưu hoặc cập nhật lịch thi
        try:
            lich_thi, created = LichSuThi.objects.update_or_create(
                sinh_vien_id=sinh_vien_id,
                dot_thi=dot_thi,
                mon_thi=request.data.get('mon_thi', 'CDR_NGOAI_NGU'),
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