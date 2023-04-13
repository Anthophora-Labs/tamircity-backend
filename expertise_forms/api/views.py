from rest_framework.generics import (
                                    CreateAPIView,
                                    ListAPIView
                                    )
from expertise_forms.api.serializers import ExpertiseTVCreateSerializer, ExpertiseWatchCreateSerializer, ExpertiseConsoleCreateSerializer, ExpertisePhoneCreateSerializer, ExpertisePcCreateSerializer, ExpertiseConsoleListSerializer, ExpertisePhoneListSerializer, ExpertisePcListSerializer
from expertise_forms.models import ExpertiseTV, ExpertiseWatch, ExpertiseConsole, ExpertisePhone, ExpertisePc


class ExpertiseTVCreateAPIView(CreateAPIView):
    queryset = ExpertiseTV.objects.all()
    serializer_class = ExpertiseTVCreateSerializer


class ExpertiseWatchCreateAPIView(CreateAPIView):
    queryset = ExpertiseWatch.objects.all()
    serializer_class = ExpertiseWatchCreateSerializer


class ExpertiseConsoleCreateAPIView(CreateAPIView):
    queryset = ExpertiseConsole.objects.all()
    serializer_class = ExpertiseConsoleCreateSerializer

class ExpertisePhoneCreateAPIView(CreateAPIView):
    queryset = ExpertisePhone.objects.all()
    serializer_class = ExpertisePhoneCreateSerializer

class ExpertisePcCreateAPIView(CreateAPIView):
    queryset = ExpertisePc.objects.all()
    serializer_class = ExpertisePcCreateSerializer

class ExpertiseConsoleListAPIView(ListAPIView):
    queryset = ExpertiseConsole.objects.all()
    serializer_class = ExpertiseConsoleListSerializer

class ExpertisePhoneListAPIView(ListAPIView):
    queryset = ExpertisePhone.objects.all()
    serializer_class = ExpertisePhoneListSerializer

class ExpertisePcListAPIView(ListAPIView):
    queryset = ExpertisePc.objects.all()
    serializer_class = ExpertisePcListSerializer