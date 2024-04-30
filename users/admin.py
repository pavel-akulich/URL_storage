from django.contrib import admin

from users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    """
    Admin class for managing User model instances in the Django admin interface.

    Attributes:
        list_display (tuple): The fields to display in the admin list view.
    """
    list_display = ('pk', 'email', 'first_name', 'last_name', 'phone', 'country', 'avatar',)
