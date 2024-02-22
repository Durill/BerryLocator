from django.urls import path

from .views import register_trip, show_map

urlpatterns = [
    path("register/", register_trip, name="register"),
    path("show_map/", show_map, name="show_map")
]
