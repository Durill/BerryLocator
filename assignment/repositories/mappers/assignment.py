from uuid import UUID

from berry_site.assignment.models import AssignmentModel
from device import DeviceMapper
from user import UserMapper

from ...models import Assignment, AssignmentStatus

__all__ = ("AssignmentMapper",)


class AssignmentMapper:
    @classmethod
    def from_domain(cls, assignment: Assignment) -> AssignmentModel:
        return AssignmentModel(
            id=assignment.id,
            user=UserMapper.from_domain(user=assignment.user),
            device=DeviceMapper.from_domain(device=assignment.device),
            status=assignment.status,
        )

    @classmethod
    def to_domain(cls, assignment_model: AssignmentModel) -> Assignment:
        return Assignment(
            id=UUID(assignment_model.id),
            user=UserMapper.to_domain(user_model=assignment_model.user),
            device=DeviceMapper.to_domain(device_model=assignment_model.device),
            status=AssignmentStatus(assignment_model.status)
        )
