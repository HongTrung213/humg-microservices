import re
import pandas as pd
from django.db import transaction
from students.models import SinhVien, Khoa, NganhDaoTao

def normalize_key(text):
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
    text = str(text or '').lower().strip()
    text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
    text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
    text = re.sub(r'[ìíịỉĩ]', 'i', text)
    text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
    text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
    text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
    text = re.sub(r'đ', 'd', text)
    return re.sub(r'[^a-z0-9]', '', text)

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

@transaction.atomic
def ensure_student(mssv, ho_ten='', lop='', email='', phone='', ten_nganh='', ma_lop=''):
    mssv = extract_mssv(mssv)
    if not mssv:
        return None
    ho_ten = ho_ten or f'SV_{mssv}'
    khoa = get_khoa_from_mssv(mssv)
    if not khoa:
        ma_khoa = mssv[3:6] if len(mssv) >= 6 else '000'
        khoa, _ = Khoa.objects.get_or_create(
            ma_khoa=ma_khoa,
            defaults={'ten_khoa': f'Khoa mã {ma_khoa}'}
        )
    nganh = None
    if ten_nganh:
        nganh = get_or_create_nganh(khoa, ten_nganh)
    khoa_ts = extract_khoa_tuyen_sinh(ma_lop or lop)
    nam_nhap = calculate_nam_nhap_hoc(khoa_ts)
    nam_tn = calculate_nam_tot_nghiep(khoa_ts, nganh)
    chuong_trinh = normalize_chuong_trinh(ma_lop or lop, ten_nganh)
    email_truong = email or f'{mssv}@student.humg.edu.vn'
    sv, created = SinhVien.objects.get_or_create(ma_sv=mssv,
        defaults={
            'ho_ten': ho_ten,
            'lop': lop or None,
            'khoa': khoa,
            'email_truong': email_truong,   # <-- đổi thành email_truong
            'so_dien_thoai': phone or None,
            'nganh_dao_tao': nganh,
            'khoa_tuyen_sinh': khoa_ts,
            'nam_nhap_hoc': nam_nhap,
            'nam_du_kien_tot_nghiep': nam_tn,
            'chuong_trinh_dao_tao': chuong_trinh,
        }
    )
    # Cập nhật các field khi tồn tại
    if not created:
        updated = False
        if sv.ho_ten != ho_ten:
            sv.ho_ten = ho_ten; updated = True
        if lop and sv.lop != lop:
            sv.lop = lop; updated = True
        if khoa and sv.khoa_id != khoa.id:
            sv.khoa = khoa; updated = True
        if email_truong and sv.email_truong != email_truong:
            sv.email_truong = email_truong; updated = True
        if phone and sv.so_dien_thoai != phone:
            sv.so_dien_thoai = phone; updated = True
        if nganh and sv.nganh_dao_tao_id != nganh.id:
            sv.nganh_dao_tao = nganh; updated = True
        if khoa_ts and sv.khoa_tuyen_sinh != khoa_ts:
            sv.khoa_tuyen_sinh = khoa_ts; updated = True
        if nam_nhap and sv.nam_nhap_hoc != nam_nhap:
            sv.nam_nhap_hoc = nam_nhap; updated = True
        if nam_tn and sv.nam_du_kien_tot_nghiep != nam_tn:
            sv.nam_du_kien_tot_nghiep = nam_tn; updated = True
        if chuong_trinh and sv.chuong_trinh_dao_tao != chuong_trinh:
            sv.chuong_trinh_dao_tao = chuong_trinh; updated = True
        if updated:
            sv.save()
    return sv

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
