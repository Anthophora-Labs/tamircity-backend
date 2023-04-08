from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from models.models import Model


class ModelCreateSerializer(ModelSerializer):
    class Meta:
        model = Model
        fields = ['name', 'short_description', 'device_type', 'brand']

    # def validate(self, attrs):
    #     if(attrs["parent"]):
    #         if attrs["parent"].post != attrs["post"]:
    #             raise serializers.ValidationError("something went wrong")
    #     return attrs


class ModelListSerializer(ModelSerializer):
    queryset = Model.objects.all()


    class Meta:
        model = Model
        fields = '__all__'

    # def get_replies(self, obj):
    #     if obj.any_children:
    #         return CommentListSerializer(obj.children(), many=True).data

    # def get_queryset(self):
    #     return Comment.objects.filter(parent = None)