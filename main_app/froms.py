# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Trip
from django.conf import settings

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class TripForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Give your trip a name!'}),
        label='Trip Name'
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Where is your trip?'}),
        label='Location'
    )
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'MM-DD-YYYY', 'type': 'text'}),
        label='Start Date',
        input_formats=['%m-%d-%Y']
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'MM-DD-YYYY', 'type': 'text'}),
        label='End Date',
        input_formats=['%m-%d-%Y']
    )

    class Meta:
        model = Trip
        fields = ['name', 'location', 'start_date', 'end_date']
        
