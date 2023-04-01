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
from reservations.api.permissions import IsOwner
from rest_framework.permissions import (
    IsAuthenticated, IsAdminUser
)

from reservations.models import Reservation
from .serializers import ReservationSerializer, ReservationUpdateCreateSerializer


class ReservationListAPIView(ListAPIView):
    #throttle_scope  = 'mustafa'
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['full_name','description'] # api/v1/reservations/list?search=mustafa&ordering=full_name
    #pagination_class = ReservationPagination

    # def get_queryset(self): # Return only non draft posts
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
    permission_classes = [IsOwner] # If you want to allow only owner users or admin to delete a post


class ReservationUpdateAPIView(RetrieveUpdateAPIView):  # UpdateAPIView
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'pk' #pk or slug
    permission_classes = [IsOwner] # If you want to allow only owner users or admin to update a post

    # def perform_update(self, serializer):
    #     serializer.save(modified_by = self.request.user)


class ReservationUpdateWithDeleteAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = Reservation.objects.all()
    serializer_class = ReservationUpdateCreateSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner] # If you want to allow only owner users or admin to update a post

    def perform_update(self, serializer):
        serializer.save(modified_by = self.request.user)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ReservationCreateAPIView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationUpdateCreateSerializer
    permission_classes = [IsAuthenticated] # If you want to allow only authenticated users to create a post

    def perform_create(self, serializer): # Save user who created the post
        serializer.save(user = self.request.user)
        # Write here custom code for creating a post