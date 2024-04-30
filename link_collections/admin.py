from django.contrib import admin

from link_collections.models import Collection


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    """
    Admin model for the Collection model.

    This class is a subclass of `admin.ModelAdmin` and is used to customize the admin interface for the Collection model
    It is registered using the `@admin.register` decorator to register the `Collection` model with the admin site.

    Attributes:
        list_display (tuple): A tuple of field names to display as columns on the change list page of the admin.

    Customization:
        list_display: Specifies the fields to display in the list view of the admin.
    """
    list_display = ('pk', 'name', 'description', 'created_at', 'updated_at', 'owner',)
