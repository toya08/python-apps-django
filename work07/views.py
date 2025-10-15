import random
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, "work07/index.html")


def omikuji(request):
    # ページを表示するだけ（結果はJavaScriptが取得する）
    return render(request, "work07/omikuji.html")


def omikuji_result(request):
    # JavaScriptから呼び出されるエンドポイント
    results = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
    result = random.choice(results)
    return JsonResponse({"result": result})


def janken(request):
    return render(request, "work07/janken.html")


def janken_result(request):
    choices = ["グー", "チョキ", "パー"]
    user_choice = request.GET.get("choice")
    cpu_choice = random.choice(choices)

    if user_choice == cpu_choice:
        result = "あいこ"
    elif (
        (user_choice == "グー" and cpu_choice == "チョキ")
        or (user_choice == "チョキ" and cpu_choice == "パー")
        or (user_choice == "パー" and cpu_choice == "グー")
    ):
        result = "あなたの勝ち"
    else:
        result = "あなたの負け"

    return JsonResponse({"user": user_choice, "cpu": cpu_choice, "result": result})


def hi_low(request):
    # セッションに前回のカードを保存（1〜13の数字）
    if "hi_low_card" not in request.session:
        request.session["hi_low_card"] = random.randint(1, 13)
    return render(request, "work07/hi_low.html")


def hi_low_result(request):
    user_guess = request.GET.get("guess")  # 'hi' or 'low'
    prev_card = int(request.session.get("hi_low_card", 7))
    next_card = random.randint(1, 13)
    request.session["hi_low_card"] = next_card

    if (user_guess == "hi" and next_card > prev_card) or (
        user_guess == "low" and next_card < prev_card
    ):
        result = "正解"
    elif next_card == prev_card:
        result = "同じ"
    else:
        result = "不正解"

    return JsonResponse({"prev": prev_card, "next": next_card, "result": result})
