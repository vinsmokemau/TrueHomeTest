"""Survey models."""

# Django
from django.db import models

# Utilities
from modules.utils.models import BaseModel


class Survey(BaseModel):
    """
    Survey model.

    A Survey is |.
    """

    activity = models.OneToOneField(
        'activities.Activity',
        related_name='survey',
        on_delete=models.CASCADE,
    )
    answers = models.JSONField()
