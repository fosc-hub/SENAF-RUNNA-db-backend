from rest_framework import serializers
from infrastructure.models import (
    TInstitucionUsuarioExterno, 
    TVinculoUsuarioExterno, 
    TUsuarioExterno, 
    TDemanda, 
    TPrecalificacionDemanda, 
    TDemandaScore, 
    TDemandaHistory, 
    TPrecalificacionDemandaHistory,
    TDemandaScoreHistory
)


class TInstitucionUsuarioExternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionUsuarioExterno
        fields = '__all__'

        
class TVinculoUsuarioExternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVinculoUsuarioExterno
        fields = '__all__'


class TUsuarioExternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TUsuarioExterno
        fields = '__all__'


class TDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemanda
        fields = '__all__'
    

class TPrecalificacionDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPrecalificacionDemanda
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'demanda' in validated_data:
            raise serializers.ValidationError({"demanda": "This field cannot be updated."})
        return super().update(instance, validated_data)
    


class TDemandaScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaScore
        fields = '__all__'


class TDemandaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaHistory
        fields = '__all__'


class TPrecalificacionDemandaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TPrecalificacionDemandaHistory
        fields = '__all__'


class TDemandaScoreHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaScoreHistory
        fields = '__all__'
