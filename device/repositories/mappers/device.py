from uuid import UUID

from berry_site.device.models import DeviceModel

from ...models import Device, DeviceKind, DeviceStatus

__all__ = ("DeviceMapper",)


class DeviceMapper:
    @classmethod
    def from_domain(cls, device: Device) -> DeviceModel:
        return DeviceModel(
            id=device.id,
            name=device.name,
            kind=device.kind,
            bind_timestamp=device.bind_timestamp,
            unbind_timestamp=device.unbind_timestamp,
            status=device.status,
        )

    @classmethod
    def to_domain(cls, device_model: DeviceModel) -> Device:
        return Device(
            id=UUID(str(device_model.id)),
            name=str(device_model.name),
            kind=DeviceKind(device_model.kind),
            bind_timestamp=device_model.bind_timestamp,
            unbind_timestamp=device_model.unbind_timestamp,
            status=DeviceStatus(device_model.status),
        )
