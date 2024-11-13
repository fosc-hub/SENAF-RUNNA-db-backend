from rest_framework.routers import DefaultRouter
from api.views import (
    CustomUserViewSet, TProvinciaViewSet, TDepartamentoViewSet, TLocalidadViewSet, TBarrioViewSet, TCPCViewSet,
    TLocalizacionViewSet , TVinculoUsuarioLineaViewSet, TInstitucionUsuarioLineaViewSet, TCargoViewSet , TResponsableViewSet, TUsuarioLineaViewSet
    , TDemandaViewSet, TPrecalificacionDemandaViewSet, TPersonaViewSet, TDemandaPersonaViewSet, TInstitucionEducativaViewSet, TNNyAEducacionViewSet
    , TInstitucionSanitariaViewSet, TNNyAViewSet, TCategoriaMotivoViewSet, TCategoriaSubmotivoViewSet, TGravedadVulneracionViewSet, TUrgenciaVulneracionViewSet, TVulneracionViewSet
    , TInstitucionRespuestaViewSet, TRespuestaViewSet, TDemandaAsignadoViewSet, TActividadTipoViewSet, TInstitucionActividadViewSet, TActividadViewSet
    , TDemandaVinculadaViewSet, TLegajoViewSet, TLegajoAsignadoViewSet, TIndicadoresValoracionViewSet, TEvaluacionesViewSet, TDecisionViewSet
    , TVinculoViewSet, TVinculoPersonaPersonaViewSet, TVinculoPersonaNNyAViewSet, TScoreViewSet, TCondicionesVulnerabilidadViewSet
    , TNNyACondicionesVulnerabilidadViewSet, TMotivoIntervencionViewSet, TNNyAMotivoIntervencionViewSet
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
router.register(r'institucion-respuesta', TInstitucionRespuestaViewSet, basename='institucion-respuesta')
router.register(r'respuesta', TRespuestaViewSet, basename='respuesta')
router.register(r'demanda-asignado', TDemandaAsignadoViewSet, basename='demanda-asignado')
router.register(r'actividades-tipo', TActividadTipoViewSet, basename='actividades-tipo')
router.register(r'institucion-actividad', TInstitucionActividadViewSet, basename='institucion-actividad')
router.register(r'actividades', TActividadViewSet, basename='actividades')
router.register(r'demanda-vinculada', TDemandaVinculadaViewSet, basename='demanda-vinculada')
router.register(r'legajo', TLegajoViewSet, basename='legajo')
router.register(r'legajo-asignado', TLegajoAsignadoViewSet, basename='legajo-asignado')
router.register(r'indicadores-valoracion', TIndicadoresValoracionViewSet, basename='indicadores-valoracion')
router.register(r'evaluaciones', TEvaluacionesViewSet, basename='evaluaciones')
router.register(r'decision', TDecisionViewSet, basename='decision')
router.register(r'vinculo', TVinculoViewSet, basename='vinculo')
router.register(r'vinculo-persona-persona', TVinculoPersonaPersonaViewSet, basename='vinculo-persona-persona')
router.register(r'vinculo-persona-nnya', TVinculoPersonaNNyAViewSet, basename='vinculo-persona-nnya')
router.register(r'score', TScoreViewSet, basename='score')
router.register(r'condiciones-vulnerabilidad', TCondicionesVulnerabilidadViewSet, basename='condiciones-vulnerabilidad')
router.register(r'nnya-condiciones-vulnerabilidad', TNNyACondicionesVulnerabilidadViewSet, basename='nnya-condiciones-vulnerabilidad')
router.register(r'motivo-intervencion', TMotivoIntervencionViewSet, basename='motivo-intervencion')
router.register(r'nnya-motivo-intervencion', TNNyAMotivoIntervencionViewSet, basename='nnya-motivo-intervencion')

urlpatterns = router.urls
