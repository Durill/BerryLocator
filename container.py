from functools import cached_property

from assignment import DjangoAssignmentRepository, IAssignmentRepository
from device import DjangoDeviceRepository, IDeviceRepository
from user import DjangoUserRepository, IUserRepository


class DIContainer:
    # USER
    @cached_property
    def user_repository(self) -> IUserRepository:
        return DjangoUserRepository()

    # DEVICE
    @cached_property
    def device_repository(self) -> IDeviceRepository:
        return DjangoDeviceRepository()

    @cached_property
    def assignment_repository(self) -> IAssignmentRepository:
        return DjangoAssignmentRepository()


container = DIContainer()
