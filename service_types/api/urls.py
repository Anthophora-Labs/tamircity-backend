from django.urls import path
from service_types.api.views import (
                            ServiceTypeCreateAPIView,
                            ServiceTypeListAPIView,
                        )

app_name = "service_types"


urlpatterns = [
    path('create', ServiceTypeCreateAPIView.as_view(), name='create'),
    path('list', ServiceTypeListAPIView.as_view(), name='list'),
]