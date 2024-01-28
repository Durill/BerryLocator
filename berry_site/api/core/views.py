from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView


class HealthCheck(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(
            data={"status": "Server ACTIVE and ready to action!"}, status=status.HTTP_200_OK
        )
