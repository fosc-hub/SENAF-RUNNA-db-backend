# api/serializers.py
'''
class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
'''

from rest_framework import serializers
from infrastructure.models import (
    User, TProvincia, TDepartamento, TLocalidad, TBarrio, TCPC, TLocalizacion
    , TVinculoUsuarioLinea, TInstitucionUsuarioLinea, TCargo, TResponsable, TUsuarioLinea
    , TDemanda, TPrecalificacionDemanda, TPersona, TDemandaPersona, TInstitucionEducativa, TNNyAEducacion
    , TInstitucionSanitaria, TNNyA, TCategoriaMotivo, TCategoriaSubmotivo, TGravedadVulneracion, TUrgenciaVulneracion, TVulneracion
    , TInstitucionRespuesta, TRespuesta, TDemandaAsignado, TActividadTipo, TInstitucionActividad, TActividad
    , TDemandaVinculada, TLegajo, TLegajoAsignado, TIndicadoresValoracion, TEvaluaciones, TDecision
    , TVinculo, TVinculoPersonaPersona, TVinculoPersonaNNyA, TScore, TCondicionesVulnerabilidad
    , TNNyACondicionesVulnerabilidad, TMotivoIntervencion, TNNyAMotivoIntervencion
)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TProvincia
        fields = '__all__'

class TDepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDepartamento
        fields = '__all__'

class TLocalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLocalidad
        fields = '__all__'

class TBarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBarrio
        fields = '__all__'

class TCPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCPC
        fields = '__all__'

class TLocalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLocalizacion
        fields = '__all__'

class TVinculoUsuarioLineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVinculoUsuarioLinea
        fields = '__all__'

class TInstitucionUsuarioLineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionUsuarioLinea
        fields = '__all__'

class TCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCargo
        fields = '__all__'

class TResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TResponsable
        fields = '__all__'

class TUsuarioLineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TUsuarioLinea
        fields = '__all__'

class TDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemanda
        fields = '__all__'

class TPrecalificacionDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPrecalificacionDemanda
        fields = '__all__'

class TPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersona
        fields = '__all__'

class TDemandaPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaPersona
        fields = '__all__'

class TInstitucionEducativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionEducativa
        fields = '__all__'

class TNNyAEducacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TNNyAEducacion
        fields = '__all__'

class TInstitucionSanitariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionSanitaria
        fields = '__all__'

class TNNyASerializer(serializers.ModelSerializer):
    class Meta:
        model = TNNyA
        fields = '__all__'

class TCategoriaMotivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCategoriaMotivo
        fields = '__all__'

class TCategoriaSubmotivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCategoriaSubmotivo
        fields = '__all__'

class TGravedadVulneracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TGravedadVulneracion
        fields = '__all__'

class TUrgenciaVulneracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TUrgenciaVulneracion
        fields = '__all__'

class TVulneracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVulneracion
        fields = '__all__'

class TInstitucionRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionRespuesta
        fields = '__all__'

class TRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRespuesta
        fields = '__all__'

class TDemandaAsignadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaAsignado
        fields = '__all__'

class TActividadTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TActividadTipo
        fields = '__all__'

class TInstitucionActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionActividad
        fields = '__all__'

class TActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TActividad
        fields = '__all__'

class TDemandaVinculadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaVinculada
        fields = '__all__'

class TLegajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLegajo
        fields = '__all__'

class TLegajoAsignadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLegajoAsignado
        fields = '__all__'

class TIndicadoresValoracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TIndicadoresValoracion
        fields = '__all__'

class TEvaluacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TEvaluaciones
        fields = '__all__'

class TDecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDecision
        fields = '__all__'

class TVinculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVinculo
        fields = '__all__'

class TVinculoPersonaPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVinculoPersonaPersona
        fields = '__all__'

class TVinculoPersonaNNyASerializer(serializers.ModelSerializer):
    class Meta:
        model = TVinculoPersonaNNyA
        fields = '__all__'

class TScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TScore
        fields = '__all__'

class TCondicionesVulnerabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCondicionesVulnerabilidad
        fields = '__all__'

class TNNyACondicionesVulnerabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TNNyACondicionesVulnerabilidad
        fields = '__all__'

class TMotivoIntervencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TMotivoIntervencion
        fields = '__all__'

class TNNyAMotivoIntervencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TNNyAMotivoIntervencion
        fields = '__all__'
