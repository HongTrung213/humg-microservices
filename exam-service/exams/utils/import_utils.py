"""
Đọc file Excel lịch thi / kết quả thi của Trung tâm Ngoại ngữ – Tin học HUMG.

Hỗ trợ đúng các mẫu file thực tế:
- Tiêu đề trường/hội đồng ở vài dòng đầu, dòng tiêu đề cột nằm ở giữa trang.
- Tiêu đề cột 2 tầng (ví dụ "LỊCH THI TRÊN MÁY TÍNH" > NGÀY KT / CA KT / PHÒNG THI và
  "LỊCH THI VẤN ĐÁP" > NGÀY KT / CA KT / Phòng tập trung).
- Cột mã sinh viên tên "Mã sinh viên", "MSV", "MSSV"...; họ tên tách "Họ đệm" + "Tên"
  hoặc "Họ và tên" + một cột tên không tiêu đề.
- Workbook nhiều sheet (sheet phân tích, sheet kết quả cũ...): chọn đúng sheet cần import.
"""
import re
import unicodedata
from datetime import date, datetime

import pandas as pd

MSSV_KEYS = ('mssv', 'msv', 'masv', 'masinhvien', 'masosinhvien', 'masvien')
NAME_KEYS = ('hovaten', 'hoten', 'hotensinhvien', 'tensinhvien')


# ---------------------------------------------------------------- helpers
def normalize_key(text):
    """Chuẩn hoá tên cột: bỏ dấu (kể cả chữ đ), chữ thường, chỉ giữ a-z0-9."""
    if text is None:
        return ''
    text = str(text).strip().lower()
    if text in ('nan', 'none', 'nat'):
        return ''
    text = text.replace('đ', 'd')
    text = unicodedata.normalize('NFD', text)
    text = ''.join(ch for ch in text if unicodedata.category(ch) != 'Mn')
    return re.sub(r'[^a-z0-9]', '', text)


def clean_excel_val(val):
    if val is None:
        return ''
    if isinstance(val, (pd.Timestamp, datetime)):
        return val.strftime('%d/%m/%Y')
    if isinstance(val, date):
        return val.strftime('%d/%m/%Y')
    try:
        if pd.isna(val):
            return ''
    except (TypeError, ValueError):
        pass
    if isinstance(val, float) and val.is_integer():
        return str(int(val))
    return re.sub(r'\s+', ' ', str(val)).strip()


def to_float(val):
    if val is None:
        return None
    try:
        if pd.isna(val):
            return None
    except (TypeError, ValueError):
        pass
    txt = str(val).strip().replace(',', '.')
    if not txt:
        return None
    try:
        return float(txt)
    except (TypeError, ValueError):
        return None


def extract_mssv(value):
    raw = clean_excel_val(value)
    if raw.endswith('.0'):
        raw = raw[:-2]
    digits = re.sub(r'\D', '', raw)
    return digits if len(digits) >= 5 else ''


def is_valid_mssv(mssv):
    """MSSV của HUMG gồm 10 chữ số (2 số đầu là năm nhập học)."""
    return bool(mssv) and len(mssv) == 10 and mssv.isdigit()


def get_first(row, keys, default=''):
    for key in keys:
        norm = normalize_key(key)
        if norm in row.index:
            value = clean_excel_val(row.get(norm))
            if value:
                return value
    return default


def get_float_first(row, keys):
    for key in keys:
        norm = normalize_key(key)
        if norm in row.index:
            val = to_float(row.get(norm))
            if val is not None:
                return val
    return None


# ---------------------------------------------------------------- header / sheet
def find_header_row(df_raw, max_scan=25):
    """Dòng tiêu đề = dòng đầu tiên có một ô đúng là tên cột mã sinh viên."""
    for i in range(min(max_scan, len(df_raw))):
        keys = [normalize_key(v) for v in df_raw.iloc[i].tolist()]
        if any(k in MSSV_KEYS for k in keys):
            return i
    return None


def _looks_like_subheader(top, sub, mssv_col):
    """Dòng ngay dưới tiêu đề là tiêu đề phụ (tiêu đề 2 tầng) nếu ô MSSV trống và có >=2 ô chữ."""
    if mssv_col is None or mssv_col >= len(sub):
        return False
    if extract_mssv(sub[mssv_col]):
        return False
    texts = [clean_excel_val(v) for v in sub]
    words = [t for t in texts if t and not re.fullmatch(r'[\d.,]+', t)]
    return len(words) >= 2


