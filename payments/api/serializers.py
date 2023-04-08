from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from payments.models import Payment


class PaymentCreateSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_date', 'amount', 'payment_type', 'reservation']


class PaymentListSerializer(ModelSerializer):
    queryset = Payment.objects.all()


    class Meta:
        model = Payment
        fields = '__all__'

    # def get_replies(self, obj):
    #     if obj.any_children:
    #         return CommentListSerializer(obj.children(), many=True).data

    # def get_queryset(self):
    #     return Comment.objects.filter(parent = None)


class PaymentSerializer(serializers.ModelSerializer):
   url = serializers.HyperlinkedIdentityField(
        view_name='payments:detail',
        #lookup_field='slug'
   )


   class Meta:
       model = Payment
       #fields = '__all__'
       exclude = ['updated_date', 'created_date']