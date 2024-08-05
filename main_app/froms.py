# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Trip, SuitcaseItem, TripPhoto, UserInterest, Comment, Invitation, UserPhoto, UserProfile
from django.conf import settings


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text="Required. Enter a valid email address."
    )
    profile_photo = trip_photo = forms.ModelChoiceField(
        queryset=TripPhoto.objects.all(),
        label="Trip Photo"
    )
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class TripForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Give your trip a name!"}),
        label="Trip Name",
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Where is your trip?"}),
        label="Location",
    )

    class TripForm(forms.Form):
        trip_photo = forms.ModelChoiceField(
        queryset=TripPhoto.objects.all(),
        label="Trip Photo"
    )
    public = forms.BooleanField(
        required=False,
        initial=False,
        label="Make this trip public"
    )

    class Meta:
        model = Trip
        fields = ["name", "location", "start_date", "end_date", "trip_photo", "public"]
        widgets = {
            "start_date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Select a start date", "type": "date"},
            ),
            "end_date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Select an end date", "type": "date"},
            ),
        }


class SuitcaseItemForm(forms.ModelForm):
    class Meta:
        model = SuitcaseItem
        fields = ['name', 'category', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Item name', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
        }

class ProfilePhotoForm(forms.ModelForm):
    class ProfilePhotoForm(forms.Form):
        profile_photo = forms.ModelChoiceField(
            queryset=UserPhoto.objects.all(), label="User Photo"
        )

    class Meta:
        model = UserProfile
        fields = ["profile_photo"]

class UserInterestForm(forms.ModelForm):
    class Meta:
        model = UserInterest
        fields = ['question_1', 'question_2', 'question_3', 'question_4']
        widgets = {
            'question_1': forms.Select(attrs={'class': 'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class InvitationForm(forms.ModelForm):
    invited_user = forms.ModelChoiceField(queryset=User.objects.all(), label="Invite User")

    class Meta:
        model = Invitation
        fields = ['invited_user', 'can_comment']

