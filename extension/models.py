from django.db import models

# Create your models here.

class pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key = True, verbose_name='id pregunta')
    nombreP      = models.CharField(max_length=20, verbose_name='nombre pregunta')

    def __str__(self)-> str:
        return self.nombreP
    
class rol(models.Model):
    id_rol = models.AutoField(primary_key = True, verbose_name='id rol')
    nombreR = models.CharField(max_length=20, verbose_name='nombre rol')

    def __str__(self) -> str:
        return self.nombreR
    
class usuario(models.Model):
    idUsuario = models.AutoField(primary_key = True, verbose_name='id de usuario')
    nombreU   = models.CharField(max_length=30, verbose_name='nombre usuario')
    apellido  = models.CharField(max_length=30, verbose_name='apellido usuario')
    correo    = models.CharField(max_length=40, verbose_name='correo usuario' )
    telefono  = models.IntegerField(verbose_name='telefono usuario')
    clave     = models.CharField(max_length=20, verbose_name='clave usuario')
    respuesta = models.CharField(max_length=20, verbose_name='respuesta usuario')
    pregunta_id_pregunta = models.ForeignKey(pregunta,on_delete=models.CASCADE)
    rol_id_rol = models.ForeignKey(rol,on_delete=models.CASCADE)

    def __str__(self)-> str:
        return self.nombreU
    
class videojuego(models.Model):
    id_videojuego = models.AutoField(primary_key = True, verbose_name='id videojuego')
    nombreV       = models.CharField(max_length=40, verbose_name='nombre videojuego')
    descripcion   = models.CharField(max_length=500, verbose_name='descripcion videojuego')
    trailer       = models.CharField(max_length=500, verbose_name='trailer videojuego')
    foto          = models.ImageField(upload_to="portada videojuego")
    link      = models.CharField(max_length=500, verbose_name='link tienda')

    def __str__(self)-> str:
        return self.nombreV
    

class comentario(models.Model):
    id_comentario     = models.AutoField(primary_key = True, verbose_name='id comentario')
    comentarios = models.CharField(max_length=255, verbose_name='comentario')
    tituloC           = models.CharField(max_length=30, verbose_name='')
    usuario_id_usuario = models.ForeignKey(usuario,on_delete=models.CASCADE)
    videojuego_id_videojuego = models.ForeignKey(videojuego,on_delete=models.CASCADE)

    def __str__(self)-> str:
        return self.tituloC
    

class plataforma(models.Model):
    id_plataforma = models.IntegerField(primary_key = True, verbose_name='id plataforma')
    nombrePLA        = models.CharField(max_length=20, verbose_name='nombre plataforma')

    def __str__(self)-> str:
        return self.nombrePLA
    
class plat_video(models.Model):
    id_pv = models.AutoField(primary_key = True, verbose_name='id plataforma videojuego')
    videojuego_id_videojuego = models.ForeignKey(videojuego,on_delete=models.CASCADE)
    plataforma_id_platafomra = models.ForeignKey(plataforma,on_delete=models.CASCADE)


    

    