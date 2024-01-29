from datetime import datetime
from uuid import UUID

from core import ResourceConflict, ResourceNotFound

from ..models import Device, DeviceKind
from ..repositories import IDeviceRepository

__all__ = ("DeviceCreateCommand",)


class DeviceCreateCommand:
    def __init__(self, device_repository: IDeviceRepository):
        self.device_repository = device_repository

    def execute(
        self,
        device_id: UUID,
        device_name: str,
        device_kind: DeviceKind,
    ) -> Device:
        if self.device_repository.get(device_id=device_id) is not None:
            raise ResourceConflict(
                resource_kind="Device",
                resource_id=device_id,
                message="Device with given ID has been already registered",
            )

        if device_kind not in DeviceKind.all_values():
            raise ResourceNotFound(
                resource_kind="DeviceKind", message="There is no such kind of device in our system"
            )

        device = Device(
            id=device_id,
            name=device_name,
            kind=device_kind,
            bind_timestamp=datetime.now(),
        )

        self.device_repository.create(device=device)
        return device
