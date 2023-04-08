from django.urls import path
from brands.api.views import (
                            BrandCreateAPIView,
                            BrandListAPIView,
                        )

app_name = "brands"


urlpatterns = [
    path('create', BrandCreateAPIView.as_view(), name='create'),
    path('list', BrandListAPIView.as_view(), name='list'),
]