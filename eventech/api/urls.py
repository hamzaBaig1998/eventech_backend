from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import  TestView, EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView, RegisterEventView, SwapEventView, DeleteEventView,\
      AdminUserSignInAPIView, AdminUserSignUpAPIView, AdminUserSignOutAPIView, AdminUserDeleteAccountAPIView, RegisterAttendeeView, AttendeeEventsView, CancelEventView,\
        EventRequestListCreateAPIView, EventRequestRetrieveUpdateDestroyAPIView, EventRequestListByAttendeeAPIView, AdminAttendeeAPIView, AttendeeViewSet, generate_qrcode

router = routers.DefaultRouter()
router.register(r'attendees', AttendeeViewSet, basename='attendees')

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

    path('event-requests/', EventRequestListCreateAPIView.as_view(), name='event-request-list'),
    path('event-requests/<int:pk>/', EventRequestRetrieveUpdateDestroyAPIView.as_view(), name='event-request-detail'),
    path('event-requests/attendee/<int:attendee_id>/', EventRequestListByAttendeeAPIView.as_view(), name='event-request-list-by-attendee'),

    path('admin/<int:admin_id>/attendees/', AdminAttendeeAPIView.as_view(), name='admin-attendees'),
    # path('event_images/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),

    path('admin/generate-qrcode/', generate_qrcode, name='generate_qrcode'),

    path('', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)