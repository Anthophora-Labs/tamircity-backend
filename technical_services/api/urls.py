from django.urls import path
from technical_services.api.views import (
                        TechServiceListAPIView,
                        )

app_name = "technical_services"


urlpatterns = [
    path('list', TechServiceListAPIView.as_view(), name='list'),
]