"""Property models."""

# Django
from django.db import models

# Utilities
from modules.utils.models import BaseModel


class Property(BaseModel):
    """
    Property model.

    A Property is |.
    """

    title = models.CharField(max_length=255)
    address = models.TextField()
    description = models.TextField()
    disabled_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    status = models.CharField(max_length=35)

    def __str__(self):
        return self.title
