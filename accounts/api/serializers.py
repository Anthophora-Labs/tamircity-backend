from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from accounts.models import TechService


class TechServiceSerializer(ModelSerializer):
    class Meta:
        model = TechService
        fields = ('id', 'description', 'twitter')


class UserSerializer(ModelSerializer):
    tech_service = TechServiceSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'tech_service')

    def update(self, instance, validated_data):
        tech_service = validated_data.pop('tech_service')
        tech_service_serializer = TechServiceSerializer(instance.tech_service, data=tech_service)
        tech_service_serializer.is_valid(raise_exception=True)
        tech_service_serializer.save()
        return super(UserSerializer, self).update(instance, validated_data)
        # Additional TechService Update, also update User


# API Views Unlike Generic Views
class ChangePasswordSerializer(Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def validate(self, attr):
        validate_password(attr['password']) # Check password strength or raise ValidationError
        return attr

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
