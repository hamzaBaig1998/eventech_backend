from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import TestView, EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView
from .views import AdminUserSignUpAPIView, AdminUserSignInAPIView, AdminUserSignOutAPIView, AdminUserDeleteAccountAPIView


urlpatterns = [
    path('test/', TestView.as_view(), name='user-logout'),
    path('events/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view(), name='event-retrieve-update-destroy'),
    
    path('admin-signup/', AdminUserSignUpAPIView.as_view(), name='admin-signup'),
    path('admin-signin/', AdminUserSignInAPIView.as_view(), name='admin-signin'),
    path('admin-signout/', AdminUserSignOutAPIView.as_view(), name='admin-signout'),
    path('admin-delete-account/', AdminUserDeleteAccountAPIView.as_view(), name='admin-delete-account'),
]
    