from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Trip, Itinerary
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .froms import TripForm


def about(request):
    return render(request, "base.html")


def about(request):
    return render(request, "map.html")


def trip_index(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'trip.html', { 'trips': trips })

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


class Login(LoginView):
    template_name = 'login.html'


class Map(LoginView):
    template_name = "map.html"


class Trip(LoginView):
    template_name = "trip.html"


class AddTrip(LoginRequiredMixin, View):
    def get(self, request):
        form = TripForm()
        return render(request, 'addTrip.html', {'form': form})

    def post(self, request):
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.user = request.user
            trip.save()
            return redirect('/trip')  
        return render(request, 'addTrip.html', {'form': form})

