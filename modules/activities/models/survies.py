"""Survey models."""

# Django
from django.db import models

# Utilities
from modules.utils.models import BaseModel


class Survey(models.Model):
    """
    Survey model.

    A Survey is |.
    """

    activity_id = models.OneToOneField(
        'activities.Activity',
        related_name='survey',
        on_delete=models.CASCADE,
    )
