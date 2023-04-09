from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from newletters.models import NewLetter


class NewLetterCreateSerializer(ModelSerializer):
    class Meta:
        model = NewLetter
        fields = ['email']

    # def validate(self, attrs):
    #     if(attrs["parent"]):
    #         if attrs["parent"].post != attrs["post"]:
    #             raise serializers.ValidationError("something went wrong")
    #     return attrs


class NewLetterListSerializer(ModelSerializer):
    queryset = NewLetter.objects.all()


    class Meta:
        model = NewLetter
        fields = '__all__'

    # def get_replies(self, obj):
    #     if obj.any_children:
    #         return CommentListSerializer(obj.children(), many=True).data

    # def get_queryset(self):
    #     return Comment.objects.filter(parent = None)