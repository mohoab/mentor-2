from django.shortcuts import render
from template import *
from .models import service 





def home(request):
    services = service.objects.filter(status=True)[:3]
    context = {
        'service':services
    }
    return render(request,"root/index.html",context=context)

def trainers(request):
    return render(request , 'root/trainers.html')

def about(request):
    return render(request , 'root/about.html')


def contact(request):
    return render(request , 'root/contact.html')

