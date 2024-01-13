from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from ..value_objects import Password

__all__ = ("User",)


@dataclass(frozen=True)
class User:
    id: UUID

    email: str
    password: Password
    first_name: str
    last_name: str

    created_at: datetime
    updated_at: datetime
