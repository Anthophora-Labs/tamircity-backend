from rest_framework.generics import ListAPIView

from reservations.models import Reservation
from .serializers import ReservationSerializer

class ReservationListAPIView(ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationListAPIView(ListAPIView):
    #throttle_scope  = 'mustafa'
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    #filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title','content']
    #pagination_class = ReservationPagination

    # def get_queryset(self):
    #     queryset = Reservation.objects.filter(draft=False)
    #     return queryset