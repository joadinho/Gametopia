from django.shortcuts import render
# APIS 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import videojuegoSerializer
from extension.models import videojuego
# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def lista_juego(request):
    if request.method == 'GET':
        Videojuego =  videojuego.objects.all()
        serializer = videojuegoSerializer(Videojuego, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = videojuegoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
