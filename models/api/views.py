from rest_framework.generics import (
                                    CreateAPIView,
                                    ListAPIView,
                                    )
from rest_framework.permissions import IsAuthenticated
from models.api.serializers import ModelCreateSerializer, ModelListSerializer
from models.models import Model


class ModelCreateAPIView(CreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelCreateSerializer
    permission_classes = [IsAuthenticated]


class ModelListAPIView(ListAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelListSerializer

    # def get_queryset(self):
    #     queryset = Comment.objects.filter(parent = None)
    #     query = self.request.GET.get("q") # queryparam olaarak gonderilen q, query varsa postu filtrele
    #     if query:
    #         queryset = queryset.filter(post = query)
    #     return queryset


class ModelListByDeviceTypeBrandAPIView(ListAPIView):
    serializer_class = ModelListSerializer

    def get_queryset(self):
        queryset = Model.objects.filter(device_type = self.kwargs['pk_device_type'], brand = self.kwargs['pk_brand'])
        return queryset