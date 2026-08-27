from django.db import models

# ----- Model hiện có (giữ nguyên) -----
class LopBoiDuong(models.Model):
    LOAI_CHOICES = [
        ('NN', 'Ngoại ngữ'),
        ('TH', 'Tin học'),
    ]
    
    ma_lop = models.CharField(max_length=20, unique=True)
    ten_lop = models.CharField(max_length=200)
    loai = models.CharField(max_length=20, choices=LOAI_CHOICES)
    so_luong_toi_da = models.IntegerField(default=30)
    bat_dau = models.DateField()
    ket_thuc = models.DateField()
    trang_thai = models.CharField(max_length=20, default='OPEN')
    
    # ====== THÊM MỚI: ======
    ma_mh = models.CharField('Mã môn học', max_length=20, blank=True, null=True)
    nhom = models.CharField('Nhóm', max_length=10, blank=True, null=True)  # VD: 01, 02
    si_so_hien_tai = models.IntegerField('Sĩ số hiện tại', default=0)

    def __str__(self):
        return self.ten_lop


class DangKyLop(models.Model):
    TRANG_THAI_CHOICES = [
        ('PENDING', 'Chờ duyệt'),
        ('DA_DUYET', 'Đã duyệt'),
        ('TU_CHOI', 'Từ chối'),
    ]
    
    sinh_vien_id = models.IntegerField()
    lop = models.ForeignKey(LopBoiDuong, on_delete=models.CASCADE, related_name='ds_dang_ky')
    ngay_dang_ky = models.DateTimeField(auto_now_add=True)
    trang_thai = models.CharField(max_length=20, choices=TRANG_THAI_CHOICES, default='PENDING')

    class Meta:
        unique_together = ('sinh_vien_id', 'lop')  # Chống đăng ký trùng

    def __str__(self):
        return f"SV {self.sinh_vien_id} - {self.lop.ten_lop}"


# ====== THÊM MỚI: Model lịch học ======
class LichHoc(models.Model):
    THU_CHOICES = [
        (2, 'Thứ 2'),
        (3, 'Thứ 3'),
        (4, 'Thứ 4'),
        (5, 'Thứ 5'),
        (6, 'Thứ 6'),
        (7, 'Thứ 7'),
        (8, 'Chủ nhật'),
    ]
    
    lop = models.ForeignKey(LopBoiDuong, on_delete=models.CASCADE, related_name='lich_hoc')
    thu = models.IntegerField('Thứ', choices=THU_CHOICES)
    tiet_bat_dau = models.IntegerField('Tiết bắt đầu', default=1)
    tiet_ket_thuc = models.IntegerField('Tiết kết thúc', default=3)
    phong_hoc = models.CharField('Phòng học', max_length=50)
    giang_vien = models.CharField('Giảng viên', max_length=100, blank=True)
    ghi_chu = models.TextField('Ghi chú', blank=True)
    
    class Meta:
        verbose_name = 'Lịch học'
        verbose_name_plural = 'Lịch học'
        ordering = ['thu', 'tiet_bat_dau']
    
    def __str__(self):
        return f"{self.lop.ten_lop} - {self.get_thu_display()} - Tiết {self.tiet_bat_dau}-{self.tiet_ket_thuc}"
