from core import StrEnum

__all__ = ("DeviceStatus",)


class DeviceStatus(StrEnum):
    NOT_VERIFIED = "NOT_VERIFIED"
    CONNECTED = "CONNECTED"
    DISCONNECTED = "DISCONNECTED"
