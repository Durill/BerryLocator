from core import StrEnum

__all__ = ("DeviceStatus",)


class DeviceStatus(StrEnum):
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
