from django.http import HttpResponse
from django.shortcuts import render

from device import DeviceKind, DjangoDeviceRepository, DeviceCreateCommand

__all__ = (
    "index",
    "create_device",
)


def index(request):
    return render(request=request, template_name="home.html")


def create_device(request):
    if request.method == 'POST':
        device_name = request.POST.get('name')
        device_kind = DeviceKind(request.POST.get('kind'))

        device = (DeviceCreateCommand(device_repository=DjangoDeviceRepository())
                  .execute(device_name=device_name, device_kind=device_kind))
        return HttpResponse(f"{device.kind} {device.name} got status {device.status.value}")
    else:
        return HttpResponse(f"Nothing to show here")
