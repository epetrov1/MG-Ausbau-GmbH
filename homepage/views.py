from django.shortcuts import render
from . models import HomePage
from django.core.mail import send_mail


#Home page view 
def home(request):
    home_context = HomePage.objects.get(pk=1)
    context = {
        "home_context": home_context,
    }
    return render(request, "homepage/home.html", context)


#Contsact view +sending emails
def contacts(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        send_mail(
            message_name, #subject
            message, #message
            message_email, #sender 
            ['office@mgausbaugmbh.de'], #recivers
            )        

        return render(request, "homepage/contacts.html", {'message_name': message_name})
    else:
        return render(request, "homepage/contacts.html")

