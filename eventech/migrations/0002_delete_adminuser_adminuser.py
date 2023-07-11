# Generated by Django 4.2.2 on 2023-06-22 00:39

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("eventech", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AdminUser",
        ),
        migrations.CreateModel(
            name="AdminUser",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]