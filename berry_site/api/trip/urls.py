from django.urls import path

from .views import register_trip

urlpatterns = [path("register/", register_trip, name="register")]
