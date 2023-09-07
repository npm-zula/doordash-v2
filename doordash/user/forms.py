from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


from .models import CustomUser


class LoginForm(AuthenticationForm):
    pass


class RegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'display_name', 'full_name')


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'display_name', 'full_name',
                  'is_active', 'is_staff', 'is_superuser')
