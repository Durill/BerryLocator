from uuid import uuid4

from assignment import Assignment, DjangoAssignmentRepository
from device import Device, DjangoDeviceRepository
from user import User, DjangoUserRepository


class AssignmentCreateCommand:
    def __init__(
        self,
        assignment_repository: DjangoAssignmentRepository,
        device_repository: DjangoDeviceRepository,
        user_repository: DjangoUserRepository,
    ):
        self.assignment_repository = assignment_repository
        self.device_repository = device_repository
        self.user_repository = user_repository

    def execute(
        self,
        user: User,
        device: Device,
    ) -> Assignment:

        if not self.user_repository.get_by_email(user_email=user.email):
            print("User with given email not found #404")
            raise Exception

        if not self.device_repository.get(device_id=device.id):
            print("Device with given id not found #404")
            raise Exception

        assignment = Assignment(
            id=uuid4(),
            user=user,
            device=device,
        )

        try:
            self.assignment_repository.create(assignment=assignment)
            return assignment
        except Exception as error:
            print(error)


