# accounts/forms.py
from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    password  = forms.CharField(widget=forms.PasswordInput, label="Mật khẩu")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Xác nhận mật khẩu")

    class Meta:
        model  = CustomUser
        fields = ['username', 'email', 'phone', 'password', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Placeholder cho từng field
        placeholders = {
            'username': 'Nhập tên đăng nhập',
            'email':    'Nhập email',
            'phone':    'Nhập số điện thoại',
            'password': 'Nhập mật khẩu',
            'password2':'Xác nhận mật khẩu',
        }
        # Gán class + placeholder cho widget
        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': placeholders.get(name, '')
            })

    def clean(self):
        cleaned = super().clean()
        pw  = cleaned.get('password')
        pw2 = cleaned.get('password2')
        if pw and pw2 and pw != pw2:
            self.add_error('password2', 'Mật khẩu xác nhận không khớp.')
        return cleaned
