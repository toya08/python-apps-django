from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from openai import OpenAI
import os


def index(request):
    my_name = "toya"
    return render(request, "work05/index.html", {"name": my_name})


def top(request):
    return HttpResponse("Hello, world. You're at the work05 top.")

    return HttpResponse("Hello, world. You're at the work05 index.")


def list(request):
    return HttpResponse("Hello, world. You're at the work05 list.")


def simple_qa_openai(request):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # query stringから質問を取得
    question = request.GET.get("question", "おすすめのレシピは？")
    prompt = "質問: {question}\n回答:".format(question=question)

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # または "gpt-4o" など
        messages=[{"role": "user", "content": prompt}],
    )
    return HttpResponse(f"<pre>{response.choices[0].message.content}</pre>")