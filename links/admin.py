from django.contrib import admin

from links.models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    """
    Admin model for the Link model.

    This class is a subclass of `admin.ModelAdmin` and is used to customize the admin interface for the `Link` model.
    It is registered using the `@admin.register` decorator to register the `Link` model with the admin site.

    Attributes:
        list_display (tuple): A tuple of field names to display as columns on the change list page of the admin.

    Customization:
        list_display: Specifies the fields to display in the list view of the admin.
    """
    list_display = ('pk', 'title', 'description', 'url', 'preview', 'type', 'created_at', 'updated_at', 'owner',)
