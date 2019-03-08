from django.contrib.auth import authenticate, logout, login
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import User, Doctor, Appointment

# Create your views here.

def accounts(request):
    if not request.user.authenticated:
        return render(request, 'accounts/login.html', {"message": None})
    context = {
        "user": user.request
    }
    return render(request, 'accounts/index.html', context=context)
def login(request):
    email = request.POST["email"]
    password = request.POST["password"]

    user = authenticate(request, email=email, password = password)

    if user is None:
        return render(request, "accounts/login.html", {"message": "Invalid Credentials"})
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('home'))

def logout(request):
    logout(request)
    return render(request, "accounts/login.html", {"message": "Logged out Successfully!"})
    


def book(request, user_id ):
    try:
        doctor_id = int (request.POST['doctor'])
        user = User.objects.get(pk=user_id)
        doctor = Doctor.objects.get(pk=doctor_id)
    except KeyError:
        return render(request, 'accounts/error.html', {"message": "Make Sure you Select Doctor and User"})
    except User.DoesNotExist:
        return render(request, 'accounts/error.html', {"message": "No user."})
    except Doctor.DoesNotExist:
        return render(request, 'accounts/error.html', {"message": "No Doctor."})
    


