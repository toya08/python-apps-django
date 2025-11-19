from django.shortcuts import render, redirect  # ここがポイント
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
