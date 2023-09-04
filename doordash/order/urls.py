from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('view_order/', views.view_order, name='view_order'),
    path('clear_orders/', views.clear_orders, name='clear_orders'),
    path('order_details/<int:order_id>/',
         views.order_details, name='order_details'),
]
