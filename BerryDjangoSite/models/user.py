from __future__ import annotations

from django.db import models

__all__ = (
    "UserModel",
)


class UserModel(models.Model):
    id = models.CharField(primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
