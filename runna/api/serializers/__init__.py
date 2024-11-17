from .CustomUserSerializer import CustomUserSerializer, GroupSerializer, PermissionSerializer
from .LocalizacionSerializer import TProvinciaSerializer, TDepartamentoSerializer, TLocalidadSerializer, TBarrioSerializer, TCPCSerializer, TLocalizacionSerializer
from .DemandaSerializer import  TInstitucionUsuarioExternoSerializer, TVinculoUsuarioExternoSerializer, TCargoExternoSerializer, TResponsableExternoSerializer, TUsuarioExternoSerializer, TDemandaSerializer, TPrecalificacionDemandaSerializer, TScoreDemandaSerializer
from .PersonaSerializer import TPersonaSerializer, TInstitucionEducativaSerializer, TNNyAEducacionSerializer, TInstitucionSanitariaSerializer, TNNyASaludSerializer, TNNyAScoreSerializer, TLegajoSerializer
from .VulneracionSerializer import TCategoriaMotivoSerializer, TCategoriaSubmotivoSerializer, TGravedadVulneracionSerializer, TUrgenciaVulneracionSerializer, TCondicionesVulnerabilidadSerializer, TMotivoIntervencionSerializer, TVulneracionSerializer
from .IntermediasSerializer import TLocalizacionPersonaSerializer, TDemandaPersonaSerializer, TDemandaAsignadoSerializer, TDemandaVinculadaSerializer, TLegajoAsignadoSerializer, TVinculoPersonaSerializer, TVinculoPersonaPersonaSerializer, TDemandaMotivoIntervencionSerializer, TPersonaCondicionesVulnerabilidadSerializer
from .EvaluacionSerializer import TActividadTipoSerializer, TInstitucionActividadSerializer, TActividadSerializer, TInstitucionRespuestaSerializer, TRespuestaSerializer, TIndicadoresValoracionSerializer, TEvaluacionesSerializer, TDecisionSerializer
