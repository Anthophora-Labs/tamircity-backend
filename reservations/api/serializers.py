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
           'username',
           'full_name',
           'email',
           'phone_number',
           'second_phone_number',
           'description',
           'slug',
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
           'slug',
       ]

    # Save create e mi yoksa update gidecegini karar verr obje ilk ise create
    # def save(self, **kwargs): # Bunu yazarken kendi save metodunu override edersin save islemi yerine print calsıtırrsn sadece
    #     print("Test")
    #     return True

   # def create(self, validated_data):
   #     return Reservation.objects.create(user = self.context['request'].user, **validated_data)
   # #bu metod useri otomatik olarak ekler bunun yerine perform_Create kllnıyoruz

   #custom update
   # def update(self, instance, validated_data):
   #       instance.full_name = validated_data.get('full_name', instance.full_name)
   #       instance.email = validated_data.get('email', instance.email)
   #       instance.phone_number = validated_data.get('phone_number', instance.phone_number)
   #       instance.second_phone_number = validated_data.get('second_phone_number', instance.second_phone_number)
   #       instance.description = validated_data.get('description', instance.description)
   #       instance.slug = validated_data.get('slug', instance.slug)
   #       instance.customfields = "asdas"
   #       instance.save()
   #       return instance

   # def validate_title(self, value): # For a certain field
   #     if value == "mustafa":
   #            raise serializers.ValidationError("This title has already been used.")
   #     return value
   #     # qs = Reservation.objects.filter(title__iexact=value)
   #     # if self.instance:
   #     #     qs = qs.exclude(pk=self.instance.pk)
   #     # if qs.exists():
   #     #     raise serializers.ValidationError("This title has already been used.")
   #     # return value
   #
   # def validate(self, data): # For all fields
   #     if data["full_name"] == "mustafa":
   #            raise serializers.ValidationError("This title has already been used.")
   #     return data