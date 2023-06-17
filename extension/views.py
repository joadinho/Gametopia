from django.shortcuts import render, redirect
from .models import pregunta, rol, usuario, videojuego, comentario, plataforma
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

# Create your views here.

def Pantalla(request,id):
    if id == 0:
        return render(request,'extension/Pantalla.html')
    lista = usuario.objects.get(idUsuario=id)
    contexto = {
        "Panta": lista
    }
    return render(request,'extension/Pantalla.html',contexto)

def Comentarios(request):
    listaUsuarios = usuario.objects.all()
    listaComentarios = comentario.objects.all()
    contexto = {
    "usuarios": listaUsuarios,
    "comentarios": listaComentarios

    }
    return render(request,'extension/Comentarios.html',contexto)

def ModificarJuegos(request):
    lista = videojuego.objects.all()
    contexto = {
        "ModificarV": lista
    }
    return render(request,'extension/ModificarJuegos.html',contexto)

def MJuegos(request,id):
    PlataM = plataforma.objects.all()
    VideoM = videojuego.objects.get(id_videojuego = id)
    contexto = {
        "lista_plataformas": PlataM,
        "datos": VideoM
    }
    return render(request,'extension/MJuegos.html',contexto)

def modiJuegos(request):

    vFotoM = request.FILES.get('fotoMV' , '')
    vIDV = request.POST['idV']
    vNombreV = request.POST['nombreV']
    vDesc = request.POST['descripcion']
    vTrailerV = request.POST['trailer']
    vLinkV = request.POST['link']
    vPlataM = request.POST['plataformaM']
                  
    VideojuegoModi = videojuego.objects.get(id_videojuego = vIDV)
    VideojuegoModi.nombreV = vNombreV
    VideojuegoModi.descripcion = vDesc
    VideojuegoModi.trailer = vTrailerV
    VideojuegoModi.link = vLinkV

    registroPlataM = plataforma.objects.get(id_plataforma = vPlataM)
    VideojuegoModi.plataforma_id = registroPlataM

    if vFotoM!='':
        VideojuegoModi.foto=vFotoM

    VideojuegoModi.save()
    return redirect('ModificarJuegos')

def eliminarJuego(request,id):
    EliminarV = videojuego.objects.get(id_videojuego = id)
    EliminarV.delete()
    return redirect('ModificarJuegos')

def Registrarse(request):
    listaPreguntas = pregunta.objects.all()
    contexto = {
        "preguntas": listaPreguntas
    }

    return render(request,'extension/Registrarse.html', contexto)

def CambiarRol(request,id):
    usuariosC = usuario.objects.get(idUsuario = id)
    rolesC = rol.objects.all()

    contexto={
        "usuarioCa": usuariosC,
        "RolesU": rolesC
    }
    return render(request,'extension/CambiarRol.html', contexto)

def Administrador(request):
    listaUsuarios = usuario.objects.all()
    listaRoles = rol.objects.all()

    contexto = {
        "usuarios": listaUsuarios,
        "Roles" : listaRoles
    }
    return render(request,'extension/administrador.html', contexto)

def CambiRol(request):
    vID = request.POST['IDU']
    vCorreoC = request.POST['NombreUC']
    vRolC = request.POST['RolC']

    RolCambiar = usuario.objects.get(idUsuario = vID)
    RolCambiar.correo = vCorreoC
    
    registroRolC = rol.objects.get(id_rol = vRolC)
    RolCambiar.rol_id_rol = registroRolC

    RolCambiar.save()
    return redirect('Administrador')

def Contacto(request,id):
    if id == 0:
        return render(request,'extension/Contacto.html')
    lista = usuario.objects.get(idUsuario=id)
    contexto = {
        "contac": lista
    }

    return render(request,'extension/Contacto.html',contexto)

def Login(request):
    logout(request)
    return render(request,'extension/Login.html')

def Modificar(request):

    return render(request,'extension/Modificar.html')

def eliminarRol(request,id):
    EliminarR = rol.objects.get(id_rol = id)
    EliminarR.delete()
    return redirect('AgregarRP')

