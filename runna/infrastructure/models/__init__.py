from .Localizacion import TProvincia, TDepartamento, TLocalidad, TBarrio, TCPC, TLocalizacion
from .Demanda import  TInstitucionUsuarioExterno, TVinculoUsuarioExterno, TUsuarioExterno, TDemanda, TPrecalificacionDemanda, TScoreDemanda
from .Persona import TPersona, TInstitucionEducativa, TNNyAEducacion, TInstitucionSanitaria, TNNyASalud, TNNyAScore, TLegajo
from .Vulneracion import TCategoriaMotivo, TCategoriaSubmotivo, TGravedadVulneracion, TUrgenciaVulneracion, TCondicionesVulnerabilidad, TMotivoIntervencion, TVulneracion
from .Intermedias import TLocalizacionPersona, TDemandaPersona, TDemandaAsignado, TDemandaVinculada, TLegajoAsignado, TVinculoPersona, TVinculoPersonaPersona, TDemandaMotivoIntervencion, TPersonaCondicionesVulnerabilidad
from .Evaluacion import TActividadTipo, TInstitucionActividad, TActividad, TInstitucionRespuesta, TRespuesta, TIndicadoresValoracion, TEvaluaciones, TDecision