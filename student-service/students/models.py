from django.db import models
from .utils.cdr_utils import check_dat_ngoai_ngu, check_dat_tin_hoc, dat_chuan_dau_ra


class Khoa(models.Model):
    ma_khoa = models.CharField(max_length=20, unique=True)
    ten_khoa = models.CharField(max_length=200)

    def __str__(self):
        return self.ten_khoa

class NganhDaoTao(models.Model):
    ma_nganh = models.CharField(max_length=30, blank=True, null=True)
    ten_nganh = models.CharField(max_length=255)
    khoa = models.ForeignKey(Khoa, on_delete=models.SET_NULL, null=True, blank=True, related_name='cac_nganh')
    loai_nganh = models.CharField(max_length=30, choices=[('THUONG', 'Ngành thông thường'), ('NGON_NGU_ANH', 'Ngôn ngữ Anh'), ('NGON_NGU_TRUNG', 'Ngôn ngữ Trung Quốc')], default='THUONG')
    thoi_gian_dao_tao_nam = models.FloatField(default=4.0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.ten_nganh

class SinhVien(models.Model):
    ma_sv = models.CharField(max_length=20, unique=True)
    ho_ten = models.CharField(max_length=100)
    ngay_sinh = models.DateField(null=True, blank=True)
    gioi_tinh = models.CharField(max_length=10, choices=[('Nam','Nam'),('Nữ','Nữ')], blank=True)
    email_truong = models.EmailField(unique=True, null=True, blank=True, verbose_name="Email trường")
    email_ca_nhan = models.EmailField(blank=True, null=True, verbose_name="Email cá nhân")
    anh_dai_dien = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Ảnh đại diện")
    so_dien_thoai = models.CharField(max_length=15, blank=True)
    khoa = models.ForeignKey(Khoa, on_delete=models.SET_NULL, null=True)
    nganh = models.ForeignKey(NganhDaoTao, on_delete=models.SET_NULL, null=True)
    khoa_hoc = models.CharField(max_length=10)
    nam_nhap_hoc = models.IntegerField()
    da_mien_cdr = models.BooleanField(default=False)
    lop = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.ma_sv} - {self.ho_ten}"
    
    @property
    def check_dat_ngoai_ngu(self):
        required_bac = self.get_required_foreign_language_level()
        return check_dat_ngoai_ngu(self.id, required_bac)

    @property
    def check_dat_tin_hoc(self):
        return check_dat_tin_hoc(self.id)

    @property
    def dat_chuan_dau_ra(self):
        return dat_chuan_dau_ra(self.id)
    
    def get_required_foreign_language_level(self):
        # Logic xác định bậc yêu cầu dựa trên loại ngành và chương trình đào tạo
        if self.nganh and self.nganh.loai_nganh in ['NGON_NGU_ANH', 'NGON_NGU_TRUNG']:
            return 5
        # Nếu có thêm trường chuong_trinh_dao_tao thì xử lý (tạm thời mặc định 3)
        return 3
