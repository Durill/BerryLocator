from django.urls import path

from .views import HealthCheck

urlpatterns = [path("health-check/", HealthCheck.as_view(), name="health_check")]
