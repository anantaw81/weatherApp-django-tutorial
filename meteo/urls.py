from django.urls import path

from meteo import views

urlpatterns = [
    path("meteo/discover", views.temp_somewhere, name="temp_somewhere"),
    path("meteo/", views.temp_here, name="temp_here"),
]
