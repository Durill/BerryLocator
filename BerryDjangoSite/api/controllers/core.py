from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view


__all__ = (
    "health_check",
)


@api_view(http_method_names=['GET'])
def health_check(*args, **kwargs):
    return JsonResponse(
        data={"status": "Server ACTIVE and ready to action!"},
        status=status.HTTP_200_OK
    )
