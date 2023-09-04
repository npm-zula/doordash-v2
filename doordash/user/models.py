from django.db import models

from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MinLengthValidator


from restaurant.models import Item


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    display_name = models.CharField(
        max_length=32, default='Anonymous', validators=[MinLengthValidator(2)])
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.display_name


class CartItem(models.Model):
    session_key = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             blank=True, null=True)  # For authenticated users
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.item.name} ({self.quantity})"
