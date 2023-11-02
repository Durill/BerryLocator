from uuid import UUID

from BerryDjangoSite.models import DeviceModel


__all__ = ("DjangoDeviceRepository",)


class DjangoDeviceRepository:

    def create(self, device: DeviceModel) -> UUID:
        try:
            device.save()
            return device.id
        except Exception as error:
            print(error)
