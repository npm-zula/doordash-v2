from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'CustomUser', 'created_at', 'total_price', 'status')
    list_filter = ('status',)

    readonly_fields = ('id', 'CustomUser', 'created_at', 'total_price')
