from random import randint

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import connection


def signup_(request, ):
    name = request.POST.get("name")
    psw = request.POST.get("psw")
    email = request.POST.get("email")
    mobile = request.POST.get("mob")
    address = request.POST.get("address")
  #  ---- to validate duplicate signup ----
    cursor = connection.cursor()
    query = "select * from app1_users where email = '" + email + "'"
    cursor.execute(query)
    if cursor.rowcount == 0:
        # ----insert data to database----
        query = ''' insert into app1_users(name,password,email,mob,Address)values(%s,%s,%s,%s,%s)'''
        value = (name,psw,email,mobile,address)
        cursor.execute(query, value)
        msg = (" Signup success ")
        return render(request, "Profile Page")                      ############
    else:
        msg = ("This email is already exists. Try to login")
        return render(request,'login_signup.html')

