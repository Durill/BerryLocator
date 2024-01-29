from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from berry_site.device.models import DeviceModel
from device import Device

__all__ = ("IDeviceRepository",)


class IDeviceRepository(ABC):
    __model__ = DeviceModel

    @abstractmethod
    def create(self, device: Device) -> UUID:
        raise NotImplementedError

    @abstractmethod
    def get(self, device_id: UUID) -> Optional[Device]:
        raise NotImplementedError
