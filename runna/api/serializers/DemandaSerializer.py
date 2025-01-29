from rest_framework import serializers
from infrastructure.models import ( 
    TOrigenDemanda,
    TSubOrigenDemanda, 
    TInformante, 
    TDemanda, 
    TPrecalificacionDemanda, 
    TDemandaScore, 
    TDemandaHistory, 
    TInforme101,
    TPrecalificacionDemandaHistory,
    TCalificacionDemanda,
    TCalificacionDemandaHistory,
    TDemandaScoreHistory
)
        
class TOrigenDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TOrigenDemanda
        fields = '__all__'

class TSubOrigenDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TSubOrigenDemanda
        fields = '__all__'

class TInformanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInformante
        fields = '__all__'


class TDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemanda
        fields = '__all__'

class TInforme101Serializer(serializers.ModelSerializer):
    class Meta:
        model = TInforme101
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


class TCalificacionDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCalificacionDemanda
        fields = '__all__'


class TCalificacionDemandaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TCalificacionDemandaHistory
        fields = '__all__'


class TPrecalificacionDemandaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TPrecalificacionDemandaHistory
        fields = '__all__'


class TDemandaScoreHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaScoreHistory
        fields = '__all__'
