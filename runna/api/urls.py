from rest_framework.routers import DefaultRouter
from api.views import (
    TProvinciaViewSet, 
    TDepartamentoViewSet, 
    TLocalidadViewSet, 
    TBarrioViewSet, 
    TCPCViewSet, 
    TLocalizacionViewSet, 
    TLocalizacionHistoryViewSet
)
from api.views import (
    TOrigenDemandaViewSet,
    TSubOrigenDemandaViewSet, 
    TInformanteViewSet, 
    TDemandaViewSet, 
    TPrecalificacionDemandaViewSet, 
    TDemandaScoreViewSet, 
    TDemandaHistoryViewSet, 
    TInforme101ViewSet,
    TPrecalificacionDemandaHistoryViewSet,
    TCalificacionDemandaViewSet,
    TCalificacionDemandaHistoryViewSet,
    TDemandaScoreHistoryViewSet
)
from api.views import (
    TPersonaViewSet, 
    TInstitucionEducativaViewSet, 
    TNNyAEducacionViewSet, 
    TInstitucionSanitariaViewSet, 
    TNNyASaludViewSet, 
    TNNyAScoreViewSet, 
    TLegajoViewSet, 
    TPersonaHistoryViewSet, 
    TNNyAEducacionHistoryViewSet, 
    TNNyASaludHistoryViewSet,
    TLegajoHistoryViewSet,
    TNNyAScoreHistoryViewSet
)
from api.views import (
    TCategoriaMotivoViewSet, 
    TCategoriaSubmotivoViewSet, 
    TGravedadVulneracionViewSet, 
    TUrgenciaVulneracionViewSet, 
    TCondicionesVulnerabilidadViewSet, 
    TMotivoIntervencionViewSet, 
    TVulneracionViewSet, 
    TVulneracionHistoryViewSet
)
from api.views import (
    TLocalizacionPersonaViewSet, 
    TDemandaPersonaViewSet, 
    TDemandaAsignadoViewSet, 
    TDemandaVinculadaViewSet, 
    TLegajoAsignadoViewSet, 
    TVinculoPersonaViewSet, 
    TVinculoPersonaPersonaViewSet, 
    TDemandaMotivoIntervencionViewSet, 
    TPersonaCondicionesVulnerabilidadViewSet, 
    TLocalizacionPersonaHistoryViewSet, 
    TDemandaPersonaHistoryViewSet, 
    TDemandaAsignadoHistoryViewSet, 
    TDemandaVinculadaHistoryViewSet,
    TVinculoPersonaPersonaHistoryViewSet,
    TPersonaCondicionesVulnerabilidadHistoryViewSet,
    TDemandaMotivoIntervencionHistoryViewSet
)
from api.views import (
    TActividadTipoViewSet, 
    TInstitucionActividadViewSet, 
    TActividadViewSet,
    TRespuestaViewSet, 
    TIndicadoresValoracionViewSet, 
    TEvaluacionesViewSet, 
    TDecisionViewSet, 
    TActividadHistoryViewSet,
    TEvaluacionesHistoryViewSet
)
from api.views import (
    MesaDeEntradaView
)
from api.views import SuggestDecisionView
from django.urls import path, include

router = DefaultRouter()
router.register(r'provincia', TProvinciaViewSet, basename='provincia')
router.register(r'departamento', TDepartamentoViewSet, basename='departamento')
router.register(r'localidad', TLocalidadViewSet, basename='localidad')
router.register(r'barrio', TBarrioViewSet, basename='barrio')
router.register(r'cpc', TCPCViewSet, basename='cpc')
router.register(r'localizacion', TLocalizacionViewSet, basename='localizacion')
router.register(r'localizacion-history', TLocalizacionHistoryViewSet, basename='localizacion-history')

router.register(r'informante', TInformanteViewSet, basename='informante')
router.register(r'origen-demanda', TOrigenDemandaViewSet, basename='origen-demanda')
router.register(r'sub-origen-demanda', TSubOrigenDemandaViewSet, basename='sub-origen-demanda')
router.register(r'demanda', TDemandaViewSet, basename='demanda')
router.register(r'precalificacion-demanda', TPrecalificacionDemandaViewSet, basename='precalificacion-demanda')
router.register(r'demanda-score', TDemandaScoreViewSet, basename='demanda-score')
router.register(r'demanda-history', TDemandaHistoryViewSet, basename='demanda-history')
router.register(r'informe101', TInforme101ViewSet, basename='informe101')
router.register(r'precalificacion-demanda-history', TPrecalificacionDemandaHistoryViewSet, basename='precalificacion-demanda-history')
router.register(r'calificacion-demanda', TCalificacionDemandaViewSet, basename='calificacion-demanda')
router.register(r'calificacion-demanda-history', TCalificacionDemandaHistoryViewSet, basename='calificacion-demanda-history')
router.register(r'demanda-score-history', TDemandaScoreHistoryViewSet, basename='demanda-score-history')

