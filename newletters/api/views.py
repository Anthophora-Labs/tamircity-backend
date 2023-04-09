from rest_framework.generics import (
                                    CreateAPIView,
                                    ListAPIView,
                                    )
from rest_framework.permissions import IsAuthenticated
from newletters.api.serializers import NewLetterCreateSerializer, NewLetterListSerializer
from newletters.models import NewLetter


class NewLetterCreateAPIView(CreateAPIView):
    queryset = NewLetter.objects.all()
    serializer_class = NewLetterCreateSerializer
    permission_classes = [IsAuthenticated]


class NewLetterListAPIView(ListAPIView):
    queryset = NewLetter.objects.all()
    serializer_class = NewLetterListSerializer

    # def get_queryset(self):
    #     queryset = Comment.objects.filter(parent = None)
    #     query = self.request.GET.get("q") # queryparam olaarak gonderilen q, query varsa postu filtrele
    #     if query:
    #         queryset = queryset.filter(post = query)
    #     return queryset