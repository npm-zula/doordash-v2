from django.shortcuts import render, get_object_or_404
from .models import Restaurant

# Create your views here.


def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'restaurant/restaurant_detail.html', {'restaurant': restaurant})
