from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True, null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=32, unique=True, null=True)
    password = models.CharField(max_length=32, default='password')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


# class User(models.Model):
#     full_name = models.CharField(max_length=100)
#     display_name = models.CharField(
#         max_length=32, validators=[MinLengthValidator(4)])
#     email = models.CharField(max_length=100, unique=True)
#     phone = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.display_name)
