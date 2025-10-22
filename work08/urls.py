from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 既存の path()
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.create_memo, name="create_memo"),
    path("edit/<int:memo_id>/", views.edit_memo, name="edit_memo"),
    path("delete/<int:memo_id>/", views.delete_memo, name="delete_memo"),
]
