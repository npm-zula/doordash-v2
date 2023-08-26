from django.db import models

from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUser(AbstractUser):
    # username = None
    email = models.EmailField(unique=True)
    display_name = models.CharField(max_length=32)
    full_name = models.CharField(max_length=100)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['full_name', 'display_name', 'password']

    def __str__(self):
        return self.display_name

# class AccountManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, email, display_name, full_name, password):
#         values = [email, display_name, full_name]
#         field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
#         for field_name, value in field_value_map.items():
#             if not value:
#                 raise ValueError('The {} value must be set'.format(field_name))

#         email = self.normalize_email(email)
#         user = self.model(
#             email=email,
#             display_name=display_name,
#             full_name=full_name,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, display_name, full_name, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, display_name, full_name, password, **extra_fields)

#     def create_superuser(self, email, display_name, full_name, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, display_name, full_name, password, **extra_fields)


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     display_name = models.CharField(max_length=32)
#     full_name = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)

#     # objects = AccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def get_full_name(self):
#         return self.full_name
