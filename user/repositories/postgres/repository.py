from typing import Optional
from uuid import UUID

from ...models import User
from ..interface import IUserRepository
from ..mappers import UserMapper

__all__ = ("DjangoUserRepository",)


class DjangoUserRepository(IUserRepository):
    def create(self, user: User) -> UUID:
        try:
            parsed_user = UserMapper.from_domain(user=user)
            parsed_user.save()
            return user.id
        except Exception as error:
            print(f"Repository raised error: {error}")

    def get_by_email(self, user_email: str) -> Optional[User]:
        try:
            user = self.__model__.objects.get(id=user_email)
            user = UserMapper.to_domain(user_model=user)
            return user or None
        except Exception as error:
            print(f"Repository raised error: {error}")
