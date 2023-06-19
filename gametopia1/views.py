from django.shortcuts import render
# APIS 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import comentarioSerializer,videojuegoSerializer
from extension.models import comentario,videojuego
# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def lista_comentario(request):
    if request.method == 'GET':
        Comentario =  comentario.objects.all()
        serializer = comentarioSerializer(Comentario, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = comentarioSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','PUT','DELETE'])
def detalle_comentario(request,id):
    try:
        Comentario =comentario.objects.get(id_comentario=id)
    except comentario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = comentarioSerializer(Comentario)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer =comentarioSerializer(Comentario, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.erros , status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        Comentario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



@api_view(['GET','POST'])
def lista_videojuego(request):
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
        

@api_view(['GET','PUT','DELETE'])
def detalle_videojuego(request,id):
    try:
        Videojuego =videojuego.objects.get(id_videojuego=id)
    except videojuego.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = videojuegoSerializer(Videojuego)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer =videojuegoSerializer(Videojuego, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.erros , status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        Videojuego.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    