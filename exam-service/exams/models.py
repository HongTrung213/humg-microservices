from django.db import models

class DotThi(models.Model):
    ma_dot = models.CharField(max_length=20, unique=True)
    ten_dot = models.CharField(max_length=200)
    ngay_bat_dau = models.DateField()
    ngay_ket_thuc = models.DateField()
    loai = models.CharField(max_length=20, choices=[
        ('TIN_CHI', 'Tín chỉ'),
        ('CDR_NN', 'CĐR Ngoại ngữ'),
        ('CDR_TH', 'CĐR Tin học')
    ])

    def __str__(self):
        return self.ten_dot

class LichSuThi(models.Model):
    sinh_vien_id = models.IntegerField()  # thay vì ForeignKey
    dot_thi = models.ForeignKey(DotThi, on_delete=models.CASCADE)
    diem = models.FloatField(null=True, blank=True)
    dat = models.BooleanField(default=False)
    so_lan_thi = models.IntegerField(default=1)
    so_lan_bao_luu = models.IntegerField(default=0)
    ghi_chu_vang_thi = models.TextField(blank=True)
    mat_khau = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.sinh_vien_id} - {self.dot_thi.ten_dot}"

class BaoLuuDiem(models.Model):
    sinh_vien_id = models.IntegerField()
    dot_thi = models.ForeignKey(DotThi, on_delete=models.CASCADE)
    diem_bao_luu = models.FloatField()
    ngay_tao = models.DateTimeField(auto_now_add=True)
    trang_thai = models.CharField(max_length=20, default='ACTIVE')

    def __str__(self):
        return f"Bảo lưu {self.diem_bao_luu} - SV {self.sinh_vien_id}"