from django.contrib import admin
from .models import Restaurant, Item, Category
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Category)
