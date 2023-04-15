from django.urls import path
from brands.api.views import (
                            BrandCreateAPIView,
                            BrandListAPIView,
                            BrandListByDeviceTypeAPIView,
                        )

app_name = "brands"


urlpatterns = [
    path('create', BrandCreateAPIView.as_view(), name='create'),
    path('list', BrandListAPIView.as_view(), name='list'),
    path('device-types/<pk>', BrandListByDeviceTypeAPIView.as_view(), name='list_by_device_type'),
]