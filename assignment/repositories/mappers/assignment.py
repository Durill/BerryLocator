from uuid import UUID

from BerryDjangoSite.models.assignment import AssignmentModel
from ...models import Assignment
from device import DeviceMapper
from user import UserMapper

__all__ = ("AssignmentMapper",)


class AssignmentMapper:
    @classmethod
    def from_domain(cls, assignment: Assignment) -> AssignmentModel:
        return AssignmentModel(
            id=assignment.id,
            user=UserMapper.from_domain(user=assignment.user),
            device=DeviceMapper.from_domain(device=assignment.device),
        )

    @classmethod
    def to_domain(cls, assignment_model: AssignmentModel) -> Assignment:
        return Assignment(
            id=UUID(assignment_model.id),
            user=UserMapper.to_domain(user_model=assignment_model.user),
            device=DeviceMapper.to_domain(device_model=assignment_model.device),
        )
