from django.contrib import admin
from django.urls import path
from .views import Pantalla,agregarJ,agregarP,Registrarse,formAgregarU,Administrador,Agregar,Contacto,Login,Modificar,Olvidado,VerPerfil,WebServices,xbox,Play,Pc,Nintendo,Batman,DeadR,Animal,BMesa,plantillaMenu,formAgregarJ

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
    path('xbox',xbox,name="xbox"),
    path('Play',Play,name="Play"),
    path('Pc',Pc,name="Pc"),
    path('Nintendo',Nintendo,name="Nintendo"),
    path('Batman',Batman,name="Batman"),
    path('DeadR' ,DeadR,name="DeadR"),
    path('Animal',Animal,name="Animal"),
    path('BMesa',BMesa,name="BMesa"),
    path('plantillaMenu',plantillaMenu,name="plantillaMenu"),
    path('formAgregarJ', formAgregarJ,name="formAgregarJ"),
    path('formAgregarU', formAgregarU,name="formAgregarU"),
]