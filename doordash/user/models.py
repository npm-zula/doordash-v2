from django.db import models

from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    display_name = models.CharField(max_length=32)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.display_name
