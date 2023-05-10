from django.contrib import admin
from django.urls import path
from .views import Pantalla,Registrarse

urlpatterns = [
    path('',Pantalla,name="Pantalla"),
    path('Registrarse',Registrarse,name="Registrarse"),
]