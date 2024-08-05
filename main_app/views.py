from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from .models import UserProfile, Trip, Itinerary, SuitcaseItem, UserPhoto, TripPhoto, UserInterest
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .froms import TripForm, SuitcaseItemForm, UserInterestForm
=======
from .models import UserProfile, Trip, Itinerary, SuitcaseItem, UserPhoto, TripPhoto, Invitation
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .froms import TripForm, SuitcaseItemForm, ProfilePhotoForm, UserInterestForm, InvitationForm, CommentForm
>>>>>>> bee001e6df84980be2930b7a2b7235b5f815b3ba
from datetime import date, timedelta
from collections import defaultdict
from django.contrib import messages
from django.http import HttpResponseForbidden

def about(request):
    return render(request, "base.html")


def map(request):
    context = {"api_key": settings.GOOGLE_MAPS_API_KEY, "map_id": settings.MAP_ID}
    return render(request, "map.html", context)


def trip_index(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, "trip.html", {"trips": trips})



def user_interest(request):
    userProfile = UserProfile.objects.get(user=request.user)

    error_message = ""
    form = UserInterestForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            user_interest = form.save(commit=False)
            selected_1 = form.cleaned_data["question_1"]
            userProfile.interest1 = selected_1
            selected_2 = form.cleaned_data["question_2"]
            userProfile.interest2 = selected_2
            selected_3 = form.cleaned_data["question_3"]
            userProfile.interest3 = selected_3
            selected_4 = form.cleaned_data["question_4"]
            userProfile.interest4 = selected_4
            userProfile.save()
            return redirect('/')
        else:
            error_message = "Plese fill out the form before moving forward."
            return redirect('/')
    else:
        form = UserInterestForm()
    
    context = {"form": form, "error_message": error_message}
    return render(request, 'registration/interestQuestions.html', context)


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            userProfile = UserProfile.objects.create(user=user, name=user.username)
            userProfile.save()
            return redirect("interest")
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
            selected_photo = form.cleaned_data["trip_photo"]
            trip.trip_photo = selected_photo
            trip.user = request.user
            trip.save()
            return redirect("trip_list")
        return render(request, "addTrip.html", {"form": form})


class TripListView(LoginRequiredMixin, View):
    def get(self, request):
        user_trips = Trip.objects.filter(user=request.user)
        public_trips = Trip.objects.filter(public=True).exclude(user=request.user)
        return render(request, 'trip.html', {
            'user_trips': user_trips,
            'public_trips': public_trips
        })


class TripDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        trip = get_object_or_404(Trip, pk=pk)
        num_days = trip.number_of_days()
        itineraries_by_day = {}
        for day in range(1, num_days + 1):
            itineraries_by_day[day] = list(Itinerary.objects.filter(trip=trip, day=day))
        comments = trip.comments.all()
        comment_form = CommentForm()
        can_comment = trip.user == request.user or trip.can_comment(request.user)
        can_edit = trip.user == request.user
        return render(request, 'trip_detail.html', {
            'trip': trip,
            'num_days': num_days,
            'itineraries_by_day': itineraries_by_day,
            'comments': comments,
            'comment_form': comment_form,
            'can_comment': can_comment,
            'can_edit': can_edit
        })

    def post(self, request, pk):
        trip = get_object_or_404(Trip, pk=pk)
        if trip.user != request.user and not trip.can_comment(request.user):
            return redirect('trip_detail', pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.trip = trip
            comment.user = request.user
            comment.save()
        return redirect('trip_detail', pk=pk)


class AddItinerary(LoginRequiredMixin, View):
    def post(self, request, pk, day):
        trip = get_object_or_404(Trip, pk=pk)
        if trip.user != request.user:
            return HttpResponseForbidden("You are not allowed to add itineraries to this trip.")
        itinerary_name = request.POST.get("itinerary_name")
        if itinerary_name:
            Itinerary.objects.create(trip=trip, day=day, name=itinerary_name)

        return redirect('trip_detail', pk=pk)
    
def user_interest(request):
    if request.method == "POST":
        form = UserInterestForm(request.POST)
        if form.is_valid():
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile = form.save()
            trip = form.save(commit=False)


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

@login_required
def send_invitation(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, user=request.user)
    if request.method == 'POST':
        form = InvitationForm(request.POST)
        if form.is_valid():
            invitation = form.save(commit=False)
            invitation.trip = trip
            invitation.save()
            messages.success(request, f"Invitation sent to {invitation.invited_user.username}")
            return redirect('trip_detail', pk=trip.id)
    else:
        form = InvitationForm()
    return render(request, 'send_invitation.html', {'form': form, 'trip': trip})