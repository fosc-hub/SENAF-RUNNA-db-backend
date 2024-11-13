from rest_framework.routers import DefaultRouter
from api.views import (
    CustomUserViewSet, TProvinciaViewSet, TDepartamentoViewSet, TLocalidadViewSet, TBarrioViewSet, TCPCViewSet,
    TLocalizacionViewSet , TVinculoUsuarioLineaViewSet, TInstitucionUsuarioLineaViewSet, TCargoViewSet , TResponsableViewSet, TUsuarioLineaViewSet
    , TDemandaViewSet, TPrecalificacionDemandaViewSet, TPersonaViewSet, TDemandaPersonaViewSet, TInstitucionEducativaViewSet, TNNyAEducacionViewSet
    , TInstitucionSanitariaViewSet, TNNyAViewSet, TCategoriaMotivoViewSet, TCategoriaSubmotivoViewSet, TGravedadVulneracionViewSet, TUrgenciaVulneracionViewSet, TVulneracionViewSet
)

router = DefaultRouter()
router.register(r'user', CustomUserViewSet, basename='user')
router.register(r'provincias', TProvinciaViewSet, basename='provincias')
router.register(r'departamentos', TDepartamentoViewSet, basename='departamentos')
router.register(r'localidades', TLocalidadViewSet, basename='localidades')
router.register(r'barrios', TBarrioViewSet, basename='barrios')
router.register(r'cpc', TCPCViewSet, basename='cpc')
router.register(r'localizacion', TLocalizacionViewSet, basename='localizacion')
router.register(r'vinculo-usuario-linea', TVinculoUsuarioLineaViewSet, basename='vinculo-usuario-linea')
router.register(r'institucion-usuario-linea', TInstitucionUsuarioLineaViewSet, basename='institucion-usuario-linea')
router.register(r'cargo', TCargoViewSet, basename='cargo')
router.register(r'responsable', TResponsableViewSet, basename='responsable')
router.register(r'usuario-linea', TUsuarioLineaViewSet, basename='usuario-linea')
router.register(r'demanda', TDemandaViewSet, basename='demanda')
router.register(r'precalificacion-demanda', TPrecalificacionDemandaViewSet, basename='precalificacion-demanda')
router.register(r'persona', TPersonaViewSet, basename='persona')
router.register(r'demanda-persona', TDemandaPersonaViewSet, basename='demanda-persona')
router.register(r'institucion-educativa', TInstitucionEducativaViewSet, basename='institucion-educativa')
router.register(r'nnya-educacion', TNNyAEducacionViewSet, basename='nnya-educacion')
router.register(r'institucion-sanitaria', TInstitucionSanitariaViewSet, basename='institucion-sanitaria')
router.register(r'nnya', TNNyAViewSet, basename='nnya')
router.register(r'categoria-motivo', TCategoriaMotivoViewSet, basename='categoria-motivo')
router.register(r'categoria-submotivo', TCategoriaSubmotivoViewSet, basename='categoria-submotivo')
router.register(r'gravedad-vulneracion', TGravedadVulneracionViewSet, basename='gravedad-vulneracion')
router.register(r'urgencia-vulneracion', TUrgenciaVulneracionViewSet, basename='urgencia-vulneracion')
router.register(r'vulneracion', TVulneracionViewSet, basename='vulneracion')

urlpatterns = router.urls
