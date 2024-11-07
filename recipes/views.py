from django.shortcuts import render

# Create your views here.

#HTTP Request <- HTTP Response

#Request

def home(request):
    ...
    return render(request, 'recipes/pages/home.html')