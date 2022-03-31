from django.db import connection
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request, "aboutus.html")
def login_signup(request):
    return render(request, "login_signup.html")

def update_appointment_page(request):
    appointment_id= request.GET['appointment_id']
    data={'id': appointment_id }
    return render(request, "update_appointment.html",data)
