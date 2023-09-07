from django.db import models
from restaurant.models import Item
from user.models import CustomUser
from .enums import status_options

# import enums file


class Order(models.Model):

    # status_choices = (
    #     ('Ordered', 'Orderd'),
    #     ('Paid', 'Paid'),
    #     ('Cancelled', 'Cancelled'),
    #     ('Completed', 'Completed')
    # )

    CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    status = models.CharField(
        max_length=10, choices=[(status.value, status.name) for status in status_options], default='Ordered')

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal_price = models.DecimalField(max_digits=10, decimal_places=2)
