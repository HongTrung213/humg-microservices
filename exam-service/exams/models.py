import unicodedata

from django.db import models

# Điểm đạt (thang 100) theo quy định của Trung tâm:
#   Thi đánh giá năng lực TA đầu vào (TĐNN) >= 50, CĐR Ngoại ngữ >= 90, CĐR Tin học >= 50
DIEM_DAT = {
    'TA_DAU_VAO': 50.0,
    'CDR_NGOAI_NGU': 90.0,
    'CDR_TIN_HOC': 50.0,
}


def _bo_dau(text):
    text = str(text or '').lower().replace('đ', 'd')
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')


def tinh_ket_qua_dat(mon_thi, diem_tong, xep_loai='', ghi_chu=''):
    """Đạt khi có điểm, không vắng thi / huỷ kết quả và điểm tổng >= điểm đạt của môn."""
    if diem_tong is None:
        return False
    xl = _bo_dau(xep_loai)
    gc = _bo_dau(ghi_chu)
    if 'vang thi' in xl or 'vang thi' in gc or 'huy' in xl or 'huy kq' in gc or 'vpqc' in gc:
        return False
    return float(diem_tong) >= DIEM_DAT.get(mon_thi, 50.0)

class DotThi(models.Model):
    LOAI_CHOICES = [
        ('TIN_CHI', 'Tín chỉ'),
        ('CDR_NN', 'CĐR Ngoại ngữ'),
        ('CDR_TH', 'CĐR Tin học'),
    ]
    ma_dot = models.CharField(max_length=20, unique=True)
    ten_dot = models.CharField(max_length=200)
    ngay_bat_dau = models.DateField()
    ngay_ket_thuc = models.DateField()
    loai = models.CharField(max_length=20, choices=LOAI_CHOICES)
    
    # Điểm chuẩn (giống monolith)
    diem_chuan_ngoai_ngu = models.FloatField(default=5.0)
    diem_liet_ngoai_ngu = models.FloatField(default=0.0)
    diem_chuan_tin_hoc = models.FloatField(default=5.0)
    diem_liet_tin_hoc = models.FloatField(default=0.0)
    
    # File thông báo (nếu có)
    file_thong_bao = models.FileField(upload_to='announcements/', blank=True, null=True)

    def __str__(self):
        return self.ten_dot


class LichSuThi(models.Model):
    MON_THI_CHOICES = [
        ('TA_DAU_VAO', 'Tiếng Anh đầu vào'),
        ('CDR_NGOAI_NGU', 'CĐR Ngoại ngữ'),
        ('CDR_TIN_HOC', 'CĐR Tin học'),
    ]
    sinh_vien_id = models.IntegerField()
    dot_thi = models.ForeignKey(DotThi, on_delete=models.CASCADE, related_name='lich_su_thi')
    mon_thi = models.CharField(max_length=20, choices=MON_THI_CHOICES, default='CDR_NGOAI_NGU')
    
    # Thông tin lịch thi
    sbd = models.CharField(max_length=50, blank=True, null=True)
    ngay_thi = models.CharField(max_length=50, blank=True, null=True)
    ca_thi = models.CharField(max_length=50, blank=True, null=True)
    phong_thi = models.CharField(max_length=50, blank=True, null=True)
    ngay_thi_2 = models.CharField(max_length=50, blank=True, null=True)
    ca_thi_2 = models.CharField(max_length=50, blank=True, null=True)
    phong_thi_2 = models.CharField(max_length=50, blank=True, null=True)
    
    # Điểm thành phần
    diem_thanh_phan_1 = models.FloatField(null=True, blank=True)  # Nghe / Trắc nghiệm
    diem_thanh_phan_2 = models.FloatField(null=True, blank=True)  # Đọc / Thực hành
    diem_thanh_phan_3 = models.FloatField(null=True, blank=True)  # Viết
    diem_thanh_phan_4 = models.FloatField(null=True, blank=True)  # Nói
    diem_tong = models.FloatField(null=True, blank=True)
    xep_loai = models.CharField(max_length=100, null=True, blank=True)
    ghi_chu = models.TextField(null=True, blank=True)
    
    ket_qua_dat = models.BooleanField(default=False)
    co_bao_luu = models.BooleanField(default=False)
    so_lan_thi = models.IntegerField(default=1)
    so_lan_bao_luu = models.IntegerField(default=0)
    mat_khau = models.CharField(max_length=20, blank=True)
    
    ngay_cap_nhat = models.DateTimeField(auto_now=True)

    @property
    def diem_dat(self):
        return DIEM_DAT.get(self.mon_thi, 50.0)

    def save(self, *args, **kwargs):
        # Kết quả luôn tính theo điểm đạt của môn -> import, sửa tay hay API đều nhất quán
        self.ket_qua_dat = tinh_ket_qua_dat(self.mon_thi, self.diem_tong, self.xep_loai, self.ghi_chu)
        update_fields = kwargs.get('update_fields')
        if update_fields is not None and 'ket_qua_dat' not in update_fields:
            kwargs['update_fields'] = list(update_fields) + ['ket_qua_dat']
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SV {self.sinh_vien_id} - {self.get_mon_thi_display()} - {self.dot_thi.ten_dot}"


class BaoLuuDiem(models.Model):
    LOAI_CHOICES = [
        ('NN', 'Ngoại ngữ'),
        ('TH', 'Tin học'),
    ]
    
    sinh_vien_id = models.IntegerField()
    dot_thi = models.ForeignKey(DotThi, on_delete=models.CASCADE)
    loai = models.CharField(max_length=2, choices=LOAI_CHOICES, default='NN')
    
    # Điểm từng phần (dùng chung cho cả ngoại ngữ và tin học)
    diem_phan_1 = models.FloatField(null=True, blank=True)  # NN: Nghe, TH: Trắc nghiệm
    diem_phan_2 = models.FloatField(null=True, blank=True)  # NN: Đọc, TH: Word
    diem_phan_3 = models.FloatField(null=True, blank=True)  # NN: Viết, TH: Excel
    diem_phan_4 = models.FloatField(null=True, blank=True)  # NN: Nói, TH: PowerPoint
    
    # Danh sách phần đạt (lưu CSV)
    danh_sach_phan = models.CharField(max_length=100, blank=True)
    
    # Tổng điểm bảo lưu (có thể là tổng các điểm đạt)
    diem_bao_luu = models.FloatField(default=0)
    
    # Thời hạn bảo lưu (tính từ ngày thi)
    ngay_het_han = models.DateField(null=True, blank=True)
    
    # Trạng thái: ACTIVE, EXPIRED, USED
    trang_thai = models.CharField(max_length=20, default='ACTIVE')
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ngay_cap_nhat = models.DateTimeField(auto_now=True)
