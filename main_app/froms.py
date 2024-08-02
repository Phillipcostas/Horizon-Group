# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Trip, SuitcaseItem
from django.conf import settings


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text="Required. Enter a valid email address."
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

    class Meta:
        model = Trip
        fields = ["name", "location", "start_date", "end_date"]
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
        fields = ['name', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Item name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'packed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

        
        }
