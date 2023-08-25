from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user object first
            login(request, user)

            # renders home.html with the context {'user': user}
            return render(request, 'home.html', {'user': user})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to your desired page after login
            return render(request, 'home.html', {'user': user})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
