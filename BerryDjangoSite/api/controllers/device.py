from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

__all__ = (
    "register_device",
)


@api_view(http_method_names=['POST'])
def register_device(request):
    return JsonResponse(
        data={
            "dataFromYou": {
                "serial_key": request.data['serial_device_id'],
                "email": request.data['user_email']
            }
        },
        status=status.HTTP_201_CREATED
    )
