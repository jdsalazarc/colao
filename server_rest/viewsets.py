from rest_framework import viewsets
from rest_framework.response import Response
from .models import Usuario, CategoriaNivel, Nivel, Respuesta, SesionJuego
from .serializer import UsuarioSerializer, CategoriaNivelSerializer, NivelSerializer, RespuestaSerializer, SesionJuegoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class SesionJuegoViewSet(viewsets.ModelViewSet):
    queryset = SesionJuego.objects.all()
    serializer_class =  SesionJuegoSerializer

class CategoriaNivelViewSet(viewsets.ModelViewSet):
    queryset = CategoriaNivel.objects.all()
    serializer_class = CategoriaNivelSerializer

class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

class RespuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer