from rest_framework import serializers
from .models import Subscriber


STATUS_CHOICES = {
    True: 'active',
    False: 'inactive',
}

# Created Serializer for Subscriber 
class SubscriberSerializer(serializers.ModelSerializer):
    status_tag = serializers.SerializerMethodField()
    class Meta:
        model = Subscriber
        fields = ('id', 'email', 'name', 'status_tag')

    def get_status_tag(self, obj):
        return STATUS_CHOICES[obj.status_tag]
