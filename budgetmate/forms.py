from django import forms
from .models import Income, Expense, SavingGoal


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["date", "source", "amount", "memo"]
        widgets = {
            "amount": forms.NumberInput(
                attrs={
                    "step": 1000,  # 千円単位で増減
                    "min": 0,
                    "id": "income-amount",
                    "placeholder": "例: 10000",
                }
            ),
            "date": forms.DateInput(attrs={"type": "date"}),
            "source": forms.TextInput(attrs={"placeholder": "例: バイト代"}),
            "memo": forms.Textarea(attrs={"rows": 2, "placeholder": "メモ"}),
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
