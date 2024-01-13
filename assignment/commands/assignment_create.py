from uuid import uuid4, UUID

from ..models import Assignment
from ..repositories import IAssignmentRepository
from device import IDeviceRepository
from user import IUserRepository


class AssignmentCreateCommand:
    def __init__(
        self,
        assignment_repository: IAssignmentRepository,
        device_repository: IDeviceRepository,
        user_repository: IUserRepository,
    ):
        self.assignment_repository = assignment_repository
        self.device_repository = device_repository
        self.user_repository = user_repository

    def execute(
        self,
        user_email: str,
        device_id: UUID,
    ) -> Assignment:

        user = self.user_repository.get_by_email(user_email=user_email)
        if not user:
            print("User with given email not found #404")
            raise Exception

        device = self.device_repository.get(device_id=device_id)
        if not device:
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


