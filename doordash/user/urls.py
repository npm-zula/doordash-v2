from django.urls import path, include
from . import views

# from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
