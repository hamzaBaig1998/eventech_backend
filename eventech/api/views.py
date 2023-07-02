from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.db import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from .serializers import EventSerializer, AdminUserSerializer,AttendeeSerializer
from ..models import Event, AdminUser, Attendee, EventAttendee


class TestView(APIView):

    def post(self, request):
        return Response({"This is a Test API"}, status=status.HTTP_200_OK)

#event Related APIs

class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

#Admin Signin Signup APIs

# class AdminUserSignUpAPIView(APIView):

#     def post(self, request):
#         serializer = AdminUserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"message": "User created successfully"})
#         return Response(serializer.errors)


class AdminUserSignUpAPIView(APIView):
    def post(self, request):
        serializer = AdminUserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if User.objects.filter(email=email).exists():
                return Response({"message": "A user with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()
            return Response({"message": "User created successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminUserSignInAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=401)


class AdminUserSignOutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response({"message": "Successfully logged out"})


class AdminUserDeleteAccountAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        user = request.user
        user.delete()
        return Response({"message": "Account deleted"})
    

class RegisterEventView(APIView):
    def post(self, request):
        event_id = request.data.get('event_id')
        attendee_id = request.data.get('attendee_id')
        ticket_type = request.data.get('ticket_type')
        payment_amount = request.data.get('payment_amount')

        event = Event.objects.get(id=event_id)
        attendee = Attendee.objects.get(id=attendee_id)

        if EventAttendee.objects.filter(event=event, attendee=attendee).exists():
            return Response({'error': 'Attendee is already registered for this event'})

        if event.max_attendees <= EventAttendee.objects.filter(event=event).count():
            return Response({'error': 'Event is already sold out'})

        event_attendee = EventAttendee.objects.create(
            event=event,
            attendee=attendee,
            ticket_type=ticket_type,
            payment_amount=payment_amount
        )

        return Response({'message': 'Event registration successful'})
    

class SwapEventView(APIView):
    def post(self, request):
        event_id = request.data.get('event_id')
        attendee_id = request.data.get('attendee_id')
        new_attendee_id = request.data.get('new_attendee_id')

        event = Event.objects.get(id=event_id)
        attendee = Attendee.objects.get(id=attendee_id)
        new_attendee = Attendee.objects.get(id=new_attendee_id)

        event_attendee = EventAttendee.objects.get(event=event, attendee=attendee)
        event_attendee.attendee = new_attendee
        event_attendee.save()

        return Response({'message': 'Event swap successful'})
    

class DeleteEventView(APIView):
    def delete(self, request, event_id):
        event = Event.objects.get(id=event_id)
        event.delete()
        return Response({'message': 'Event deleted successfully'})
    

class RegisterAttendeeView(APIView):
    def post(self, request):
        serializer = AttendeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@method_decorator(csrf_exempt, name='dispatch')
class AttendeeEventsView(APIView):
    def get(self, request, attendee_id):
        # Retrieve all events that the attendee is registered for
        attendee_events = Event.objects.filter(eventattendee__attendee_id=attendee_id)

        # Serialize the events and return a JSON response
        events = []
        for event in attendee_events:
            events.append({
                'id': event.id,
                'name': event.name,
                'description': event.description,
                'start_date': event.start_date,
                'end_date': event.end_date,
                'location': event.location,
                'max_attendees': event.max_attendees,
                'event_image': event.event_image.url if event.event_image else None,
            })
        return JsonResponse({'events': events})

# @method_decorator(csrf_exempt, name='dispatch')
# class CancelEventView(APIView):
#     def post(self, request, attendee_id, event_id):
#         try:
#             # Retrieve the event attendee record
#             event_attendee = EventAttendee.objects.get(attendee_id=attendee_id, event_id=event_id)

#             # Set the payment status to "cancelled"
#             event_attendee.payment_status = 'cancelled'
#             event_attendee.save()

#             # Return a success response
#             return JsonResponse({'status': 'success'})
#         except EventAttendee.DoesNotExist:
#             # Return an error response if the event attendee record does not exist
#             return JsonResponse({'status': 'error', 'message': 'Event attendee not found.'}, status=404)

class CancelEventView(APIView):
    def delete(self, request):
        attendee_id = request.data.get('attendee_id')
        event_id = request.data.get('event_id')

        try:
            event_attendee = EventAttendee.objects.get(attendee_id=attendee_id, event_id=event_id)
            # event_attendee.payment_status = 'cancelled'
            event_attendee.delete()
            return Response({'message': 'Registration cancelled successfully'})
        except EventAttendee.DoesNotExist:
            return Response({'error': 'Event registration not found'}, status=status.HTTP_404_NOT_FOUND)