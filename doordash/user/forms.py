from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'email', 'password')


class LoginForm(AuthenticationForm):
    # You don't need to define anything here since AuthenticationForm covers it.
    pass
