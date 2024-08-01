from django.urls import path, include
from . import views
from django.contrib.auth.models import User


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("map/", views.map, name="map"),
    path("trip", views.Trip.as_view(), name="trip"),
    path("addTrip", views.AddTrip.as_view(), name="addTrip"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", views.signup, name="signup"),
    path("accounts/login/", views.LoginView.as_view(), name="login"),
]
