from accounts.models import TechService
from rest_framework.generics import ListAPIView


from technical_services.api.serializers import TechServiceListSerializer


class TechServiceListAPIView(ListAPIView):
    queryset = TechService.objects.all()
    serializer_class = TechServiceListSerializer