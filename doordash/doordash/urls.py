
from django.contrib import admin
from django.urls import path, include
from user import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('', include('doordash_app.urls')),
]
