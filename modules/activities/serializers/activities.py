"""Menus serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from modules.activities.models import Activity
from modules.properties.models import Property

# Serializers
from modules.properties.serializers import PropertySerializer


class GetActivitySerializer(serializers.ModelSerializer):

    property = PropertySerializer(
        read_only=True,
    )

    class Meta:
        model = Activity
        fields = (
            'id',
            'schedule',
            'title',
            'created_at',
            'status',
            'property',
        )


class PostActivitySerializer(serializers.ModelSerializer):

    property = serializers.PrimaryKeyRelatedField(
        queryset=Property.objects.all(),
    )

    class Meta:
        model = Activity
        depth = 1
        fields = (
            'schedule',
            'title',
            'status',
            'property',
        )

    def validate_property(self, property):
        if property.status.lower() != 'active':
            return serializers.ValidationError("The property is deactivate")
        return property
    
    """
    def create(self, validated_data):
        schedule = validated_data['schedule']
        date = schedule.date()
        time = schedule.time()
        property = validated_data['property']
        activities = property.activities.filter(schedule__date=date)
        times = [n_activschedule.time() for]
        print(time)
        activity = Activity.objects.create(**validated_data)
        return activity
    """


class RescheduleActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = (
            'schedule',
        )


class CancelActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = (
            'status',
        )
