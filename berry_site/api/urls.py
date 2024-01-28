from django.urls import include, path

urlpatterns = [
    path('', include(("berry_site.api.core.urls", 'core'))),
    path('device/', include(("berry_site.api.device.urls", 'device'))),
]
