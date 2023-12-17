import re
from uuid import UUID

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

__all__ = (
    "register_device",
)

from device import DeviceKind, DeviceCreateCommand, DjangoDeviceRepository


@api_view(http_method_names=['POST'])
def register_device(request):
    device_id = request.data['device_id']
    device_kind = request.data['device_kind']
    device_name = request.data['device_name']
    user_email = request.data['user_email']

    # TODO: @WojciechBatorski here You have to parse this to value objects
    device = DeviceCreateCommand(device_repository=DjangoDeviceRepository())

    try:
        device.execute(
            device_id=UUID(device_id),
            device_name=device_name,
            device_kind=DeviceKind(device_kind),
        )

        return JsonResponse(
            data={
                "status": "Device assigned to User, registered but NOT VERIFIED"
            },
            status=status.HTTP_201_CREATED
        )
    except Exception as error:
        print(error)
