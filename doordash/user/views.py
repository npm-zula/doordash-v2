from typing import Any, Dict, Optional
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.views.generic.edit import CreateView
from .forms import RegistrationForm, LoginForm

from .models import CustomUser


# def signup(request):
#     context = {}
#     if request.POST:
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             display_name = form.cleaned_data.get('display_name')
#             full_name = form.cleaned_data.get('full_name')
#             raw_password = form.cleaned_data.get('password1')
#             account = authenticate(
#                 email=email, display_name=display_name, full_name=full_name, password=raw_password)
#             login(request, account)
#             return redirect('home')
#         else:
#             context['registration_form'] = form

#     else:
#         form = RegistrationForm()
#         context['registration_form'] = form

#     return render(request, 'user/signup.html', context)


# def user_login(request):
#     context = {}
#     # user = request.user
#     # if user.is_authenticated:
#     #     return redirect('home')

#     if request.POST:
#         # form = LoginForm(request.POST)
#         form = AuthenticationForm(data=request.POST)

#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(email=email, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('home')
#             # else:
#             #     return redirect('signup')

#     else:
#         form = LoginForm()

#     context['login_form'] = form
#     return render(request, 'user/login.html', context)


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)

            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'user/signup.html', {'form': form})


def user_login(request):
    # if request.user and request.user.is_authenticated:
    #     return redirect('home')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 form.add_error(None, 'Invalid email or password')
#     else:
#         form = LoginForm()
#     return render(request, 'user/login.html', {'form': form})
