from django.shortcuts import render
from . models import HomePage

def home(request):
    home_context = HomePage.objects.get(pk=1)
    context = {
        "home_context": home_context,
    }
    return render(request, "homepage/home.html", context)

def contacts(request):
    return render(request, "homepage/contacts.html")