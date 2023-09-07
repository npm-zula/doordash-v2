from django.shortcuts import render
from restaurant.models import Restaurant
from restaurant.models import Item
# Create your views here.


def home(request):
    # You can adjust the number of featured restaurants
    featured_restaurants = Restaurant.objects.all()[:5]
    featured_items = Item.objects.all()[:5]
    return render(request, 'doordash_app/home.html', {'featured_restaurants': featured_restaurants, 'featured_Items': featured_items})


# all items
def all_items(request):
    all_items = Item.objects.all()
    return render(request, 'doordash_app/all_items.html', {'all_items': all_items})


# 404 page
def error_404(request, exception):
    return render(request, 'doordash_app/error_404.html', status=404)
