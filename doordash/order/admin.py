from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


def mark_as_paid(modeladmin, request, queryset):
    queryset.update(status='Paid')


def mark_as_completed(modeladmin, request, queryset):
    queryset.update(status='Completed')


def cancel_orders(modeladmin, request, queryset):
    queryset.filter(status__in=['Ordered', 'Paid']).update(status='Cancelled')


mark_as_paid.short_description = "Mark selected orders as Paid"
mark_as_completed.short_description = "Mark selected orders as Completed"
cancel_orders.short_description = "Cancel selected orders"


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    # not editable
    readonly_fields = ('order', 'item', 'quantity', 'subtotal_price')
    # cant add new items
    can_delete = False
    extra = 0

    def has_add_permission(self, request, obj):
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    #    list total orders by status
    list_display = ('id', 'CustomUser', 'status',)

    #    filter orders by status type
    list_filter = ('status',)
    inlines = [OrderItemInline]

    # readonly_fields = ('id', 'CustomUser', 'created_at', 'total_price')
    actions = [mark_as_paid, mark_as_completed, cancel_orders]

    fieldsets = (
        (None, {
            'fields': ('CustomUser', 'created_at', 'status')
        }),
        ('Order Total', {
            'fields': ('total_price',),
        }),

    )

    readonly_fields = ('id', 'CustomUser', 'created_at', 'total_price')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'item', 'quantity', 'subtotal_price')
    readonly_fields = ('order', 'item', 'quantity', 'subtotal_price')
