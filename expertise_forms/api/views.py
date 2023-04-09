from rest_framework.generics import (
                                    CreateAPIView,
                                    )
from expertise_forms.api.serializers import ExpertiseTVCreateSerializer, ExpertiseWatchCreateSerializer
from expertise_forms.models import ExpertiseTV, ExpertiseWatch


class ExpertiseTVCreateAPIView(CreateAPIView):
    queryset = ExpertiseTV.objects.all()
    serializer_class = ExpertiseTVCreateSerializer


class ExpertiseWatchCreateAPIView(CreateAPIView):
    queryset = ExpertiseWatch.objects.all()
    serializer_class = ExpertiseWatchCreateSerializer