def eliminarPlata(request,id):
    EliminarP = plataforma.objects.get(id_plataforma = id)
    EliminarP.delete()
    return redirect('AgregarPla')

def AgregarRP(request):
    listaRols = rol.objects.all()
    
    contexto={
        "Roles" : listaRols
        
    }
    return render(request,'extension/AgregarRP.html',contexto)

def AgregarPla(request):
    listaPlat = plataforma.objects.all()
    
    contexto={
        "Plataforma" : listaPlat
    }
    return render(request,'extension/AgregarPla.html',contexto)

def FormAgregarR(request):

    vRolN = request.POST['RolName']
    rol.objects.create( nombreR=vRolN )

    return redirect('AgregarRP')

def FormAgregarP(request):

    vPlata = request.POST['PlataformaName']
    plataforma.objects.create( nombrePLA=vPlata )

    return redirect('AgregarPla')

def ModificarP(request,id):
    lista = usuario.objects.get(idUsuario=id)
    contexto={
        "ModificarP":lista
    }

    return render(request,'extension/ModificarP.html',contexto)

def Olvidado(request):
    
    listaPreguntas = pregunta.objects.all()
    contexto = {
        "preguntas": listaPreguntas
    }
    return render(request,'extension/olvidado.html', contexto)

def VerPerfil(request,id):

    lista = usuario.objects.get(idUsuario=id)
    contexto = {
        "usuarios": lista
    }

    return render(request,'extension/ver perfil.html', contexto)

def WebServices(request):
    return render(request,'extension/webServices.html')

def xbox(request,id):
    if id == 0:
        listaJuegos = videojuego.objects.filter(plataforma_id = 1)
        contexto = {
            "juegos": listaJuegos
        }
        return render(request,'extension/Exclusivo Xbox/xbox.html',contexto)
    
    lista = usuario.objects.get(idUsuario=id)
    listaJuegos = videojuego.objects.filter(plataforma_id = 1)
    contexto = {
        "xbo": lista,
        "juegos": listaJuegos
    }

    return render(request,'extension/Exclusivo Xbox/xbox.html', contexto)

def Play(request,id):
    if id == 0:
        listaJuegos = videojuego.objects.filter(plataforma_id = 3)
        contexto = {
            "juegos1": listaJuegos
        }
        return render(request,'extension/Exclusivo Play/playstation.html',contexto)

    lista = usuario.objects.get(idUsuario=id)
    listaJuegos = videojuego.objects.filter(plataforma_id = 3)
    contexto = {
        "Pla": lista,
        "juegos1": listaJuegos
    }
    return render(request,'extension/Exclusivo Play/playstation.html', contexto)

def Pc(request,id):
    if id == 0:
        listaJuegos = videojuego.objects.filter(plataforma_id = 4)
        contexto = {
            "juegos2": listaJuegos
        }
        return render(request,'extension/Exclusivo PC/pc.html',contexto)
    
    lista = usuario.objects.get(idUsuario=id)
    listaJuegos = videojuego.objects.filter(plataforma_id = 4)
    contexto = {
        "PC": lista,
        "juegos2": listaJuegos
    }
    return render(request,'extension/Exclusivo PC/pc.html',contexto)

def Nintendo(request, id):
    if id == 0:
        listaJuegos = videojuego.objects.filter(plataforma_id = 2)
        contexto = {
            "juegos3": listaJuegos
        }
        return render(request,'extension/Exclusivo Nintendo/nintendo.html',contexto)
    lista = usuario.objects.get(idUsuario=id)
    listaJuegos = videojuego.objects.filter(plataforma_id = 2)
    contexto = {
        "Nin": lista,
        "juegos3": listaJuegos
    }

    return render(request,'extension/Exclusivo Nintendo/nintendo.html',contexto)

