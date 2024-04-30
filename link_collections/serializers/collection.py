from rest_framework import serializers

from link_collections.models import Collection
from link_collections.validators import validate_links_owner
from links.models import Link


class CollectionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Collection model.

    This serializer inherits from `serializers.ModelSerializer` and is used to serialize and deserialize instances
    of the `Collection` model.
    It includes custom fields for `links_count` and `links`, and a custom validation method.

    Attributes:
        links_count (IntegerField): A read-only field that represents the count of links in the collection.
        links (PrimaryKeyRelatedField): A field that represents the links in the collection.

    Methods:
        validate: Custom validation method that checks if the links belong to the user.

    Meta:
        model (Collection): The model that this serializer is for.
        fields (tuple): The fields to include in the serialized representation.
        read_only_fields (tuple): The fields that should be read-only.

    Custom Fields:
        links_count: A read-only field that represents the count of links in the collection.
        links: A field that represents the links in the collection.
    """
    links_count = serializers.IntegerField(source='links.all.count', required=False, read_only=True)
    links = serializers.PrimaryKeyRelatedField(many=True, queryset=Link.objects.all(), required=False)

    def validate(self, data):
        if 'links' in data:
            validate_links_owner(data['links'], self.context['request'].user)
        return data

    class Meta:
        model = Collection
        fields = (
            'pk', 'name', 'description', 'links_count', 'links', 'created_at', 'updated_at', 'owner',)
        read_only_fields = ('owner', 'created_at', 'updated_at',)
