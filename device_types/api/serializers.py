from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from device_types.models import DeviceType


class DeviceTypeCreateSerializer(ModelSerializer):
    class Meta:
        model = DeviceType
        fields = ['name', 'short_description']

    # def validate(self, attrs):
    #     if(attrs["parent"]):
    #         if attrs["parent"].post != attrs["post"]:
    #             raise serializers.ValidationError("something went wrong")
    #     return attrs


class DeviceTypeListSerializer(ModelSerializer):
    queryset = DeviceType.objects.all()


    class Meta:
        model = DeviceType
        fields = '__all__'

    # def get_replies(self, obj):
    #     if obj.any_children:
    #         return CommentListSerializer(obj.children(), many=True).data

    # def get_queryset(self):
    #     return Comment.objects.filter(parent = None)