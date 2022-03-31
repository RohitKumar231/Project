from django.db import connection
from django.shortcuts import render
def update_appointment(request):
    appointment_id = request.GET['appointment_id']
    Time= request.GET['time']
    Date = request.GET['date']
    Location = request.GET['location']
    cursor = connection.cursor()
    query = "update appointment set (Time,Date,Location) values(%S,%s,%s) where appointment_id='" + appointment_id + "'"
    value = (Time,Date,Location)
    cursor.execute(query, value)
    return render(request, "sucess_update_appointment.html")