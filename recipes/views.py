from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#HTTP Request <- HTTP Response

#Request

def home(request):
    ...
    return render(request, 'recipes/home.html')

def about(request):
    ...
    return render(request, 'recipes/about.html')

def contact(request):
    ...
    return render(request, 'recipes/contact.html')

def login(request):
    ...
    return render(request, 'recipes/login.html')