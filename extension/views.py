from django.shortcuts import render, redirect
from .models import pregunta, rol, usuario, videojuego, comentario, plataforma
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

# Create your views here.

def Pantalla(request):
    return render(request,'extension/Pantalla.html')

def Registrarse(request):
    listaPreguntas = pregunta.objects.all()
    contexto = {
        "preguntas": listaPreguntas
    }

    return render(request,'extension/Registrarse.html', contexto)
def Administrador(request):
    return render(request,'extension/administrador.html')
def Contacto(request):
    logout(request)
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

    

def Agregar(request):
    listaPlataforma = plataforma.objects.all()
    contexto = {
        "Plataformas": listaPlataforma
    }
    return render(request,'extension/AgregarJuego.html', contexto)

def formAgregarJ(request):
    
    vNombreJ = request.POST['NombreJ']
    vDescripcion = request.POST['DescripcionJ']
    vTrailer     = request.POST['TrailerJ']
    vFotoJ       = request.FILES.get('SeleccioneJ',"")
    vLink        = request.POST['LinkJ']
    vPlataforma  = request.POST['plataforma']

    vRegistroPlataforma = plataforma.objects.get(id_plataforma=vPlataforma)
    videojuego.objects.create( nombreV=vNombreJ, descripcion=vDescripcion,  
                              trailer=vTrailer, foto=vFotoJ,link=vLink , plataforma_id=vRegistroPlataforma)
    
    if vRegistroPlataforma.id_plataforma==4:
        return redirect ('Pc')
    if vRegistroPlataforma.id_plataforma==1:
        return redirect ('xbox')
    if vRegistroPlataforma.id_plataforma==3:
        return redirect ('Play')
    if vRegistroPlataforma.id_plataforma==2:
        return redirect ('Nintendo')
    

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
    vRol = 1 
    vRegistroRol = rol.objects.get(id_rol=vRol)

    vRegistroPregunta = pregunta.objects.get(id_pregunta = vPregunta)
    usuario.objects.create(nombreU=vNombreU, apellido=vApellidoU, clave=vClaveU, correo=vCorreoU, 
                            telefono=vTelefonoU, fechaU=vFechaU, fotoU=vFotoU, pregunta_id_pregunta=vRegistroPregunta, respuesta=vRespuesta, rol_id_rol=vRegistroRol) 
    
    user = User.objects.create_user(vCorreoU,vCorreoU, vClaveU)
    return redirect('Registrarse')


def formSesion(request):
    try:
        vCorreo = request.POST['loginEmail']
        vClave = request.POST['loginPassword']
        vRol = 0
        
        registro = usuario.objects.all()


        for rol in registro:
            if rol.correo == vCorreo and rol.clave == vClave:

                    
                    vRol = rol.rol_id_rol.id_rol
        print(vRol)
        print(vClave)
        user1 = User.objects.get(username = vCorreo)
        print(user1)
        pass_valida = check_password(vClave,user1.password)

        if not pass_valida:
            messages.error(request,"El usuario o la contraseña son incorrectos")
            return redirect('Login')

        user = authenticate(username=vCorreo,password = vClave)

        print(user)
        if user is not None:
            if vRol == 1:
                login(request,user)
                return redirect('Pantalla')
                

            if vRol == 2:
                login(request,user)
                return redirect('Administrador') 

            if vRol == 0:
                messages.success(request, "Usuario no registrado")
                return redirect('Login')
    except User.DoesNotExist:
            messages.error(request,"El usuario o la contraseña son incorrecto123")
            return redirect('Login')
    except Exception as e:
        print(e)
