# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import (
    Trip,
    SuitcaseItem,
    TripPhoto,
    UserInterest,
    Comment,
    Invitation,
    UserPhoto,
)
from django.conf import settings
from django.forms import ModelForm, Textarea
from django.utils.safestring import mark_safe


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text="Required. Enter a valid email address."
    )
    profile_photo = trip_photo = forms.ModelChoiceField(
        queryset=TripPhoto.objects.all(), label="Trip Photo"
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ImagePreviewWidgetTrip(forms.RadioSelect):
    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
        )
        if value:
            photo_id = value.value if hasattr(value, "value") else value
            try:
                photo = TripPhoto.objects.get(pk=photo_id)
                option["label"] = mark_safe(
                    f'<img src="{photo.url}" alt="{photo.name}" style="width: 100px; height: 100px; object-fit: cover;">'
                )
            except TripPhoto.DoesNotExist:
                pass
        return option

class TripForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Give your trip a name!"}),
        label="Trip Name",
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Where is your trip?"}),
        label="Location",
    )
    trip_photo = forms.ModelChoiceField(
        queryset=TripPhoto.objects.all(),
        widget=ImagePreviewWidgetTrip,
        empty_label=None,
        label="Choose a Trip photo",
    )
    public = forms.BooleanField(
        required=False, initial=False, label="Make this trip public"
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
        fields = ["name", "category", "quantity"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Item name", "class": "form-control"}
            ),
            "category": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"min": 1, "class": "form-control"}),
        }


class ImagePreviewWidgetProfile(forms.RadioSelect):
    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option = super().create_option(
            name, value, label, selected, index, subindex, attrs
        )
        if value:
            photo_id = value.value if hasattr(value, "value") else value
            try:
                photo = UserPhoto.objects.get(pk=photo_id)
                option["label"] = mark_safe(
                    f'<img src="{photo.url}" alt="{photo.name}" style="width: 100px; height: 100px; object-fit: cover;">'
                )
            except UserPhoto.DoesNotExist:
                pass
        return option


class ProfilePhotoForm(forms.Form):
    profile_photo = forms.ModelChoiceField(
        queryset=UserPhoto.objects.all(),
        widget=ImagePreviewWidgetProfile,
        empty_label=None,
        label="Choose a profile photo",
    )


class UserInterestForm(forms.ModelForm):
    class Meta:
        model = UserInterest
        fields = ["question_1", "question_2", "question_3", "question_4"]
        widgets = {
            "question_1": forms.Select(attrs={"class": "form-control"}),
            "question_2": forms.Select(attrs={"class": "form-control"}),
            "question_3": forms.Select(attrs={"class": "form-control"}),
            "question_4": forms.Select(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class InvitationForm(forms.ModelForm):
    invited_user = forms.ModelChoiceField(
        queryset=User.objects.all(), label="Invite User"
    )

    class Meta:
        model = Invitation
        fields = ["invited_user", "can_comment"]
