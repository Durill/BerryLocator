from datetime import datetime
from uuid import uuid4

from device import DjangoDeviceRepository, Device, DeviceKind

__all__ = ("DeviceCreateCommand",)


class DeviceCreateCommand:
    def __init__(
        self,
        device_repository: DjangoDeviceRepository
    ):
        self.device_repository = device_repository

    def execute(self, device_name: str, device_kind: DeviceKind) -> Device:
        device = Device(
            id=uuid4(),
            name=device_name,
            kind=device_kind.value,
            bind_timestamp=datetime.now(),
            unbind_timestamp=datetime.now(),
        )

        try:
            self.device_repository.create(device=device)
            return device
        except Exception as error:
            print(error)
