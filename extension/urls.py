from django.contrib import admin
from django.urls import path
from .views import Pantalla,Registrarse,Administrador,Agregar,Contacto,Login,Modificar,Olvidado,VerPerfil,WebServices,Xbox,Play,Pc,Nintendo

urlpatterns = [
    path('',Pantalla,name="Pantalla"),
    path('Registrarse',Registrarse,name="Registrarse"),
    path('Administrador',Administrador,name="Administrador"),
    path('Agregar',Agregar,name="Agregar"),
    path('Contacto',Contacto,name="Contacto"),
    path('Login',Login,name="Login"),
    path('Modificar',Modificar,name="Modificar"),
    path('Olvidado',Olvidado,name="Olvidado"),
    path('VerPerfil',VerPerfil,name="VerPerfil"),
    path('WebServices',WebServices,name="WebServices"),
    path('Xbox',Xbox,name="Xbox"),
    path('Play',Play,name="Play"),
    path('Pc',Modificar,name="Modificar"),
    path('Nintendo',Nintendo,name="Nintendo"),

]