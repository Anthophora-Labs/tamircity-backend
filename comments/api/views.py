from rest_framework.generics import (
                                    CreateAPIView,
                                     ListAPIView,
                                    UpdateAPIView,
                                    RetrieveAPIView
                                    )
#mixinler
from rest_framework.mixins import  DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from comments.api.paginations import CommentPagination
from comments.api.permissions import IsOwner
from comments.api.serializers import CommentCreateSerializer, CommentListSerializer, CommentDeleteUpdateSerializer
from comments.models import Comment


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    pagination_class = CommentPagination
    def get_queryset(self):
        queryset = Comment.objects.filter(parent = None)
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(post = query)
        return queryset



class CommentUpdateAPIView(DestroyModelMixin, UpdateAPIView, RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)