from http.client import HTTPSConnection
from tkinter import Wm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from uservalidation.models import *
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, check_password

import random
# Create your views here.


def dashboard(request):
    pass
    wm = WM.objects.get(wm_id=request.user.id)
    hnis = WMtoHNI.objects.filter(wm=wm)
    if(request.method == "POST"):
        o = WMtoHNI.objects.get(id=int(request.POST.get("hni")))
        hni = HNI.objects.get(hni=o.hni)
        date = request.POST.get("date")
        print(hni)
        print(date)

    return render(request, "WealthManager/dashboard.html", {"hnis": hnis})


def setup(request):
    pass
    wm = WM.objects.get(wm_id=request.user.id)
    if(request.method == "POST"):
        email = request.POST.get("email")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = generatePassword()
        hni = NewUser(email=email, firstName=firstname,
                      lastName=lastname, isHNI=True, password=make_password(password))
        hni.save()
        obj = HNI(hni_id=hni)
        obj.save()
        connectwmtohni = WMtoHNI(wm=wm, hni=obj)
        connectwmtohni.save()
        # -------------SENDING MAIL-----------------

        body = '''Dear {name},            
    Your account is created successfully 
    Your login credentials are as given:
        Username: {username}
        Password: {password}
    You can change your password by logining into our application

                                    -Thank you
                                    
                                        
                                    '''.format(name=hni.getFullName(), username=hni.email, password=password)

        send_mail(
            'Welcome to DBS', body, 'bankproject23@gmail.com', [hni.email], fail_silently=False)

        # -------------SENDING MAIL-----------------

        return redirect("WealthManager:setup")

    return render(request, "WealthManager/setup.html")


def generatePassword():
    series = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = "".join(random.sample(series, 6))
    return password
