from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('view_order/', views.view_order, name='view_order')
]