router.register(r'persona', TPersonaViewSet, basename='persona')
router.register(r'institucion-educativa', TInstitucionEducativaViewSet, basename='institucion-educativa')
router.register(r'nnya-educacion', TNNyAEducacionViewSet, basename='nnya-educacion')
router.register(r'institucion-sanitaria', TInstitucionSanitariaViewSet, basename='institucion-sanitaria')
router.register(r'nnya-salud', TNNyASaludViewSet, basename='nnya-salud')
router.register(r'nnya-score', TNNyAScoreViewSet, basename='nnya-score')
router.register(r'legajo', TLegajoViewSet, basename='legajo')
router.register(r'persona-history', TPersonaHistoryViewSet, basename='persona-history')
router.register(r'nnya-educacion-history', TNNyAEducacionHistoryViewSet, basename='nnya-educacion-history')
router.register(r'nnya-salud-history', TNNyASaludHistoryViewSet, basename='nnya-salud-history')
router.register(r'legajo-history', TLegajoHistoryViewSet, basename='legajo-history')
router.register(r'nnya-score-history', TNNyAScoreHistoryViewSet, basename='nnya-score-history')

router.register(r'categoria-motivo', TCategoriaMotivoViewSet, basename='categoria-motivo')
router.register(r'categoria-submotivo', TCategoriaSubmotivoViewSet, basename='categoria-submotivo')
router.register(r'gravedad-vulneracion', TGravedadVulneracionViewSet, basename='gravedad-vulneracion')
router.register(r'urgencia-vulneracion', TUrgenciaVulneracionViewSet, basename='urgencia-vulneracion')
router.register(r'condiciones-vulnerabilidad', TCondicionesVulnerabilidadViewSet, basename='condiciones-vulnerabilidad')
router.register(r'motivo-intervencion', TMotivoIntervencionViewSet, basename='motivo-intervencion')
router.register(r'vulneracion', TVulneracionViewSet, basename='vulneracion')
router.register(r'vulneracion-history', TVulneracionHistoryViewSet, basename='vulneracion-history')

router.register(r'localizacion-persona', TLocalizacionPersonaViewSet, basename='localizacion-persona')
router.register(r'demanda-persona', TDemandaPersonaViewSet, basename='demanda-persona')
router.register(r'demanda-asignado', TDemandaAsignadoViewSet, basename='demanda-asignado')
router.register(r'demanda-vinculada', TDemandaVinculadaViewSet, basename='demanda-vinculada')
router.register(r'legajo-asignado', TLegajoAsignadoViewSet, basename='legajo-asignado')
router.register(r'vinculo-persona', TVinculoPersonaViewSet, basename='vinculo-persona')
router.register(r'vinculo-persona-persona', TVinculoPersonaPersonaViewSet, basename='vinculo-persona-persona')
router.register(r'demanda-motivo-intervencion', TDemandaMotivoIntervencionViewSet, basename='demanda-motivo-intervencion')
router.register(r'persona-condiciones-vulnerabilidad', TPersonaCondicionesVulnerabilidadViewSet, basename='persona-condiciones-vulnerabilidad')
router.register(r'localizacion-persona-history', TLocalizacionPersonaHistoryViewSet, basename='localizacion-persona-history')
router.register(r'demanda-persona-history', TDemandaPersonaHistoryViewSet, basename='demanda-persona-history')
router.register(r'demanda-asignado-history', TDemandaAsignadoHistoryViewSet, basename='demanda-asignado-history')
router.register(r'demanda-vinculada-history', TDemandaVinculadaHistoryViewSet, basename='demanda-vinculada-history')
router.register(r'vinculo-persona-persona-history', TVinculoPersonaPersonaHistoryViewSet, basename='vinculo-persona-persona-history')
router.register(r'persona-condiciones-vulnerabilidad-history', TPersonaCondicionesVulnerabilidadHistoryViewSet, basename='persona-condiciones-vulnerabilidad-history')
router.register(r'demanda-motivo-intervencion-history', TDemandaMotivoIntervencionHistoryViewSet, basename='demanda-motivo-intervencion-history')

router.register(r'actividad-tipo', TActividadTipoViewSet, basename='actividad-tipo')
router.register(r'institucion-actividad', TInstitucionActividadViewSet, basename='institucion-actividad')
router.register(r'actividad', TActividadViewSet, basename='actividad')
router.register(r'respuesta', TRespuestaViewSet, basename='respuesta')
router.register(r'indicadores-valoracion', TIndicadoresValoracionViewSet, basename='indicadores-valoracion')
router.register(r'evaluaciones', TEvaluacionesViewSet, basename='evaluaciones')
router.register(r'decision', TDecisionViewSet, basename='decision')
router.register(r'actividad-history', TActividadHistoryViewSet, basename='actividad-history')
router.register(r'evaluaciones-history', TEvaluacionesHistoryViewSet, basename='evaluaciones-history')

urlpatterns = [
    path('', include(router.urls)),  # Include all router URLs
    path('suggest-decision/<int:nnya_id>/<int:demanda_id>', SuggestDecisionView.as_view(), name='suggest-decision'),
    path('mesa-de-entrada/', MesaDeEntradaView.as_view(), name='mesa-de-entrada-all'),  # List all
    path('mesa-de-entrada/<int:pk>/', MesaDeEntradaView.as_view(), name='mesa-de-entrada-single'),  # Retrieve single
]