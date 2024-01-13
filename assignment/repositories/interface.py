from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from BerryDjangoSite.models.assignment import AssignmentModel
from ..models import Assignment

__all__ = ("IAssignmentRepository",)


class IAssignmentRepository(ABC):
    __model__ = AssignmentModel

    @abstractmethod
    def create(self, assignment: Assignment) -> UUID:
        raise NotImplementedError

    @abstractmethod
    def get(self, assignment_id: UUID) -> Optional[Assignment]:
        raise NotImplementedError
