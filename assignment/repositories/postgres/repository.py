from typing import Optional
from uuid import UUID

from assignment import IAssignmentRepository, Assignment, AssignmentMapper

__all__ = ("DjangoAssignmentRepository",)


class DjangoAssignmentRepository(IAssignmentRepository):

    def create(self, assignment: Assignment) -> UUID:
        try:
            parsed_assignment = AssignmentMapper.from_domain(assignment=assignment)
            parsed_assignment.save()
            return assignment.id
        except Exception as error:
            print(f"Repository raised error: {error}")

    def get(self, assignment_id: UUID) -> Optional[Assignment]:
        try:
            assignment = self.__model__.objects.get(id=assignment_id)
            assignment = AssignmentMapper.to_domain(assignment_model=assignment)
            return assignment if assignment else None
        except Exception as error:
            print(f"Repository raised error: {error}")
