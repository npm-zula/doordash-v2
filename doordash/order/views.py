from django.shortcuts import render, redirect
from .models import Order, OrderItem
from restaurant.models import Item
from django.contrib.auth.decorators import login_required
from user.models import CustomUser, CartItem


def place_order(request):
    user = request.user

    cart_items = CartItem.objects.filter(
        session_key=request.session.session_key)

    if not user.is_authenticated:
        # cart_items.delete()
        # return redirect('home')
        return redirect('users:login')

    order = Order.objects.create(CustomUser=user, total_price=0)
    for cart_item in cart_items:
        subtotal_price = cart_item.quantity * cart_item.item.price
        OrderItem.objects.create(order=order, item=cart_item.item,
                                 quantity=cart_item.quantity, subtotal_price=subtotal_price)
        order.total_price += subtotal_price
        order.save()

    cart_items.delete()

    return redirect('home')


def view_order(request):
    user = request.user
    orders = Order.objects.filter(CustomUser=user)
    # get all order items for each order
    for order in orders:
        order_items = OrderItem.objects.filter(order_id=order.id)
        order.order_items = order_items

    return render(request, 'order/order.html', {'orders': orders})


def order_details(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order_id=order_id)

    # get item names for each order item
    for order_item in order_items:
        item = Item.objects.get(id=order_item.item_id)
        order_item.item_name = item.name

    return render(request, 'order/order_details.html', {'order': order, 'order_items': order_items})


def clear_orders(request):
    user = request.user
    orders = Order.objects.filter(CustomUser=user)

    for order in orders:
        order_items = OrderItem.objects.filter(order_id=order.id)
        order_items.delete()

    orders.delete()

    return redirect('home')
