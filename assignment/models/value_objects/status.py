from core import StrEnum

__all__ = ("AssignmentStatus",)


class AssignmentStatus(StrEnum):
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
