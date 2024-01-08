from django.urls import path
from .views import index
from .api import health_check, register_device

__all__ = ("urlpatterns",)


urlpatterns = [
    path("", index, name="index"),
    path('api/healthCheck', health_check),
    path('api/registerDevice', register_device)
]
