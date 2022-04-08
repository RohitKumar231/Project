from django.shortcuts import render
from sign.models import Workers

# Create your views here.
def service(request):
    service = request.GET.get("service")
    x = Workers.objects.filter(service=service)
    return render(request, 'services.html', {'service': service,'rows':x})


# def services(request):
#     workername = request.GET.get("WorkerName")
#     service = request.GET.get("service")
#     datetime = request.GET.get("datetime")
#     data = { 'workername': workername,'datetime':datetime,'service':service}
#     return render(request, 'services.html',data)
