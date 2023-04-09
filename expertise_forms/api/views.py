from rest_framework.generics import (
                                    CreateAPIView,
                                    )
from expertise_forms.api.serializers import ExpertiseTVCreateSerializer
from expertise_forms.models import ExpertiseTV


class ExpertiseTVCreateAPIView(CreateAPIView):
    queryset = ExpertiseTV.objects.all()
    serializer_class = ExpertiseTVCreateSerializer
