from rest_framework.routers import DefaultRouter
from api.views import LocalizacionViewSet, UsuarioLineaViewSet, DemandaViewSet, PersonaViewSet, VulneracionViewSet #, PrecalificacionDemandaViewSet, DecisionViewSet

router = DefaultRouter()
router.register(r'localizaciones', LocalizacionViewSet, basename='localizacion')
router.register(r'usuarios-linea', UsuarioLineaViewSet, basename='usuario-linea')
router.register(r'demandas', DemandaViewSet, basename='demanda')
router.register(r'personas', PersonaViewSet, basename='persona')
router.register(r'vulneraciones', VulneracionViewSet, basename='vulneracion')
# router.register(r'precalificaciones', PrecalificacionDemandaViewSet, basename='precalificacion-demanda')
# router.register(r'decisiones', DecisionViewSet, basename='decision')

urlpatterns = router.urls
