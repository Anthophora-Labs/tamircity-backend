from rest_framework import serializers
from reservations.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
   # url = serializers.HyperlinkedIdentityField(
   #      view_name='post:detail',
   #      lookup_field='slug'
   # )
   username = serializers.SerializerMethodField()


   class Meta:
       model = Reservation
       fields = [
           'user',
           'full_name',
           'email',
           'phone_number',
           'second_phone_number',
           'description',
       ]

   def get_username(self, obj):
        return str(obj.user.username)


class ReservationUpdateCreateSerializer(serializers.ModelSerializer):


   class Meta:
       model = Reservation
       fields = [
           'full_name',
           'email',
           'phone_number',
           'second_phone_number',
           'description',
       ]