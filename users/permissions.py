from rest_framework import permissions

from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    """
    Custom permission class to check if the user is a superuser.

    Attributes:
        message (str): The error message to be displayed if the user is not a superuser.
    """
    message = 'You are not a superuser!'

    def has_permission(self, request, view):
        """
        Method to check if the user is a superuser.

        Args:
            request (HttpRequest): The request object.
            view (APIView): The view object.

        Returns:
            bool: True if the user is a superuser, False otherwise.
        """
        if request.user.is_superuser:
            return True
        return False


class IsOwner(permissions.BasePermission):
    """
    Permission class to check if the user is the owner of a profile.

    Attributes:
        message (str): The error message to be displayed if the user is not the owner.
    """
    message = 'You are not the owner of this profile!'

    def has_object_permission(self, request, view, obj):
        """
        Method to check if the user is the owner of the profile object.

        Args:
            request: The request object.
            view: The view object.
            obj: The profile object.

        Returns:
            bool: True if the user is the owner, False otherwise.
        """
        if request.user == obj:
            return True
        return False
