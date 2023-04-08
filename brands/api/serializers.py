from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from brands.models import Brand


class BrandCreateSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'device_type']

    # def validate(self, attrs):
    #     if(attrs["parent"]):
    #         if attrs["parent"].post != attrs["post"]:
    #             raise serializers.ValidationError("something went wrong")
    #     return attrs


class BrandListSerializer(ModelSerializer):
    queryset = Brand.objects.all()


    class Meta:
        model = Brand
        fields = '__all__'

    # def get_replies(self, obj):
    #     if obj.any_children:
    #         return CommentListSerializer(obj.children(), many=True).data

    # def get_queryset(self):
    #     return Comment.objects.filter(parent = None)