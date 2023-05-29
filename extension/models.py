from django.db import models

# Create your models here.

class pregunta(models.model):
    id_pregunta = models.AutoField(primary_key = True, verbose_name='id pregunta')
    nombreP      = models.CharField(max_length=20, verbose_name='nombre pregunta')

    def __str__(self):
        return self.nombreP
    
class rol(models.model):
    id_rol = models.AutoField(primary_key = True, verbose_name='id rol')
    nombreR = models.CharField(max_length=20, verbose_name='nombre rol')

    def __str__(self):
        return self.nombreR
    
class usuario(models.model):
    idUsuario = models.AutoField(primary_key = True, verbose_name='id de usuario')
    nombreU    = models.CharField(max_length=30, verbose_name='nombre usuario')
    apellido  = models.CharField(max_length=30, verbose_name='apellido usuario')
    rut       = models.IntegerField(verbose_name='rut usario')
    correo    = models.CharField(max_length=40, verbose_name='correo usuario' )
    telefono  = models.IntegerField(verbose_name='telefono usuario')
    clave     = models.CharField(max_length=20, verbose_name='clave usuario')
    respuesta = models.CharField(max_length=20, verbose_name='respuesta usuario')
    pregunta_id_pregunta = models.ForeignKey(pregunta,on_delete=models.CASCADE)
    rol_id_rol = models.ForeignKey(rol,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreU
    
class videojuego(models.model):
    id_videojuego = models.AutoField(primary_key = True, verbose_name='id videojuego')
    nombreV       = models.CharField(max_length=40, verbose_name='nombre videojuego')
    descripcion   = models.CharField(max_length=2500, verbose_name='descripcion videojuego')
    fecha_lanz    = models.DateField(verbose_name='fecha lanzamiento')
    trailer       = models.CharField(max_length=500, verbose_name='trailer videojuego')
    foto          = models.ImageField(upload_to="portada videojuego")

    def __str__(self):
        return self.nombreV
    
class valoracion(models.model):
    id_valoracion = models.AutoField(primary_key = True, verbose_name='id valoracion')
    puntaje       = models.IntegerField(verbose_name='puntaje de valoracion')
    usuario_id_usuario = models.ForeignKey(usuario,on_delete=models.CASCADE)
    videojuego_id_videojuego = models.ForeignKey(videojuego,on_delete=models.CASCADE)
    


class comentario(models.model):
    id_comentario     = models.AutoField(primary_key = True, verbose_name='id comentario')
    fecha_comentario  = models.DateField(verbose_name='fecha de comentario')
    comentario = models.CharField(max_length=2500, verbose_name='comentario')
    tituloC           = models.CharField(max=30, verbose_name='')
    usuario_id_usuario = models.ForeignKey(usuario,on_delete=models.CASCADE)
    videojuego_id_videojuego = models.ForeignKey(videojuego,on_delete=models.CASCADE)

    def __str__(self):
        return self.tituloC
    

class plataforma(models.model):
    id_plataforma = models.IntegerField(primary_key = True, verbose_name='id plataforma')
    nombrePLA        = models.CharField(max_length=20, verbose_name='nombre plataforma')

    def __str__(self):
        return self.nombrePLA
    
class plat_video(models.model):
    id_pv = models.AutoField(primary_key = True, verbose_name='id plataforma videojuego')
    videojuego_id_videojuego = models.ForeignKey(videojuego,on_delete=models.CASCADE)
    plataforma_id_platafomra = models.ForeignKey(plataforma,on_delete=models.CASCADE)

    
class tienda(models.model):
    id_tienda = models.AutoField(primary_key = True, verbose_name='id tienda')
    nombreT    = models.CharField(max_length=30, verbose_name='nombre tienda')
    link      = models.CharField(max_length=500, verbose_name='link tienda')
    foto      = models.ImageField(upload_to="foto tienda")

    def __str__(self):
        return self.nombreT
    

    
class vid_tienda(models.model):
    id_vi_tien = models.AutoField(primary_key = True, verbose_name='id vid_tien')
    videojuego_id_videojuego = models.ForeignKey(videojuego,on_delete=models.CASCADE)
    tienda_id_tienda = models.ForeignKey(tienda,on_delete=models.CASCADE)

    

    