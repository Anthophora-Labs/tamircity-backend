from rest_framework.generics import (
                                    CreateAPIView,
                                    ListAPIView,
                                    )
from rest_framework.permissions import IsAuthenticated
from brands.api.serializers import BrandCreateSerializer, BrandListSerializer
from brands.models import Brand


class BrandCreateAPIView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer
    permission_classes = [IsAuthenticated]


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer

    # def get_queryset(self):
    #     queryset = Comment.objects.filter(parent = None)
    #     query = self.request.GET.get("q") # queryparam olaarak gonderilen q, query varsa postu filtrele
    #     if query:
    #         queryset = queryset.filter(post = query)
    #     return queryset


class BrandListByDeviceTypeAPIView(ListAPIView):
    serializer_class = BrandListSerializer

    def get_queryset(self):
        queryset = Brand.objects.filter(device_type = self.kwargs['pk'])
        return queryset