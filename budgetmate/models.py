from django.db import models
from django.utils import timezone


class Income(models.Model):
    date = models.DateField(default=timezone.now)
    amount = models.PositiveIntegerField()
    source = models.CharField(max_length=100, verbose_name="収入の種類（例: バイト代）")
    memo = models.TextField(blank=True, verbose_name="メモ")

    def __str__(self):
        return f"{self.date} - {self.source}（{self.amount}円）"


class Expense(models.Model):
    date = models.DateField(default=timezone.now)
    amount = models.PositiveIntegerField()
    category = models.CharField(
        max_length=100, verbose_name="カテゴリ（例: 食費・趣味）"
    )
    memo = models.TextField(blank=True, verbose_name="メモ")

    def __str__(self):
        return f"{self.date} - {self.category}（{self.amount}円）"


class SavingGoal(models.Model):
    goal_name = models.CharField(max_length=100, verbose_name="目標名（例: 新しいPC）")
    target_amount = models.PositiveIntegerField(verbose_name="目標金額")
    target_date = models.DateField(verbose_name="目標日")
    created_at = models.DateTimeField(auto_now_add=True)

    def monthly_saving(self):
        """残り期間から1ヶ月あたりの貯金目安を出す"""
        today = timezone.now().date()
        months_left = max(
            (self.target_date.year - today.year) * 12
            + (self.target_date.month - today.month),
            1,
        )
        return self.target_amount // months_left

    def __str__(self):
        return (
            f"{self.goal_name} - 目標 {self.target_amount}円（{self.target_date}まで）"
        )
