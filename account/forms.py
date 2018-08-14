from django import forms
from account.models import Signup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address.')
    class Meta:
        model = Signup
        widgets = {'pwd': forms.PasswordInput(), }
        fields = ['user','pwd']

# class LoginForm(UserCreationForm):
#     user = forms.CharField(max_length=20)
#     pwd = forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = User
#         fields = ['user', 'pwd']
class LoginForm(forms.Form):
    user = forms.CharField(max_length=20)
    pwd = forms.CharField(widget=forms.PasswordInput())