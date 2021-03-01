"""Menus serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from modules.properties.models import Property


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'address',
        )
