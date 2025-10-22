from django.shortcuts import render, get_object_or_404, redirect
from .models import Memo
from .forms import MemoForm


# 一覧ページ
def index(request):
    memos = Memo.objects.all().order_by("-updated_at")
    return render(request, "work08/index.html", {"memos": memos})


# 新規作成ボタンを押したとき
def create_memo(request):
    memo = Memo.objects.create(title="no title")  # デフォルトタイトルで作成
    return redirect("edit_memo", memo_id=memo.id)  # 作成後に編集画面へリダイレクト


# 編集画面
def edit_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)

    if request.method == "POST":
        form = MemoForm(request.POST, request.FILES, instance=memo)  # 画像も受け取る
        if form.is_valid():
            form.save()
            return redirect("index")  # 保存後は一覧ページへ戻る
    else:
        form = MemoForm(instance=memo)

    # memo もテンプレートに渡す
    return render(request, "work08/edit_memo.html", {"form": form, "memo": memo})


def delete_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()
    return redirect("index")
