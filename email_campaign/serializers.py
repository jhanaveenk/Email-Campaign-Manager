from rest_framework import serializers
from .models import Subscriber

# Created Serializer for Subscriber 
class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('id', 'email', 'name')
