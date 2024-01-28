from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..value_objects import DeviceKind, DeviceStatus

__all__ = ("Device",)


@dataclass(frozen=True)
class Device:
    id: UUID

    name: str
    kind: DeviceKind

    status: DeviceStatus

    bind_timestamp: datetime
    unbind_timestamp: Optional[datetime] = None
