from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from favourite.models import Favourite


class FavouriteListCreateAPISerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'

    def validate(self, attrs):
        queryset = Favourite.objects.filter(fav_user = attrs["fav_user"], user = attrs["user"])
        if queryset.exists():
            raise serializers.ValidationError("Zaten favorilere eklendi.")
        return attrs


class FavouriteAPISerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = ('content',)