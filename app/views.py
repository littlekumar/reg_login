from django.shortcuts import render

# Create your views here.


def home(requests):
    return render(requests,'home.html')

def login(request):
    return render(request,'reg_login/login.html')

def register(request):
    return render(request,'reg_login/registration.html')

