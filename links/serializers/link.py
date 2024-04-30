from rest_framework import serializers

from links.models import Link
from links.validators import unique_url_validator


class LinkSerializer(serializers.ModelSerializer):
    """
    Serializer for the Link model.

    This serializer inherits from `serializers.ModelSerializer` and is used to serialize and deserialize instances
    of the `Link` model.
    It includes a custom validation method for the `url` field.

    Attributes:
        Meta: A nested class that defines metadata for the serializer.

    Methods:
        validate_url: Custom validation method for the `url` field.

    Meta:
        model (Link): The model that this serializer is for.
        fields (tuple): The fields to include in the serialized representation.
        read_only_fields (tuple): The fields that should be read-only.
    """

    def validate_url(self, value):
        """
        Custom validation method for the `url` field.

        This method calls the `unique_url_validator` function to validate the uniqueness of the URL.

        Args:
            value (str): The URL value to validate.

        Returns:
            str: The validated URL.
        """
        return unique_url_validator(value, self)

    class Meta:
        model = Link
        fields = (
            'pk', 'title', 'description', 'url', 'preview', 'type', 'created_at', 'updated_at', 'collection', 'owner',)
        read_only_fields = ('owner', 'created_at', 'updated_at',)
