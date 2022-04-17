from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#def home(request):
   #return render(request,"home.html")
   #return HttpResponse('Home')


def home(request):
   return render(request, "users/home.html")