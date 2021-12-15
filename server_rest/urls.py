from rest_framework import routers

from .views import UsuarioViewSet, CategoriaNivelViewSet, NivelViewSet, RespuestaViewSet, SesionJuegoViewSet

router = routers.SimpleRouter()

router.register('usuarios', UsuarioViewSet)
router.register('categoriasnivel', CategoriaNivelViewSet)
router.register('niveles', NivelViewSet)
router.register('respuestas', RespuestaViewSet)
router.register('sesionjuegos', SesionJuegoViewSet)

urlpatterns = router.urls