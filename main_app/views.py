from django.shortcuts import render
from django.contrib.auth.views import LoginView



def home(request):
        return render(request, 'home.html')

def about(request):
    return render(request, 'base.html')



class Home(LoginView):
    template_name = 'home.html'