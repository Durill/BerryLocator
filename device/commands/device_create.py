from datetime import datetime
from uuid import UUID
from re import match

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
        device_id: str,
        device_name: str,
        device_kind: str,
    ) -> Device:

        uuid_pattern = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
        if not match(uuid_pattern, device_id):
            print("** This shit is not UUID?! **")
            raise Exception

        if self.device_repository.get(device_id=UUID(device_id)) is not None:
            print("This device has already been registered")
            raise Exception

        if device_kind not in DeviceKind.all_values():
            print("** What kind of shit is this? **")

        device = Device(
            id=UUID(device_id),
            name=device_name,
            kind=DeviceKind(device_kind),
            status=DeviceStatus.NOT_VERIFIED,
            bind_timestamp=datetime.now(),
        )

        try:
            self.device_repository.create(device=device)
            return device
        except Exception as error:
            print(error)
