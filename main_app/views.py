from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Trip, Itinerary, SuitcaseItem, UserPhoto, TripPhoto
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .froms import TripForm, SuitcaseItemForm, ProfilePhotoForm, UserInterestForm
from datetime import date, timedelta
from collections import defaultdict


def about(request):
    return render(request, "base.html")


def map(request):
    context = {"api_key": settings.GOOGLE_MAPS_API_KEY, "map_id": settings.MAP_ID}
    return render(request, "map.html", context)


def trip_index(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, "trip.html", {"trips": trips})


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


@login_required
def suitcase_view(request):
    if request.method == "POST":
        form = SuitcaseItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            # checkbox_value = form.cleaned_data['my_checkbox']

            return redirect("suitcase")
    else:
        form = SuitcaseItemForm()

    items = SuitcaseItem.objects.filter(user=request.user)
    categories = ["Essentials", "Toiletries", "Speciality Clothes", "Lounge Wear"]
    categorized_items = {
        category: items.filter(category=category) for category in categories
    }
    context = {"form": form, "categorized_items": categorized_items}
    return render(request, "suitcase.html", context)


@login_required
def remove_suitcase_item(request, pk):
    item = get_object_or_404(SuitcaseItem, pk=pk, user=request.user)
    item.delete()
    return redirect("suitcase")


@login_required
def toggle_packed_status(request, pk):
    item = get_object_or_404(SuitcaseItem, pk=pk, user=request.user)
    if "packed" in request.POST:
        item.packed = not item.packed
    if "quantity" in request.POST:
        item.quantity = request.POST.get("quantity")
    item.save()
    return redirect("suitcase")


class Home(LoginRequiredMixin, LoginView):
    def get(self, request):
        upcoming_trips, other_trips = self.get_trips(request.user)
        return render(
            request,
            "home.html",
            {
                "upcoming_trips": upcoming_trips,
                "other_trips": other_trips,
            },
        )

    def get_trips(self, user):
        today = date.today()
        ten_days_later = today + timedelta(days=10)
        upcoming_trips = Trip.objects.filter(
            user=user, start_date__range=(today, ten_days_later)
        )
        other_trips = Trip.objects.filter(user=user).exclude(
            start_date__range=(today, ten_days_later)
        )
        return upcoming_trips, other_trips


class Login(LoginView):
    template_name = "login.html"


class AddTrip(LoginRequiredMixin, View):
    trip_photos = TripPhoto.objects.all

    def get(self, request):
        form = TripForm()
        return render(request, "addTrip.html", {"form": form})

    def post(self, request):
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.user = request.user
            trip.save()
            return redirect("trip_list")
        return render(request, "addTrip.html", {"form": form})


class TripListView(LoginRequiredMixin, View):
    def get(self, request):
        trips = Trip.objects.filter(user=request.user)
        return render(request, "trip.html", {"trips": trips})


class TripDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        trip = get_object_or_404(Trip, pk=pk, user=request.user)
        trip_photo_id = trip.trip_photo_id
        trip_photo = TripPhoto.objects.filter(id=trip_photo_id)
        photo = trip_photo[0]
        num_days = trip.number_of_days()
        itineraries_by_day = {}
        for day in range(1, num_days + 1):
            itineraries_by_day[day] = list(Itinerary.objects.filter(trip=trip, day=day))
        return render(
            request,
            "trip_detail.html",
            {
                "trip": trip,
                "num_days": num_days,
                "itineraries_by_day": itineraries_by_day,
                "photo": photo,
            },
        )


class AddItinerary(LoginRequiredMixin, View):
    def post(self, request, pk, day):
        trip = get_object_or_404(Trip, pk=pk, user=request.user)
        itinerary_name = request.POST.get("itinerary_name")
        if itinerary_name:
            Itinerary.objects.create(trip=trip, day=day, name=itinerary_name)
            print(f"Added itinerary: {itinerary_name} to day: {day}")  # Debugging line
        else:
            print("Itinerary name is empty")  # Debugging line

        return redirect("trip_detail", pk=pk)


def profile(request):
    userProfile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        form = ProfilePhotoForm(request.POST)
        if form.is_valid():
            selected_photo = form.cleaned_data["profile_photo"]
            userProfile.profile_photo = selected_photo
            userProfile.save()
            return redirect("profile")
    else:
        form = ProfilePhotoForm()

    context = {
        "userProfile": userProfile,
        "form": form,
    }
    return render(request, "profile.html", context)

        return redirect('trip_detail', pk=pk)
    
def user_interest(request):
    if request.method == "POST":
        form = UserInterestForm(request.POST)
        if form.is_valid():
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile = form.save()
            trip = form.save(commit=False)

