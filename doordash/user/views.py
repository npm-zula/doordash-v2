from typing import Any, Dict, Optional
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm

from .models import CartItem
from restaurant.models import Item

from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'user/signup.html', {'form': form})


def user_login(request):
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


# cart views
def add_to_cart(request, item_id):
    item = Item.objects.get(pk=item_id)

    if request.user.is_authenticated:
        # Authenticated user
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user, item=item)
    else:
        # Non-authenticated user
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart_item, created = CartItem.objects.get_or_create(
            session_key=session_key, item=item)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('home')

# create a view to display the cart


@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'doordash_app/cart.html', {'cart_items': cart_items})
