from rest_framework import generics

from links.models import Link
from links.paginators import LinkPaginator
from links.permissions import IsOwner
from links.serializers.link import LinkSerializer
from users.permissions import IsSuperUser


class LinkCreateAPIView(generics.CreateAPIView):
    """
    APIView for creating a new Link instance.

    This APIView inherits from `generics.CreateAPIView` and is used to create a new instance of the `Link` model.
    It uses the `LinkSerializer` for serialization.

    Attributes:
        serializer_class (LinkSerializer): The serializer class used for the Link model.

    Methods:
        perform_create: Overrides the `perform_create` method to set the owner field of the instance to the current user
    """
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        """
        Overrides the `perform_create` method to set the `owner` field of the instance to the current user.

        Args:
            serializer (LinkSerializer): The serializer instance used to create the Link instance.
        """
        serializer.save(owner=self.request.user)


class LinkListAPIView(generics.ListAPIView):
    """
    APIView for listing Link instances.

    This APIView inherits from `generics.ListAPIView` and is used to list instances of the `Link` model.
    It uses the `LinkSerializer` for serialization and the `LinkPaginator` for pagination.

    Attributes:
        serializer_class (LinkSerializer): The serializer class used for the Link model.
        queryset (QuerySet): The queryset containing all Link model instances.
        pagination_class (LinkPaginator): The pagination class used to handle pagination for Link model instances.
        permission_classes (list): List of permission classes required for this view.

    Methods:
        get_queryset: Overrides the `get_queryset` method to filter the queryset based on the user's permissions.
    """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    pagination_class = LinkPaginator
    permission_classes = [IsOwner | IsSuperUser]

    def get_queryset(self):
        """
        Overrides the `get_queryset` method to filter the queryset based on the user's permissions.

        If the user is a superuser, it returns all Link instances. Otherwise, it returns only the Link instances
        owned by the user.

        Returns:
            QuerySet: The filtered queryset.
        """
        if self.request.user.is_superuser:
            return Link.objects.all()
        return Link.objects.filter(owner=self.request.user)


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    """
    APIView for retrieving a single Link instance.

    This APIView inherits from `generics.RetrieveAPIView` and is used to retrieve a single instance of the `Link` model.
    It uses the `LinkSerializer` for serialization.

    Attributes:
        serializer_class (LinkSerializer): The serializer class used for the Link model.
        queryset (QuerySet): The queryset containing all Link model instances.
        permission_classes (list): List of permission classes required for this view.
    """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsOwner | IsSuperUser]


class LinkUpdateAPIView(generics.UpdateAPIView):
    """
    APIView for updating a Link instance.

    This APIView inherits from `generics.UpdateAPIView` and is used to update an existing instance of the `Link` model.
    It uses the `LinkSerializer` for serialization.

    Attributes:
        serializer_class (LinkSerializer): The serializer class used for the Link model.
        queryset (QuerySet): The queryset containing all Link model instances.
        permission_classes (list): List of permission classes required for this view.
    """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsOwner | IsSuperUser]


class LinkDestroyAPIView(generics.DestroyAPIView):
    """
    APIView for deleting a Link instance.

    This APIView inherits from `generics.DestroyAPIView` and is used to delete an existing instance of the `Link` model.

    Attributes:
        queryset (QuerySet): The queryset containing all Link model instances.
        permission_classes (list): List of permission classes required for this view.
    """
    queryset = Link.objects.all()
    permission_classes = [IsOwner | IsSuperUser]
