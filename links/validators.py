from rest_framework import serializers
from links.models import Link


def unique_url_validator(value, serializer):
    """
    Validate that the provided URL is unique for the user who is creating the link.

    This function is used to validate that the provided URL does not already exist in the user's links.
    If the URL already exists, a `serializers.ValidationError` is raised.

    Args:
        value (str): The URL value to validate.
        serializer (serializers.ModelSerializer): The serializer instance that is calling this validator.

    Raises:
        serializers.ValidationError: If the URL already exists for the user.

    Returns:
        str: The validated URL.
    """
    user = serializer.context['request'].user
    if Link.objects.filter(url=value, owner=user).exists():
        raise serializers.ValidationError("У вас уже есть ссылка с этим URL.")
    return value
