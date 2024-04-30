from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Permission class to check if the user is the owner of the object.

    This class is a subclass of BasePermission and is used to check if the authenticated user is the owner of an object.
    It is typically used in a view to restrict access to the object.

    Attributes:
        message (str): The message to display if the user does not have the required permissions.

    Methods:
        has_object_permission: Checks if the user is the owner of the object.
    """
    message = 'You are not the owner!'

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is the owner of the object.

        Args:
            request (Request): The request instance.
            view (View): The view instance.
            obj (Model): The model instance to check permissions against.

        Returns:
            bool: True if the user is the owner of the object, False otherwise.
        """
        if request.user == obj.owner:
            return True
        return False
