# students/utils/import_utils.py
import re
import pandas as pd
from django.db import transaction
from students.models import SinhVien, Khoa, NganhDaoTao

# ---------- HÀM TIỆN ÍCH CHUẨN HÓA ----------
def normalize_key(text):
    """Chuẩn hóa tên cột: bỏ dấu, viết thường, bỏ khoảng trắng và dấu gạch."""
    text = str(text or '').lower().strip()
    # Bỏ dấu tiếng Việt đơn giản
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
    """Làm sạch giá trị từ Excel."""
    if pd.isna(val):
        return ''
    if isinstance(val, float) and val.is_integer():
        return str(int(val))
    return str(val).strip()

def extract_mssv(value):
    """Trích xuất MSSV từ chuỗi hoặc số, xử lý .0 và ký tự thừa."""
    raw = clean_excel_val(value)
    if raw.endswith('.0'):
        raw = raw[:-2]
    digits = re.sub(r'\D', '', raw)
    return digits if len(digits) >= 5 else ''

def to_float(val):
    """Chuyển sang float, xử lý dấu phẩy thập phân."""
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
    """Chuyển chuỗi tiếng Việt thành slug không dấu."""
    text = str(text or '').lower().strip()
    text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
    text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
    text = re.sub(r'[ìíịỉĩ]', 'i', text)
    text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
    text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
    text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
    text = re.sub(r'đ', 'd', text)
    return re.sub(r'[^a-z0-9]', '', text)

# ---------- HÀM XỬ LÝ KHOA, NGÀNH ----------
def get_khoa_from_mssv(mssv):
    """Tự động suy Khoa từ MSSV (3 số ở vị trí 4-6)."""
    mssv_str = str(mssv or '').strip()
    if not mssv_str.isdigit() or len(mssv_str) < 6:
        return None
    ma_khoa = mssv_str[3:6]
    return Khoa.objects.filter(ma_khoa=ma_khoa).first()

def detect_loai_nganh(ten_nganh):
    """Nhận diện loại ngành (đặc biệt cho ngoại ngữ)."""
    text = vi_slugify(ten_nganh)
    if 'ngonnguanh' in text:
        return 'NGON_NGU_ANH'
    if 'ngonngutrung' in text or 'trungquoc' in text:
        return 'NGON_NGU_TRUNG'
    return 'THUONG'

def get_or_create_nganh(khoa, ten_nganh):
    """Lấy hoặc tạo Ngành đào tạo."""
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
    """Suy khóa tuyển sinh từ mã lớp (VD: K70, CTTTK70 -> 70)."""
    text = str(ma_lop or '').upper()
    numbers = re.findall(r'(\d{2})', text)
    for num in reversed(numbers):
        val = int(num)
        if 50 <= val <= 99:
            return val
    return None

def calculate_nam_nhap_hoc(khoa_ts):
    """Tính năm nhập học từ khóa: K69 -> 2024, K70 -> 2025."""
    if khoa_ts is None:
        return None
    return 1955 + int(khoa_ts)

def calculate_nam_tot_nghiep(khoa_ts, nganh=None):
    """Tính năm dự kiến tốt nghiệp (mặc định 4 năm)."""
    nam_nhap = calculate_nam_nhap_hoc(khoa_ts)
    if not nam_nhap:
        return None
    thoi_gian = 4.0
    if nganh and hasattr(nganh, 'thoi_gian_dao_tao_nam') and nganh.thoi_gian_dao_tao_nam:
        thoi_gian = float(nganh.thoi_gian_dao_tao_nam)
    return int(nam_nhap + thoi_gian)

def normalize_chuong_trinh(ma_lop='', ten_nganh=''):
    """Xác định chương trình đào tạo từ mã lớp hoặc tên ngành."""
    text = vi_slugify(f"{ma_lop} {ten_nganh}")
    if 'chatluongcao' in text or 'clc' in text:
        return 'CHAT_LUONG_CAO'
    if 'tientien' in text or 'cttt' in text:
        return 'TIEN_TIEN'
    return 'DAI_TRA'

# ---------- HÀM TẠO/CẬP NHẬT SINH VIÊN ----------
@transaction.atomic
def ensure_student(mssv, ho_ten='', lop='', email='', phone='', ten_nganh='', ma_lop=''):
    """
    Tạo hoặc cập nhật sinh viên từ thông tin cơ bản.
    Tự động suy Khoa từ MSSV, Ngành từ tên ngành + khoa.
    """
    mssv = extract_mssv(mssv)
    if not mssv:
        return None

    ho_ten = ho_ten or f'SV_{mssv}'

    # Xác định Khoa
    khoa = get_khoa_from_mssv(mssv)
    if not khoa:
        # Tạo Khoa mặc định nếu chưa có
        ma_khoa = mssv[3:6] if len(mssv) >= 6 else '000'
        khoa, _ = Khoa.objects.get_or_create(
            ma_khoa=ma_khoa,
            defaults={'ten_khoa': f'Khoa mã {ma_khoa}'}
        )

    # Xác định Ngành
    nganh = None
    if ten_nganh:
        nganh = get_or_create_nganh(khoa, ten_nganh)

    # Tính các thông tin
    khoa_ts = extract_khoa_tuyen_sinh(ma_lop or lop)
    nam_nhap = calculate_nam_nhap_hoc(khoa_ts)
    nam_tn = calculate_nam_tot_nghiep(khoa_ts, nganh)
    chuong_trinh = normalize_chuong_trinh(ma_lop or lop, ten_nganh)
    email_truong = email or f'{mssv}@student.humg.edu.vn'

    # Tạo hoặc cập nhật SinhVien
    sv, created = SinhVien.objects.get_or_create(
        mssv=mssv,
        defaults={
            'ho_ten': ho_ten,
            'lop': lop or None,
            'khoa': khoa,
            'email_truong': email_truong,
            'so_dien_thoai': phone or None,
            'nganh_dao_tao': nganh,
            'khoa_tuyen_sinh': khoa_ts,
            'nam_nhap_hoc': nam_nhap,
            'nam_du_kien_tot_nghiep': nam_tn,
            'chuong_trinh_dao_tao': chuong_trinh,
        }
    )

    if not created:
        # Cập nhật các trường nếu thay đổi
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

# ---------- HÀM ĐỌC EXCEL THÔNG MINH ----------
def read_excel_with_smart_header(excel_file, sheet_name=0):
    """Đọc Excel, tự động tìm dòng header."""
    df_raw = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
    # Tìm dòng có chứa từ khóa 'mssv'
    header_idx = 0
    keywords = ['mssv', 'ma sinh vien', 'masv', 'mã sinh viên']
    for i, row in df_raw.iterrows():
        row_text = ' '.join(str(v).lower() for v in row if pd.notna(v))
        if any(k in row_text for k in keywords):
            header_idx = i
            break
    df = df_raw.iloc[header_idx + 1:].copy()
    df.columns = [normalize_key(c) for c in df_raw.iloc[header_idx]]
    df = df.dropna(how='all')
    return df