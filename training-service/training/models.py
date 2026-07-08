from django.db import models

class LopBoiDuong(models.Model):
    ma_lop = models.CharField(max_length=20, unique=True)
    ten_lop = models.CharField(max_length=200)
    loai = models.CharField(max_length=20, choices=[('NN', 'Ngoại ngữ'), ('TH', 'Tin học')])
    so_luong_toi_da = models.IntegerField(default=30)
    bat_dau = models.DateField()
    ket_thuc = models.DateField()
    trang_thai = models.CharField(max_length=20, default='OPEN')

    def __str__(self):
        return self.ten_lop

class DangKyLop(models.Model):
    sinh_vien_id = models.IntegerField()
    lop = models.ForeignKey(LopBoiDuong, on_delete=models.CASCADE)
    ngay_dang_ky = models.DateTimeField(auto_now_add=True)
    trang_thai = models.CharField(max_length=20, default='PENDING')

    def __str__(self):
        return f"SV {self.sinh_vien_id} - {self.lop.ten_lop}"