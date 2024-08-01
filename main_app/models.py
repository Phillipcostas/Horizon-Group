from django.contrib.auth.tokens import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    interests = models.TextField(default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.name


class Trip(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trips")
    location = models.CharField(max_length=255, default="")
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)

    def __str__(self):
        return self.name

    def clean(self):
        if self.start_date and self.end_date:
            if self.end_date < self.start_date:
                raise ValidationError('End date cannot be before start date')
        else:
            if not self.start_date:
                raise ValidationError('Start date is required')
            if not self.end_date:
                raise ValidationError('End date is required')
            
    def number_of_days(self):
        return (self.end_date - self.start_date).days + 1


class Itinerary(models.Model):
    name = models.CharField(max_length=255)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="itineraries")
    day = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} on Day {self.day} of {self.trip.name}"

