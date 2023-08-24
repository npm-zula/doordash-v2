from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # doesn't exist right now
            return redirect('/user/profile')

    else:
        form = SignupForm()

    return render(request, 'register/register.html', {'form': form})
