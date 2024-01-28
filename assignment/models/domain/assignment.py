from dataclasses import dataclass
from uuid import UUID

from ..value_objects import AssignmentStatus
from device import Device
from user import User

__all__ = ("Assignment",)


@dataclass(frozen=True)
class Assignment:
    id: UUID
    user: User
    device: Device
    status: AssignmentStatus
