from django.urls import path
from gametopia1.views import lista_juego

urlpatterns = [
    path('lista_juego', lista_juego, name="lista_juego"),
]