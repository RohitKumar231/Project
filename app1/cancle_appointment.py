from django.db import connection
from django.shortcuts import render
def cancle_appointment(request):
    appointment_id= request.GET['appointment_id']
    cursor = connection.cursor()
    query = "delete from appointment where appointment_id='" + appointment_id + "'"
    cursor.execute(query)
    return render(request, "succes_cancle_appointment.html")