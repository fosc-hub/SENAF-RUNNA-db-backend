from .BaseHistory import BaseHistory
from .Localizacion import TProvincia, TDepartamento, TLocalidad, TBarrio, TCPC, TLocalizacion, TLocalizacionHistory
from .Demanda import  TInstitucionUsuarioExterno, TVinculoUsuarioExterno, TUsuarioExterno, TDemanda, TPrecalificacionDemanda, TScoreDemanda
from .Persona import TPersona, TInstitucionEducativa, TNNyAEducacion, TInstitucionSanitaria, TNNyASalud, TNNyAScore, TLegajo
from .Vulneracion import TCategoriaMotivo, TCategoriaSubmotivo, TGravedadVulneracion, TUrgenciaVulneracion, TCondicionesVulnerabilidad, TMotivoIntervencion, TVulneracion, TVulneracionHistory
from .Intermedias import TLocalizacionPersona, TDemandaPersona, TDemandaAsignado, TDemandaVinculada, TLegajoAsignado, TVinculoPersona, TVinculoPersonaPersona, TDemandaMotivoIntervencion, TPersonaCondicionesVulnerabilidad, TLocalizacionPersonaHistory
from .Evaluacion import TActividadTipo, TInstitucionActividad, TActividad, TInstitucionRespuesta, TRespuesta, TIndicadoresValoracion, TEvaluaciones, TDecision