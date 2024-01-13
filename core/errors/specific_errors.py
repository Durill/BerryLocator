from .error import ResourceError, Error, ErrorCode
from .codes import ResourceCodes

__all__ = (
    "UnexpectedError",
    "ResourceNotFound",
    "ResourcePermissionDenied",
    "ResourceConflict",
)


class UnexpectedError(Error):
    class Code(ErrorCode):
        SELF = "UNEXPECTED_ERROR"

    INTERNAL_CODE = Code.SELF
    DEFAULT_MESSAGE = "Unexpected error occured"


class ResourceNotFound(ResourceError):
    INTERNAL_CODE = ResourceCodes.NOT_FOUND
    DEFAULT_MESSAGE = "Resource not found"


class ResourcePermissionDenied(ResourceError):
    INTERNAL_CODE = ResourceCodes.PERMISSION_DENIED
    DEFAULT_MESSAGE = "Resource permission denied"


class ResourceConflict(ResourceError):
    INTERNAL_CODE = ResourceCodes.CONFLICT
    DEFAULT_MESSAGE = "Resource conflict"