def build_frame(df_raw):
    """Trả về (DataFrame dữ liệu với tên cột đã chuẩn hoá, danh sách cột hiển thị, header_row) hoặc None."""
    h = find_header_row(df_raw)
    if h is None:
        return None
    top = df_raw.iloc[h].tolist()
    top_keys = [normalize_key(v) for v in top]
    mssv_col = next((j for j, k in enumerate(top_keys) if k in MSSV_KEYS), None)
    sub = df_raw.iloc[h + 1].tolist() if h + 1 < len(df_raw) else []
    two_row = bool(sub) and _looks_like_subheader(top, sub, mssv_col)

    names, labels, seen = [], [], {}
    prev_key = ''
    for j in range(df_raw.shape[1]):
        t = clean_excel_val(top[j]) if j < len(top) else ''
        s = clean_excel_val(sub[j]) if two_row and j < len(sub) else ''
        label = s or t
        key = normalize_key(label)
        if not key and prev_key in NAME_KEYS + ('hodem',):
            key, label = 'tenghep', 'Tên'          # cột tên không tiêu đề ngay sau cột họ
        if not key:
            key = f'cot{j + 1}'
        if key in MSSV_KEYS:
            key = 'mssv'
        seen[key] = seen.get(key, 0) + 1
        if seen[key] > 1:
            key = f'{key}{seen[key]}'             # NGÀY KT (máy tính) -> ngaykt, NGÀY KT (vấn đáp) -> ngaykt2
        names.append(key)
        labels.append(label)
        prev_key = key

    start = h + (2 if two_row else 1)
    df = df_raw.iloc[start:].copy()
    df.columns = names
    df = df.dropna(how='all')
    return df, [lb for lb in labels if lb], h


def scan_workbook(excel_file):
    """Liệt kê sheet: có tiêu đề MSSV không, có bao nhiêu dòng có MSSV."""
    xls = pd.ExcelFile(excel_file)
    sheets = []
    frames = {}
    for name in xls.sheet_names:
        df_raw = xls.parse(name, header=None, dtype=object)
        built = build_frame(df_raw)
        rows = 0
        if built:
            df = built[0]
            if 'mssv' in df.columns:
                rows = int(df['mssv'].map(lambda v: bool(extract_mssv(v))).sum())
            frames[name] = built
        sheets.append({'name': name, 'has_header': bool(built), 'rows': rows})
    return sheets, frames


def default_sheet(sheets):
    """Sheet mặc định: có dữ liệu, ưu tiên tên có "mới"/"print"/"in", tránh "(cũ)"."""
    candidates = [s for s in sheets if s['has_header'] and s['rows'] > 0]
    if not candidates:
        return None

    def score(s):
        n = normalize_key(s['name'])
        raw = s['name'].lower()
        sc = 0
        if 'moi' in n:
            sc += 2
        if 'print' in n or raw.endswith('-in') or raw.endswith(' in'):
            sc += 1
        if 'cũ' in raw or '(cu)' in raw:
            sc -= 5
        return sc
    return max(candidates, key=lambda s: (score(s), -sheets.index(s)))['name']


# ---------------------------------------------------------------- row parsers
def _ho_ten(row):
    name = get_first(row, NAME_KEYS)
    if name:
        extra = get_first(row, ['tenghep'])
        return re.sub(r'\s+', ' ', f'{name} {extra}').strip()
    return re.sub(r'\s+', ' ', f"{get_first(row, ['hodem', 'ho'])} {get_first(row, ['ten'])}").strip()


def _notes(row, keys):
    parts = []
    for k in keys:
        v = get_first(row, [k])
        if v and v not in ('0', '-', '–', 'x') and v not in parts:
            parts.append(v)
    return parts


def _skip_by_note(note_text):
    n = normalize_key(note_text)
    if 'saima' in n or 'thieuma' in n:
        return 'File ghi chú: ' + note_text
    return None


def parse_xep_loai(text):
    """'Đạt (Bậc 3)' -> (True, 3); 'Không đạt' -> (False, None); 'Đủ điều kiện học TA chính khóa' -> (True, None)."""
    n = normalize_key(text)
    if not n:
        return None, None
    m = re.search(r'bac(\d)', n)
    bac = int(m.group(1)) if m else None
    if any(x in n for x in ('khongdat', 'chuadat', 'truot', 'khongdudieukien')):
        return False, bac
    if 'dat' in n or 'dudieukien' in n:
        return True, bac
    return None, bac


SCORE_COLUMNS = {
    'tdnn': {'d1': ['nghe'], 'd2': ['doc'], 'd3': ['viet'], 'd4': ['noi']},
    'cdr_nn': {'d1': ['nghe'], 'd2': ['doc'], 'd3': ['viet'], 'd4': ['noi']},
    'cntt': {'d1': ['tracnghiem', 'tn'], 'd2': ['thuchanh', 'th'], 'd3': [], 'd4': []},
}


