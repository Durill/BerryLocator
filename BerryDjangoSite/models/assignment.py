from django.db import models

from BerryDjangoSite.models import UserModel, DeviceModel

__all__ = ("AssignmentModel",)


class AssignmentModel(models.Model):
    id = models.CharField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT)
    device = models.ForeignKey(DeviceModel, on_delete=models.PROTECT)
    status = models.TextField()
