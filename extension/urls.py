from django.contrib import admin
from django.urls import path
from .views import Pantalla,Agregar,Comentarios,ModificarJuegos,formAgregarMP,ModificarP,formAgregarM,formOlvidado,formSesion,Registrarse,formAgregarU,Administrador,Contacto,Login,Modificar,Olvidado,VerPerfil,WebServices,xbox,Play,Pc,Nintendo,Batman,DeadR,Animal,BMesa,plantillaMenu,formAgregarJ

urlpatterns = [
    
    path('Pantalla/<int:id>',Pantalla,name="Pantalla"),
    path('Registrarse',Registrarse,name="Registrarse"),
    path('Administrador',Administrador,name="Administrador"),
    path('Agregar',Agregar,name="Agregar"),
    path('Contacto/<int:id>',Contacto,name="Contacto"),
    path('',Login,name="Login"),
    path('Modificar',Modificar,name="Modificar"),
    path('Olvidado',Olvidado,name="Olvidado"),
    path('VerPerfil/<int:id>',VerPerfil,name="VerPerfil"),
    path('WebServices',WebServices,name="WebServices"),
    path('xbox/<int:id>',xbox,name="xbox"),
    path('Play/<int:id>',Play,name="Play"),
    path('Pc/<int:id>',Pc,name="Pc"),
    path('Nintendo/<int:id>',Nintendo,name="Nintendo"),
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