from django.contrib.auth.tokens import datetime
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    interests = models.TextField(default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.name


class Trip(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trips")
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class Itinerary(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="itineraries")

    def __str__(self):
        return f"{self.name} - {self.location}"
