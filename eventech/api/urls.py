from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import TestView, EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView, RegisterEventView, SwapEventView, DeleteEventView
from .views import AdminUserSignUpAPIView, AdminUserSignInAPIView, AdminUserSignOutAPIView, AdminUserDeleteAccountAPIView, RegisterAttendeeView, AttendeeEventsView, CancelEventView


urlpatterns = [
    path('test/', TestView.as_view(), name='user-logout'),
    path('events/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view(), name='event-retrieve-update-destroy'),

    path('register-event/', RegisterEventView.as_view(), name='register-event'),
    path('swap-event/', SwapEventView.as_view(), name='swap-event'),
    path('delete-event/<int:event_id>/', DeleteEventView.as_view(), name='delete-event'),

    path('register-attendee/', RegisterAttendeeView.as_view(), name='register-attendee'),

    path('attendees/<int:attendee_id>/events/', AttendeeEventsView.as_view(), name='attendee_events'),
   path('events/cancel/', CancelEventView.as_view(), name='cancel_event'),
    
    path('admin-signup/', AdminUserSignUpAPIView.as_view(), name='admin-signup'),
    path('admin-signin/', AdminUserSignInAPIView.as_view(), name='admin-signin'),
    path('admin-signout/', AdminUserSignOutAPIView.as_view(), name='admin-signout'),
    path('admin-delete-account/', AdminUserDeleteAccountAPIView.as_view(), name='admin-delete-account'),
]
    