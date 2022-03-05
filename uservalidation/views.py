from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib import messages


# Create your views here.

def loginpage(request):
    if(request.user.is_authenticated):
        pass
        user = request.user

        if(user.isWM):
            pass  # redirecting to the WM dashboard
        elif(user.isHNI):
            pass  # redirecting to the HNI dashboard
    else:
        if(request.method == "POST"):
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(email=email, password=password)
            if(user is not None):
                login(request, user)
                if(user.isWM):
                    # redirecting to the WM dashboard
                    return redirect("WealthManager:dashbaord")
                else:
                    # redirecting to the HNI dashboard
                    return HttpResponse("HNI")
            else:
                messages.error(
                    request, " email or password are wrong please try again")
                return redirect("uservalidation:loginpage")
        return render(request, "uservalidation/loginpage.html")
