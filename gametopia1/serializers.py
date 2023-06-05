from rest_framework import serializers
from extension.models import videojuego
class videojuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = videojuego
        fields = ['nombreV','descripcion']
