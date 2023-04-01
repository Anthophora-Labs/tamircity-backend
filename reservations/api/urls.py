from django.urls import path, include
from reservations.api.views import (
    ReservationListAPIView,
    ReservationDetailAPIView,
    ReservationDeleteAPIView,
    ReservationUpdateAPIView,
    ReservationCreateAPIView,
    )


urlpatterns = [
    path('list', ReservationListAPIView.as_view(), name='list'),
    path('detail/<pk>', ReservationDetailAPIView.as_view(), name='detail'),
    path('update/<pk>', ReservationUpdateAPIView.as_view(), name='update'),
    path('delete/<pk>', ReservationDeleteAPIView.as_view(), name='delete'),
    path('create', ReservationCreateAPIView.as_view(), name='create'),
]