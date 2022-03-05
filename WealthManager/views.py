from tkinter import Wm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from uservalidation.models import *
# Create your views here.


def dashboard(request):
    pass
    return HttpResponse("wealth Manager dashbaord")


def setup(request):
    pass
    wm = WM.objects.get(wm_id=request.user.id)
    print(request.user)
    if(request.method == "POST"):
        email = request.POST.get("email")
        firstname = request.POST.get("firstname")
        lastname = request.PSOT.get("lastname")
        hni = NewUser(email=email, firstname=firstname,
                      lastname=lastname, isHNI=True)
        hni.save()
        obj = HNI(hni_id=hni)
        obj.save()
        connectwmtohni = WMtoHNI(wm=wm, hni=hni)
        connectwmtohni.save()
        return redirect("WealthManager:setup")

    return render(request, "WealthManager/setup.html")
