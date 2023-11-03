from uuid import UUID

from ..models import Device
from .mappers import DeviceMapper


__all__ = ("DjangoDeviceRepository",)


class DjangoDeviceRepository:

    def create(self, device: Device) -> UUID:
        try:
            parsed_device = DeviceMapper.from_domain(device=device)
            parsed_device.save()
            return device.id
        except Exception as error:
            print(error)
