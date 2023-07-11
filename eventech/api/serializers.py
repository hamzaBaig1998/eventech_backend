from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


from ..models import Event, AdminUser, Attendee, EventRequest

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number')

class EventRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRequest
        fields = '__all__'