from rest_framework import viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import DotThi, LichSuThi, BaoLuuDiem
from .serializers import DotThiSerializer, LichSuThiSerializer, BaoLuuDiemSerializer
from .utils.import_utils import (
    scan_workbook,
    default_sheet,
    parse_score_row,
    parse_schedule_row,
    is_valid_mssv,
)
from .utils.bao_luu_utils import tao_bao_luu_tu_lich_su_thi
import requests


class DotThiViewSet(viewsets.ModelViewSet):
    queryset = DotThi.objects.all()
    serializer_class = DotThiSerializer

    @action(detail=True, methods=['get'], url_path='export-scores')
    def export_scores(self, request, pk=None):
        """Xuất danh sách thí sinh + lịch thi + điểm của đợt ra Excel (mỗi môn thi một sheet)."""
        from io import BytesIO
        from django.http import HttpResponse
        from openpyxl import Workbook
        from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
        from openpyxl.utils import get_column_letter

        dot = self.get_object()
        sv_info = {}
        try:
            resp = requests.get(STUDENT_API + 'sinhvien/', timeout=60)
            data = resp.json() if resp.status_code == 200 else []
            if isinstance(data, dict):
                data = data.get('results', [])
            sv_info = {sv.get('id'): sv for sv in data}
        except Exception:
            pass

        MON = [('TA_DAU_VAO', 'Tiếng Anh đầu vào', ['Nghe', 'Đọc', 'Viết', 'Nói']),
               ('CDR_NGOAI_NGU', 'CĐR Ngoại ngữ', ['Nghe', 'Đọc', 'Viết', 'Nói']),
               ('CDR_TIN_HOC', 'CĐR Tin học', ['Trắc nghiệm', 'Thực hành'])]
        navy = PatternFill('solid', fgColor='0A3D91')
        thin = Side(style='thin', color='C9D6E8')
        wb = Workbook()
        wb.remove(wb.active)
        for code, title, parts in MON:
            rows = list(LichSuThi.objects.filter(dot_thi=dot, mon_thi=code).order_by('sbd', 'id'))
            if not rows:
                continue
            ws = wb.create_sheet(title[:31])
            ws.append([f'{dot.ma_dot} – {dot.ten_dot}'])
            ws.append([f'Môn thi: {title}   ·   Số thí sinh: {len(rows)}'])
            ws.append([])
            header = ['STT', 'Mã sinh viên', 'Họ và tên', 'SBD', 'Ngày thi', 'Ca thi', 'Phòng thi',
                      'Ngày VĐ', 'Ca VĐ', 'Phòng VĐ'] + parts + ['Điểm đánh giá', 'Xếp loại', 'Kết quả', 'Bảo lưu', 'Ghi chú']
            ws.append(header)
            for c in range(1, len(header) + 1):
                cell = ws.cell(row=4, column=c)
                cell.font = Font(bold=True, color='FFFFFF')
                cell.fill = navy
                cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
            rows.sort(key=lambda l: (sv_info.get(l.sinh_vien_id, {}).get('ho_ten', '').split() or [''])[-1:] + [str(sv_info.get(l.sinh_vien_id, {}).get('ho_ten', ''))])
            for i, l in enumerate(rows, 1):
                sv = sv_info.get(l.sinh_vien_id, {})
                diem = [l.diem_thanh_phan_1, l.diem_thanh_phan_2, l.diem_thanh_phan_3, l.diem_thanh_phan_4][:len(parts)]
                co_diem = l.diem_tong is not None or bool(l.xep_loai)
                ws.append([i, sv.get('ma_sv', ''), sv.get('ho_ten', f'SV #{l.sinh_vien_id}'), l.sbd or '',
                           l.ngay_thi or '', l.ca_thi or '', l.phong_thi or '',
                           l.ngay_thi_2 or '', l.ca_thi_2 or '', l.phong_thi_2 or ''] + diem +
                          [l.diem_tong, l.xep_loai or '', ('Đạt' if l.ket_qua_dat else 'Chưa đạt') if co_diem else 'Chờ điểm',
                           'Có' if l.co_bao_luu else '', l.ghi_chu or ''])
            for row in ws.iter_rows(min_row=4, max_row=ws.max_row):
                for cell in row:
                    cell.border = Border(top=thin, bottom=thin, left=thin, right=thin)
            ws['A1'].font = Font(bold=True, size=14, color='0A3D91')
            ws['A2'].font = Font(italic=True, color='667085')
            widths = [6, 14, 26, 9, 12, 18, 11, 12, 18, 13] + [11] * len(parts) + [13, 22, 11, 9, 40]
            for c, w in enumerate(widths, 1):
                ws.column_dimensions[get_column_letter(c)].width = w
            ws.freeze_panes = 'D5'
        if not wb.sheetnames:
            ws = wb.create_sheet('Trống')
            ws.append([f'Đợt {dot.ma_dot} chưa có thí sinh.'])
        buf = BytesIO()
        wb.save(buf)
        response = HttpResponse(buf.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="bang_diem_{dot.ma_dot}.xlsx"'
        return response


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


# ---------- IMPORT LỊCH THI / ĐIỂM THI ----------
SCORE_MON = {'tdnn': 'TA_DAU_VAO', 'cdr_nn': 'CDR_NGOAI_NGU', 'cntt': 'CDR_TIN_HOC'}


def _truthy(value):
    return str(value or '').strip().lower() in ('1', 'true', 'yes', 'on')


def _ensure_students(request, students):
    """Nhờ Student Service tạo các sinh viên còn thiếu (MSSV + họ tên). Trả về {ma_sv: id}."""
    if not students:
        return {}, None
    headers = {}
    if request.headers.get('Authorization'):
        headers['Authorization'] = request.headers['Authorization']
    try:
        resp = requests.post(STUDENT_API + 'ensure-students/', json={'students': students},
                             headers=headers, timeout=120)
        if resp.status_code == 200:
            return {str(k): v for k, v in (resp.json().get('map') or {}).items()}, None
        return {}, f'Student Service trả lỗi {resp.status_code}'
    except Exception:
        return {}, 'Không kết nối được Student Service để thêm sinh viên mới'


def _ket_qua(parsed, dot_thi, mon_thi, has_xep_loai_col):
    """Kết quả Đạt/Chưa đạt: ưu tiên cột Xếp loại do Hội đồng kiểm tra quyết định (QĐ 2323/QĐ-MĐC)."""
    if parsed['vang_thi'] or parsed.get('huy_kq'):
        return False
    if parsed['ket_qua_file'] is not None:
        return parsed['ket_qua_file']
    if has_xep_loai_col:
        return False          # file có cột Xếp loại nhưng ô trống -> không đạt
    diem_tong = parsed.get('diem_tong')
    if diem_tong is None:
        return False
    if mon_thi in ('TA_DAU_VAO', 'CDR_NGOAI_NGU'):
        diem_chuan, diem_liet = dot_thi.diem_chuan_ngoai_ngu, dot_thi.diem_liet_ngoai_ngu
    else:
        diem_chuan, diem_liet = dot_thi.diem_chuan_tin_hoc, dot_thi.diem_liet_tin_hoc
    parts = [parsed.get(f'd{i}') for i in (1, 2, 3, 4) if parsed.get(f'd{i}') is not None]
    co_diem_liet = bool(diem_liet and diem_liet > 0 and any(d < diem_liet for d in parts))
    return diem_tong >= diem_chuan and not co_diem_liet


def _run_import(request, kind):
    """
    kind = 'lich' (lịch thi) hoặc 'diem' (kết quả thi).
    Tham số (multipart): dot_thi_id, file, mon_thi (lịch) | loai (điểm: tdnn/cdr_nn/cntt),
    sheet (tên sheet, tuỳ chọn), dry_run=1 (chỉ xem trước), tao_sv_moi=1 (tự thêm SV chưa có).
    """
    dot_thi_id = request.data.get('dot_thi_id')
    if not dot_thi_id:
        return Response({'error': 'Vui lòng chọn đợt thi'}, status=400)
    dot_thi = DotThi.objects.filter(id=dot_thi_id).first()
    if not dot_thi:
        return Response({'error': 'Đợt thi không tồn tại'}, status=404)
    if 'file' not in request.FILES:
        return Response({'error': 'Vui lòng chọn file Excel'}, status=400)

    if kind == 'diem':
        loai = request.data.get('loai', 'tdnn')
        mon_thi = SCORE_MON.get(loai)
        if not mon_thi:
            return Response({'error': 'Loại không hợp lệ. Chọn: tdnn, cdr_nn, cntt'}, status=400)
    else:
        loai = None
        mon_thi = request.data.get('mon_thi', 'CDR_NGOAI_NGU')
        if mon_thi not in dict(LichSuThi.MON_THI_CHOICES):
            return Response({'error': 'Môn thi không hợp lệ'}, status=400)

    dry_run = _truthy(request.data.get('dry_run'))
    tao_sv_moi = _truthy(request.data.get('tao_sv_moi'))

    try:
        sheets, frames = scan_workbook(request.FILES['file'])
    except Exception as e:
        return Response({'error': f'Không đọc được file Excel: {e}'}, status=400)

    sheet = request.data.get('sheet') or default_sheet(sheets)
    if not sheet or sheet not in frames:
        return Response({
            'error': 'Không tìm thấy sheet có dòng tiêu đề "Mã sinh viên"/"MSSV" trong file.' if not sheet
                     else f'Sheet "{sheet}" không có dòng tiêu đề "Mã sinh viên"/"MSSV".',
            'sheets': sheets,
        }, status=400)
    df, column_labels, header_row = frames[sheet]
    has_xep_loai_col = 'xeploai' in df.columns or 'ketqua' in df.columns

    # ---- Đọc & phân loại từng dòng
    rows, skipped, errors = [], [], []
    seen = set()
    for idx, row in df.iterrows():
        line = idx + 1                      # số dòng thật trong Excel
        parsed = parse_score_row(row, loai) if kind == 'diem' else parse_schedule_row(row)
        mssv = parsed['mssv']
        if not mssv:
            continue                        # dòng trống / chữ ký cuối trang
        if not is_valid_mssv(mssv):
            errors.append(f'Dòng {line}: MSSV "{mssv}" không hợp lệ (cần 10 chữ số)')
            continue
        if parsed['skip_reason']:
            skipped.append(f"Dòng {line} ({mssv}): {parsed['skip_reason']}")
            continue
        if mssv in seen:
            skipped.append(f'Dòng {line} ({mssv}): trùng MSSV trong file, dùng dòng đầu tiên')
            continue
        seen.add(mssv)
        parsed['line'] = line
        rows.append(parsed)

    mssv_map = _build_mssv_map()
    missing = [r for r in rows if r['mssv'] not in mssv_map]

    existing_ids = set(LichSuThi.objects.filter(dot_thi=dot_thi, mon_thi=mon_thi)
                       .values_list('sinh_vien_id', flat=True))

    if dry_run:
        sample = []
        for r in rows[:12]:
            item = {k: r.get(k) for k in ('line', 'mssv', 'ho_ten', 'sbd', 'ngay_thi', 'ca_thi', 'phong_thi',
                                           'ngay_thi_2', 'ca_thi_2', 'phong_thi_2', 'd1', 'd2', 'd3', 'd4',
                                           'diem_tong', 'xep_loai', 'ghi_chu')}
            if kind == 'diem':
                item['ket_qua_dat'] = _ket_qua(r, dot_thi, mon_thi, has_xep_loai_col)
                item['vang_thi'] = r['vang_thi']
            item['trang_thai'] = 'moi_sv' if r['mssv'] not in mssv_map else (
                'cap_nhat' if mssv_map[r['mssv']] in existing_ids else 'them_moi')
            sample.append(item)
        se_cap_nhat = sum(1 for r in rows if mssv_map.get(r['mssv']) in existing_ids)
        return Response({
            'dry_run': True,
            'sheets': sheets,
            'sheet': sheet,
            'header_row': header_row + 1,
            'columns': column_labels,
            'tong_dong': len(rows),
            'se_them_moi': len(rows) - se_cap_nhat,
            'se_cap_nhat': se_cap_nhat,
            'sv_chua_co': len(missing),
            'sv_chua_co_mau': [f"{r['mssv']} – {r['ho_ten']}" for r in missing[:15]],
            'dat': sum(1 for r in rows if kind == 'diem' and _ket_qua(r, dot_thi, mon_thi, has_xep_loai_col)),
            'vang': sum(1 for r in rows if kind == 'diem' and r['vang_thi']),
            'skipped': skipped[:100],
            'errors': errors[:100],
            'sample': sample,
        })

    # ---- Thêm sinh viên còn thiếu (nếu được phép)
    so_sv_moi = 0
    if missing and tao_sv_moi:
        created_map, err = _ensure_students(request, [{'ma_sv': r['mssv'], 'ho_ten': r['ho_ten']} for r in missing])
        if err:
            errors.append(err)
        so_sv_moi = sum(1 for r in missing if r['mssv'] in created_map)
        mssv_map.update(created_map)

    created_count = updated_count = 0
    for r in rows:
        sinh_vien_id = mssv_map.get(r['mssv'])
        if not sinh_vien_id:
            errors.append(f"Dòng {r['line']}: SV {r['mssv']} ({r['ho_ten']}) chưa có trong hệ thống")
            continue
        try:
            if kind == 'diem':
                ket_qua_dat = _ket_qua(r, dot_thi, mon_thi, has_xep_loai_col)
                defaults = {
                    'diem_thanh_phan_1': r.get('d1'),
                    'diem_thanh_phan_2': r.get('d2'),
                    'diem_thanh_phan_3': r.get('d3'),
                    'diem_thanh_phan_4': r.get('d4'),
                    'diem_tong': r.get('diem_tong'),
                    'xep_loai': ('Vắng thi' if r['vang_thi'] else 'Hủy kết quả (VPQC)' if r.get('huy_kq')
                                 else r.get('xep_loai') or ('Đạt' if ket_qua_dat else 'Chưa đạt'))[:100],
                    'ghi_chu': r.get('ghi_chu') or None,
                    'ket_qua_dat': ket_qua_dat,
                    'co_bao_luu': r.get('co_bao_luu', False),
                }
                # Chỉ ghi SBD khi file điểm có cột SBD -> không xoá SBD đã import từ lịch thi
                if r.get('sbd'):
                    defaults['sbd'] = r['sbd']
            else:
                defaults = {k: (r.get(k) or None) for k in ('ngay_thi', 'ca_thi', 'phong_thi',
                                                            'ngay_thi_2', 'ca_thi_2', 'phong_thi_2', 'ghi_chu')}
                if r.get('sbd'):
                    defaults['sbd'] = r['sbd']
            lich_su, created = LichSuThi.objects.update_or_create(
                sinh_vien_id=sinh_vien_id, dot_thi=dot_thi, mon_thi=mon_thi, defaults=defaults,
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

            # Tự động bảo lưu phần thi đạt cho sinh viên CHƯA đạt (QĐ: bảo lưu tối đa 24 tháng)
            if kind == 'diem' and not defaults['ket_qua_dat'] and not r['vang_thi'] and loai in ('cdr_nn', 'cntt'):
                bao_luu = tao_bao_luu_tu_lich_su_thi(
                    sinh_vien_id=sinh_vien_id, dot_thi=dot_thi, loai='NN' if loai == 'cdr_nn' else 'TH',
                    diem_1=r.get('d1'), diem_2=r.get('d2'), diem_3=r.get('d3'), diem_4=r.get('d4'), nguong=25,
                )
                if bao_luu and not lich_su.co_bao_luu:
                    lich_su.co_bao_luu = True
                    lich_su.so_lan_bao_luu = (lich_su.so_lan_bao_luu or 0) + 1
                    lich_su.save(update_fields=['co_bao_luu', 'so_lan_bao_luu'])
        except Exception as e:
            errors.append(f"Dòng {r['line']}: Lỗi lưu - {e}")

    return Response({
        'message': f'Import {"điểm" if kind == "diem" else "lịch thi"} hoàn tất (sheet "{sheet}")',
        'sheet': sheet,
        'created': created_count,
        'updated': updated_count,
        'sv_moi': so_sv_moi,
        'skipped': skipped[:100],
        'errors': errors[:100],
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def import_exam_scores(request):
    return _run_import(request, 'diem')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def import_exam_schedule(request):
    return _run_import(request, 'lich')
