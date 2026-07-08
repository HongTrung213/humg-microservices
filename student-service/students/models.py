from django.db import models

class Khoa(models.Model):
    ma_khoa = models.CharField(max_length=20, unique=True)
    ten_khoa = models.CharField(max_length=200)

    def __str__(self):
        return self.ten_khoa

class NganhDaoTao(models.Model):
    ma_nganh = models.CharField(max_length=20, unique=True)
    ten_nganh = models.CharField(max_length=200)
    khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE, related_name='nganh_dao_tao')

    def __str__(self):
        return self.ten_nganh

class SinhVien(models.Model):
    ma_sv = models.CharField(max_length=20, unique=True)
    ho_ten = models.CharField(max_length=100)
    ngay_sinh = models.DateField(null=True, blank=True)
    gioi_tinh = models.CharField(max_length=10, choices=[('Nam','Nam'),('Nữ','Nữ')], blank=True)
    email = models.EmailField(unique=True)
    so_dien_thoai = models.CharField(max_length=15, blank=True)
    khoa = models.ForeignKey(Khoa, on_delete=models.SET_NULL, null=True)
    nganh = models.ForeignKey(NganhDaoTao, on_delete=models.SET_NULL, null=True)
    khoa_hoc = models.CharField(max_length=10)
    nam_nhap_hoc = models.IntegerField()
    da_mien_cdr = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ma_sv} - {self.ho_ten}"