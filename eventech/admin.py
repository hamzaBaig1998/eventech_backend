from django.contrib import admin
from .models import AdminUser, EventRequest, Event, EventAttendee
# Register your models here.

admin.site.register(AdminUser)
admin.site.register(EventRequest)
admin.site.register(Event)
admin.site.register(EventAttendee)


