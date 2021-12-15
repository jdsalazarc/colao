from django.contrib import admin

from server_rest.models import respuesta

from .models import Usuario, Nivel, CategoriaNivel, Respuesta, SesionJuego
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Nivel)
admin.site.register(CategoriaNivel)
admin.site.register(Respuesta)
admin.site.register(SesionJuego)