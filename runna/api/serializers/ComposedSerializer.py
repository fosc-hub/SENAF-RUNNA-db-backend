from rest_framework import serializers
from infrastructure.models import (
    TDemanda,
    TDemandaScore,
    TOrigenDemanda,
    TDemandaPersona,
    TPersona,
    TPrecalificacionDemanda,
    TLocalizacion,
    TNNyAEducacion,
    TInformante
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
    TGravedadVulneracionSerializer,
    TLocalizacionSerializer,
    TInformanteSerializer
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


# Custom ChoiceField Serializer to avoid redundant code
class ChoiceFieldSerializer(serializers.Serializer):
    key = serializers.CharField()
    value = serializers.CharField()

    @staticmethod
    def from_model(choices):
        """Converts model choices into a serializable format"""
        return [{"key": key, "value": value} for key, value in choices]

class NuevoRegistroFormDropdownsSerializer(serializers.Serializer):
    """Main serializer to group all dropdown data"""
    
    estado_demanda_choices = serializers.SerializerMethodField()
    ambito_vulneracion_choices = serializers.SerializerMethodField()
    tipo_calle_choices = serializers.SerializerMethodField()
    situacion_dni_choices = serializers.SerializerMethodField()
    genero_choices = serializers.SerializerMethodField()
    supuesto_autordv_choices = serializers.SerializerMethodField()
    nivel_choices = serializers.SerializerMethodField()
    turno_choices = serializers.SerializerMethodField()

    origenes = TOrigenDemandaSerializer(many=True)
    sub_origenes = TSubOrigenDemandaSerializer(many=True)
    motivos_ingreso = TCategoriaMotivoSerializer(many=True)
    submotivos_ingreso = TCategoriaSubmotivoSerializer(many=True)
    barrios = TBarrioSerializer(many=True)
    localidades = TLocalidadSerializer(many=True)
    cpcs = TCPCSerializer(many=True)
    vinculos = TVinculoPersonaSerializer(many=True)
    condiciones_vulnerabilidad = TCondicionesVulnerabilidadSerializer(many=True)
    instituciones_educativas = TInstitucionEducativaSerializer(many=True)
    instituciones_sanitarias = TInstitucionSanitariaSerializer(many=True)
    gravedades_vulneracion = TGravedadVulneracionSerializer(many=True)
    urgencias_vulneracion = TUrgenciaVulneracionSerializer(many=True)

    class Meta:
        fields = '__all__'

    # 🔥 Optimized Choice Fields using SerializerMethodField
    def get_estado_demanda_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TDemanda.estado_demanda_choices)

    def get_ambito_vulneracion_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TDemanda.ambito_vulneracion_choices)

    def get_tipo_calle_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TLocalizacion.tipo_calle_choices)

    def get_situacion_dni_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TPersona.situacion_dni_choices)

    def get_genero_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TPersona.genero_choices)

    def get_supuesto_autordv_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TDemandaPersona.supuesto_autordv_choices)

    def get_nivel_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TNNyAEducacion.nivel_choices)

    def get_turno_choices(self, obj):
        return ChoiceFieldSerializer.from_model(TNNyAEducacion.turno_choices)


class RegistroCasoFormSerializer(serializers.ModelSerializer):
    localizacion = TLocalizacionSerializer()
    informante = TInformanteSerializer(required=False, allow_null=True)

    class Meta:
        model = TDemanda
        fields = '__all__'
        extra_kwargs = {
            'localizacion': {'write_only': True},
            'informante': {'write_only': True},
        }

    def create(self, validated_data):
        localizacion_data = validated_data.pop('localizacion')
        informante = validated_data.pop('informante', None)
        
        localizacion = TLocalizacion.objects.create(**localizacion_data)
        if informante is not None:
            informante = TInformante.objects.create(**informante)
        demanda = TDemanda.objects.create(localizacion=localizacion, informante=informante, **validated_data)
        
        return demanda

    def update(self, instance, validated_data):
        localizacion_data = validated_data.pop('localizacion', None)
        informante = validated_data.pop('informante', None)

        if localizacion_data:
            for attr, value in localizacion_data.items():
                setattr(instance.localizacion, attr, value)
            instance.localizacion.save()

        if informante is not None:
            if instance.informante is not None:
                instance.informante = informante
            else:
                informante = TInformante.objects.create(**informante)
                instance.informante = informante

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
