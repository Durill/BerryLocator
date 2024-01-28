from uuid import uuid4, UUID

from core import ResourceNotFound
from ..models import Assignment, AssignmentStatus
from ..repositories import IAssignmentRepository
from device import IDeviceRepository
from user import IUserRepository

__all__ = ("AssignmentCreateCommand",)


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
            raise ResourceNotFound(
                resource_kind="User",
                message="User with given email does not exist"
            )

        device = self.device_repository.get(device_id=device_id)
        if not device:
            raise ResourceNotFound(
                resource_kind="Device",
                resource_id=device_id,
                message="Device with given ID does not exist"
            )

        assignment = Assignment(
            id=uuid4(),
            user=user,
            device=device,
            status=AssignmentStatus.CONNECTED
        )

        self.assignment_repository.create(assignment=assignment)
        return assignment


