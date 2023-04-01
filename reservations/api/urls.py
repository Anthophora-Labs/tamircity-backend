from django.urls import path, include
from reservations.api.views import ReservationListAPIView


urlpatterns = [
    path('list', ReservationListAPIView.as_view(), name='list'),
]