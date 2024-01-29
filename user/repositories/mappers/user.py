from berry_site.user.models import UserModel
from user import User

__all__ = ("UserMapper",)


class UserMapper:
    @classmethod
    def from_domain(cls, user: User) -> UserModel:
        return UserModel(
            id=user.id,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    @classmethod
    def to_domain(cls, user_model: UserModel) -> User:
        return User(
            id=user_model.id,
            email=user_model.email,
            password=user_model.password,
            first_name=user_model.first_name,
            last_name=user_model.last_name,
            created_at=user_model.created_at,
            updated_at=user_model.updated_at,
        )
