from .error import ErrorCode


class ResourceCodes(ErrorCode):
    NOT_FOUND = "RESOURCE_NOT_FOUND"
    PERMISSION_DENIED = "RESOURCE_PERMISSION_DENIED"
    CONFLICT = "RESOURCE_CONFLICT"
