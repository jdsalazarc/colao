from django.db import models

from .usuario import Usuario
from .nivel import  Nivel

class SesionJuego(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,)
    tiempoTotal = models.CharField
    puntajeTotal = models.IntegerField
    tiempoParcial = models.CharField
    nivelParcial = models.ForeignKey(Nivel,on_delete=models.CASCADE,)
    finalizada = models.BooleanField