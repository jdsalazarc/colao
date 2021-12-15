from django.db import models


class Respuesta(models.Model):
    url_imagen = models.CharField(max_length=300)
    esCorrecta = models.BooleanField(default=False)
    def __str__(self):
        return self.url_imagen
    
    