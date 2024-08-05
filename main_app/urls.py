from django.urls import path, include
from . import views
from django.contrib.auth.models import User
from .views import AddTrip, TripListView, TripDetailView, AddItinerary, send_invitation

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("map", views.map, name="map"),
    path("trip/", TripListView.as_view(), name="trip_list"),
    path("addTrip", AddTrip.as_view(), name="addTrip"),
    path("trip/<int:pk>/", TripDetailView.as_view(), name="trip_detail"),
    path('trip/<int:pk>/add-itinerary/<int:day>/', AddItinerary.as_view(), name='add_itinerary'),
    path('trip/<int:trip_id>/send-invitation/', send_invitation, name='send_invitation'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", views.signup, name="signup"),
    path("accounts/login/", views.Login.as_view(), name="login"),
    path('suitcase/', views.suitcase_view, name='suitcase'),
    path('suitcase/remove/<int:pk>/', views.remove_suitcase_item, name='remove_suitcase_item'),
    path('suitcase/toggle/<int:pk>/', views.toggle_packed_status, name='toggle_packed_status'),

]
