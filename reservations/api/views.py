from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    UpdateAPIView,
)

from rest_framework.mixins import DestroyModelMixin

# from account.api.throttles import RegisterThrottle
# from post.api.paginations import PostPagination
# from reservations.api.permissions import IsOwner
from rest_framework.permissions import (
    IsAuthenticated,
)

from reservations.models import Reservation
from .serializers import ReservationSerializer, ReservationUpdateCreateSerializer


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


class ReservationDetailAPIView(RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'pk' #pk or slug


class ReservationDeleteAPIView(DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'pk' #pk or slug


class ReservationUpdateAPIView(UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'pk' #pk or slug


class ReservationUpdateAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = Reservation.objects.all()
    serializer_class = ReservationUpdateCreateSerializer
    lookup_field = 'slug'
    #permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by = self.request.user)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ReservationCreateAPIView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationUpdateCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)