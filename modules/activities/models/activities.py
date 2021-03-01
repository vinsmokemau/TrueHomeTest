"""Activity models."""

# Django
from django.db import models

# Utilities
from modules.utils.models import BaseModel


class Activity(BaseModel):
    """
    Activity model.

    A Activity is |.
    """

    property = models.ForeignKey(
        'properties.Property',
        related_name='activities',
        on_delete=models.CASCADE,
    )
    schedule = models.DateTimeField()
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=35)

    def __str__(self):
        return self.title
