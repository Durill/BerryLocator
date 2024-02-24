from django.contrib.gis.db import models

from berry_site.device.models import DeviceModel


class TripModel(models.Model):
    geometry = models.GeometryField(srid=4326)
    device_id = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField(null=True)
