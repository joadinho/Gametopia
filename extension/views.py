from django.shortcuts import render

# Create your views here.
def Pantalla(request):
    return render(request,'extension/Pantalla.html')

def Registrarse(request):
    return render(request,'extension/Registrarse.html')    