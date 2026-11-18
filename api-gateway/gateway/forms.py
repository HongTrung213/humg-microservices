from django import forms


class StudentForm(forms.Form):
    """Form them/sua sinh vien - khop model SinhVien va API payload."""

    ma_sv = forms.CharField(
        label='Mã số sinh viên', max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'VD: 2121067899',
            'id': 'id_ma_sv',
            'autocomplete': 'off',
        })
    )
    ho_ten = forms.CharField(
        label='Họ và tên', max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'VD: Nguyễn Văn An',
        })
    )
    ngay_sinh = forms.DateField(
        label='Ngày sinh', required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    gioi_tinh = forms.ChoiceField(
        label='Giới tính', required=False,
        choices=[('', '— Chọn giới tính —'), ('Nam', 'Nam'), ('Nữ', 'Nữ')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    email_truong = forms.EmailField(
        label='Email trường', required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control bg-light',
            'readonly': 'readonly',
            'id': 'id_email_truong',
            'placeholder': 'Tự động: <MSSV>@student.humg.edu.vn',
        })
    )
    email_ca_nhan = forms.EmailField(
        label='Email cá nhân', required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    so_dien_thoai = forms.CharField(
        label='Số điện thoại', required=False, max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: 0912345678'})
    )
    khoa_hoc = forms.CharField(
        label='Khóa học', required=False, max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: K66'})
    )
    nam_nhap_hoc = forms.IntegerField(
        label='Năm nhập học', required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 2000, 'max': 2100})
    )
    lop = forms.CharField(
        label='Lớp', required=False, max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VD: DCKT K66'})
    )

    khoa = forms.ChoiceField(
        label='Khoa', required=False,
        choices=[], widget=forms.Select(attrs={'class': 'form-select'})
    )
    nganh = forms.ChoiceField(
        label='Ngành đào tạo', required=False,
        choices=[], widget=forms.Select(attrs={'class': 'form-select'})
    )

    anh_dai_dien = forms.ImageField(
        label='Ảnh đại diện', required=False,
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'})
    )

    def __init__(self, *args, khoas=None, nganhs=None, **kwargs):
        super().__init__(*args, **kwargs)

        khoas = khoas or []
        nganhs = nganhs or []

        self.fields['khoa'].choices = [('', '— Chọn khoa —')] + [
            (str(k.get('id')), k.get('ten_khoa', '')) for k in khoas
        ]
        self.fields['nganh'].choices = [('', '— Chọn ngành —')] + [
            (str(n.get('id')), n.get('ten_nganh', '')) for n in nganhs
        ]

        if self.initial:
            if self.initial.get('khoa'):
                self.fields['khoa'].initial = str(self.initial['khoa'])
            if self.initial.get('nganh'):
                self.fields['nganh'].initial = str(self.initial['nganh'])
