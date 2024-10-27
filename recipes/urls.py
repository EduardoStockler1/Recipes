from django.urls import path, include 
from recipes.views import home, about, contact, login

#dominio.com/recipes/
urlpatterns = [
    path('', home),#Home
    path('About', about),#About
    path('contact', contact),#Contact
    path('login', login)#Login

]
