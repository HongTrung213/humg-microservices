import re
import unicodedata
import pandas as pd
from django.db import transaction
from students.models import SinhVien, Khoa, NganhDaoTao

def _unaccent(text):
    text = str(text if text is not None else '').strip().lower()
    if text in ('nan', 'none', 'nat'):
        return ''
    text = text.replace('đ', 'd')
    text = unicodedata.normalize('NFD', text)
    return ''.join(ch for ch in text if unicodedata.category(ch) != 'Mn')


def normalize_key(text):
    """Chuẩn hoá tên cột: bỏ dấu tiếng Việt (kể cả đ), chữ thường, chỉ giữ a-z0-9."""
    return re.sub(r'[^a-z0-9]', '', _unaccent(text))


def clean_excel_val(val):
    if pd.isna(val):
        return ''
    if isinstance(val, float) and val.is_integer():
        return str(int(val))
    return str(val).strip()

def extract_mssv(value):
    raw = clean_excel_val(value)
    if raw.endswith('.0'):
        raw = raw[:-2]
    digits = re.sub(r'\D', '', raw)
    return digits if len(digits) >= 5 else ''

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

def vi_slugify(text):
    return normalize_key(text)

def get_khoa_from_mssv(mssv):
    mssv_str = str(mssv or '').strip()
    if not mssv_str.isdigit() or len(mssv_str) < 6:
        return None
    ma_khoa = mssv_str[3:6]
    return Khoa.objects.filter(ma_khoa=ma_khoa).first()

def detect_loai_nganh(ten_nganh):
    text = vi_slugify(ten_nganh)
    if 'ngonnguanh' in text:
        return 'NGON_NGU_ANH'
    if 'ngonngutrung' in text or 'trungquoc' in text:
        return 'NGON_NGU_TRUNG'
    return 'THUONG'

def get_or_create_nganh(khoa, ten_nganh):
    ten_nganh = ten_nganh.strip()
    loai = detect_loai_nganh(ten_nganh)
    nganh, created = NganhDaoTao.objects.get_or_create(
        khoa=khoa,
        ten_nganh=ten_nganh,
        defaults={'loai_nganh': loai, 'is_active': True}
    )
    if not created and nganh.loai_nganh != loai:
        nganh.loai_nganh = loai
        nganh.save(update_fields=['loai_nganh'])
    return nganh

def extract_khoa_tuyen_sinh(ma_lop):
    text = str(ma_lop or '').upper()
    numbers = re.findall(r'(\d{2})', text)
    for num in reversed(numbers):
        val = int(num)
        if 50 <= val <= 99:
            return val
    return None

def calculate_nam_nhap_hoc(khoa_ts):
    if khoa_ts is None:
        return None
    return 1955 + int(khoa_ts)

def calculate_nam_tot_nghiep(khoa_ts, nganh=None):
    nam_nhap = calculate_nam_nhap_hoc(khoa_ts)
    if not nam_nhap:
        return None
    thoi_gian = 4.0
    if nganh and hasattr(nganh, 'thoi_gian_dao_tao_nam') and nganh.thoi_gian_dao_tao_nam:
        thoi_gian = float(nganh.thoi_gian_dao_tao_nam)
    return int(nam_nhap + thoi_gian)

def normalize_chuong_trinh(ma_lop='', ten_nganh=''):
    text = vi_slugify(f"{ma_lop} {ten_nganh}")
    if 'chatluongcao' in text or 'clc' in text:
        return 'CHAT_LUONG_CAO'
    if 'tientien' in text or 'cttt' in text:
        return 'TIEN_TIEN'
    return 'DAI_TRA'

def nam_nhap_hoc_tu_mssv(mssv):
    """MSSV HUMG: 2 số đầu là năm nhập học (2121050001 -> 2021)."""
    if mssv and len(mssv) >= 2 and mssv[:2].isdigit():
        return 2000 + int(mssv[:2])
    return None


