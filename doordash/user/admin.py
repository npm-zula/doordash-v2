from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    list_display = ('display_name', 'username', 'email', 'display_name',
                    'full_name', 'is_staff')
    form = CustomUserChangeForm

    def get_readonly_fields(self, request, obj=None):
        if obj and request.user.id != obj.id:
            # If the user is not editing their own record, make all fields read-only
            return [field.name for field in obj._meta.fields]
        return super().get_readonly_fields(request, obj)


admin.site.register(CustomUser, CustomUserAdmin)
