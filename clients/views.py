from django.shortcuts import render
from django.http import HttpResponse
from .models import Client


# Create your views here.

# /clients  -> index
def index(request):
    # Contact.objects.filter()
    clients = Client.objects.all()
    # return HttpResponse('Hello World')
    return render(request, 'index.html', {'clients': clients})


def new(request):
    return HttpResponse('New Contacts')
