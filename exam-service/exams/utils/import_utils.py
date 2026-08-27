import re
import pandas as pd

def normalize_key(text):
    """Chuẩn hóa tên cột: bỏ dấu, viết thường, bỏ khoảng trắng và dấu gạch."""
    text = str(text or '').lower().strip()
    text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
    text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
    text = re.sub(r'[ìíịỉĩ]', 'i', text)
    text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
    text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
    text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
    text = re.sub(r'đ', 'd', text)
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

def clean_excel_val(val):
    if pd.isna(val):
        return ''
    if isinstance(val, float) and val.is_integer():
        return str(int(val))
    return str(val).strip()

def to_float(val):
    if val is None or pd.isna(val):
        return None
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

def get_first(row, keys, default=''):
    for key in keys:
        norm = normalize_key(key)
        if norm in row and pd.notna(row.get(norm)):
            value = clean_excel_val(row.get(norm))
            if value:
                return value
    return default

def get_float_first(row, keys):
    for key in keys:
        norm = normalize_key(key)
        if norm in row:
            val = to_float(row.get(norm))
            if val is not None:
                return val
    return None

def read_excel_with_smart_header(excel_file, sheet_name=0):
    df_raw = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
    keywords = ['mssv', 'ma sinh vien', 'masv', 'mã sinh viên']
    header_idx = 0
    for i, row in df_raw.iterrows():
        row_text = ' '.join(str(v).lower() for v in row if pd.notna(v))
        if any(k in row_text for k in keywords):
            header_idx = i
            break
    df = df_raw.iloc[header_idx + 1:].copy()
    df.columns = [normalize_key(c) for c in df_raw.iloc[header_idx]]
    df = df.dropna(how='all')
    return df

# ---------- PARSERS ----------
def parse_tdnn_row(row):
    mssv = extract_mssv(get_first(row, ['mssv', 'ma sinh vien', 'masinhvien', 'ma sv']))
    if not mssv:
        return None
    return {
        'mssv': mssv,
        'ho_ten': get_first(row, ['hoten', 'ho ten', 'hovaten', 'ten sinh vien']),
        'd1': get_float_first(row, ['nghe']),
        'd2': get_float_first(row, ['doc']),
        'd3': get_float_first(row, ['viet']),
        'd4': get_float_first(row, ['noi']),
        'diem_tong': get_float_first(row, ['diem danh gia', 'diemtong', 'tongdiem']),
        'xep_loai': get_first(row, ['xeploai', 'xep loai']),
        'ghi_chu': get_first(row, ['ghichu', 'ghi chu']),
        'co_bao_luu': False,
        'sbd': '',
    }

def parse_cdr_nn_row(row):
    mssv = extract_mssv(get_first(row, ['mssv', 'ma sinh vien', 'masinhvien', 'ma sv']))
    if not mssv:
        return None
    bao_luu = get_first(row, ['bao luu', 'baoluu'])
    co_bao_luu = bool(bao_luu and str(bao_luu).strip() not in ['', '0', 'false', 'no'])
    ghi_chu = get_first(row, ['ghichu', 'ghi chu'])
    if co_bao_luu:
        if ghi_chu:
            ghi_chu = f"{ghi_chu} | Bảo lưu: {bao_luu}"
        else:
            ghi_chu = f"Bảo lưu: {bao_luu}"
    return {
        'mssv': mssv,
        'ho_ten': get_first(row, ['hoten', 'ho ten', 'hovaten', 'ten sinh vien']),
        'd1': get_float_first(row, ['nghe']),
        'd2': get_float_first(row, ['doc']),
        'd3': get_float_first(row, ['viet']),
        'd4': get_float_first(row, ['noi']),
        'diem_tong': get_float_first(row, ['diem danh gia', 'diemtong', 'tongdiem']),
        'xep_loai': get_first(row, ['xeploai', 'xep loai']),
        'ghi_chu': ghi_chu,
        'co_bao_luu': co_bao_luu,
        'sbd': '',
    }

def parse_cntt_row(row):
    mssv = extract_mssv(get_first(row, ['mssv', 'ma sinh vien', 'masinhvien', 'ma sv']))
    if not mssv:
        return None
    bao_luu = get_first(row, ['bao luu', 'baoluu'])
    co_bao_luu = bool(bao_luu and str(bao_luu).strip() not in ['', '0', 'false', 'no'])
    ghi_chu = get_first(row, ['ghichu', 'ghi chu'])
    if co_bao_luu:
        if ghi_chu:
            ghi_chu = f"{ghi_chu} | Bảo lưu: {bao_luu}"
        else:
            ghi_chu = f"Bảo lưu: {bao_luu}"
    return {
        'mssv': mssv,
        'ho_ten': get_first(row, ['hoten', 'ho ten', 'hovaten', 'ten sinh vien']),
        'd1': get_float_first(row, ['trac nghiem', 'tracnghiem']),
        'd2': get_float_first(row, ['thuc hanh', 'thuchanh']),
        'd3': None,
        'd4': None,
        'diem_tong': get_float_first(row, ['diem danh gia', 'diemtong', 'tongdiem']),
        'xep_loai': get_first(row, ['xeploai', 'xep loai']),
        'ghi_chu': ghi_chu,
        'co_bao_luu': co_bao_luu,
        'sbd': '',
    }
