from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('all_items/', views.all_items, name='all_items'),
]
