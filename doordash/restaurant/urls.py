from django.urls import path

from . import views

app_name = 'restaurant'

urlpatterns = [
    # path('restuarants/<int:restuarant_id>/', views.restuarant_detail, name='restuarant_detail'),
    path('<int:restaurant_id>/',
         views.restaurant_detail, name='restaurant_detail'),
]
