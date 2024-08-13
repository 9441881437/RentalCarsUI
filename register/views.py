from django.shortcuts import render
from .models import * 

# Create your views here.


# def register(request):
#     if request.method == 'POST':
#         a = request.POST.get('name')
#         b = request.POST.get('email')
#         c = request.POST.get('phone')
#         details = SignupModel(name = a, email = b, phone = c)
#         details.save()
#     return render(request, 'register.html')

# def login(request):
#     return render(request, 'login_page2.html')