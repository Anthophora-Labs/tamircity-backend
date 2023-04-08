from django.urls import path
from payments.api.views import (
                            PaymentCreateAPIView,
                            PaymentListAPIView,
                            PaymentDetailAPIView,
                        )

app_name = "payments"


urlpatterns = [
    path('create', PaymentCreateAPIView.as_view(), name='create'),
    path('list', PaymentListAPIView.as_view(), name='list'),
    path('detail/<pk>', PaymentDetailAPIView.as_view(), name='detail'),
]