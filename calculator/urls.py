from os import name
from django.urls import include, path
from . import views
urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('',views.welcomeCalculator, name="welcomeCalculator"),
]
