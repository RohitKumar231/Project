from django.db import connection
from django.shortcuts import render
def register_for_profession(request):
    Name = request.GET['name']
    Age = request.GET['age']
    Contact_number = request.GET['contact_no']
    Adhar_number = request.GET['adhar_number']
    Password = request.GET['psw']
    Email = request.GET['email']
    Address = request.GET['address']
    cursor = connection.cursor()
    query = "insert into worker(Name,Age,Email,Password,Contact_number,Adhar_number,Address) values (%s,%s,%s,%s,%s,%s,%s)"
    value = (Name,Age,Email,Password,Contact_number,Adhar_number,Address)
    cursor.execute(query, value)
    return render(request, "sucess_registerforprofession.html")