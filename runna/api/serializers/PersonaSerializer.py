from rest_framework import serializers
from infrastructure.models import TPersona, TInstitucionEducativa, TNNyAEducacion, TInstitucionSanitaria, TNNyASalud, TNNyAScore, TLegajo, TPersonaHistory, TNNyAEducacionHistory, TNNyASaludHistory

class TPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersona
        fields = '__all__'
    
    def create(self, validated_data):
        if 'deleted' in validated_data:
            raise serializers.ValidationError({"delete": "This field is not allowed on creation."})
        return super().create(validated_data)

class TInstitucionEducativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionEducativa
        fields = '__all__'

class TNNyAEducacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TNNyAEducacion
        fields = '__all__'
    
    def update(self, instance, validated_data):
        if 'nnya' in validated_data:
            raise serializers.ValidationError({"nnya": "This field cannot be updated."})
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        if 'deleted' in validated_data:
            raise serializers.ValidationError({"delete": "This field is not allowed on creation."})
        return super().create(validated_data)

class TInstitucionSanitariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionSanitaria
        fields = '__all__'

class TNNyASaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = TNNyASalud
        fields = '__all__'
        
    def update(self, instance, validated_data):
        if 'nnya' in validated_data:
            raise serializers.ValidationError({"nnya": "This field cannot be updated."})
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        if 'deleted' in validated_data:
            raise serializers.ValidationError({"delete": "This field is not allowed on creation."})
        return super().create(validated_data)


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

