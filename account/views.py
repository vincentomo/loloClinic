from django.contrib.auth import authenticate, logout, login
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

def accounts(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/userlogin.html', {"message": None})
    context = {
        "user": request.user
    }
    return render(request, 'accounts/index.html', context=context)
def user_login(request):
    #email = request.POST['email']
    #password = request.POST['password']

    #user = authenticate(request,  email=email, password=password)
    return render(request, "accounts/login.html")

def user_logout(request):
    logout(request)
    return render(request, "accounts/userlogin.html", {"message": "Logged out Successfully!"})

def  adduser(request):
    pass

def adddoctor(request):
    pass

def about(request):
    context = {
        "title": "About Us",
    }
    return render(request, 'accounts/about.html', context)
