from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile


class UserUpdateForm(forms.ModelForm):
    """Form cập nhật User cơ bản."""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Họ'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email).exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError('Email này đã được sử dụng bởi tài khoản khác.')
        return email


class UserProfileForm(forms.ModelForm):
    """Form cập nhật thông tin mở rộng của profile."""
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'date_of_birth', 'bio']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Số điện thoại'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Địa chỉ'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Giới thiệu bản thân...'}),
        }


class AvatarUploadForm(forms.ModelForm):
    """Form upload ảnh đại diện."""
    class Meta:
        model = UserProfile
        fields = ['avatar']
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            if avatar.size > 2 * 1024 * 1024:
                raise forms.ValidationError('Ảnh không được lớn hơn 2MB.')
            ctype = getattr(avatar, 'content_type', '')
            if ctype and not ctype.startswith('image/'):
                raise forms.ValidationError('File phải là ảnh (JPG, PNG, GIF...).')
        return avatar


class CustomPasswordChangeForm(PasswordChangeForm):
    """Form đổi mật khẩu có style Bootstrap."""
    old_password = forms.CharField(
        label='Mật khẩu hiện tại',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mật khẩu hiện tại'}),
    )
    new_password1 = forms.CharField(
        label='Mật khẩu mới',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mật khẩu mới'}),
    )
    new_password2 = forms.CharField(
        label='Nhập lại mật khẩu mới',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nhập lại mật khẩu mới'}),
    )