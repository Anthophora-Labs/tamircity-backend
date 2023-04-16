from django.urls import path
from models.api.views import (
                            ModelCreateAPIView,
                            ModelListAPIView,
                            ModelListByDeviceTypeBrandAPIView,
                        )

app_name = "models"


urlpatterns = [
    path('create', ModelCreateAPIView.as_view(), name='create'),
    path('list', ModelListAPIView.as_view(), name='list'),
    path('device-types/<pk_device_type>/brands/<pk_brand>', ModelListByDeviceTypeBrandAPIView.as_view(), name='list_by_device_type-brand'),
]