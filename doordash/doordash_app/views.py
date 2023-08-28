from django.shortcuts import render
from restaurant.models import Restaurant
from restaurant.models import Item
# Create your views here.


def home(request):
    # You can adjust the number of featured restaurants
    featured_restaurants = Restaurant.objects.all()[:5]
    featured_items = Item.objects.all()[:5]
    return render(request, 'doordash_app/home.html', {'featured_restaurants': featured_restaurants, 'featured_Items': featured_items})
