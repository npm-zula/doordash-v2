from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('admin/', admin.site.urls, name='admin')
]
