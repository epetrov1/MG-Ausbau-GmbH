from django.urls import path
from .views import home, contacts



urlpatterns = [
    path('', home, name="home-page"),
    path('contacts/', contacts, name="contact"),
]