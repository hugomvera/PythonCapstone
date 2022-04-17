from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


# Create your views here.

# /contacts  -> index
def index(request):
    # Contact.objects.filter()
    contacts = Contact.objects.all()
    # return HttpResponse('Hello World')
    return render(request, 'index.html', {'contacts': contacts})


def new(request):
    return HttpResponse('New Contacts')
