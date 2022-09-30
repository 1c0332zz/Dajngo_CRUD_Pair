from django.urls import path
from . import views

urlpatterns = [
    # - 리뷰 목록 보기
    path("reviews/", views.index, name="index"),
    # - 리뷰 내용 보기
    path("reviews/<int:review_id>", views.detail, name="detail"),
    # - 리뷰 작성 하기
    path("reviews/create", views.create, name="create"),
    # - 리뷰 수정하기
    # - 리뷰 삭제하기
]
