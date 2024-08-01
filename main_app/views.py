from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Trip, Itinerary
from django.conf import settings


def about(request):
    return render(request, "base.html")


def map(request):
    context = {"api_key": settings.GOOGLE_MAPS_API_KEY, "map_id": settings.MAP_ID}
    return render(request, "map.html", context)


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            userProfile = UserProfile.objects.create(user=user, name=user.username)
            userProfile.save()
            return redirect("home")
        else:
            error_message = "Invalid sign up - try again"
    else:
        form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)


class Home(LoginView):
    template_name = "home.html"


class LoginView(LoginView):
    template_name = "login.html"


class Trip(LoginView):
    template_name = "trip.html"


class AddTrip(LoginView):
    template_name = "addTrip.html"
