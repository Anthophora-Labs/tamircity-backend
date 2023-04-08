from rest_framework.generics import (
                                    CreateAPIView,
                                    ListAPIView,
                                    )
from rest_framework.permissions import IsAuthenticated
from device_types.api.serializers import DeviceTypeCreateSerializer, DeviceTypeListSerializer
from device_types.models import DeviceType


class DeviceTypeCreateAPIView(CreateAPIView):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeCreateSerializer
    permission_classes = [IsAuthenticated]


class DeviceTypeListAPIView(ListAPIView):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeListSerializer

    # def get_queryset(self):
    #     queryset = Comment.objects.filter(parent = None)
    #     query = self.request.GET.get("q") # queryparam olaarak gonderilen q, query varsa postu filtrele
    #     if query:
    #         queryset = queryset.filter(post = query)
    #     return queryset