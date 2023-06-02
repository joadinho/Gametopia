from django.shortcuts import render, redirect
from .models import pregunta, rol, usuario, videojuego, comentario, plataforma
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
# Create your views here.
def Pantalla(request):
    return render(request,'extension/Pantalla.html')

def Registrarse(request):
    return render(request,'extension/Registrarse.html')
def Administrador(request):
    return render(request,'extension/administrador.html')
def Agregar(request):
    return render(request,'extension/AgregarJuego.html')
def Contacto(request):
    return render(request,'extension/Contacto.html')
def Login(request):
    return render(request,'extension/Login.html')
def Modificar(request):
    return render(request,'extension/Modificar.html')
def Olvidado(request):
    return render(request,'extension/olvidado.html')
def VerPerfil(request):
    return render(request,'extension/ver perfil.html')
def WebServices(request):
    return render(request,'extension/webServices.html')
def xbox(request):
    return render(request,'extension/Exclusivo Xbox/xbox.html')
def Play(request):
    return render(request,'extension/Exclusivo Play/playstation.html')
def Pc(request):
    return render(request,'extension/Exclusivo PC/pc.html')
def Nintendo(request):
    return render(request,'extension/Exclusivo Nintendo/nintendo.html')
def Batman(request):
    return render(request,'extension/Exclusivo Play/BATMAN_ARKHAM_KNIGHT.html')
def DeadR(request):
    return render(request,'extension/Exclusivo Xbox/deadrising.html')
def Animal(request):
    return render(request,'extension/Exclusivo Nintendo/ANIMAL CROSSING.html')
def BMesa(request):
    return render(request,'extension/Exclusivo PC/BLACK MESA.html')
def plantillaMenu(request):
    return render(request,'extension/plantillaMenu.html')

def agregarP(request):
    listaPreguntas = pregunta.objects.all()
    contexto = {
        "preguntas": listaPreguntas
    }

    return render(request,'extension/Registrarse.html', contexto)

def agregarJ(request):
    listaPlataforma = plataforma.objects.all()
    contexto = {
        "Plataformas": listaPlataforma
    }

    return render(request,'extension/AgregarJuego.html', contexto)

def formAgregarJ(request):
    vIdjuego = request.POST['id_juego']
    vNombreJ = request.POST['NombreJ']
    vDescripcion = request.POST['DescripcionJ']
    vTrailer     = request.POST['TraileJ']
    vFotoJ       = request.FILES['SeleccioneJ']
    vLink        = request.POST['LinkJ']
    vPlataforma  = request.POST['plataforma']

    vRegistroPlataforma = plataforma.objects.get(codigoJ=vPlataforma)
    videojuego.objects.create(id_videojuego=vIdjuego, nombreV=vNombreJ, descripcion=vDescripcion,  trailer=vTrailer, foto=vFotoJ,link=vLink , plataforma_id=vRegistroPlataforma)
    return redirect('AgregarJuego')

def formAgregarU(request):
    vNombreU = request.POST['nombre']
    vApellidoU = request.POST['apellido']
    vClaveU = request.POST['password']
    vCorreoU = request.POST['email']  
    vPregunta=request.POST['pregunta']
    vRespuesta=request.POST['respuesta']
    vTelefonoU = request.POST['telefono']
    vFechaU = request.POST['fecha']
    vFotoU = request.FILES['fotoU']

    vRegistroPregunta = pregunta.objects.get(codigo = vPregunta)
    usuario.objects.create(nombreU=vNombreU, apellido=vApellidoU, clave=vClaveU, correo=vCorreoU, 
                            telefono=vTelefonoU, fechaU=vFechaU, fotoU=vFotoU, pregunta_id_pregunta=vRegistroPregunta, respuesta=vRespuesta) 
    return redirect('Registrarse')