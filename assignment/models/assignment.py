from dataclasses import dataclass
from uuid import UUID

from device import Device
from user import User

__all__ = ("Assignment",)


@dataclass(frozen=True)
class Assignment:
    id: UUID
    user: User
    device: Device
