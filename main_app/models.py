from django.contrib.auth.tokens import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date

class UserPhoto(models.Model):
    photo_url = models.URLField(max_length=1000)

    def __str__(self):
        return self.photo_url

class TripPhoto(models.Model):
    photo_url = models.URLField(max_length=1000)

    def __str__(self):
        return self.photo_url

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    interests = models.TextField(default="")
    profile_photo = models.ForeignKey(UserPhoto, on_delete=models.SET_NULL, null=True, blank=True, related_name="user_profiles")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.name


class Trip(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trips")
    location = models.CharField(max_length=255, default="")
    trip_photo = models.ForeignKey(TripPhoto, on_delete=models.SET_NULL, null=True, blank=True, related_name="trips")
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

class SuitcaseItem(models.Model):
    CATEGORY_CHOICES = [
        ('Essentials', 'Essentials'),
        ('Toiletries', 'Toiletries'),
        ('Speciality Clothes', 'Speciality Clothes'),
        ('Lounge Wear', 'Lounge Wear'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)  # New field
    packed = models.BooleanField(default=False)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="some-string")

    def __str__(self):
        return self.name

