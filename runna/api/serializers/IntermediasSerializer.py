from rest_framework import serializers
from infrastructure.models import TLocalizacionPersona, TDemandaPersona, TDemandaAsignado, TDemandaVinculada, TLegajoAsignado, TVinculoPersona, TVinculoPersonaPersona, TDemandaMotivoIntervencion, TPersonaCondicionesVulnerabilidad, TLocalizacionPersonaHistory


class TLocalizacionPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLocalizacionPersona
        fields = '__all__'

    def create(self, validated_data):
        if 'deleted' in validated_data:
            raise serializers.ValidationError({"delete": "This field is not allowed on creation."})
        return super().create(validated_data)


class TDemandaPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaPersona
        fields = '__all__'

class TDemandaAsignadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaAsignado
        fields = '__all__'

class TDemandaVinculadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaVinculada
        fields = '__all__'

class TLegajoAsignadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLegajoAsignado
        fields = '__all__'

class TVinculoPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVinculoPersona
        fields = '__all__'

class TVinculoPersonaPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVinculoPersonaPersona
        fields = '__all__'

class TDemandaMotivoIntervencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaMotivoIntervencion
        fields = '__all__'    

    def update(self, instance, validated_data):
        if 'demanda' in validated_data:
            raise serializers.ValidationError({"demanda": "This field cannot be updated."})
        if 'motivo_intervencion' in validated_data:
            raise serializers.ValidationError({"motivo_intervencion": "This field cannot be updated."})
        return super().update(instance, validated_data)
    

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
