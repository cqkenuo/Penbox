from django import forms
from captcha.fields import CaptchaField
class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))
    captcha = CaptchaField(label='验证码')

class ChangePwdForm(forms.Form):
    old_password = forms.CharField(label="旧密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))
    new_password = forms.CharField(label="新密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))
    captcha = CaptchaField(label='验证码')
