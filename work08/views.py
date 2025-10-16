from django.shortcuts import render, redirect
from .models import Memo
from .forms import MemoForm


# Create your views here.
def index(request):
    memos = Memo.objects.all().order_by("-updated_at")
    return render(request, "work08/index.html", {"memos": memos})


def add_memo(request):
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = MemoForm()

    # ここで必ず render を返す
    return render(request, "work08/add_memo.html", {"form": form})
