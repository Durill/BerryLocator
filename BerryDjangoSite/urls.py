from django.urls import path
from .views import create_device, index

__all__ = ("urlpatterns",)


urlpatterns = [
    path("", index, name="index"),
    path("create-device", create_device, name="create_device")
]
