from django.http import HttpResponse


def top(request):
    return HttpResponse("Hello, world. You're at the work05 top.")


def index(request):
    return HttpResponse("Hello, world. You're at the work05 index.xxxxxxxx")


def list(request):
    return HttpResponse("Hello, world. You're at the work05 list.")
