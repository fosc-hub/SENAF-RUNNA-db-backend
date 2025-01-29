from rest_framework import serializers
from infrastructure.models import (
    TDemanda,
    TDemandaScore,
    TOrigenDemanda,
    TDemandaPersona,
    TPrecalificacionDemanda
)
from api.serializers import (
    TDemandaSerializer,
    TDemandaScoreSerializer,
    TOrigenDemandaSerializer,
    TDemandaPersonaSerializer,
    TPrecalificacionDemandaSerializer
)

class ComposedDemandaSerializer(serializers.Serializer):
    demanda = TDemandaSerializer()
    demanda_score = serializers.SerializerMethodField()
    origen_demanda = serializers.SerializerMethodField()
    personas = serializers.SerializerMethodField()
    precalificacion = serializers.SerializerMethodField()

    def get_demanda_score(self, obj):
        try:
            score = TDemandaScore.objects.get(demanda=obj)
            return TDemandaScoreSerializer(score).data
        except TDemandaScore.DoesNotExist:
            return None

    def get_origen_demanda(self, obj):
        return TOrigenDemandaSerializer(obj.origendemanda).data if obj.origendemanda else None

    def get_personas(self, obj):
        personas = TDemandaPersona.objects.filter(demanda=obj)
        return TDemandaPersonaSerializer(personas, many=True).data

    def get_precalificacion(self, obj):
        try:
            precalificacion = TPrecalificacionDemanda.objects.get(demanda=obj)
            return TPrecalificacionDemandaSerializer(precalificacion).data
        except TPrecalificacionDemanda.DoesNotExist:
            return None
