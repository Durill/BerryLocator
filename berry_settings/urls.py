from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("berry_site.core.urls", "core"), namespace="core")),
    path("api/", include(("berry_site.api.urls", "api"), namespace="api")),
    path("device/", include(("berry_site.device.urls", "device"), namespace="device")),
    path("user/", include(("berry_site.user.urls", "user"), namespace="user")),
]
