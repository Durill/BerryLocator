from django.urls import path

from .views import register_device

urlpatterns = [path("register/", register_device, name="register")]
