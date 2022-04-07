from django.shortcuts import render

# Create your views here.
def booking(request):
    workername = request.GET.get('name')
    service = request.GET.get('service')
    print(workername,service)
    return render(request, 'booking_confirmation.html',{'workername':workername, 'service':service})



def booking_done(request):
    workername = request.GET.get('name')
    service = request.GET.get('service')
    print(workername,service)
    return render(request, 'booking_confirmation.html',{'workername':workername, 'service':service})