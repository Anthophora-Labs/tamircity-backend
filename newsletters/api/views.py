from rest_framework.generics import (
                                    CreateAPIView,
                                    ListAPIView,
                                    )
from rest_framework.permissions import IsAuthenticated
from newsletters.api.serializers import NewsLetterCreateSerializer, NewsLetterListSerializer
from newsletters.models import NewsLetter


class NewsLetterCreateAPIView(CreateAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterCreateSerializer
    permission_classes = [IsAuthenticated]


class NewsLetterListAPIView(ListAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterListSerializer

    # def get_queryset(self):
    #     queryset = Comment.objects.filter(parent = None)
    #     query = self.request.GET.get("q") # queryparam olaarak gonderilen q, query varsa postu filtrele
    #     if query:
    #         queryset = queryset.filter(post = query)
    #     return queryset