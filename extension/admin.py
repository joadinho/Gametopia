from django.contrib import admin
from .models import usuario,valoracion,comentario,rol,pregunta,plat_vid,plataforma,videojuego,vid_tien,tienda
# Register your models here.
admin.site.register(usuario)
admin.site.register(valoracion)
admin.site.register(comentario)
admin.site.register(rol)
admin.site.register(pregunta)
admin.site.register(plat_vid)
admin.site.register(plataforma)
admin.site.register(videojuego)
admin.site.register(vid_tien)
admin.site.register(tienda)