from __future__ import annotations

from typing import Dict, Optional
from uuid import UUID

from core import StrEnum


class Error(Exception):
    """
    ONLY for inheritance
    """

    INTERNAL_CODE: ErrorCode
    DEFAULT_MESSAGE: str

    _message: Optional[str]

    def __init__(
        self,
        message: Optional[str] = None,
    ) -> None:
        self._message = str(message) if message not in ("", None) else None

    def __str__(self) -> str:
        return f"""
            \n
            CODE: {self.INTERNAL_CODE},
            MESSAGE: {self._message},
        """

    @property
    def as_dict(self) -> Dict:
        return {
            "code": self.INTERNAL_CODE.value,
            "message": self._message,
        }

    @property
    def message(self) -> str:
        return self._message if self._message is not None else self.DEFAULT_MESSAGE


class ErrorCode(StrEnum):
    """
    ONLY for type checking
    """


class RepositoryError(Error):
    class Code(ErrorCode):
        SELF = "REPOSITORY_ERROR"

    INTERNAL_CODE = Code.SELF
    DEFAULT_MESSAGE = "Repository error"


class ResourceError(Error):
    class Code(ErrorCode):
        SELF = "RESOURCE_ERROR"

    INTERNAL_CODE = Code.SELF
    DEFAULT_MESSAGE = "Resource error"

    def __init__(
        self,
        resource_kind: str,
        resource_id: Optional[UUID] = None,
        message: Optional[str] = None,
    ) -> None:
        self.resource_kind = resource_kind
        self.resource_id = resource_id
        super().__init__(message=message)

    def __str__(self) -> str:
        return f"""
            CODE: {self.INTERNAL_CODE.value},
            KIND: {self.resource_kind},
            ID: {self.resource_id},
            MESSAGE: {self.message}
        """

    @property
    def as_dict(self) -> Dict:
        return {
            "code": self.INTERNAL_CODE.value,
            "kind": self.resource_kind,
            "id": str(self.resource_id),
            "message": self._message,
        }
