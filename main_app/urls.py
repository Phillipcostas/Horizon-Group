from django.urls import path, include
from . import views
from django.contrib.auth.models import User



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('base/', views.about, name='base'),
    path('accounts/', include('django.contrib.auth.urls')),
]
