from django.shortcuts import render

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

    