def Batman(request, id):
    if request.user.is_authenticated:
        vCorreo = request.user.username
        vUser = usuario.objects.get(correo=vCorreo)
        vID = vUser.idUsuario

        juego = videojuego.objects.get(id_videojuego = id)
        contexto = {
            "ID" : vID,
            "videojuego1": juego
        }
        return render(request,'extension/Exclusivo Play/BATMAN_ARKHAM_KNIGHT.html', contexto)
    else:

        juego = videojuego.objects.get(id_videojuego = id)
        contexto = {
            "videojuego1" : juego
        }
        return render(request,'extension/Exclusivo Play/BATMAN_ARKHAM_KNIGHT.html', contexto)

def DeadR(request, id):
    if request.user.is_authenticated:
        vCorreo = request.user.username
        vUser = usuario.objects.get(correo=vCorreo)
        vID = vUser.idUsuario
        
        juego = videojuego.objects.get(id_videojuego = id)
        Vcomen= comentario.objects.filter(videojuego_id_videojuego=id)
        contexto = {
            "ID" : vID,
            "videojuego": juego,
            "comenT" : Vcomen
        }
        return render(request,'extension/Exclusivo Xbox/deadrising.html', contexto)
    
    else:
        juego = videojuego.objects.get(id_videojuego = id)
        Vcomen= comentario.objects.filter(videojuego_id_videojuego=id)
        contexto = {
            "videojuego": juego,
            "comenT" : Vcomen
        }
        return render(request,'extension/Exclusivo Xbox/deadrising.html', contexto)

def Animal(request, id):
    if request.user.is_authenticated:
        vCorreo = request.user.username
        vUser = usuario.objects.get(correo=vCorreo)
        vID = vUser.idUsuario
        
        juego = videojuego.objects.get(id_videojuego = id)
        contexto = {
            "ID" : vID,
            "videojuego3": juego
        }
        return render(request,'extension/Exclusivo Nintendo/ANIMAL CROSSING.html', contexto)
    
    else:
        juego = videojuego.objects.get(id_videojuego = id)
        contexto = {
            "videojuego3": juego
        }
        return render(request,'extension/Exclusivo Nintendo/ANIMAL CROSSING.html', contexto)
    
def BMesa(request, id):
    if request.user.is_authenticated:
        vCorreo = request.user.username
        vUser = usuario.objects.get(correo=vCorreo)
        vID = vUser.idUsuario
        
        juego = videojuego.objects.get(id_videojuego = id)
        contexto = {
            "ID" : vID,
            "videojuego2": juego
        }
        return render(request,'extension/Exclusivo PC/BLACK MESA.html', contexto)
    
    else:
        juego = videojuego.objects.get(id_videojuego = id)
        contexto = {
            "videojuego2": juego
        }
        return render(request,'extension/Exclusivo PC/BLACK MESA.html', contexto)
    
def plantillaMenu(request,id):
    lista = usuario.objects.get(idUsuario=id)
    contexto ={
        "usuarios":lista

    }
    return render(request,'extension/plantillaMenu.html',contexto)
    
def formOlvidado(request):
    try: 
        vPregunta=request.POST['pregunta']
        vRespuesta=request.POST['respuestas']
        vRegistroPregunta = pregunta.objects.get(id_pregunta = vPregunta)
        vVariable = usuario.objects.get(pregunta_id_pregunta=vRegistroPregunta, respuesta=vRespuesta) 
    

        contexto ={ 
            "olvidado":vVariable

        }


        if vRespuesta==vVariable.respuesta:
            return render(request,'extension/Modificar.html',contexto)
        else: 
            return redirect('Login')
    except usuario.DoesNotExist:
        messages.error(request, "No hay coincidencias ")
        return redirect('Olvidado')
    
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
    vFotoJ       = request.FILES['SeleccioneJ']
    vLink        = request.POST['LinkJ']
    vPlataforma  = request.POST['plataforma']

    vRegistroPlataforma = plataforma.objects.get(id_plataforma=vPlataforma)
    videojuego.objects.create( nombreV=vNombreJ, descripcion=vDescripcion,  
                              trailer=vTrailer, foto=vFotoJ,link=vLink , plataforma_id=vRegistroPlataforma)
    
    if vRegistroPlataforma.id_plataforma==4:
        return redirect ('ModificarJuegos' )
    if vRegistroPlataforma.id_plataforma==1:
        return redirect ('ModificarJuegos')
    if vRegistroPlataforma.id_plataforma==3:
        return redirect ('ModificarJuegos ')
    if vRegistroPlataforma.id_plataforma==2:
        return redirect ('ModificarJuegos')
    
