
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Users
from django.contrib import messages


# Create your views here.
def signup_login(request):
    return render(request, 'login_signup.html')


def signup(request):
    name = request.POST.get("name")
    psw = request.POST.get("psw")
    email = request.POST.get("email")
    mobile = request.POST.get("mob")
    address = request.POST.get("address")
    if Users.objects.filter(Email=email).exists():
        return redirect('signup')                     ####### Need to improve
    else:
        users = Users(name=name, mob=mobile, Address=address, Email=email, password=psw)
        users.save()
        messages.success(request, 'Signup Success')         ############
        return HttpResponse('Signup fxn')


def signin(request):
    email = request.POST.get("email")
    psw = request.POST.get("psw")
    if Users.objects.filter(Email=email,password=psw):
        messages.success(request,'Log In Success')          ##########
        return render(request,'profile.html')               ###########
    else:
        messages.warning(request,'Email/Password is Incorrect')
        return redirect('signup_login')
