from __future__ import annotations

from django.db import models


__all__ = (
    "DeviceModel",
)


class DeviceModel(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=255)
    bind_timestamp = models.DateTimeField()
    unbind_timestamp = models.DateTimeField(null=True)
    # created_at = models.DateTimeField()
    # updated_at = models.DateTimeField()
    status = models.TextField()

#
# class DeviceTemporary(models.Model):
#     id = models.CharField(primary_key=True)
#     kind = models.CharField(max_length=255)
#     email = models.CharField(max_length=100)
#     expiration_date = models.DateTimeField()
