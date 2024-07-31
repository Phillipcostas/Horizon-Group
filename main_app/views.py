from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



def about(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'map.html')

def about(request):
    return render(request, 'trip.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = UserCreationForm()
        context = {'form': form, 'error_message': error_message}
        return render(request, 'signup.html', context)





class Home(LoginView):
    template_name = 'home.html'

class LoginView(LoginView):
    template_name = 'login.html'

class Map(LoginView):
    template_name = 'map.html'

class Trip(LoginView):
    template_name = 'trip.html'        

class AddTrip(LoginView):
    template_name = 'addTrip.html'        