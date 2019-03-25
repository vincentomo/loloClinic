from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    context = {
        "title": "Contact Us",
    }
    return render(request, 'contact/contact.html', context)
