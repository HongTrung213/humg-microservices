from django.db import models
import bleach  # Đã cài sẵn

ALLOWED_TAGS = ['p', 'br', 'b', 'i', 'u', 'a', 'img', 'div', 'span', 
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 
                'table', 'tr', 'td', 'th', 'strong', 'em', 'blockquote']


class BaiViet(models.Model):
    tieu_de = models.CharField(max_length=200)
    noi_dung = models.TextField()
    slug = models.SlugField(unique=True)
    hinh_anh = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tieu_de

    def save(self, *args, **kwargs):
        if self.noi_dung:
            self.noi_dung = bleach.clean(
                self.noi_dung,
                tags=ALLOWED_TAGS,
                attributes={'a': ['href', 'title'], 'img': ['src', 'alt']},
                strip=True
            )
        super().save(*args, **kwargs)

class Slider(models.Model):
    tieu_de = models.CharField(max_length=100)
    hinh_anh = models.URLField()
    duong_dan = models.CharField(max_length=200, blank=True)
    thu_tu = models.IntegerField(default=0)

    def __str__(self):
        return self.tieu_de

class QuickLink(models.Model):
    ten = models.CharField(max_length=100)
    duong_dan = models.CharField(max_length=200)
    thu_tu = models.IntegerField(default=0)

    def __str__(self):
        return self.ten

from django.db import models
from django.utils.text import slugify

class VanBanQuyChe(models.Model):
    LOAI_CHOICES = [
        ('QUY_CHE', 'Quy chế'),
        ('BIEU_MAU', 'Biểu mẫu'),
        ('HUONG_DAN', 'Hướng dẫn'),
        ('VAN_BAN', 'Văn bản khác'),
    ]
    
    tieu_de = models.CharField(max_length=200, verbose_name="Tiêu đề")
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="Đường dẫn")
    loai = models.CharField(max_length=20, choices=LOAI_CHOICES, default='QUY_CHE', verbose_name="Loại văn bản")
    noi_dung = models.TextField(verbose_name="Nội dung")
    file_dinh_kem = models.FileField(upload_to='van_ban/', blank=True, null=True, verbose_name="File đính kèm")
    thu_tu = models.IntegerField(default=0, verbose_name="Thứ tự hiển thị")
    is_active = models.BooleanField(default=True, verbose_name="Hiển thị")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['thu_tu', '-created_at']
        verbose_name = "Văn bản quy chế"
        verbose_name_plural = "Văn bản quy chế"

    def __str__(self):
        return self.tieu_de

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tieu_de)
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        # Tạo slug nếu chưa có
        if not self.slug:
            self.slug = slugify(self.tieu_de)
        # Lọc HTML để chống XSS
        if self.noi_dung:
            self.noi_dung = bleach.clean(
                self.noi_dung,
                tags=ALLOWED_TAGS,
                attributes={'a': ['href', 'title'], 'img': ['src', 'alt']},
                strip=True
            )
        super().save(*args, **kwargs)