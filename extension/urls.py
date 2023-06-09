from django.contrib import admin
from django.urls import path
from .views import Pantalla,Agregar,eliminarComentario,formComentarioA,formComentarioBT,formComentarioBL,VerComentarios,eliminarPlata,formComentario,AgregarPla,FormAgregarP,eliminarRol,CambiRol,FormAgregarR,AgregarRP,CambiarRol,modiJuegos,MJuegos,eliminarJuego,Comentarios,ModificarJuegos,formAgregarMP,ModificarP,formAgregarM,formOlvidado,formSesion,Registrarse,formAgregarU,Administrador,Contacto,Login,Modificar,Olvidado,VerPerfil,WebServices,xbox,Play,Pc,Nintendo,Batman,DeadR,Animal,BMesa,plantillaMenu,formAgregarJ

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
    path('MJuegos/<int:id>', MJuegos,name="MJuegos"),
    path('ModificarJuegos', ModificarJuegos,name="ModificarJuegos"),
    path('modiJuegos', modiJuegos,name="modiJuegos"),
    path('eliminarJuego/<int:id>', eliminarJuego,name="eliminarJuego"),
    path('CambiarRol/<int:id>', CambiarRol,name="CambiarRol"),
    path('CambiRol', CambiRol,name="CambiRol"),
    path('AgregarRP', AgregarRP,name="AgregarRP"),
    path('AgregarPla', AgregarPla,name="AgregarPla"),
    path('FormAgregarR', FormAgregarR,name="FormAgregarR"),
    path('FormAgregarP', FormAgregarP,name="FormAgregarP"),
    path('eliminarRol/<int:id>', eliminarRol,name="eliminarRol"),
    path('eliminarPlata/<int:id>', eliminarPlata,name="eliminarPlata"),
    path('formComentario', formComentario,name="formComentario"),
    path('VerComentarios/<int:id>', VerComentarios,name="VerComentarios"),
    path('eliminarComentario/<int:id>', eliminarComentario,name="eliminarComentario"),
    path('formComentarioA', formComentarioA,name="formComentarioA"),
    path('formComentarioBL', formComentarioBL,name="formComentarioBL"),
    path('formComentarioBT', formComentarioBT,name="formComentarioBT"),
]