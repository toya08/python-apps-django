from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("income/add/", views.add_income, name="add_income"),  # ←追加
    path("income/delete/<int:income_id>/", views.delete_income, name="delete_income"),
    path("expense/add/", views.add_expense, name="add_expense"),
    path("saving/add/", views.add_saving_goal, name="add_saving_goal"),
]
