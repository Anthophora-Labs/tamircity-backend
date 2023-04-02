from django.urls import path
from comments.api.views import (
                            CommentCreateAPIView,
                            CommentListAPIView,
                            CommentUpdateAPIView
                        )

app_name = "comments"


urlpatterns = [
    path('create', CommentCreateAPIView.as_view(), name='create'),
    path('list', CommentListAPIView.as_view(), name='list'),
    path('update/<pk>', CommentUpdateAPIView.as_view(), name='update'),
]