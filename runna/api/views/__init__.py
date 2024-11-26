from .BaseView import BaseViewSet
from .LocalizacionView import (
    TProvinciaViewSet, 
    TDepartamentoViewSet, 
    TLocalidadViewSet, 
    TBarrioViewSet, 
    TCPCViewSet, 
    TLocalizacionViewSet, 
    TLocalizacionHistoryViewSet
)
from .DemandaView import (
    TInstitucionUsuarioExternoViewSet, 
    TVinculoUsuarioExternoViewSet, 
    TUsuarioExternoViewSet, 
    TDemandaViewSet, 
    TPrecalificacionDemandaViewSet, 
    TDemandaScoreViewSet, 
    TDemandaHistoryViewSet, 
    TPrecalificacionDemandaHistoryViewSet,
    TDemandaScoreHistoryViewSet
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
from .EvaluacionView import (
    TActividadTipoViewSet, 
    TInstitucionActividadViewSet, 
    TActividadViewSet, 
    TInstitucionRespuestaViewSet, 
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