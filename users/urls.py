from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.api_views.user import UserViewSet, ChangePasswordView
from users.apps import UsersConfig

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
                  path('change_password/', ChangePasswordView.as_view(), name='change_password'),
              ] + router.urls
