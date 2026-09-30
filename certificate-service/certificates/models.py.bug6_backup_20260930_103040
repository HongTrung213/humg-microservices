from django.db import models

class DanhMucChungChi(models.Model):
    ma_danh_muc = models.CharField(max_length=20, unique=True)
    ten_danh_muc = models.CharField(max_length=200)
    loai = models.CharField(max_length=20, choices=[('NN', 'Ngoại ngữ'), ('TH', 'Tin học')])
    bac = models.IntegerField(default=1)

    def __str__(self):
        return self.ten_danh_muc

class ChungChi(models.Model):
    sinh_vien_id = models.IntegerField()
    danh_muc = models.ForeignKey(DanhMucChungChi, on_delete=models.CASCADE)
    so_chung_chi = models.CharField(max_length=50, unique=True)
    ngay_cap = models.DateField()
    ngay_het_han = models.DateField(null=True, blank=True)
    diem_so = models.FloatField(null=True, blank=True)
    hinh_thuc_thi = models.CharField(max_length=50, blank=True)
    trang_thai = models.CharField(max_length=20, default='ACTIVE')
    da_xet_duyet = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.so_chung_chi} - SV {self.sinh_vien_id}"
