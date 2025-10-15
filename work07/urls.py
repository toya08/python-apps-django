from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("omikuji/", views.omikuji, name="omikuji"),
    path("omikuji_result/", views.omikuji_result, name="omikuji_result"),
    path("janken/", views.janken, name="janken"),
    path("janken_result/", views.janken_result, name="janken_result"),
    path("hi_low/", views.hi_low, name="hi_low"),
    path("hi_low_result/", views.hi_low_result, name="hi_low_result"),
]
