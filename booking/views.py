from django.shortcuts import render
from sign.models import Workers
# Create your views here.
def booking(request):
    workername = request.GET.get('name')
    service = request.GET.get('service')

    return render(request, 'booking_confirmation.html',{'workername':workername, 'service':service})



def booking_done(request):
    workername = request.GET.get("WorkerName")
    service = request.GET.get("service")
    email = request.GET.get("email")
    datetime = request.GET.get("datetime")
    # Id = Workers.objects.filter(Email=email)
    return render(request, 'booking_completed.html',{'workername':workername, 'service':service, 'datetime':datetime,'id':Id})