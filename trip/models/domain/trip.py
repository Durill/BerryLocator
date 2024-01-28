from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from device import Device

__all__ = ("Trip",)


@dataclass(frozen=True)
class Trip:
    id: UUID
    geometry: Geometry
    device: Device
    started_at: datetime
    finished_at: Optional[datetime] = None
