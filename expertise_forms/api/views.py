from rest_framework.generics import (
                                    CreateAPIView,
                                    ListAPIView,
                                    RetrieveAPIView,
                                    )
from expertise_forms.api.serializers import ExpertiseTVCreateSerializer, ExpertiseWatchCreateSerializer, ExpertiseConsoleCreateSerializer, ExpertisePhoneCreateSerializer, ExpertisePcCreateSerializer, ExpertiseConsoleListSerializer, ExpertisePhoneListSerializer, ExpertisePcListSerializer, ExpertisePcSerializer, ExpertiseTVSerializer, ExpertisePhoneSerializer, ExpertiseWatchSerializer, ExpertiseConsoleSerializer
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

class ExpertisePcDetailAPIView(RetrieveAPIView):
    queryset = ExpertisePc.objects.all()
    serializer_class = ExpertisePcSerializer
    lookup_field = 'pk'

class ExpertiseTVDetailAPIView(RetrieveAPIView):
    queryset = ExpertiseTV.objects.all()
    serializer_class = ExpertiseTVSerializer
    lookup_field = 'pk'

class ExpertiseConsoleDetailAPIView(RetrieveAPIView):
    queryset = ExpertiseConsole.objects.all()
    serializer_class = ExpertiseConsoleSerializer
    lookup_field = 'pk'

class ExpertiseWatchDetailAPIView(RetrieveAPIView):
    queryset = ExpertiseWatch.objects.all()
    serializer_class = ExpertiseWatchSerializer
    lookup_field = 'pk'

class ExpertisePhoneDetailAPIView(RetrieveAPIView):
    queryset = ExpertisePhone.objects.all()
    serializer_class = ExpertisePhoneSerializer
    lookup_field = 'pk'