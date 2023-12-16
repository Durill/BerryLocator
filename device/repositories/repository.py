from typing import Optional
from uuid import UUID

from BerryDjangoSite.models import DeviceModel
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

    def get(self, device_id: UUID) -> Optional[Device]:
        try:
            device = DeviceModel.objects.get(id=device_id)
            device = DeviceMapper.to_domain(device_model=device)
            return device if device else None
        except Exception as error:
            print(error)
