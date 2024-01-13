from datetime import datetime
from uuid import uuid4

from core import ResourceConflict
from ..models import User, Password
from ..repositories import IUserRepository

__all__ = ("UserCreateCommand",)


class UserCreateCommand:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(
        self,
        email: str,
        password: Password,
        first_name: str,
        last_name: str,
    ) -> User:

        if self.user_repository.get_by_email(user_email=email) is not None:
            raise ResourceConflict(
                resource_kind="User",
                message=f"User with given email: {email} already exist"
            )

        now = datetime.now()
        user = User(
            id=uuid4(),
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            created_at=now,
            updated_at=now,
        )

        self.user_repository.create(user=user)
        return user
