from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Trip, Itinerary
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .froms import TripForm

def about(request):
    return render(request, "base.html")


def map(request):
    context = {"api_key": settings.GOOGLE_MAPS_API_KEY, "map_id": settings.MAP_ID}
    return render(request, "map.html", context)


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
            return redirect('trip_list')  
        return render(request, 'addTrip.html', {'form': form})
    
class TripListView(LoginRequiredMixin, View):
    def get(self, request):
        trips = Trip.objects.filter(user=request.user)
        return render(request, 'trip.html', {'trips': trips})
    
class TripDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        trip = get_object_or_404(Trip, pk=pk, user=request.user)
        form = TripForm(instance=trip)
        return render(request, 'trip_detail.html', {'form': form, 'trip': trip})

    def post(self, request, pk):
        trip = get_object_or_404(Trip, pk=pk, user=request.user)
        if 'save' in request.POST:
            form = TripForm(request.POST, instance=trip)
            if form.is_valid():
                form.save()
                return redirect('trip_detail', pk=pk)
        elif 'delete' in request.POST:
            trip.delete()
            return redirect('trip_list')
        else:
            form = TripForm(instance=trip)
        return render(request, 'trip_detail.html', {'form': form, 'trip': trip})
