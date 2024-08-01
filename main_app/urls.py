from django.urls import path, include
from . import views
from django.contrib.auth.models import User
from .views import AddTrip, TripListView, TripDetailView, AddItinerary

urlpatterns = [
    path("", views.Home.as_view(), name="home"),

    path("map", views.map, name="map"),
    path("trip/", TripListView.as_view(), name="trip_list"),
    path("addTrip", views.AddTrip.as_view(), name="addTrip"),
    path("trip/<int:pk>/", TripDetailView.as_view(), name="trip_detail"),
    path('trip/<int:pk>/add-itinerary/<int:day>/', AddItinerary.as_view(), name='add_itinerary'),    
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", views.signup, name="signup"),
    path("accounts/login/", views.Login.as_view(), name="login"),
]
