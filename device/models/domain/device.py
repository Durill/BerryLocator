from datetime import datetime
from uuid import UUID
from dataclasses import dataclass
from ..value_objects import DeviceKind, DeviceStatus


__all__ = ("Device",)


@dataclass(frozen=True)
class Device:
    id: UUID

    name: str
    kind: DeviceKind

    bind_timestamp: datetime
    unbind_timestamp: datetime

    status: DeviceStatus = DeviceStatus.CONNECTED