@transaction.atomic
def ensure_student(mssv, ho_ten='', lop='', email='', phone='', ten_nganh='', ma_lop=''):
    """Tạo mới hoặc cập nhật sinh viên theo MSSV. Chỉ dùng các trường có trong model SinhVien."""
    mssv = extract_mssv(mssv)
    if not mssv:
        return None
    ho_ten = re.sub(r'\s+', ' ', ho_ten or '').strip() or f'SV_{mssv}'
    khoa = get_khoa_from_mssv(mssv)
    if not khoa:
        ma_khoa = mssv[3:6] if len(mssv) >= 6 else '000'
        khoa, _ = Khoa.objects.get_or_create(ma_khoa=ma_khoa, defaults={'ten_khoa': f'Khoa mã {ma_khoa}'})
    nganh = get_or_create_nganh(khoa, ten_nganh) if ten_nganh else None

    khoa_ts = extract_khoa_tuyen_sinh(ma_lop or lop)
    nam_nhap = calculate_nam_nhap_hoc(khoa_ts) or nam_nhap_hoc_tu_mssv(mssv) or 2000
    khoa_hoc = f'K{nam_nhap - 1955}'
    email_truong = email or f'{mssv}@student.humg.edu.vn'
    if SinhVien.objects.filter(email_truong=email_truong).exclude(ma_sv=mssv).exists():
        email_truong = None      # tránh trùng email (trường unique)

    sv, created = SinhVien.objects.get_or_create(
        ma_sv=mssv,
        defaults={
            'ho_ten': ho_ten,
            'lop': lop or None,
            'khoa': khoa,
            'nganh': nganh,
            'email_truong': email_truong,
            'so_dien_thoai': phone or '',
            'khoa_hoc': khoa_hoc,
            'nam_nhap_hoc': nam_nhap,
        },
    )
    if not created:
        changed = []
        if ho_ten and not ho_ten.startswith('SV_') and sv.ho_ten != ho_ten:
            sv.ho_ten = ho_ten; changed.append('ho_ten')
        if lop and sv.lop != lop:
            sv.lop = lop; changed.append('lop')
        if khoa and not sv.khoa_id:
            sv.khoa = khoa; changed.append('khoa')
        if nganh and sv.nganh_id != nganh.id:
            sv.nganh = nganh; changed.append('nganh')
        if email and sv.email_truong != email:
            sv.email_truong = email; changed.append('email_truong')
        if phone and sv.so_dien_thoai != phone:
            sv.so_dien_thoai = phone; changed.append('so_dien_thoai')
        if changed:
            sv.save(update_fields=changed)
    return sv


def read_excel_with_smart_header(excel_file, sheet_name=0):
    """Tìm dòng tiêu đề có cột Mã sinh viên/MSSV/MSV; tên cột chuẩn hoá, không trùng.
    Cột không tiêu đề ngay sau "Họ và tên"/"Họ đệm" được đặt tên "tenghep" (phần tên tách riêng)."""
    df_raw = pd.read_excel(excel_file, sheet_name=sheet_name, header=None, dtype=object)
    keys = {'mssv', 'msv', 'masv', 'masinhvien', 'masosinhvien'}
    header_idx = 0
    for i in range(min(25, len(df_raw))):
        if any(normalize_key(v) in keys for v in df_raw.iloc[i].tolist()):
            header_idx = i
            break
    names, seen, prev = [], {}, ''
    for j, v in enumerate(df_raw.iloc[header_idx].tolist()):
        key = normalize_key(v)
        if key in keys:
            key = 'mssv'
        if not key and prev in ('hoten', 'hovaten', 'hodem'):
            key = 'tenghep'
        if not key:
            key = f'cot{j + 1}'
        seen[key] = seen.get(key, 0) + 1
        if seen[key] > 1:
            key = f'{key}{seen[key]}'
        names.append(key)
        prev = key
    df = df_raw.iloc[header_idx + 1:].copy()
    df.columns = names
    df = df.dropna(how='all')
    return df
