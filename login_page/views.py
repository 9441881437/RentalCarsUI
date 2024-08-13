from django.shortcuts import render
from login_page.models import *
from register.models import *

# Create your views here.

def greet(request):
    return render(request, 'hello.html')

def login(request):
    if request.method == 'POST':
        a = request.POST.get('username')
        b = request.POST.get('password')
        display = LoginModels(username = a, password = b)
        display.save()
    return render(request, 'login_page2.html')


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        details = SignupModel(name = a, email = b, phone = c)
        details.save()
    return render(request, 'register.html')

def car_booking(request):
    return render(request, 'cars_page.html')