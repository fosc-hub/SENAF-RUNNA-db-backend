from .BaseHistory import BaseHistory
from .Localizacion import (
    TLocalidad, 
    TBarrio, 
    TCPC, 
    TLocalizacion, 
    TLocalizacionHistory
)
from .Demanda import  (
    TBloqueDatosRemitente,
    TTipoInstitucionDemanda,
    TAmbitoVulneracion,
    TTipoPresuntoDelito,
    TInstitucionDemanda,
    TDemanda,
    TDemandaHistory,
    TTipoCodigoDemanda,
    TCodigoDemanda,
    TCalificacionDemanda,
    TCalificacionDemandaHistory,
    TDemandaScore, 
    TDemandaScoreHistory,
)
from .Persona import (
    TPersona,
    TInstitucionEducativa,
    TNNyAEducacion,
    TInstitucionSanitaria,
    TNNyASalud,
    TNNyAScore,
    TLegajo,
    TPersonaHistory,
    TNNyAEducacionHistory,
    TNNyASaludHistory,
    TLegajoHistory,
    TNNyAScoreHistory
)
from .Vulneracion import (
    TCategoriaMotivo,
    TCategoriaSubmotivo,
    TGravedadVulneracion,
    TUrgenciaVulneracion,
    TCondicionesVulnerabilidad,
    TMotivoIntervencion,
    TVulneracion,
    TVulneracionHistory
)
from .Intermedias import (
    TLocalizacionPersona, 
    TDemandaPersona, 
    TDemandaZona, 
    TDemandaVinculada, 
    TLegajoAsignado, 
    TVinculoPersona, 
    TVinculoPersonaPersona, 
    TDemandaMotivoIntervencion, 
    TPersonaCondicionesVulnerabilidad, 
    TLocalizacionPersonaHistory, 
    TDemandaPersonaHistory, 
    TDemandaZonaHistory, 
    TDemandaVinculadaHistory, 
    TVinculoPersonaPersonaHistory,
    TPersonaCondicionesVulnerabilidadHistory,
    TDemandaMotivoIntervencionHistory
)
from .Evaluacion import (
    TActividadTipo, 
    TInstitucionActividad, 
    TActividad,
    TRespuesta, 
    TIndicadoresValoracion, 
    TEvaluaciones, 
    TDecision, 
    TActividadHistory, 
    TEvaluacionesHistory
)