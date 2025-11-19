from django import forms
from .models import Income, Expense, SavingGoal


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["date", "amount", "source", "memo"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "amount": forms.NumberInput(attrs={"min": 0}),
            "source": forms.TextInput(attrs={"placeholder": "例: バイト代"}),
            "memo": forms.Textarea(attrs={"rows": 2}),
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["date", "amount", "category", "memo"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "memo": forms.Textarea(attrs={"rows": 3}),
        }


class SavingGoalForm(forms.ModelForm):
    class Meta:
        model = SavingGoal
        fields = ["goal_name", "target_amount", "target_date"]
        widgets = {
            "target_date": forms.DateInput(attrs={"type": "date"}),
        }
