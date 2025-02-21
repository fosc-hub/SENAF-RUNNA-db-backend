from rest_framework import serializers
from infrastructure.models import (
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

class TLocalizacionPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLocalizacionPersona
        fields = '__all__'


class TDemandaPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaPersona
        fields = '__all__'
        read_only_fields = ['demanda', 'persona']

class TDemandaZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaZona
        fields = '__all__'
        read_only_fields = ['demanda']

class TDemandaVinculadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaVinculada
        fields = '__all__'


class TPersonaCondicionesVulnerabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersonaCondicionesVulnerabilidad
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'persona' in validated_data:
            raise serializers.ValidationError({"persona": "This field cannot be updated."})
        if 'condicion_vulnerabilidad' in validated_data:
            raise serializers.ValidationError({"condicion_vulnerabilidad": "This field cannot be updated."})
        return super().update(instance, validated_data)


class TLocalizacionPersonaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TLocalizacionPersonaHistory
        fields = '__all__'

class TDemandaPersonaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaPersonaHistory
        fields = '__all__'
    
class TDemandaZonaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaZonaHistory
        fields = '__all__'

class TDemandaVinculadaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaVinculadaHistory
        fields = '__all__'


class TPersonaCondicionesVulnerabilidadHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersonaCondicionesVulnerabilidadHistory
        fields = '__all__'

