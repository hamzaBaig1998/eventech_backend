from django.urls import path
from .views import TestView, EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('test/', TestView.as_view(), name='user-logout'),
    path('events/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view(), name='event-retrieve-update-destroy'),
]
