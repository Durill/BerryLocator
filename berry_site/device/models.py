from __future__ import annotations

from django.db import models

__all__ = ("DeviceModel",)


class DeviceModel(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=255)
    bind_timestamp = models.DateTimeField()
    unbind_timestamp = models.DateTimeField(null=True)
