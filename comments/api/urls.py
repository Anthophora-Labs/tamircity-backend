from django.urls import path
from comments.api.views import (
                            CommentCreateAPIView,
                            CommentListAPIView,
                            CommentUpdateAPIView,
                            CommentDeleteAPIView,
                            CommentUpdateDeleteAPIView
                        )

app_name = "comments"


urlpatterns = [
    path('create', CommentCreateAPIView.as_view(), name='create'),
    path('list', CommentListAPIView.as_view(), name='list'),
    path('update/<pk>', CommentUpdateAPIView.as_view(), name='update'),
    path('delete/<pk>', CommentDeleteAPIView.as_view(), name='delete'),
    path('update-delete/<pk>', CommentUpdateDeleteAPIView.as_view(), name='update_delete'),
]