from .LocalizacionSerializer import (
    TLocalidadSerializer,
    TBarrioSerializer,
    TCPCSerializer,
    TLocalizacionSerializer,
    TLocalizacionHistorySerializer,
)
from .DemandaSerializer import (
    TBloqueDatosRemitenteSerializer,
    TTipoInstitucionDemandaSerializer,
    TAmbitoVulneracionSerializer,
    TTipoPresuntoDelitoSerializer,
    TInstitucionDemandaSerializer,
    TDemandaSerializer,
    TDemandaHistorySerializer,
    TTipoCodigoDemandaSerializer,
    TCodigoDemandaSerializer,
    TCalificacionDemandaSerializer,
    TCalificacionDemandaHistorySerializer,
    TDemandaScoreSerializer, 
    TDemandaScoreHistorySerializer,
)
from .PersonaSerializer import (
    TVinculoDePersonasSerializer,
    TPersonaSerializer,
    TPersonaHistorySerializer,
    TInstitucionEducativaSerializer,
    TEducacionSerializer,
    TEducacionHistorySerializer,
    TInstitucionSanitariaSerializer,
    TSituacionSaludSerializer,
    TEnfermedadSerializer,
    TMedicoSerializer,
    TCoberturaMedicaSerializer,
    TCoberturaMedicaHistorySerializer,
    TPersonaEnfermedadesSerializer,
    TPersonaEnfermedadesHistorySerializer,
    TNNyAScoreSerializer,
    TNNyAScoreHistorySerializer,
    TLegajoSerializer,
    TLegajoHistorySerializer,
)
from .VulneracionSerializer import (
    TCategoriaMotivoSerializer,
    TCategoriaSubmotivoSerializer,
    TGravedadVulneracionSerializer,
    TUrgenciaVulneracionSerializer,
    TCondicionesVulnerabilidadSerializer, 
    TVulneracionSerializer,
    TVulneracionHistorySerializer,
)
from .IntermediasSerializer import (
    TLocalizacionPersonaSerializer,
    TLocalizacionPersonaHistorySerializer,
    TDemandaPersonaSerializer,
    TDemandaPersonaHistorySerializer,
    TDemandaZonaSerializer,
    TDemandaZonaHistorySerializer,
    TDemandaVinculadaSerializer,
    TDemandaVinculadaHistorySerializer,
    TPersonaCondicionesVulnerabilidadSerializer,
    TPersonaCondicionesVulnerabilidadHistorySerializer,
)
from .EvaluacionSerializer import (
    TActividadTipoSerializer,
    TInstitucionActividadSerializer,
    TActividadSerializer,
    TRespuestaSerializer,
    TIndicadoresValoracionSerializer,
    TEvaluacionesSerializer,
    TDecisionSerializer,
    TActividadHistorySerializer,
    TEvaluacionesHistorySerializer
)
from .ComposedSerializer import (
    RegistroDemandaFormDropdownsSerializer,
    RegistroDemandaFormSerializer,
    MesaDeEntradaSerializer,
    GestionDemandaZonaSerializer,
    TActividadDropdownSerializer,
)