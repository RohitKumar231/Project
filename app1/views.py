from django.db import connection
from django.shortcuts import render


# Create your views here.
from .login import login_
from .Signup import signup_

def home(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request, "aboutus.html")

def login_signup(request):
    return render(request, "login_signup.html")



def login(request):
    return login_(request)

def signup (request):
    return signup_(request)


def update_appointment_page(request):
    appointment_id= request.GET['appointment_id']
    data={'id': appointment_id }
    return render(request, "update_appointment.html",data)
