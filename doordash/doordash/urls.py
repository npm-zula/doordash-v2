
from django.contrib import admin
from django.urls import path, include
from user import views as v
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url


handler404 = 'doordash_app.views.error_404'


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
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, }),


]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
