from .BaseHistory import BaseHistory
from .Localizacion import (
    TProvincia, 
    TDepartamento, 
    TLocalidad, 
    TBarrio, 
    TCPC, 
    TLocalizacion, 
    TLocalizacionHistory
)
from .Demanda import  (
    TInstitucionDemanda, 
    TOrigenDemanda,
    TSubOrigenDemanda, 
    TInformante, 
    TDemanda, 
    TPrecalificacionDemanda, 
    TDemandaScore, 
    TDemandaHistory, 
    TInforme101,
    TPrecalificacionDemandaHistory,
    TDemandaScoreHistory
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
    TDemandaAsignado, 
    TDemandaVinculada, 
    TLegajoAsignado, 
    TVinculoPersona, 
    TVinculoPersonaPersona, 
    TDemandaMotivoIntervencion, 
    TPersonaCondicionesVulnerabilidad, 
    TLocalizacionPersonaHistory, 
    TDemandaPersonaHistory, 
    TDemandaAsignadoHistory, 
    TDemandaVinculadaHistory, 
    TVinculoPersonaPersonaHistory,
    TPersonaCondicionesVulnerabilidadHistory,
    TDemandaMotivoIntervencionHistory
)
from .Evaluacion import (
    TActividadTipo, 
    TInstitucionActividad, 
    TActividad, 
    TInstitucionRespuesta, 
    TRespuesta, 
    TIndicadoresValoracion, 
    TEvaluaciones, 
    TDecision, 
    TActividadHistory, 
    TEvaluacionesHistory
)