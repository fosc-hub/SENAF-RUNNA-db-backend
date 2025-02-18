from rest_framework import serializers
from infrastructure.models import (
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
    TNNyAScore,
    TNNyAScoreHistory,
    TLegajo,
    TLegajoHistory,
)


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


class TPersonaEnfermedadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersonaEnfermedades
        read_only_fields = ['persona']
        fields = '__all__'


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
