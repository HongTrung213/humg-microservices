from django.db import models


class DanhMucChungChi(models.Model):
    LOAI_CHOICES = [
        ('NGOAI_NGU', 'Ngoại ngữ'),      # ✅ Đổi từ 'NN'
        ('TIN_HOC',   'Tin học'),         # ✅ Đổi từ 'TH'
    ]

    ma_danh_muc = models.CharField(max_length=20, unique=True)
    ten_danh_muc = models.CharField(max_length=200)
    loai = models.CharField(max_length=20, choices=LOAI_CHOICES)
    bac = models.IntegerField(default=1)

    def __str__(self):
        return self.ten_danh_muc


class ChungChi(models.Model):
    TRANG_THAI_CHOICES = [
        ('DAT',      'Đạt / Hợp lệ'),      # ✅ Thêm mới
        ('CHUA_DAT', 'Chưa đạt'),
        ('CHO',      'Chờ duyệt'),         # ✅ Thêm mới
        ('TU_CHOI',  'Từ chối'),           # ✅ Thêm mới
        ('HET_HAN',  'Hết hạn'),
        ('THU_HOI',  'Thu hồi'),
    ]

    sinh_vien_id = models.IntegerField(db_index=True)          # ✅ Thêm index
    danh_muc = models.ForeignKey(
        DanhMucChungChi,
        on_delete=models.PROTECT,                              # ✅ Đổi từ CASCADE
        related_name='cac_chung_chi',                          # ✅ Thêm related_name
    )
    so_chung_chi = models.CharField(max_length=50, unique=True)
    ngay_cap = models.DateField()
    ngay_het_han = models.DateField(null=True, blank=True)
    diem_so = models.FloatField(null=True, blank=True)
    hinh_thuc_thi = models.CharField(max_length=50, blank=True)
    trang_thai = models.CharField(
        max_length=20,
        choices=TRANG_THAI_CHOICES,
        default='CHO',                                         # ✅ Đổi default
    )
    da_xet_duyet = models.BooleanField(default=False)

    class Meta:
        ordering = ['-ngay_cap']

    def __str__(self):
        return f"{self.so_chung_chi} - SV {self.sinh_vien_id}"