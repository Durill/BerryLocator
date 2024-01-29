from core import StrEnum

__all__ = ("DeviceKind",)


class DeviceKind(StrEnum):
    RASPBERRY_PI_3 = "Raspberry Pi 3"
    RASPBERRY_PI_4 = "Raspberry Pi 4"
