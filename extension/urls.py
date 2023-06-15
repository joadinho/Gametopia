from django.contrib import admin
from django.urls import path
from .views import Pantalla,Agregar,Comentarios,ModificarJuegos,formAgregarMP,ModificarP,formAgregarM,formOlvidado,formSesion,Registrarse,formAgregarU,Administrador,Contacto,Login,Modificar,Olvidado,VerPerfil,WebServices,xbox,Play,Pc,Nintendo,Batman,DeadR,Animal,BMesa,plantillaMenu,formAgregarJ

urlpatterns = [
    path('',Pantalla,name="Pantalla"),
    path('Registrarse',Registrarse,name="Registrarse"),
    path('Administrador',Administrador,name="Administrador"),
    path('Agregar',Agregar,name="Agregar"),
    path('Contacto',Contacto,name="Contacto"),
    path('Login',Login,name="Login"),
    path('Modificar',Modificar,name="Modificar"),
    path('Olvidado',Olvidado,name="Olvidado"),
    path('VerPerfil/<int:id>',VerPerfil,name="VerPerfil"),
    path('WebServices',WebServices,name="WebServices"),
    path('xbox',xbox,name="xbox"),
    path('Play',Play,name="Play"),
    path('Pc',Pc,name="Pc"),
    path('Nintendo',Nintendo,name="Nintendo"),
    path('Batman/<int:id>',Batman,name="Batman"),
    path('DeadR/<int:id>' ,DeadR,name="DeadR"),
    path('Animal/<int:id>',Animal,name="Animal"),
    path('BMesa/<int:id>',BMesa,name="BMesa"),
    path('plantillaMenu/<int:id>',plantillaMenu,name="plantillaMenu"),
    path('formAgregarJ', formAgregarJ,name="formAgregarJ"),
    path('formAgregarU', formAgregarU,name="formAgregarU"),
    path('formSesion', formSesion,name="formSesion"),
    path('formOlvidado', formOlvidado,name="formOlvidado"),
    path('formAgregarM', formAgregarM,name="formAgregarM"),
    path('ModificarP/<int:id>', ModificarP,name="ModificarP"),
    path('formAgregarMP', formAgregarMP,name="formAgregarMP"),
    path('Comentarios', Comentarios,name="Comentarios"),
    path('ModificarJuegos', ModificarJuegos,name="ModificarJuegos"),
]