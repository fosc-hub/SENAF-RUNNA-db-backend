from .BaseView import BaseViewSet
from .LocalizacionView import (
    TLocalidadViewSet, 
    TBarrioViewSet, 
    TCPCViewSet, 
    TLocalizacionViewSet, 
    TLocalizacionHistoryViewSet
)
from .DemandaView import (
    TDemandaViewSet,
    TDemandaHistoryViewSet,
    TCalificacionDemandaViewSet,
    TCalificacionDemandaHistoryViewSet,
    TDemandaScoreViewSet, 
    TDemandaScoreHistoryViewSet,
)
from .PersonaView import (
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
from .VulneracionView import (
    TCategoriaMotivoViewSet, 
    TCategoriaSubmotivoViewSet, 
    TGravedadVulneracionViewSet, 
    TUrgenciaVulneracionViewSet, 
    TCondicionesVulnerabilidadViewSet, 
    TMotivoIntervencionViewSet, 
    TVulneracionViewSet, 
    TVulneracionHistoryViewSet
)
from .IntermediasView import (
    TLocalizacionPersonaViewSet, 
    TDemandaPersonaViewSet, 
    TDemandaZonaViewSet, 
    TDemandaVinculadaViewSet, 
    TLegajoAsignadoViewSet, 
    TVinculoPersonaViewSet, 
    TVinculoPersonaPersonaViewSet, 
    TDemandaMotivoIntervencionViewSet, 
    TPersonaCondicionesVulnerabilidadViewSet, 
    TLocalizacionPersonaHistoryViewSet, 
    TDemandaPersonaHistoryViewSet, 
    TDemandaZonaHistoryViewSet, 
    TDemandaVinculadaHistoryViewSet,
    TVinculoPersonaPersonaHistoryViewSet,
    TPersonaCondicionesVulnerabilidadHistoryViewSet,
    TDemandaMotivoIntervencionHistoryViewSet
)
from .EvaluacionView import (
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
from .SuggestDecision import (
    SuggestDecisionView
)
from .ComposedView import (
    MesaDeEntradaListView,
    NuevoRegistroFormDropdownsView,
    RegistroCasoFormView
)