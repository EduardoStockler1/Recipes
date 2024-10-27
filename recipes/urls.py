from django.urls import path, include 
from recipes.views import home

#dominio.com/recipes/
urlpatterns = [
    path('', home),#Home
]
