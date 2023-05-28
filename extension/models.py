from django.db import models

# Create your models here.

class usuario(models.model):
    idUsuario = models.IntegerField(primary_key = True, verbose_name='id de usuario')
    nombre    = models.CharField(max_length=30, verbose_name='nombre usuario')
    apellido  = models.CharField(max_length=30, verbose_name='apellido usuario')
    rut       = models.IntegerField(verbose_name='rut usario')
    correo    = models.CharField(max_length=40, verbose_name='correo usuario' )
    telefono  = models.IntegerField(verbose_name='telefono usuario')
    clave     = models.CharField(max_length=20, verbose_name='clave usuario')
    respuesta = models.CharField(max_length=20, verbose_name='respuesta usuario')


    def __str__(self):
        return self.nombre
    
class valoracion(models.model):
    id_valoracion = models.IntegerField(primary_key = True, verbose_name='id valoracion')
    puntaje       = models.IntegerField(verbose_name='puntaje de valoracion')

    def __str__(self):
        return self.puntaje

class comentario(models.model):
    id_comentario     = models.IntegerField(primary_key = True, verbose_name='id comentario')
    fecha_comentario  = models.DateField(verbose_name='fecha de comentario')
    comentario_status = models.CharField(max_length=20, verbose_name='estado comentario')

    def __str__(self):
        return self.comentario_status
    
class rol(models.model):
    id_rol = models.IntegerField(primary_key = True, verbose_name='id rol')
    nombre = models.CharField(max_length=20, verbose_name='nombre rol')

    def __str__(self):
        return self.nombre

class pregunta(models.model):
    id_pregunta = models.IntegerField(primary_key = True, verbose_name='id pregunta')
    nombre      = models.CharField(max_length=20, verbose_name='nombre pregunta')

    def __str__(self):
        return self.nombre
    
class plat_vid(models.model):
    id_pv = models.IntegerField(primary_key = True, verbose_name='id plataforma videojuego')

    def __str__(self):
        return self.id_pv
    
class plataforma(models.model):
    id_plataforma = models.IntegerField(primary_key = True, verbose_name='id plataforma')
    nombre        = models.CharField(max_length=20, verbose_name='nombre plataforma')

    def __str__(self):
        return self.nombre
    
class videojuego(models.model):
    id_videojuego = models.IntegerField(primary_key = True, verbose_name='id videojuego')
    nombre        = models.CharField(max_length=40, verbose_name='nombre videojuego')
    descripcion   = models.CharField(max_length=2500, verbose_name='descripcion videojuego')
    fecha_lanz    = models.DateField(verbose_name='fecha lanzamiento')
    trailer       = models.CharField(max_length=500, verbose_name='trailer videojuego')
    foto          = models.ImageField(upload_to="portada videojuego")

    def __str__(self):
        return self.nombre
    
class vid_tien(models.model):
    id_vi_tien = models.IntegerField(primary_key = True, verbose_name='id vid_tien')

    def __str__(self):
        return self.id_vi_tien
    
class tienda(models.model):
    id_tienda = models.IntegerField(primary_key = True, verbose_name='id tienda')
    nombre    = models.CharField(max_length=30, verbose_name='nombre tienda')
    link      = models.CharField(max_length=500, verbose_name='link tienda')
    foto      = models.ImageField(upload_to="foto tienda")

    def __str__(self):
        return self.nombre
    