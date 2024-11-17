from rest_framework import serializers
from infrastructure.models import TActividadTipo, TInstitucionActividad, TActividad, TInstitucionRespuesta, TRespuesta, TIndicadoresValoracion, TEvaluaciones, TDecision


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
        
    def update(self, instance, validated_data):
        if 'demanda' in validated_data:
            raise serializers.ValidationError({"demanda": "This field cannot be updated."})
        return super().update(instance, validated_data)

class TInstitucionRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionRespuesta
        fields = '__all__'

class TRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRespuesta
        fields = '__all__'

class TIndicadoresValoracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TIndicadoresValoracion
        fields = '__all__'

class TEvaluacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TEvaluaciones
        fields = '__all__'
        
    def update(self, instance, validated_data):
        if 'demanda' in validated_data:
            raise serializers.ValidationError({"demanda": "This field cannot be updated."})
        if 'indicador_valoracion' in validated_data:
            raise serializers.ValidationError({"indicador_valoracion": "This field cannot be updated."})
        return super().update(instance, validated_data)


class TDecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDecision
        fields = '__all__'
