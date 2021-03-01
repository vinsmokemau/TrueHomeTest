"""Activities views."""

# Utilities
import pytz
from datetime import datetime, timedelta

# Django REST Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Filters
from django_filters.rest_framework import DjangoFilterBackend

# Models
from modules.activities.models import Activity

# Serializers
from modules.activities.serializers import (
    GetActivitySerializer,
    PostActivitySerializer,
)


class ActivityViewset(viewsets.ModelViewSet):
    """Activity viewset."""

    queryset = Activity.objects.all()
    serializer_class = GetActivitySerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostActivitySerializer
        else:
            return GetActivitySerializer

    @action(detail=True, methods=['get'])
    def current_activities(self, request, *args, **kwargs):
        """Retrieve a list of actvities.

        The activities' list includes all activities
        that their schedules are in the range of
        today - 3 days and today + 2 weeks.
        """
        utc_now = pytz.utc.localize(datetime.utcnow())
        mex_now = utc_now.astimezone(pytz.timezone("America/Mexico_City"))
        today, time = mex_now.date(), mex_now.time()
        low_limit = today - timedelta(days=3)
        high_limit = today + timedelta(days=14)
        current_activities = Activity.objects.filter(
            schedule__date__range=(
                low_limit,
                high_limit,
            )
        )
        data = GetActivitySerializer(current_activities, many=True).data
        return Response(data)

    @action(detail=True, methods=['put'])
    def reschedule(self, request, *args, **kwargs):
        activity = self.get_object()
        serializer = RescheduleActivitySerializer(
            activity,
            data=request.data,
        )
        serializer.is_valid(raise_exeption=True)
        serializer.save()
        data = GetActivitySerializer(activity).data
        return Response(data)

    @action(detail=True, methods=['put'])
    def cancel(self, request, *args, **kwargs):
        activity = self.get_object()
        serializer = CancelActivitySerializer(
            activity,
            data=request.data,
        )
        serializer.is_valid(raise_exeption=True)
        serializer.save()
        data = GetActivitySerializer(activity).data
        return Response(data)
