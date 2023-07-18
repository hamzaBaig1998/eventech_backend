from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


from ..models import Event, AdminUser, Attendee, EventRequest, EventAttendee

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class AttendeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Attendee
        fields = '__all__'
        
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        attendee = Attendee.objects.create_user(**validated_data)
        attendee.set_password(password)
        attendee.save()
        return attendee

# class AttendeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attendee
#         fields = ('id', 'first_name', 'last_name', 'email', 'phone_number')

class EventRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRequest
        fields = '__all__'

#fetch attendee records
# class AttendeeStatusSerializer(serializers.Serializer):
#     cancelled = serializers.IntegerField()
#     paid = serializers.IntegerField()
#     pending = serializers.IntegerField()

# # class EventSerializer(serializers.ModelSerializer):
# #     attendee_status = AttendeeStatusSerializer(read_only=True)

# #     class Meta:
# #         model = Event
# #         fields = ['id', 'name', 'attendee_status']

# # class AdminEventSerializer(serializers.ModelSerializer):
# #     events = EventSerializer(many=True)

# #     class Meta:
# #         model = AdminUser
# #         fields = ['id', 'username', 'events']

# class EventSerializer(serializers.ModelSerializer):
#     attendee_status = AttendeeStatusSerializer(read_only=True)

#     class Meta:
#         model = Event
#         fields = ['id', 'name', 'attendee_status']


# class AdminUserSerializer2(serializers.ModelSerializer):
#     events = serializers.SerializerMethodField()

#     class Meta:
#         model = AdminUser
#         fields = ['id', 'username', 'events']

#     def get_events(self, obj):
#         events = Event.objects.filter(admin=obj)
#         return EventSerializer(events, many=True).data

class AttendeeStatusSerializer(serializers.Serializer):
    cancelled = serializers.IntegerField()
    paid = serializers.IntegerField()
    pending = serializers.IntegerField()


# class EventSerializer(serializers.ModelSerializer):
#     attendee_status = AttendeeStatusSerializer(read_only=True)

#     class Meta:
#         model = Event
#         fields = ['id', 'name', 'attendee_status']


class AdminUserSerializer2(serializers.ModelSerializer):
    events = serializers.SerializerMethodField()

    class Meta:
        model = AdminUser
        fields = ['id', 'username', 'events']

    def get_events(self, obj):
        events = Event.objects.filter(admin=obj)
        event_data = EventSerializer(events, many=True).data

        for event in event_data:
            attendees = EventAttendee.objects.filter(event_id=event['id'])
            attendee_status = {'cancelled': 0, 'paid': 0, 'pending': 0}

            for attendee in attendees:
                if attendee.payment_status == 'cancelled':
                    attendee_status['cancelled'] += 1
                elif attendee.payment_status == 'paid':
                    attendee_status['paid'] += 1
                elif attendee.payment_status == 'pending':
                    attendee_status['pending'] += 1

            event['attendee_status'] = attendee_status

        return event_data
