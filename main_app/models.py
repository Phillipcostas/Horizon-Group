from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    interests = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.name


class Trip(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trips")
    # start_date = models.DateField()
    # end_date = models.DateField()
    itinerary = models.ForeignKey(
        "Itinerary", on_delete=models.CASCADE, related_name="trips"
    )

    def __str__(self):
        return self.name


class Itinerary(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.location}"
