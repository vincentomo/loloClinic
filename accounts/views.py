from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def accounts(request):
    context = {
        "title": "Home",
    }
    return render(request, 'accounts/base.html', context=context)
