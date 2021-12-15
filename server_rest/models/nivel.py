from django.db import models

from .categoriaNivel import CategoriaNivel
from .respuesta import Respuesta


class Nivel(models.Model):
    numero = models.IntegerField()
    categoriaNivel = models.ForeignKey(CategoriaNivel,on_delete=models.CASCADE, default='6')
    respuestas = models.ManyToManyField(Respuesta)
    resuelto = models.BooleanField(default=False)
    def __int__(self):
        return self.numero
   
   
    
    

   
    