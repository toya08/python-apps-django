from django.shortcuts import render
from .forms import ReiwaForm
from .forms import BMIForm
from .forms import WarikanForm
from .forms import ChokinForm
from .forms import CalculatorForm


def top_page(request):
    # 計算ツールのリストを作る
    tools = [
        {"name": "令和何年ですかツール", "url": "reiwa/"},
        {"name": "BMIを計算してくれるくん", "url": "bmi/"},
        {"name": "割り勘の金額を計算してくれるくん", "url": "warikan/"},
        {"name": "毎月貯金シミュレーション", "url": "chokin/"},
        {"name": "２つの数字の四則演算計算機", "url": "calculator/"},
        # 他のツールがあれば追加可能
    ]
    return render(request, "work06/top_page.html", {"tools": tools})


def reiwa_view(request):
    result = None
    reiwa_year = None
    if request.method == "POST":
        form = ReiwaForm(request.POST)
        if form.is_valid():
            reiwa_year = form.cleaned_data["reiwa_year"]
            seireki = 2018 + reiwa_year  # 令和1年=2019年
            result = f"令和{reiwa_year}年 → 西暦{seireki}年"
    else:
        form = ReiwaForm()
    return render(request, "work06/reiwa.html", {"form": form, "result": result})


def bmi(request):
    result = None
    if request.method == "POST":
        form = BMIForm(request.POST)
        if form.is_valid():
            height_cm = form.cleaned_data["height"]
            weight_kg = form.cleaned_data["weight"]
            height_m = height_cm / 100  # cm → m
            bmi_value = weight_kg / (height_m**2)
            result = (
                f"身長 {height_cm}cm、体重 {weight_kg}kg の BMI は {bmi_value:.2f} です"
            )
    else:
        form = BMIForm()
    return render(request, "work06/bmi.html", {"form": form, "result": result})


def warikan(request):
    result = None
    if request.method == "POST":
        form = WarikanForm(request.POST)
        if form.is_valid():
            total = form.cleaned_data["total"]
            people = form.cleaned_data["people"]
            pay = total // people
            remainder = total % people
            result = f"1人あたり {pay} 円です（端数 {remainder} 円）"
    else:
        form = WarikanForm()
    return render(request, "work06/warikan.html", {"form": form, "result": result})


def chokin(request):
    result = None
    if request.method == "POST":
        form = ChokinForm(request.POST)
        if form.is_valid():
            monthly_saving = form.cleaned_data["monthly_saving"]
            years = form.cleaned_data["years"]

            total_months = years * 12
            total = monthly_saving * total_months
            result = f"毎月{monthly_saving:,}円を{years}年間貯金すると、合計{total:,}円になります。"
    else:
        form = ChokinForm()
    return render(request, "work06/chokin.html", {"form": form, "result": result})


def calculator(request):
    result = None
    error = None
    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data["num1"]
            num2 = form.cleaned_data["num2"]
            operator = form.cleaned_data["operator"]

            try:
                if operator == "+":
                    result = num1 + num2
                elif operator == "-":
                    result = num1 - num2
                elif operator == "*":
                    result = num1 * num2
                elif operator == "/":
                    if num2 == 0:
                        error = "0で割ることはできません。"
                    else:
                        result = num1 / num2
            except Exception as e:
                error = f"エラーが発生しました: {e}"
    else:
        form = CalculatorForm()

    return render(
        request,
        "work06/calculator.html",
        {"form": form, "result": result, "error": error},
    )
