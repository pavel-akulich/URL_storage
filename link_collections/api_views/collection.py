from rest_framework import generics

from link_collections.models import Collection
from link_collections.paginators import CollectionPaginator
from link_collections.serializers.collection import CollectionSerializer
from links.permissions import IsOwner
from users.permissions import IsSuperUser


class CollectionCreateAPIView(generics.CreateAPIView):
    """
    APIView for creating a new Collection instance.

    This APIView inherits from `generics.CreateAPIView` and is used to create a new instance of the `Collection` model.
    It uses the `CollectionSerializer` for serialization.

    Attributes:
        serializer_class (CollectionSerializer): The serializer class used for the Collection model.

    Methods:
        perform_create: Overrides the `perform_create` method to set the `owner` field of the instance to the actual user.
    """
    serializer_class = CollectionSerializer

    def perform_create(self, serializer):
        """
        Overrides the `perform_create` method to set the `owner` field of the instance to the current user.

        Args:
            serializer (CollectionSerializer): The serializer instance used to create the Collection instance.
        """
        serializer.save(owner=self.request.user)


class CollectionListAPIView(generics.ListAPIView):
    """
    APIView for listing Collection instances.

    This APIView inherits from `generics.ListAPIView` and is used to list instances of the `Collection` model.
    It uses the `CollectionSerializer` for serialization and the `CollectionPaginator` for pagination.

    Attributes:
        serializer_class (CollectionSerializer): The serializer class used for the Collection model.
        queryset (QuerySet): The queryset containing all Collection model instances.
        pagination_class (CollectionPaginator): The pagination class used to handle pagination
        for Collection model instances.
        permission_classes (list): List of permission classes required for this view.

    Methods:
        get_queryset: Overrides the `get_queryset` method to filter the queryset based on the user's permissions.
    """
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    pagination_class = CollectionPaginator
    permission_classes = [IsOwner | IsSuperUser]

    def get_queryset(self):
        """
        Overrides the `get_queryset` method to filter the queryset based on the user's permissions.

        If the user is a superuser, it returns all Collection instances. Otherwise, it returns only the Collection
        instances owned by the user.

        Returns:
            QuerySet: The filtered queryset.
        """
        if self.request.user.is_superuser:
            return Collection.objects.all()
        return Collection.objects.filter(owner=self.request.user)


class CollectionRetrieveAPIView(generics.RetrieveAPIView):
    """
    APIView for retrieving a single Collection instance.

    This APIView inherits from `generics.RetrieveAPIView` and is used to retrieve a single instance
    of the Collection model.
    It uses the `CollectionSerializer` for serialization.

    Attributes:
        serializer_class (CollectionSerializer): The serializer class used for the Collection model.
        queryset (QuerySet): The queryset containing all Collection model instances.
        permission_classes (list): List of permission classes required for this view.
    """
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    permission_classes = [IsOwner | IsSuperUser]


class CollectionUpdateAPIView(generics.UpdateAPIView):
    """
    APIView for updating a Collection instance.

    This APIView inherits from `generics.UpdateAPIView` and is used to update an existing instance
    of the Collection model.
    It uses the `CollectionSerializer` for serialization.

    Attributes:
        serializer_class (CollectionSerializer): The serializer class used for the Collection model.
        queryset (QuerySet): The queryset containing all Collection model instances.
        permission_classes (list): List of permission classes required for this view.
    """

    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    permission_classes = [IsOwner | IsSuperUser]


class CollectionDestroyAPIView(generics.DestroyAPIView):
    """
    APIView for deleting a Collection instance.

    This APIView inherits from `generics.DestroyAPIView` and is used to delete an existing instance
    of the `Collection` model.

    Attributes:
        queryset (QuerySet): The queryset containing all Collection model instances.
        permission_classes (list): List of permission classes required for this view.
    """
    queryset = Collection.objects.all()
    permission_classes = [IsOwner | IsSuperUser]
