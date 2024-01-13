from uuid import UUID

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from container import container
from core import ResourceNotFound, ResourceConflict
from device import DeviceKind, DeviceCreateCommand
from assignment import AssignmentCreateCommand

__all__ = (
    "register_device",
)


@api_view(http_method_names=['POST'])
def register_device(request):
    device_id = request.data['device_id']
    device_kind = request.data['device_kind']
    device_name = request.data['device_name']
    user_email = request.data['user_email']

    device_repository = container.device_repository

    device = DeviceCreateCommand(device_repository=device_repository)

    assignment = AssignmentCreateCommand(
        assignment_repository=container.assignment_repository,
        device_repository=device_repository,
        user_repository=container.user_repository,
    )

    try:
        device.execute(
            device_id=UUID(device_id),
            device_name=device_name,
            device_kind=DeviceKind(device_kind),
        )
        assignment.execute(
            user_email=user_email,
            device_id=device_id
        )

        return JsonResponse(
            data={
                "status": "Device assigned to User, registered but NOT VERIFIED"
            },
            status=status.HTTP_201_CREATED
        )

    except ResourceNotFound as error:
        return JsonResponse(data=error.as_dict, status=status.HTTP_404_NOT_FOUND)
    except ResourceConflict as error:
        return JsonResponse(data=error.as_dict, status=status.HTTP_409_CONFLICT)
