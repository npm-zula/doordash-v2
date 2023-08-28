from django.urls import path

from . import views

urlpatterns = [
    path('restuarants/<int:restuarant_id>/',
         views.restuarant_detail, name='restuarant_detail'),
]
