from rest_framework import serializers
from .models import Usuario, CategoriaNivel, Nivel, Respuesta, SesionJuego



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre']
        depth = 1 

class RespuestaSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Respuesta
        fields = ['id', 'url_imagen','esCorrecta']

class SesionJuegoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = SesionJuego
        fields = ('__all__')


class CategoriaNivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaNivel
        fields = ['id','nombre']
        depth = 1 

class NivelSerializer(serializers.ModelSerializer):
    respuestas = RespuestaSerializer(many=True)
    class Meta:
        model = Nivel
        fields = ['numero','respuestas','categoriaNivel','resuelto']
        depth = 1 

   



