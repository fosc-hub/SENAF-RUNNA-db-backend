from rest_framework import serializers
from infrastructure.models import (
    TActividadTipo,
    TActividadTipoModelo,
    TInstitucionActividad, 
    TActividad,
    TActividadAdjunto,
    TRespuesta,
    TRespuestaAdjunto,
    TRespuestaEtiqueta,
    TIndicadoresValoracion, 
    TEvaluaciones, 
    TDecision, 
    TEvaluacionesHistory
)
from customAuth.serializers import CustomUserSerializer

class TActividadTipoModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = TActividadTipoModelo
        fields = ['archivo']

class TActividadTipoSerializer(serializers.ModelSerializer):
    modelos = TActividadTipoModeloSerializer(many=True, required=False)
    
    class Meta:
        model = TActividadTipo
        fields = '__all__'

class TInstitucionActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionActividad
        fields = '__all__'

class TActividadAdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TActividadAdjunto
        fields = ['archivo']

class TActividadSerializer(serializers.ModelSerializer):
    adjuntos = TActividadAdjuntoSerializer(many=True, required=False)
    by_user = CustomUserSerializer(read_only=True)
    class Meta:
        model = TActividad
        fields = '__all__'
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['tipo'] = TActividadTipoSerializer(instance.tipo).data
        ret['institucion'] = TInstitucionActividadSerializer(instance.institucion).data
        return ret

    def create(self, validated_data):
        # Extract nested attachments data if provided
        adjuntos_data = validated_data.pop('adjuntos', [])
        actividad = TActividad.objects.create(**validated_data)
        for adjunto_data in adjuntos_data:
            TActividadAdjunto.objects.create(actividad=actividad, **adjunto_data)
        return actividad

    def update(self, instance, validated_data):
        # Handle updating nested attachments if needed
        adjuntos_data = validated_data.pop('adjuntos', None)
        instance = super().update(instance, validated_data)
        if adjuntos_data is not None:
            # For simplicity, here we delete existing attachments and create new ones.
            # You could implement more complex logic if needed.
            instance.adjuntos.all().delete()
            for adjunto_data in adjuntos_data:
                TActividadAdjunto.objects.create(actividad=instance, **adjunto_data)
        return instance


class TRespuestaAdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRespuestaAdjunto
        fields = ['archivo']

class TRespuestaEtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRespuestaEtiqueta
        fields = '__all__'

class TRespuestaSerializer(serializers.ModelSerializer):
    adjuntos = TRespuestaAdjuntoSerializer(many=True, required=False)
    by_user = CustomUserSerializer(read_only=True)

    class Meta:
        model = TRespuesta
        fields = '__all__'

    def create(self, validated_data):
        # Extract nested attachments data if provided.
        adjuntos_data = validated_data.pop('adjuntos', [])
        # Create the instance without saving it immediately.
        respuesta = TRespuesta(**validated_data)
        # Attach the extra data so that pre_save signal can access it.
        respuesta._adjuntos = adjuntos_data
        # Now save the instance; this will trigger pre_save and the signal will see _adjuntos.
        respuesta.save()
        if adjuntos_data:
            respuesta.adjuntos.set([TRespuestaAdjunto(**adjunto_data) for adjunto_data in adjuntos_data], bulk=False)
        return respuesta

    def update(self, instance, validated_data):
        # Handle updating nested attachments if needed
        adjuntos_data = validated_data.pop('adjuntos', None)
        instance = super().update(instance, validated_data)
        if adjuntos_data is not None:
            # For simplicity, here we delete existing attachments and create new ones.
            # You could implement more complex logic if needed.
            instance.adjuntos.all().delete()
            for adjunto_data in adjuntos_data:
                TRespuestaAdjunto.objects.create(respuesta=instance, **adjunto_data)
        return instance
    

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


class TEvaluacionesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TEvaluacionesHistory
        fields = '__all__'
