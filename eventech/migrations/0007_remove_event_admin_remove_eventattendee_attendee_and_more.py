# Generated by Django 4.2.2 on 2023-07-18 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("eventech", "0006_rename_admin_eventrequest_admin_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="admin",
        ),
        migrations.RemoveField(
            model_name="eventattendee",
            name="attendee",
        ),
        migrations.RemoveField(
            model_name="eventattendee",
            name="event",
        ),
        migrations.RemoveField(
            model_name="eventrequest",
            name="admin",
        ),
        migrations.RemoveField(
            model_name="eventrequest",
            name="attendee",
        ),
        migrations.RemoveField(
            model_name="feedback",
            name="attendee",
        ),
        migrations.RemoveField(
            model_name="feedback",
            name="event",
        ),
        migrations.RemoveField(
            model_name="poll",
            name="event",
        ),
        migrations.RemoveField(
            model_name="pollchoice",
            name="poll",
        ),
        migrations.RemoveField(
            model_name="pollvote",
            name="attendee",
        ),
        migrations.RemoveField(
            model_name="pollvote",
            name="poll_choice",
        ),
        migrations.DeleteModel(
            name="AdminUser",
        ),
        migrations.DeleteModel(
            name="Attendee",
        ),
        migrations.DeleteModel(
            name="Event",
        ),
        migrations.DeleteModel(
            name="EventAttendee",
        ),
        migrations.DeleteModel(
            name="EventRequest",
        ),
        migrations.DeleteModel(
            name="Feedback",
        ),
        migrations.DeleteModel(
            name="Poll",
        ),
        migrations.DeleteModel(
            name="PollChoice",
        ),
        migrations.DeleteModel(
            name="PollVote",
        ),
    ]
