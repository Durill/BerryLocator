from django.urls import path
from .views import create_device, index
from .api import health_check, register_device

__all__ = ("urlpatterns",)


urlpatterns = [
    path("", index, name="index"),
    path("create-device", create_device, name="create_device"),
    path('api/healthCheck', health_check),
    path('api/registerDevice', register_device)
]
