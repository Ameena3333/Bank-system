from django.urls import path
from . import views

app_name = "WealthManager"

urlpatterns = [
    path("", views.dashboard, name="dashbaord"),
    path("setup/", views.setup, name="setup")
]
