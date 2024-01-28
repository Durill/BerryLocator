from django.db import models

from BerryDjangoSite.models import DeviceModel


class TripModel(models.Model):
    geometry = models.TextField()
    device_id = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField(null=True)
