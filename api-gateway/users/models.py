from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Giảng viên'),
        ('student', 'Sinh viên'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    # Thông tin cá nhân
    phone = models.CharField('Số điện thoại', max_length=20, blank=True, default='')
    address = models.CharField('Địa chỉ', max_length=255, blank=True, default='')
    date_of_birth = models.DateField('Ngày sinh', null=True, blank=True)
    bio = models.TextField('Giới thiệu', blank=True, default='')

    # Ảnh đại diện (lưu vào media/avatars/)
    avatar = models.ImageField(
        'Ảnh đại diện',
        upload_to='avatars/%Y/%m/',
        null=True,
        blank=True,
        default=None,
    )

    # Metadata
    last_login_ip = models.GenericIPAddressField('IP đăng nhập cuối', null=True, blank=True)
    last_login_at = models.DateTimeField('Đăng nhập lúc', null=True, blank=True)

    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('Cập nhật', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Hồ sơ người dùng'
        verbose_name_plural = 'Hồ sơ người dùng'

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"

    @property
    def avatar_url(self):
        """Trả về URL ảnh đại diện hoặc ảnh mặc định."""
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return '/static/html/assets/img/profiles/avatar-01.jpg'

    @property
    def display_name(self):
        """Tên hiển thị ưu tiên."""
        full = self.user.get_full_name()
        return full if full.strip() else self.user.username


class UserActivity(models.Model):
    """Log hoạt động của người dùng."""
    ACTION_CHOICES = (
        ('login', 'Đăng nhập'),
        ('logout', 'Đăng xuất'),
        ('update_profile', 'Cập nhật hồ sơ'),
        ('change_password', 'Đổi mật khẩu'),
        ('upload_avatar', 'Cập nhật ảnh đại diện'),
        ('other', 'Khác'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='activities',
        verbose_name='Người dùng',
    )
    action = models.CharField('Hành động', max_length=30, choices=ACTION_CHOICES, default='other')
    description = models.CharField('Mô tả', max_length=255, blank=True, default='')
    ip_address = models.GenericIPAddressField('IP', null=True, blank=True)
    user_agent = models.CharField('User Agent', max_length=255, blank=True, default='')
    created_at = models.DateTimeField('Thời gian', auto_now_add=True)

    class Meta:
        verbose_name = 'Hoạt động'
        verbose_name_plural = 'Hoạt động'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.get_action_display()}"


# Tự động tạo profile khi User được tạo
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()