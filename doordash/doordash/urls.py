
from django.contrib import admin
from django.urls import path, include
from user import views as v
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('doordash_app.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('restaurant/', include('restaurant.urls', namespace="restaurant")),
    path('order/', include('order.urls', namespace="order")),

    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
