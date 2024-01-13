from django.http import HttpResponse
from django.shortcuts import render


__all__ = (
    "index",
)


def index(request):
    return render(request=request, template_name="home.html")


def create_user(request):
    pass
