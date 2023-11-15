from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    registration_trype = models.CharField(max_length=50)


class Group(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    representative_user = models.ForeignKey(User, on_delete=models.CASCADE)


class Attendee(models.Model):
    attendee_user = models.ForeignKey(User, on_delete=models.CASCADE)
    attendee_group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)


class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    event_name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)


class Addon(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    type = models.CharField(max_length=50)


class AddonInstance(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    addon = models.ForeignKey(Addon, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    instance_name = models.CharField(max_length=100)
    details = models.CharField(max_length=150)


class UserAddon(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    addon_instance = models.ForeignKey(AddonInstance, on_delete=models.CASCADE)
    registration_date = models.DateField()
    status = models.CharField(max_length=50)
