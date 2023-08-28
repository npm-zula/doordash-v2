from django.shortcuts import render, redirect
from .models import Order, OrderItem
from restaurant.models import Item
from django.contrib.auth.decorators import login_required
from user.models import CustomUser, CartItem


@login_required
def place_order(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)

    order = Order.objects.create(CustomUser=user, total_price=0)
    for cart_item in cart_items:
        subtotal_price = cart_item.quantity * cart_item.item.price
        OrderItem.objects.create(order=order, item=cart_item.item,
                                 quantity=cart_item.quantity, subtotal_price=subtotal_price)
        order.total_price += subtotal_price
        order.save()

    cart_items.delete()

    return redirect('home')


@login_required
def view_order(request):
    user = request.user

    orders = Order.objects.filter(CustomUser=user)

    return render(request, 'order/order.html', {'orders': orders})
