from django.urls import path
from . import views

app_name = "uservalidation"

urlpatterns = [
    path("", views.loginpage, name="loginpage"),
]
