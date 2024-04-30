from rest_framework import serializers


def validate_links_owner(links, owner):
    """
    Validate that all links belong to the specified owner.

    This function is used to validate that all links in the provided list are owned by the specified user.
    If any link does not belong to the user, a `serializers.ValidationError` is raised.

    Args:
        links (list): A list of Link instances.
        owner (User): The user instance to check against.

    Raises:
        serializers.ValidationError: If any link in the list does not belong to the specified owner.
    """
    for link in links:
        if link.owner != owner:
            raise serializers.ValidationError("Вы не можете добавлять свои ссылки в чужие коллекции.")
