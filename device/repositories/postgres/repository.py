from typing import Optional
from uuid import UUID

from ...models import Device
from ..interface import IDeviceRepository
from ..mappers import DeviceMapper

__all__ = ("DjangoDeviceRepository",)


class DjangoDeviceRepository(IDeviceRepository):
    def create(self, device: Device) -> UUID:
        try:
            parsed_device = DeviceMapper.from_domain(device=device)
            parsed_device.save()
            return device.id
        except Exception as error:
            print(error)

    def get(self, device_id: UUID) -> Optional[Device]:
        try:
            device = self.__model__.objects.get(id=device_id)
            device = DeviceMapper.to_domain(device_model=device)
            return device or None
        except Exception as error:
            print(error)
