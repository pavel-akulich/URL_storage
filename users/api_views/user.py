from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.paginators import UserPaginator
from users.permissions import IsOwner, IsSuperUser
from users.serializers.user import UserSerializer, ChangePasswordSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import update_session_auth_hash


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for interacting with User model.

    This ViewSet provides CRUD operations for User model. It uses the `UserSerializer` for
    serialization and the `UserPaginator` for pagination.

    Attributes:
        serializer_class (UserSerializer): The serializer class used for User model.
        queryset (QuerySet): The queryset containing all User model instances.
        pagination_class (UserPaginator): The pagination class used to handle pagination for User model instances.

    Methods:
        get_permissions: Returns the permissions required for each action.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = UserPaginator

    def get_permissions(self):
        """
        Method to return the permissions required for each action.

        Returns:
            list: List of permission classes.
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated & IsSuperUser]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated & IsOwner]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated & IsSuperUser | IsOwner]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated & IsOwner | IsSuperUser]
        else:
            permission_classes = [IsAuthenticated & IsSuperUser]
        return [permission() for permission in permission_classes]


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    """
    Handles POST requests to change the password.

    This method validates the `ChangePasswordSerializer` with the incoming data. If the
    serializer is valid and the old password matches the user's current password, the
    new password is set and the session authentication hash is updated.

    Args:
        request (Request): The incoming request.

    Returns:
        Response: A response indicating success or failure with appropriate status code.
    """

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.validated_data.get('old_password')):
                user.set_password(serializer.validated_data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)
                return Response({'message': 'Пароль успешно изменен.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Неверный старый пароль.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
