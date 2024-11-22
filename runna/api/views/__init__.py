from .BaseView import BaseViewSet
from .CustomUserView import CustomUserViewSet
from .LocalizacionView import TProvinciaViewSet, TDepartamentoViewSet, TLocalidadViewSet, TBarrioViewSet, TCPCViewSet, TLocalizacionViewSet
from .DemandaView import  TInstitucionUsuarioExternoViewSet, TVinculoUsuarioExternoViewSet, TUsuarioExternoViewSet, TDemandaViewSet, TPrecalificacionDemandaViewSet, TScoreDemandaViewSet
from .PersonaView import TPersonaViewSet, TInstitucionEducativaViewSet, TNNyAEducacionViewSet, TInstitucionSanitariaViewSet, TNNyASaludViewSet, TNNyAScoreViewSet, TLegajoViewSet
from .VulneracionView import TCategoriaMotivoViewSet, TCategoriaSubmotivoViewSet, TGravedadVulneracionViewSet, TUrgenciaVulneracionViewSet, TCondicionesVulnerabilidadViewSet, TMotivoIntervencionViewSet, TVulneracionViewSet
from .IntermediasView import TLocalizacionPersonaViewSet, TDemandaPersonaViewSet, TDemandaAsignadoViewSet, TDemandaVinculadaViewSet, TLegajoAsignadoViewSet, TVinculoPersonaViewSet, TVinculoPersonaPersonaViewSet, TDemandaMotivoIntervencionViewSet, TPersonaCondicionesVulnerabilidadViewSet
from .EvaluacionView import TActividadTipoViewSet, TInstitucionActividadViewSet, TActividadViewSet, TInstitucionRespuestaViewSet, TRespuestaViewSet, TIndicadoresValoracionViewSet, TEvaluacionesViewSet, TDecisionViewSet
