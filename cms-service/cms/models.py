from django.db import models
from django.utils.text import slugify
import bleach
from bleach.css_sanitizer import CSSSanitizer

# ============================================
# WHITELIST HTML + CSS CHO WYSIWYG
# ============================================
ALLOWED_TAGS = [
    'p', 'br', 'b', 'i', 'u', 's', 'sub', 'sup', 'a', 'img', 'div', 'span',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'ul', 'ol', 'li',
    'table', 'thead', 'tbody', 'tfoot', 'tr', 'td', 'th', 'caption',
    'strong', 'em', 'blockquote', 'pre', 'code',
    'hr', 'figure', 'figcaption',
]

ALLOWED_ATTRIBUTES = {
    '*':    ['style', 'class', 'id'],
    'a':    ['href', 'title', 'target', 'rel'],
    'img':  ['src', 'alt', 'title', 'width', 'height', 'style'],
    'td':   ['colspan', 'rowspan', 'style'],
    'th':   ['colspan', 'rowspan', 'scope', 'style'],
    'table':['border', 'cellpadding', 'cellspacing', 'style', 'width'],
    'ol':   ['type', 'start'],
}

# CSS properties được phép trong style=
ALLOWED_CSS = [
    'color', 'background-color', 'background',
    'font-family', 'font-size', 'font-weight', 'font-style',
    'text-align', 'text-decoration', 'text-indent', 'line-height',
    'border', 'border-left', 'border-right', 'border-top', 'border-bottom',
    'border-color', 'border-style', 'border-width', 'border-radius',
    'padding', 'padding-left', 'padding-right', 'padding-top', 'padding-bottom',
    'margin', 'margin-left', 'margin-right', 'margin-top', 'margin-bottom',
    'width', 'height', 'max-width', 'min-width',
    'display', 'vertical-align', 'border-collapse', 'border-spacing', 'white-space', 'word-break', 'opacity',
]

css_sanitizer = CSSSanitizer(allowed_css_properties=ALLOWED_CSS)


def sanitize_html(html):
    """Lọc HTML — cho phép style/font/màu nhưng chặn script."""
    if not html:
        return html
    return bleach.clean(
        html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        css_sanitizer=css_sanitizer,
        strip=True,
        strip_comments=True,
    )


# ============================================
# DANH MỤC BÀI VIẾT
# ============================================
class DanhMuc(models.Model):
    name = models.CharField(max_length=200, verbose_name='Tên danh mục')
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name='Đường dẫn')
    description = models.TextField(blank=True, verbose_name='Mô tả')
    show_on_navbar = models.BooleanField(default=False, verbose_name='Hiện trên menu')
    show_on_homepage = models.BooleanField(default=False, verbose_name='Hiện trang chủ')
    is_active = models.BooleanField(default=True, verbose_name='Kích hoạt')
    thu_tu = models.IntegerField(default=0, verbose_name='Thứ tự')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['thu_tu', 'name']
        verbose_name = 'Danh mục bài viết'
        verbose_name_plural = 'Danh mục bài viết'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name) or 'danh-muc'
            slug = base
            n = 1
            while DanhMuc.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                n += 1
                slug = f'{base}-{n}'
            self.slug = slug
        super().save(*args, **kwargs)


# ============================================
# BÀI VIẾT
# ============================================
class BaiViet(models.Model):
    tieu_de = models.CharField(max_length=200)
    noi_dung = models.TextField()
    slug = models.SlugField(unique=True)
    hinh_anh = models.URLField(blank=True)
    category = models.ForeignKey(
        DanhMuc,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='cac_bai_viet',
        verbose_name='Danh mục',
    )
    summary = models.TextField(blank=True, verbose_name='Tóm tắt')
    is_published = models.BooleanField(default=True, verbose_name='Xuất bản')
    thu_tu = models.IntegerField(default=0, verbose_name='Thứ tự')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.tieu_de

    def save(self, *args, **kwargs):
        if self.noi_dung:
            self.noi_dung = sanitize_html(self.noi_dung)
        super().save(*args, **kwargs)


# ============================================
# SLIDER
# ============================================
class Slider(models.Model):
    tieu_de = models.CharField(max_length=100)
    hinh_anh = models.URLField(blank=True)
    duong_dan = models.CharField(max_length=200, blank=True)
    thu_tu = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True, verbose_name='Kích hoạt')

    class Meta:
        ordering = ['thu_tu', 'id']

    def __str__(self):
        return self.tieu_de


# ============================================
# QUICKLINK
# ============================================
class QuickLink(models.Model):
    ten = models.CharField(max_length=100)
    duong_dan = models.CharField(max_length=200)
    thu_tu = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True, verbose_name='Kích hoạt')

    class Meta:
        ordering = ['thu_tu', 'id']

    def __str__(self):
        return self.ten


# ============================================
# VĂN BẢN QUY CHẾ
# ============================================
class VanBanQuyChe(models.Model):
    LOAI_CHOICES = [
        ('QUY_CHE', 'Quy chế'),
        ('BIEU_MAU', 'Biểu mẫu'),
        ('HUONG_DAN', 'Hướng dẫn'),
        ('VAN_BAN', 'Văn bản khác'),
    ]

    tieu_de = models.CharField(max_length=200, verbose_name='Tiêu đề')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    loai = models.CharField(max_length=20, choices=LOAI_CHOICES, default='QUY_CHE')
    noi_dung = models.TextField()
    file_dinh_kem = models.FileField(upload_to='van_ban/', blank=True, null=True)
    thu_tu = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['thu_tu', '-created_at']

    def __str__(self):
        return self.tieu_de

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tieu_de)
        if self.noi_dung:
            self.noi_dung = sanitize_html(self.noi_dung)
        super().save(*args, **kwargs)