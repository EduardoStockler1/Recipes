from django.urls import path, include 
from . import views

#dominio.com/recipes/
urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]
