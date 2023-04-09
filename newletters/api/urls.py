from django.urls import path
from newletters.api.views import (
                            NewLetterCreateAPIView,
                            NewLetterListAPIView,
                        )

app_name = "newletters"


urlpatterns = [
    path('create', NewLetterCreateAPIView.as_view(), name='create'),
    path('list', NewLetterListAPIView.as_view(), name='list'),
]