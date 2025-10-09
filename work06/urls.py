from django.urls import path
from . import views

urlpatterns = [
    path("", views.top_page, name="top_page"),  # トップページ
    path("reiwa/", views.reiwa_view, name="reiwa"),  # 令和何年ですかツール
    path("bmi/", views.bmi, name="bmi"),  # BMI計算ツール
    path("warikan/", views.warikan, name="warikan"),  # 割り勘計算ツール
    path("chokin/", views.chokin, name="chokin"),  # 毎月貯金シミュレーション
    path(
        "calculator/", views.calculator, name="calculator"
    ),  # ２つの数字の四則演算計算機
]
