from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # 収入（追加・編集・削除）
    path("income/add/", views.add_income, name="add_income"),
    path("income/edit/<int:income_id>/", views.edit_income, name="edit_income"),
    path("income/delete/<int:income_id>/", views.delete_income, name="delete_income"),
    # 支出（追加・編集・削除）
    path("expense/add/", views.add_expense, name="add_expense"),
    path("expense/edit/<int:expense_id>/", views.edit_expense, name="edit_expense"),
    path(
        "expense/delete/<int:expense_id>/", views.delete_expense, name="delete_expense"
    ),
    # 貯金目標（追加・編集・削除）
    path("saving/add/", views.add_saving_goal, name="add_saving_goal"),
    path("saving/edit/<int:goal_id>/", views.edit_saving_goal, name="edit_saving_goal"),
    path(
        "saving/delete/<int:goal_id>/",
        views.delete_saving_goal,
        name="delete_saving_goal",
    ),
]
