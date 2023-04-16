from rest_framework.serializers import ModelSerializer

from accounts.models import TechService


class TechServiceListSerializer(ModelSerializer):
    class Meta:
        model = TechService
        fields = '__all__'