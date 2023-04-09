from rest_framework.generics import (
                                    CreateAPIView,
                                    ListAPIView,
                                    )
from rest_framework.permissions import IsAuthenticated
from service_types.api.serializers import ServiceTypeCreateSerializer, ServiceTypeListSerializer
from service_types.models import ServiceType


class ServiceTypeCreateAPIView(CreateAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeCreateSerializer
    permission_classes = [IsAuthenticated]


class ServiceTypeListAPIView(ListAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeListSerializer

    # def get_queryset(self):
    #     queryset = Comment.objects.filter(parent = None)
    #     query = self.request.GET.get("q") # queryparam olaarak gonderilen q, query varsa postu filtrele
    #     if query:
    #         queryset = queryset.filter(post = query)
    #     return queryset