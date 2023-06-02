from django.contrib import admin
from .models import usuario,comentario,rol,pregunta,plat_video,plataforma,videojuego
# Register your models here.
admin.site.register(usuario)
admin.site.register(comentario)
admin.site.register(rol)
admin.site.register(pregunta)
admin.site.register(plat_video)
admin.site.register(plataforma)
admin.site.register(videojuego)
