from django.db import models
from config import settings
from users.models import NULLABLE


class Collection(models.Model):
    """
    Model representing a collection of links.

    Attributes:
        name (CharField): The name of the collection.
        description (TextField): A brief description of the collection.
        created_at (DateTimeField): The date and time when the collection was created.
        updated_at (DateTimeField): The date and time when the collection was last updated.
        owner (ForeignKey): The user who owns the collection.

    Methods:
        __str__: Returns a string representation of the collection.

    Meta:
        verbose_name (str): The singular name of the model used in the admin interface.
        verbose_name_plural (str): The plural name of the model used in the admin interface.
    """
    name = models.CharField(max_length=150, verbose_name='название коллекции')
    description = models.TextField(verbose_name='краткое описание', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата и время обновления')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_collections',
                              verbose_name='владелец коллекции')

    def __str__(self):
        """
        Returns a string representation of the collection.
        """
        return f'{self.name} - {self.owner}'

    class Meta:
        verbose_name = 'коллекция'
        verbose_name_plural = 'коллекции'
