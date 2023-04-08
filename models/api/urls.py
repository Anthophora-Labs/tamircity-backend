from django.urls import path
from models.api.views import (
                            ModelCreateAPIView,
                            ModelListAPIView,
                        )

app_name = "models"


urlpatterns = [
    path('create', ModelCreateAPIView.as_view(), name='create'),
    path('list', ModelListAPIView.as_view(), name='list'),
]