def parse_score_row(row, loai):
    mssv = extract_mssv(row.get('mssv'))
    cols = SCORE_COLUMNS[loai]
    parsed = {
        'mssv': mssv,
        'ho_ten': _ho_ten(row),
        'd1': get_float_first(row, cols['d1']) if cols['d1'] else None,
        'd2': get_float_first(row, cols['d2']) if cols['d2'] else None,
        'd3': get_float_first(row, cols['d3']) if cols['d3'] else None,
        'd4': get_float_first(row, cols['d4']) if cols['d4'] else None,
        'diem_tong': get_float_first(row, ['diemdanhgia', 'tongdiem', 'diemtong', 'tong', 'diem']),
        'xep_loai': get_first(row, ['xeploai', 'ketqua']),
        'sbd': get_first(row, ['sbd', 'sobaodanh']),
    }
    parts = [parsed[k] for k in ('d1', 'd2', 'd3', 'd4') if parsed[k] is not None]
    if parsed['diem_tong'] is None and parts:
        parsed['diem_tong'] = round(sum(parts), 2)

    notes = _notes(row, ['ghichu', 'ghichuvangthi'])
    note_text = ' | '.join(notes)
    bao_luu = get_first(row, ['baoluu'])
    parsed['co_bao_luu'] = bool(bao_luu and normalize_key(bao_luu) not in ('', '0', 'false', 'no', 'khong'))
    if parsed['co_bao_luu']:
        # Cột "Bảo lưu" ghi số phần thi được bảo lưu từ đợt trước (1, 2) hoặc ghi chú chữ
        notes.append(f'Bảo lưu phần {bao_luu}' if bao_luu.isdigit() else f'Bảo lưu: {bao_luu}')
    parsed['ghi_chu'] = ' | '.join(notes)

    # "Vắng thi" = vắng cả buổi; "Vắng TM"/"Vắng VĐ" chỉ vắng một phần, vẫn có điểm
    parsed['vang_thi'] = 'vangthi' in normalize_key(note_text) or normalize_key(parsed['xep_loai']) in ('vang', 'vangthi')
    # "VPQC (Hủy KQ)": vi phạm quy chế -> huỷ kết quả dù cột Xếp loại ghi Đạt
    nk = normalize_key(note_text)
    parsed['huy_kq'] = 'huykq' in nk or 'huyketqua' in nk or 'vpqc' in nk
    parsed['ket_qua_file'], parsed['bac'] = parse_xep_loai(parsed['xep_loai'])
    if parsed['huy_kq']:
        parsed['ket_qua_file'] = False
    parsed['skip_reason'] = _skip_by_note(note_text)
    return parsed


def parse_schedule_row(row):
    mssv = extract_mssv(row.get('mssv'))
    ngay = get_first(row, ['ngaythi', 'ngaykt', 'ngaykiemtra', 'ngay'])
    ca = get_first(row, ['cathi', 'ca', 'cakt', 'cakiemtra'])
    tg = get_first(row, ['thoigian', 'giothi', 'gio'])
    if tg and tg not in ca:
        ca = f'{ca} ({tg})' if ca else tg
    phong = get_first(row, ['phongthi', 'phong', 'phongkt'])

    notes = _notes(row, ['ghichu', 'ghichudotbl', 'ghichuvangthi'])
    dot_bl = get_first(row, ['dotbaoluu', 'ghichudotbl'])
    phan_bl = get_first(row, ['phanbaoluu'])
    if phan_bl:
        notes = [n for n in notes if n != dot_bl]
        notes.append(f"Bảo lưu: {dot_bl + ' – ' if dot_bl else ''}{phan_bl}")
    note_text = ' | '.join(notes)

    parsed = {
        'mssv': mssv,
        'ho_ten': _ho_ten(row),
        'sbd': get_first(row, ['sbd', 'sobaodanh']),
        'ngay_thi': ngay[:50],
        'ca_thi': ca[:50],
        'phong_thi': phong[:50],
        'ngay_thi_2': get_first(row, ['ngaythi2', 'ngaykt2', 'ngaynoi'])[:50],
        'ca_thi_2': get_first(row, ['cathi2', 'cakt2', 'canoi'])[:50],
        'phong_thi_2': get_first(row, ['phongthi2', 'phongtaptrung', 'phongnoi', 'phongkt2'])[:50],
        'ghi_chu': note_text,
    }
    parsed['skip_reason'] = _skip_by_note(note_text)
    if not parsed['skip_reason'] and not (parsed['ngay_thi'] or parsed['phong_thi'] or parsed['ngay_thi_2']):
        parsed['skip_reason'] = 'Chưa có lịch thi' + (f' ({note_text})' if note_text else '')
    return parsed


# ---------------------------------------------------------------- backward compatibility
def read_excel_with_smart_header(excel_file, sheet_name=0):
    df_raw = pd.read_excel(excel_file, sheet_name=sheet_name, header=None, dtype=object)
    built = build_frame(df_raw)
    if not built:
        raise ValueError('Không tìm thấy dòng tiêu đề có cột Mã sinh viên / MSSV')
    return built[0]


def parse_tdnn_row(row):
    return parse_score_row(row, 'tdnn')


def parse_cdr_nn_row(row):
    return parse_score_row(row, 'cdr_nn')


def parse_cntt_row(row):
    return parse_score_row(row, 'cntt')
