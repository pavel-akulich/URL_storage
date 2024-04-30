from rest_framework import serializers

from links.models import Link
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    password = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data):
        """
        Create and return a new User instance with the validated data.

        Args:
            validated_data (dict): Dictionary containing the validated data.

        Returns:
            User: Newly created User instance.
        """
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Update and return an existing User instance with the validated data.

        Args:
            instance (User): Existing User instance to be updated.
            validated_data (dict): Dictionary containing the validated data.

        Returns:
            User: Updated User instance.
        """
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

    links_count = serializers.IntegerField(source='user_links.all.count', required=False, read_only=True)

    class Meta:
        model = User
        fields = ('pk', 'password', 'email', 'first_name', 'last_name', 'phone', 'country', 'avatar', 'links_count',)


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for changing a user's password.

    This serializer is used to validate the old password and the new password provided by the user.

    Attributes:
        old_password (CharField): The old password of the user.
        new_password (CharField): The new password to be set for the user.

    Methods:
        validate_old_password: Validates the old password by checking if it matches the user's current password.
        validate: Validates the new password.
        save: Saves the new password if the serializer is valid.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
