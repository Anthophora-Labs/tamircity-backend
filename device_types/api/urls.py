from django.urls import path
from device_types.api.views import (
                            DeviceTypeCreateAPIView,
                            DeviceTypeListAPIView,
                        )

app_name = "device_types"


urlpatterns = [
    path('create', DeviceTypeCreateAPIView.as_view(), name='create'),
    path('list', DeviceTypeListAPIView.as_view(), name='list'),
]