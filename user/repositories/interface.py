from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from BerryDjangoSite.models import UserModel
from user import User

__all__ = ("IUserRepository",)


class IUserRepository(ABC):
    __model__ = UserModel

    @abstractmethod
    def create(self, user: User) -> UUID:
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, user_email: str) -> Optional[User]:
        raise NotImplementedError
