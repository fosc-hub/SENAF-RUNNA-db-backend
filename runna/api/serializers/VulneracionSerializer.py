from rest_framework import serializers
from infrastructure.models import (
    TCategoriaMotivo,
    TCategoriaSubmotivo,
    TGravedadVulneracion,
    TUrgenciaVulneracion,
    TCondicionesVulnerabilidad, 
    TVulneracion,
    TVulneracionHistory,
)


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


class TCondicionesVulnerabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCondicionesVulnerabilidad
        fields = '__all__'


class TVulneracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVulneracion
        fields = [  "principal_demanda","transcurre_actualidad", "deleted","sumatoria_de_pesos","demanda","nnya","autor_dv","categoria_motivo","categoria_submotivo","gravedad_vulneracion","urgencia_vulneracion" ]
        read_only_fields = ['sumatoria_de_pesos', 'nnya', 'deleted']

    def update(self, instance, validated_data):
        if 'nnya' in validated_data:
            raise serializers.ValidationError({"nnya": "This field cannot be updated."})
        return super().update(instance, validated_data)
    

class TVulneracionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TVulneracionHistory
        fields = '__all__'
