from rest_framework import serializers
from infrastructure.models import (
    TVinculoDePersonas,
    TPersona,
    TPersonaHistory,
    TInstitucionEducativa,
    TEducacion,
    TEducacionHistory,
    TInstitucionSanitaria,
    TSituacionSalud,
    TEnfermedad,
    TMedico,
    TCoberturaMedica,
    TCoberturaMedicaHistory,
    TPersonaEnfermedades,
    TPersonaEnfermedadesHistory,
    TPersonaOficioAdjunto,
    TPersonaCertificadoAdjunto,
    TNNyAScore,
    TNNyAScoreHistory,
    TLegajo,
    TLegajoHistory,
)


class TVinculoDePersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVinculoDePersonas
        fields = '__all__'


class TPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersona
        fields = '__all__'


class TPersonaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersonaHistory
        fields = '__all__'


class TInstitucionEducativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionEducativa
        fields = '__all__'


class TEducacionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = TEducacion
        read_only_fields = ['persona']
        fields = '__all__'


class TEducacionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TEducacionHistory
        fields = '__all__'


class TInstitucionSanitariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionSanitaria
        fields = '__all__'


class TSituacionSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = TSituacionSalud
        fields = '__all__'


class TEnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TEnfermedad
        read_only_fields = ['persona']
        fields = '__all__'


class TMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TMedico
        fields = '__all__'


class TCoberturaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCoberturaMedica
        read_only_fields = ['persona']
        fields = '__all__'


class TCoberturaMedicaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TCoberturaMedicaHistory
        fields = '__all__'

class TPersonaOficioAdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersonaOficioAdjunto
        fields = ['archivo']

class TPersonaCertificadoAdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersonaCertificadoAdjunto
        fields = ['archivo']

class TPersonaEnfermedadesSerializer(serializers.ModelSerializer):
    oficio_adjunto = TPersonaOficioAdjuntoSerializer(many=True, required=False)
    certificado_adjunto = TPersonaCertificadoAdjuntoSerializer(many=True, required=False)

    class Meta:
        model = TPersonaEnfermedades
        # read_only_fields = ['persona']
        fields = '__all__'

    def create(self, validated_data):
        oficios_adjuntos_data = validated_data.pop('oficios_adjuntos', [])
        certificados_adjuntos_data = validated_data.pop('certificados_adjuntos', [])
        persona_enfermedades = TPersonaEnfermedades.objects.create(**validated_data)
        for oficio_adjunto_data in oficios_adjuntos_data:
            TPersonaOficioAdjunto.objects.create(persona_enfermedades=persona_enfermedades, **oficio_adjunto_data)
        for certificado_adjunto_data in certificados_adjuntos_data:
            TPersonaCertificadoAdjunto.objects.create(persona_enfermedades=persona_enfermedades, **certificado_adjunto_data)
        return persona_enfermedades
    
    def update(self, instance, validated_data):
        oficios_adjuntos_data = validated_data.pop('oficios_adjuntos', None)
        certificados_adjuntos_data = validated_data.pop('certificados_adjuntos', None)
        instance = super().update(instance, validated_data)
        if oficios_adjuntos_data is not None:
            instance.oficios_adjuntos.all().delete()
            for oficio_adjunto_data in oficios_adjuntos_data:
                TPersonaOficioAdjunto.objects.create(enfermedad=instance, **oficio_adjunto_data)
        if certificados_adjuntos_data is not None:
            instance.certificados_adjuntos.all().delete()
            for certificado_adjunto_data in certificados_adjuntos_data:
                TPersonaCertificadoAdjunto.objects.create(enfermedad=instance, **certificado_adjunto_data)
        return instance

class TPersonaEnfermedadesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersonaEnfermedadesHistory
        fields = '__all__'


class TNNyAScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TNNyAScore
        fields = '__all__'


class TNNyAScoreHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TNNyAScoreHistory
        fields = '__all__'


class TLegajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLegajo
        read_only_fields = ['persona']
        fields = '__all__'


class TLegajoHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TLegajoHistory
        fields = '__all__'
