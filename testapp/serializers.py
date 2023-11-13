from rest_framework import serializers
from .models import PaystackData, Client


class PaystackDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaystackData
        fields = ['client_id', 'amount', 'currency']


# Serializer for MyClient model
class MyClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'mobile_no']
