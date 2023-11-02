from uuid import UUID

from django.db import models

# from device import Device, DeviceStatus, DeviceKind


class DeviceModel(models.Model):
    id = models.CharField()
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=255)
    bind_timestamp = models.DateTimeField()
    unbind_timestamp = models.DateTimeField()
    status = models.TextField()

    # def to_domain(self) -> Device:
    #     return Device(
    #         id=UUID(str(self.id)),
    #         name=str(self.name),
    #         kind=DeviceKind(self.kind),
    #         bind_timestamp=self.bind_timestamp,
    #         unbind_timestamp=self.unbind_timestamp,
    #         status=DeviceStatus(self.status),
    #     )
