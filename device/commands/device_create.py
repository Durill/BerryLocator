from datetime import datetime
from uuid import UUID

from device import DjangoDeviceRepository, Device, DeviceKind, DeviceStatus

__all__ = ("DeviceCreateCommand",)


class DeviceCreateCommand:
    def __init__(
        self,
        device_repository: DjangoDeviceRepository
    ):
        self.device_repository = device_repository

    def execute(
        self,
        device_id: UUID,
        device_name: str,
        device_kind: DeviceKind,
    ) -> Device:

        if self.device_repository.get(device_id=device_id) is not None:
            print("This device has already been registered")
            raise Exception

        if device_kind not in DeviceKind.all_values():
            print("** What kind of shit is this? **")
            raise Exception

        device = Device(
            id=device_id,
            name=device_name,
            kind=device_kind,
            status=DeviceStatus.NOT_VERIFIED,
            bind_timestamp=datetime.now(),
        )

        try:
            self.device_repository.create(device=device)
            return device
        except Exception as error:
            print(error)
