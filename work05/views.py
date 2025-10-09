from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    my_name = "toya"
    return render(request, "work05/index.html", {"name": my_name})


def top(request):
    return HttpResponse("Hello, world. You're at the work05 top.")

    return HttpResponse("Hello, world. You're at the work05 index.")


def list(request):
    return HttpResponse("Hello, world. You're at the work05 list.")
