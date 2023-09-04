from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views
from django.contrib import admin

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('admin/', admin.site.urls, name='admin'),

    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/',
         views.remove_from_cart, name='remove_from_cart'),
    path('increase_amount/<int:item_id>/',
         views.increase_amount, name='increase_amount'),

    path('clear_cart/', views.clear_cart, name='clear_cart'),

]
