from rest_framework.routers import DefaultRouter
from api.views import (
    CustomUserViewSet, TProvinciaViewSet, TDepartamentoViewSet, TLocalidadViewSet, TBarrioViewSet, TCPCViewSet
)

router = DefaultRouter()
router.register(r'user', CustomUserViewSet, basename='localizacion')
router.register(r'provincias', TProvinciaViewSet, basename='usuario-linea')
router.register(r'departamentos', TDepartamentoViewSet, basename='demanda')
router.register(r'localidades', TLocalidadViewSet, basename='persona')
router.register(r'barrios', TBarrioViewSet, basename='vulneracion')
# router.register(r'precalificaciones', PrecalificacionDemandaViewSet, basename='precalificacion-demanda')
# router.register(r'decisiones', DecisionViewSet, basename='decision')

urlpatterns = router.urls
