from django.contrib import admin
from .models import UserProfile, Itinerary, Trip, UserPhoto, TripPhoto, SuitcaseItem

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Itinerary)
admin.site.register(Trip)
admin.site.register(UserPhoto)
admin.site.register(TripPhoto)
admin.site.register(SuitcaseItem)
