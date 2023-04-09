from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from expertise_forms.models import ExpertiseTV


class ExpertiseTVCreateSerializer(ModelSerializer):
    class Meta:
        model = ExpertiseTV
        fields = '__all__'

    # def validate(self, attrs):
    #     if(attrs["parent"]):
    #         if attrs["parent"].post != attrs["post"]:
    #             raise serializers.ValidationError("something went wrong")
    #     return attrs