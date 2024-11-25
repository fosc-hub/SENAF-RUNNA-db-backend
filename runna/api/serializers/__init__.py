from .LocalizacionSerializer import (
    TProvinciaSerializer,
    TDepartamentoSerializer,
    TLocalidadSerializer,
    TBarrioSerializer,
    TCPCSerializer,
    TLocalizacionSerializer,
    TLocalizacionHistorySerializer,
)
from .DemandaSerializer import (
    TInstitucionUsuarioExternoSerializer,
    TVinculoUsuarioExternoSerializer,
    TUsuarioExternoSerializer,
    TDemandaSerializer,
    TPrecalificacionDemandaSerializer,
    TScoreDemandaSerializer,
    TDemandaHistorySerializer,
    TPrecalificacionDemandaHistorySerializer,
    TScoreDemandaHistorySerializer
)
from .PersonaSerializer import (
    TPersonaSerializer,
    TInstitucionEducativaSerializer,
    TNNyAEducacionSerializer,
    TInstitucionSanitariaSerializer,
    TNNyASaludSerializer,
    TNNyAScoreSerializer,
    TLegajoSerializer,
    TPersonaHistorySerializer,
    TNNyAEducacionHistorySerializer,
    TNNyASaludHistorySerializer,
    TLegajoHistorySerializer,
    TNNyAScoreHistorySerializer
)
from .VulneracionSerializer import (
    TCategoriaMotivoSerializer,
    TCategoriaSubmotivoSerializer,
    TGravedadVulneracionSerializer,
    TUrgenciaVulneracionSerializer,
    TCondicionesVulnerabilidadSerializer,
    TMotivoIntervencionSerializer,
    TVulneracionSerializer,
    TVulneracionHistorySerializer,
)
from .IntermediasSerializer import (
    TLocalizacionPersonaSerializer,
    TDemandaPersonaSerializer,
    TDemandaAsignadoSerializer,
    TDemandaVinculadaSerializer,
    TLegajoAsignadoSerializer,
    TVinculoPersonaSerializer,
    TVinculoPersonaPersonaSerializer,
    TDemandaMotivoIntervencionSerializer,
    TPersonaCondicionesVulnerabilidadSerializer,
    TLocalizacionPersonaHistorySerializer,
    TDemandaPersonaHistorySerializer,
    TDemandaAsignadoHistorySerializer,
    TDemandaVinculadaHistorySerializer,
    TVinculoPersonaPersonaHistorySerializer,
    TPersonaCondicionesVulnerabilidadHistorySerializer,
    TDemandaMotivoIntervencionHistorySerializer
)
from .EvaluacionSerializer import (
    TActividadTipoSerializer,
    TInstitucionActividadSerializer,
    TActividadSerializer,
    TInstitucionRespuestaSerializer,
    TRespuestaSerializer,
    TIndicadoresValoracionSerializer,
    TEvaluacionesSerializer,
    TDecisionSerializer,
    TActividadHistorySerializer,
    TEvaluacionesHistorySerializer
)
