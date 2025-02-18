from rest_framework.routers import DefaultRouter
from api.views import (
    TLocalidadViewSet, 
    TBarrioViewSet, 
    TCPCViewSet, 
    TLocalizacionViewSet, 
    TLocalizacionHistoryViewSet
)
from api.views import (
    TDemandaViewSet,
    TDemandaHistoryViewSet,
    TCalificacionDemandaViewSet,
    TCalificacionDemandaHistoryViewSet,
    TDemandaScoreViewSet, 
    TDemandaScoreHistoryViewSet,
)
from api.views import (
    TPersonaViewSet,
    TPersonaHistoryViewSet,
    TEducacionViewSet,
    TEducacionHistoryViewSet,
    TMedicoViewSet,
    TCoberturaMedicaViewSet,
    TCoberturaMedicaHistoryViewSet,
    TPersonaEnfermedadesViewSet,
    TPersonaEnfermedadesHistoryViewSet,
    TNNyAScoreViewSet,
    TNNyAScoreHistoryViewSet,
    TLegajoViewSet,
    TLegajoHistoryViewSet,
)
from api.views import (
    TVulneracionViewSet, 
    TVulneracionHistoryViewSet,
)
from api.views import (
    TLocalizacionPersonaViewSet,
    TLocalizacionPersonaHistoryViewSet,
    TDemandaPersonaViewSet,
    TDemandaPersonaHistoryViewSet,
    TDemandaZonaViewSet,
    TDemandaZonaHistoryViewSet,
    TDemandaVinculadaViewSet,
    TDemandaVinculadaHistoryViewSet,
    TPersonaCondicionesVulnerabilidadViewSet,
    TPersonaCondicionesVulnerabilidadHistoryViewSet,
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
    MesaDeEntradaListView,
    NuevoRegistroFormDropdownsView,
    RegistroCasoFormView
)
from api.views import SuggestDecisionView
from django.urls import path, include

router = DefaultRouter()
router.register(r'localidad', TLocalidadViewSet, basename='localidad')
router.register(r'barrio', TBarrioViewSet, basename='barrio')
router.register(r'cpc', TCPCViewSet, basename='cpc')
router.register(r'localizacion', TLocalizacionViewSet, basename='localizacion')
router.register(r'localizacion-history', TLocalizacionHistoryViewSet, basename='localizacion-history')

router.register(r'demanda', TDemandaViewSet, basename='demanda')
router.register(r'demanda-history', TDemandaHistoryViewSet, basename='demanda-history')
router.register(r'calificacion-demanda', TCalificacionDemandaViewSet, basename='calificacion-demanda')
router.register(r'calificacion-demanda-history', TCalificacionDemandaHistoryViewSet, basename='calificacion-demanda-history')
router.register(r'demanda-score', TDemandaScoreViewSet, basename='demanda-score')
router.register(r'demanda-score-history', TDemandaScoreHistoryViewSet, basename='demanda-score-history')

router.register(r'persona', TPersonaViewSet, basename='persona')
router.register(r'persona-history', TPersonaHistoryViewSet, basename='persona-history')
router.register(r'educacion', TEducacionViewSet, basename='educacion')
router.register(r'educacion-history', TEducacionHistoryViewSet, basename='educacion-history')
router.register(r'medico', TMedicoViewSet, basename='medico')
router.register(r'cobertura-medica', TCoberturaMedicaViewSet, basename='cobertura-medica')
router.register(r'cobertura-medica-history', TCoberturaMedicaHistoryViewSet, basename='cobertura-medica-history')
router.register(r'persona-enfermedades', TPersonaEnfermedadesViewSet, basename='persona-enfermedades')
router.register(r'persona-enfermedades-history', TPersonaEnfermedadesHistoryViewSet, basename='persona-enfermedades-history')
router.register(r'nnya-score', TNNyAScoreViewSet, basename='nnya-score')
router.register(r'nnya-score-history', TNNyAScoreHistoryViewSet, basename='nnya-score-history')
router.register(r'legajo', TLegajoViewSet, basename='legajo')
router.register(r'legajo-history', TLegajoHistoryViewSet, basename='legajo-history')

router.register(r'vulneracion', TVulneracionViewSet, basename='vulneracion')
router.register(r'vulneracion-history', TVulneracionHistoryViewSet, basename='vulneracion-history')

router.register(r'localizacion-persona', TLocalizacionPersonaViewSet, basename='localizacion-persona')
router.register(r'demanda-persona', TDemandaPersonaViewSet, basename='demanda-persona')
router.register(r'demanda-zona', TDemandaZonaViewSet, basename='demanda-zona')
router.register(r'demanda-vinculada', TDemandaVinculadaViewSet, basename='demanda-vinculada')
router.register(r'persona-condiciones-vulnerabilidad', TPersonaCondicionesVulnerabilidadViewSet, basename='persona-condiciones-vulnerabilidad')
router.register(r'localizacion-persona-history', TLocalizacionPersonaHistoryViewSet, basename='localizacion-persona-history')
router.register(r'demanda-persona-history', TDemandaPersonaHistoryViewSet, basename='demanda-persona-history')
router.register(r'demanda-zona-history', TDemandaZonaHistoryViewSet, basename='demanda-zona-history')
router.register(r'demanda-vinculada-history', TDemandaVinculadaHistoryViewSet, basename='demanda-vinculada-history')
router.register(r'persona-condiciones-vulnerabilidad-history', TPersonaCondicionesVulnerabilidadHistoryViewSet, basename='persona-condiciones-vulnerabilidad-history')

router.register(r'actividad-tipo', TActividadTipoViewSet, basename='actividad-tipo')
router.register(r'institucion-actividad', TInstitucionActividadViewSet, basename='institucion-actividad')
router.register(r'actividad', TActividadViewSet, basename='actividad')
router.register(r'respuesta', TRespuestaViewSet, basename='respuesta')
router.register(r'indicadores-valoracion', TIndicadoresValoracionViewSet, basename='indicadores-valoracion')
router.register(r'evaluaciones', TEvaluacionesViewSet, basename='evaluaciones')
router.register(r'decision', TDecisionViewSet, basename='decision')
router.register(r'actividad-history', TActividadHistoryViewSet, basename='actividad-history')
router.register(r'evaluaciones-history', TEvaluacionesHistoryViewSet, basename='evaluaciones-history')

router.register(r'registro-caso-form', RegistroCasoFormView, basename='registro-caso-form')

urlpatterns = [
    path('', include(router.urls)),  # Include all router URLs
    path('suggest-decision/<int:nnya_id>/<int:demanda_id>', SuggestDecisionView.as_view(), name='suggest-decision'),
    path('mesa-de-entrada/', MesaDeEntradaListView.as_view(), name='mesa-de-entrada-all'),  # List all
    path('mesa-de-entrada/<int:pk>/', MesaDeEntradaListView.as_view(), name='mesa-de-entrada-single'),  # Retrieve single
    path('registro-caso-form-dropdowns/', NuevoRegistroFormDropdownsView.as_view(), name='nuevo-registro-form-dropdowns'),  # Retrieve choices
]