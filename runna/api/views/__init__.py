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
from .VulneracionView import (
    TVulneracionViewSet, 
    TVulneracionHistoryViewSet,
)
from .IntermediasView import (
    TLocalizacionPersonaViewSet,
    TLocalizacionPersonaHistoryViewSet,
    TDemandaPersonaViewSet,
    TDemandaPersonaHistoryViewSet,
    TDemandaZonaViewSet,
    TDemandaZonaHistoryViewSet,
    AuditoriaDemandaZonaZonaView,
    TDemandaVinculadaViewSet,
    TDemandaVinculadaHistoryViewSet,
    TPersonaCondicionesVulnerabilidadViewSet,
    TPersonaCondicionesVulnerabilidadHistoryViewSet,
)
from .EvaluacionView import (
    TActividadTipoViewSet, 
    TInstitucionActividadViewSet, 
    TActividadViewSet,
    TRespuestaEtiquetaViewSet,
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
    RegistroDemandaFormDropdownsView,
    RegistroDemandaFormView,
    MesaDeEntradaListView,
    GestionDemandaZonaZonaView,
    TActividadDropdownView,
)