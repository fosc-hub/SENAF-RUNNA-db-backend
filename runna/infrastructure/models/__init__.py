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
    TVinculoDePersonas,
    TPersona,
    TPersonaHistory,
    TInstitucionEducativa,
    TEducacion,
    TEducacionHistory,
    TInstitucionSanitaria,
    TSituacionSalud,
    TEnfermedad,
    TMedico,
    TCoberturaMedica,
    TCoberturaMedicaHistory,
    TPersonaEnfermedades,
    TPersonaEnfermedadesHistory,
    TNNyAScore,
    TNNyAScoreHistory,
    TLegajo,
    TLegajoHistory,
)
from .Vulneracion import (
    TCategoriaMotivo,
    TCategoriaSubmotivo,
    TGravedadVulneracion,
    TUrgenciaVulneracion,
    TCondicionesVulnerabilidad,
    TVulneracion,
    TVulneracionHistory,
)
from .Intermedias import (
    TLocalizacionPersona,
    TLocalizacionPersonaHistory,
    TDemandaPersona,
    TDemandaPersonaHistory,
    TDemandaZona,
    TDemandaZonaHistory,
    TDemandaVinculada,
    TDemandaVinculadaHistory,
    TPersonaCondicionesVulnerabilidad,
    TPersonaCondicionesVulnerabilidadHistory,
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