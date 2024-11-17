from rest_framework.routers import DefaultRouter
from api.views import TProvinciaViewSet, TDepartamentoViewSet, TLocalidadViewSet, TBarrioViewSet, TCPCViewSet, TLocalizacionViewSet
from api.views import CustomUserViewSet
from api.views import (
    TInstitucionUsuarioExternoViewSet, TVinculoUsuarioExternoViewSet,
    TCargoExternoViewSet, TResponsableExternoViewSet, TUsuarioExternoViewSet,
    TDemandaViewSet, TPrecalificacionDemandaViewSet, TScoreDemandaViewSet
)
from api.views import TPersonaViewSet, TInstitucionEducativaViewSet, TNNyAEducacionViewSet, TInstitucionSanitariaViewSet, TNNyASaludViewSet, TNNyAScoreViewSet, TLegajoViewSet
from api.views import TCategoriaMotivoViewSet, TCategoriaSubmotivoViewSet, TGravedadVulneracionViewSet, TUrgenciaVulneracionViewSet, TCondicionesVulnerabilidadViewSet, TMotivoIntervencionViewSet, TVulneracionViewSet

router = DefaultRouter()
router.register(r'provincia', TProvinciaViewSet, basename='provincia')
router.register(r'departamento', TDepartamentoViewSet, basename='departamento')
router.register(r'localidad', TLocalidadViewSet, basename='localidad')
router.register(r'barrio', TBarrioViewSet, basename='barrio')
router.register(r'cpc', TCPCViewSet, basename='cpc')
router.register(r'localizacion', TLocalizacionViewSet, basename='localizacion')
router.register(r'user', CustomUserViewSet, basename='user')

router.register(r'institucion-usuario-externo', TInstitucionUsuarioExternoViewSet, basename='institucion-usuario-externo')
router.register(r'vinculo-usuario-externo', TVinculoUsuarioExternoViewSet, basename='vinculo-usuario-externo')
router.register(r'cargo-externo', TCargoExternoViewSet, basename='cargo-externo')
router.register(r'responsable-externo', TResponsableExternoViewSet, basename='responsable-externo')
router.register(r'usuario-externo', TUsuarioExternoViewSet, basename='usuario-externo')
router.register(r'demanda', TDemandaViewSet, basename='demanda')
router.register(r'precalificacion-demanda', TPrecalificacionDemandaViewSet, basename='precalificacion-demanda')
router.register(r'score-demanda', TScoreDemandaViewSet, basename='score-demanda')

router.register(r'persona', TPersonaViewSet, basename='persona')
router.register(r'institucion-educativa', TInstitucionEducativaViewSet, basename='institucion-educativa')
router.register(r'nnya-educacion', TNNyAEducacionViewSet, basename='nnya-educacion')
router.register(r'institucion-sanitaria', TInstitucionSanitariaViewSet, basename='institucion-sanitaria')
router.register(r'nnya-salud', TNNyASaludViewSet, basename='nnya-salud')
router.register(r'nnya-score', TNNyAScoreViewSet, basename='nnya-score')
router.register(r'legajo', TLegajoViewSet, basename='legajo')

router.register(r'categoria-motivo', TCategoriaMotivoViewSet, basename='categoria-motivo')
router.register(r'categoria-submotivo', TCategoriaSubmotivoViewSet, basename='categoria-submotivo')
router.register(r'gravedad-vulneracion', TGravedadVulneracionViewSet, basename='gravedad-vulneracion')
router.register(r'urgencia-vulneracion', TUrgenciaVulneracionViewSet, basename='urgencia-vulneracion')
router.register(r'condiciones-vulnerabilidad', TCondicionesVulnerabilidadViewSet, basename='condiciones-vulnerabilidad')
router.register(r'motivo-intervencion', TMotivoIntervencionViewSet, basename='motivo-intervencion')
router.register(r'vulneracion', TVulneracionViewSet, basename='vulneracion')

urlpatterns = router.urls
