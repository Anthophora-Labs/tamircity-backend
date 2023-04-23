from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from expertise_forms.models import ExpertiseTV, ExpertiseWatch, ExpertiseConsole, ExpertisePhone, ExpertisePc


class ExpertiseTVCreateSerializer(ModelSerializer):
    class Meta:
        model = ExpertiseTV
        fields = '__all__'

    # def validate(self, attrs):
    #     if(attrs["parent"]):
    #         if attrs["parent"].post != attrs["post"]:
    #             raise serializers.ValidationError("something went wrong")
    #     return attrs


class ExpertiseWatchCreateSerializer(ModelSerializer):
    class Meta:
        model = ExpertiseWatch
        fields = '__all__'


class ExpertiseConsoleCreateSerializer(ModelSerializer):
    class Meta:
        model = ExpertiseConsole
        fields = '__all__'

class ExpertisePhoneCreateSerializer(ModelSerializer):
    class Meta:
        model = ExpertisePhone
        fields = '__all__'

class ExpertisePcCreateSerializer(ModelSerializer):
    class Meta:
        model = ExpertisePc
        fields = '__all__'

class ExpertiseConsoleListSerializer(ModelSerializer):
    queryset = ExpertiseConsole.objects.all()


    class Meta:
        model = ExpertiseConsole
        fields = '__all__'

class ExpertisePhoneListSerializer(ModelSerializer):
    queryset = ExpertisePhone.objects.all()


    class Meta:
        model = ExpertisePhone
        fields = '__all__'

class ExpertisePcListSerializer(ModelSerializer):
    queryset = ExpertisePc.objects.all()


    class Meta:
        model = ExpertisePc
        fields = '__all__'

class ExpertisePcSerializer(serializers.ModelSerializer):
   url = serializers.HyperlinkedIdentityField(
        view_name='expertise_pc:detail',
        #lookup_field='slug'
   )


   class Meta:
       model = ExpertisePc
       #fields = '__all__'
       exclude = ['updated_date', 'created_date']

class ExpertisePhoneSerializer(serializers.ModelSerializer):
   url = serializers.HyperlinkedIdentityField(
        view_name='expertise_phone:detail',
        #lookup_field='slug'
   )


   class Meta:
       model = ExpertisePhone
       #fields = '__all__'
       exclude = ['updated_date', 'created_date']

class ExpertiseConsoleSerializer(serializers.ModelSerializer):
   url = serializers.HyperlinkedIdentityField(
        view_name='expertise_console:detail',
        #lookup_field='slug'
   )


   class Meta:
       model = ExpertiseConsole
       #fields = '__all__'
       exclude = ['updated_date', 'created_date']

class ExpertiseWatchSerializer(serializers.ModelSerializer):
   url = serializers.HyperlinkedIdentityField(
        view_name='expertise_watch:detail',
        #lookup_field='slug'
   )


   class Meta:
       model = ExpertiseWatch
       #fields = '__all__'
       exclude = ['updated_date', 'created_date']

class ExpertiseTVSerializer(serializers.ModelSerializer):
   url = serializers.HyperlinkedIdentityField(
        view_name='expertise_tv:detail',
        #lookup_field='slug'
   )


   class Meta:
       model = ExpertiseTV
       #fields = '__all__'
       exclude = ['updated_date', 'created_date']