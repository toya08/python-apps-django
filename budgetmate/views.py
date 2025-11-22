from django.shortcuts import render, redirect, get_object_or_404  # ここがポイント
from .models import Income, Expense, SavingGoal
from .forms import IncomeForm, ExpenseForm, SavingGoalForm


def dashboard(request):
    # 全データ取得
    incomes = Income.objects.all()
    expenses = Expense.objects.all()
    goals = SavingGoal.objects.all()

    # コンテキストを作成（テンプレートに渡すデータ）
    context = {
        "incomes": incomes,
        "expenses": expenses,
        "goals": goals,
    }

    # dashboard.html をレンダリングして返す
    return render(request, "budgetmate/dashboard.html", context)


def add_income(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = IncomeForm()
    return render(request, "budgetmate/add_income.html", {"form": form})


def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")  # 保存後はダッシュボードに戻る
    else:
        form = ExpenseForm()
    return render(request, "budgetmate/add_expense.html", {"form": form})


def add_saving_goal(request):
    if request.method == "POST":
        form = SavingGoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")  # 保存後はダッシュボードに戻る
    else:
        form = SavingGoalForm()
    return render(request, "budgetmate/add_saving_goal.html", {"form": form})


# 収入削除
def delete_income(request, income_id):
    income = get_object_or_404(Income, id=income_id)
    income.delete()
    return redirect("dashboard")


# 支出削除
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expense.delete()
    return redirect("dashboard")


# 貯金目標削除
def delete_saving_goal(request, goal_id):
    goal = get_object_or_404(SavingGoal, id=goal_id)
    goal.delete()
    return redirect("dashboard")


# 　収入編集
def edit_income(request, income_id):
    income = get_object_or_404(Income, id=income_id)

    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = IncomeForm(instance=income)

    return render(request, "budgetmate/edit_income.html", {"form": form})


# 支出編集
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = ExpenseForm(instance=expense)
    return render(request, "budgetmate/edit_expense.html", {"form": form})


# 貯金目標編集
def edit_saving_goal(request, goal_id):
    goal = get_object_or_404(SavingGoal, id=goal_id)
    if request.method == "POST":
        form = SavingGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = SavingGoalForm(instance=goal)
    return render(request, "budgetmate/edit_saving_goal.html", {"form": form})
