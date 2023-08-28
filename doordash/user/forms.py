from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


from .models import CustomUser


class LoginForm(AuthenticationForm):
    pass


class RegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'display_name', 'full_name')
