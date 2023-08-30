from .utils import get_or_create_cart_item
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm

from .models import CartItem
from restaurant.models import Item

from .utils import get_or_create_cart_item


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


def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)

    return render(request, 'doordash_app/cart.html', {'cart_items': cart_items})


def add_to_cart(request, item_id):
    item = Item.objects.get(pk=item_id)
    cart_item, created = get_or_create_cart_item(request.user, item, request)

    if not created:
        cart_item.quantity += 1
        cart_item.price = cart_item.item.price * cart_item.quantity
        cart_item.save()

    return redirect('home')

# create a view to display the cart


def cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
        session_key = request.session.session_key
        cart_items = CartItem.objects.filter(session_key=session_key)

    return render(request, 'doordash_app/cart.html', {'cart_items': cart_items})
