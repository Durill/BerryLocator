from django.db import models

from berry_site.device.models import DeviceModel
from berry_site.user.models import UserModel

__all__ = ("AssignmentModel",)


class AssignmentModel(models.Model):
    id = models.CharField(primary_key=True)
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT)
    device = models.ForeignKey(DeviceModel, on_delete=models.PROTECT)
    status = models.TextField()