def formAgregarM(request):
    vClaveN = request.POST['passwordN']
    vClaveU = request.POST['passwordM']
    vCorreo = request.POST['emailM']
    vFotoM = request.FILES.get('fotoP', '')
    
    listaM = usuario.objects.get(clave=vClaveU, correo=vCorreo) 

    if vClaveN=='':
        listaM.clave=vClaveU
    else:
        listaM.clave=vClaveN

    if vFotoM!='':
        listaM.fotoU=vFotoM

    listaM.save()

    u = User.objects.get(username=vCorreo)
    u.set_password(vClaveN)
    u.save()

    contexto = {
        "modificarU": listaM
    } 
    return render(request,'extension/Login.html',contexto)

def formAgregarMP(request):

    vClaveN = request.POST['claveN']
    vClaveU = request.POST['claveM']
    vCorreo = request.POST['emailM']
    vFotoM = request.FILES.get('fotoMP', '')
    
    listaM = usuario.objects.get(clave=vClaveU, correo=vCorreo) 

    if vClaveN=='':
        listaM.clave=vClaveU
    else:
        listaM.clave=vClaveN

    if vFotoM!='':
        listaM.fotoU=vFotoM

    listaM.save()

    u = User.objects.get(username=vCorreo)
    u.set_password(vClaveN)
    u.save()

    contexto = {
        "modificarU": listaM
    } 
    return render(request,'extension/Login.html',contexto)

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
    return redirect('Login')

def formSesion(request):
    try:
        vCorreo = request.POST['loginEmail']
        vClave = request.POST['loginPassword']
        vRol = 0
        vRun= 0
        registro = usuario.objects.all()

        
        for rol in registro:
            if rol.correo == vCorreo and rol.clave == vClave:

                    vRun = rol.idUsuario
                    vRol = rol.rol_id_rol.id_rol
        user1 = User.objects.get(username = vCorreo)
        print(user1.username)
        pass_valida = check_password(vClave,user1.password)

        if not pass_valida:
            messages.error(request,"El usuario o la contraseña son incorrectos")
            return redirect('Login')

        user = authenticate(username=vCorreo,password = vClave)

        print(user)
        if user is not None:
            if vRol == 1:
                login(request,user)
                return redirect(f'VerPerfil/{vRun}')
                

            if vRol == 2:
                login(request,user)
                return redirect('Administrador') 

            if vRol == 0:
                messages.success(request, "Usuario no registrado")
                return redirect('Login')
    except User.DoesNotExist:
            messages.error(request,"El usuario no existe")
            return redirect('Login')
    except Exception as e:
        print(e)

def formComentario(request):
    vTituloCo =request.POST['comentarioT']
    vComentario =request.POST['ComentarioJ']
    vIDComen =request.POST['id_com']
    
    
    vCorreo = request.user.username
    vUser = usuario.objects.get(correo=vCorreo)
    vJuego = videojuego.objects.get(id_videojuego=vIDComen)
    comentario.objects.create(tituloC=vTituloCo, comentarios=vComentario, usuario_id_usuario=vUser, videojuego_id_videojuego=vJuego)
    return redirect(f'DeadR/{vIDComen}')
    
def VerComentarios(request,id):
    comen = comentario.objects.filter(usuario_id_usuario=id)

    contexto={
        "comenT": comen
    }
    return render(request,'extension/VerComentarios.html', contexto)

def eliminarComentario(request,id):
    EliminarC = comentario.objects.get(id_comentario = id)
    EliminarC.delete()
    return redirect('Comentarios')
