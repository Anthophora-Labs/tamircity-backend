from django.urls import path
from newsletters.api.views import (
                            NewsLetterCreateAPIView,
                            NewsLetterListAPIView,
                        )

app_name = "newsletters"


urlpatterns = [
    path('create', NewsLetterCreateAPIView.as_view(), name='create'),
    path('list', NewsLetterListAPIView.as_view(), name='list'),
]