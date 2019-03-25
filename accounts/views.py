from django.contrib.auth import authenticate, logout, login
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def accounts(request):
    if not request.user.is_authenticated:
        return render(request, 'account/login.html', {"message": None})
    context = {
        "user": request.user
    }
    return render(request, 'account/index.html', context=context)
def user_login(request):
    email = request.POST['email']
    password = request.POST['password']

    user = authenticate(request,  email=email, password=password)
    #return render(request, "accounts/userlogin.html")

def user_logout(request):
    logout(request)
    return render(request, "account/login.html", {"message": "Logged out Successfully!"})

def  adduser(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid:
            form.save()
            return render(request, 'account/login.html')
    else:
        form = RegistrationForm()
        context = {
            "form": form
        }
        return render(request, 'account/addUser.html', context)
def about(request):
    context = {
        "title": "About Us",
    }
    return render(request, 'account/about.html', context)

@login_required
def userProfile(request):
    user = request.user
    title = "Profile"
    context = {
        "user": user,
        'title': title
    }
    return render(request, 'account/profile.html', context)