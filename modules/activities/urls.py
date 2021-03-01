"""activities urls."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework import routers

# Views
from .views import activities as activity_views

app_name = 'activities'

router = routers.DefaultRouter()
router.register(r'activities', activity_views.ActivityViewset, basename='activities')

urlpatterns = [
    path('', include(router.urls)),
    path('current_activities/', activity_views.ActivityViewset.as_view({"get": "current_activities"})),    
]
