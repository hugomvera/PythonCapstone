from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Player

# Create your views here.
from django.http import HttpResponse

# def home(request):
# return render(request,"home.html")
# return HttpResponse('Home')


def home(request):
    return render(request, "users/home.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def users(request):
    users = Player.objects.all()
    return render(request, "users.html", {"players": users})


def user(request):
    user = Player.balance
    return render(request, "withdraw.html", {"player": user})


def updateuser(request):
    test = request.POST.get("newbalance", "")
    response_data = {}
