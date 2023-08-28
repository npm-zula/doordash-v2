
from django.contrib import admin
from django.urls import path, include
from user import views as v


urlpatterns = [
    path('', include('doordash_app.urls')),
    path('users/', include('user.urls')),
    path('restaurant/', include('restaurant.urls', namespace="restaurant")),
]
