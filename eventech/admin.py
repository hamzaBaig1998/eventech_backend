from django.contrib import admin
from .models import AdminUser, EventRequest
# Register your models here.

admin.site.register(AdminUser)
admin.site.register(EventRequest)

