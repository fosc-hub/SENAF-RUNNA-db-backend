from rest_framework import serializers
from infrastructure.models import (
    TDemanda,
    TDemandaScore,
    TOrigenDemanda,
    TDemandaPersona,
    TPersona,
    TPrecalificacionDemanda,
)
from api.serializers import (
    TDemandaSerializer,
    TDemandaScoreSerializer,
    TOrigenDemandaSerializer,
    TDemandaPersonaSerializer,
    TPersonaSerializer,
    TPrecalificacionDemandaSerializer,
    TSubOrigenDemandaSerializer,
    TCategoriaMotivoSerializer,
    TCategoriaSubmotivoSerializer,
    TBarrioSerializer,
    TLocalidadSerializer,
    TCPCSerializer,
    TVinculoPersonaSerializer,
    TCondicionesVulnerabilidadSerializer,
    TInstitucionEducativaSerializer,
    TInstitucionSanitariaSerializer,
    TUrgenciaVulneracionSerializer,
    TGravedadVulneracionSerializer
)

class MesaDeEntradaSerializer(serializers.ModelSerializer):
    demanda_score = serializers.SerializerMethodField()
    origen_demanda = serializers.SerializerMethodField()
    nnya_principal = serializers.SerializerMethodField()
    precalificacion = serializers.SerializerMethodField()

    def get_demanda_score(self, obj):
        try:
            score = TDemandaScore.objects.get(demanda=obj)
            return TDemandaScoreSerializer(score).data
        except TDemandaScore.DoesNotExist:
            return None

    def get_origen_demanda(self, obj):
        return TOrigenDemandaSerializer(obj.origen).data if obj.origen else None

    def get_nnya_principal(self, obj):
        try:
            demandaPersona = TDemandaPersona.objects.get(demanda=obj, nnya_principal=True)
            return TPersonaSerializer(demandaPersona.persona).data
        except TDemandaPersona.DoesNotExist:
            return None

    def get_precalificacion(self, obj):
        try:
            precalificacion = TPrecalificacionDemanda.objects.get(demanda=obj)
            return TPrecalificacionDemandaSerializer(precalificacion).data
        except TPrecalificacionDemanda.DoesNotExist:
            return None
        
    class Meta:
        model = TDemanda
        fields = '__all__'


class ChoiceFieldSerializer(serializers.Serializer):
    """Serializer for enum choices"""
    key = serializers.CharField()
    value = serializers.CharField()

class NuevoRegistroFormDropdownsSerializer(serializers.Serializer):
    """Main serializer to group all dropdown data"""
    estado_demanda_choices = ChoiceFieldSerializer(many=True)
    ambito_vulneracion_choices = ChoiceFieldSerializer(many=True)
    origenes = TOrigenDemandaSerializer(many=True)
    sub_origenes = TSubOrigenDemandaSerializer(many=True)
    motivos_ingreso = TCategoriaMotivoSerializer(many=True)
    submotivos_ingreso = TCategoriaSubmotivoSerializer(many=True)
    
    tipo_calle_choices = ChoiceFieldSerializer(many=True)
    barrios = TBarrioSerializer(many=True)
    localidades = TLocalidadSerializer(many=True)
    cpcs = TCPCSerializer(many=True)
    
    situacion_dni_choices = ChoiceFieldSerializer(many=True)
    genero_choices = ChoiceFieldSerializer(many=True)
    vinculos_choices = TVinculoPersonaSerializer(many=True)
    condiciones_vulnerabilidad = TCondicionesVulnerabilidadSerializer(many=True)
    
    nivel_choices = ChoiceFieldSerializer(many=True)
    turno_choices = ChoiceFieldSerializer(many=True)
    instituciones_educativas = TInstitucionEducativaSerializer(many=True)
    
    instituciones_sanitarias = TInstitucionSanitariaSerializer(many=True)
    
    gravedades_vulneracion = TGravedadVulneracionSerializer(many=True)
    urgencias_vulneracion = TUrgenciaVulneracionSerializer(many=True)
