from django.db import models

class ThongBao(models.Model):
    tieu_de = models.CharField(max_length=200)
    noi_dung = models.TextField()
    loai = models.CharField(max_length=20, choices=[('SYSTEM','Hệ thống'),('ACADEMIC','Học vụ')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tieu_de

class CanhBao(models.Model):
    sinh_vien_id = models.IntegerField()
    tieu_de = models.CharField(max_length=200)
    noi_dung = models.TextField()
    muc_do = models.CharField(max_length=20, choices=[('LOW','Thấp'),('MEDIUM','Trung'),('HIGH','Cao')])
    da_gui = models.BooleanField(default=False)
    ngay_gui = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.tieu_de} - SV {self.sinh_vien_id}"