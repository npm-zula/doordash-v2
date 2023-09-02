
from django.contrib import admin
from django.urls import path, include
from user import views as v


urlpatterns = [
    path('', include('doordash_app.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('restaurant/', include('restaurant.urls', namespace="restaurant")),
    path('order/', include('order.urls', namespace="order")),
]
