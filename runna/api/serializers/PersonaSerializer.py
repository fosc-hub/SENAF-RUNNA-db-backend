from rest_framework import serializers
from infrastructure.models import (
    TPersona, 
    TInstitucionEducativa, 
    TNNyAEducacion, 
    TInstitucionSanitaria, 
    TNNyASalud, 
    TNNyAScore, 
    TLegajo, 
    TPersonaHistory, 
    TNNyAEducacionHistory, 
    TNNyASaludHistory,
    TLegajoHistory,
    TNNyAScoreHistory
)

class TPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersona
        fields = '__all__'
    
class TInstitucionEducativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionEducativa
        fields = '__all__'

class TNNyAEducacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TNNyAEducacion
        read_only_fields = ['nnya']
        fields = '__all__'
    
    def update(self, instance, validated_data):
        if 'nnya' in validated_data:
            raise serializers.ValidationError({"nnya": "This field cannot be updated."})
        return super().update(instance, validated_data)
    
class TInstitucionSanitariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionSanitaria
        fields = '__all__'

class TNNyASaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = TNNyASalud
        read_only_fields = ['nnya']
        fields = '__all__'
        
    def update(self, instance, validated_data):
        if 'nnya' in validated_data:
            raise serializers.ValidationError({"nnya": "This field cannot be updated."})
        return super().update(instance, validated_data)
    

class TNNyAScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TNNyAScore
        fields = '__all__'

class TLegajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLegajo
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'nnya' in validated_data:
            raise serializers.ValidationError({"nnya": "This field cannot be updated."})
        return super().update(instance, validated_data)

class TPersonaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersonaHistory
        fields = '__all__'

class TNNyAEducacionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TNNyAEducacionHistory
        fields = '__all__'

class TNNyASaludHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TNNyASaludHistory
        fields = '__all__'

class TLegajoHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TLegajoHistory
        fields = '__all__'

class TNNyAScoreHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TNNyAScoreHistory
        fields = '__all__'
