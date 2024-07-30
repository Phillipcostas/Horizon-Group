from django.contrib import admin
from .models import UserProfile, Itinerary, Trip

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Itinerary)
admin.site.register(Trip)
