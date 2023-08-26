from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


from .models import CustomUser


# class SignUpForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = CustomUser
#         fields = ('display_name', 'full_name', 'email', 'password')


class LoginForm(AuthenticationForm):
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    # email = forms.EmailField(label='Email')

    # class Meta:
    #     model = CustomUser
    #     # fields = ('email', 'password')
    pass


class RegistrationForm(UserCreationForm):
    # password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # email = forms.EmailField(label='Email')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'display_name', 'full_name')
