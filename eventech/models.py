from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    registration_start_date = models.DateTimeField()
    registration_end_date = models.DateTimeField()
    max_attendees = models.PositiveIntegerField()
    event_image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Attendee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class EventAttendee(models.Model):
    TICKET_TYPES = (
        ('general', 'General'),
        ('vip', 'VIP'),
        ('speaker', 'Speaker'),
    )
    PAYMENT_STATUSES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=50, choices=TICKET_TYPES, default='general')
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUSES, default='pending')
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)



# class AdminUser(models.Model):
#     username = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=128)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField()
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)
#     last_login = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return self.username

class AdminUser(User):

    class Meta:
        proxy = True

    def __str__(self):
        return self.username
    
class EventRequest(models.Model):
    Attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    Admin = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    event_location = models.CharField(max_length=255)
    requester_name = models.CharField(max_length=255)
    requester_email = models.EmailField()
    requester_phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Poll(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    question = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class PollChoice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class PollVote(models.Model):
    poll_choice = models.ForeignKey(PollChoice, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Feedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    feedback_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)