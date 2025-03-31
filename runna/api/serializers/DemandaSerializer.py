from rest_framework import serializers
from infrastructure.models import ( 
    TBloqueDatosRemitente,
    TTipoInstitucionDemanda,
    TAmbitoVulneracion,
    TInstitucionDemanda,
    TDemanda,
    TDemandaHistory,
    TDemandaAdjunto,
    TTipoCodigoDemanda,
    TCodigoDemanda,
    TCalificacionDemanda,
    TCalificacionDemandaHistory,
    TDemandaScore, 
    TDemandaScoreHistory,
)


class TBloqueDatosRemitenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBloqueDatosRemitente
        fields = '__all__'

class TTipoInstitucionDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TTipoInstitucionDemanda
        fields = '__all__'

class TAmbitoVulneracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TAmbitoVulneracion
        fields = '__all__'

class TInstitucionDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionDemanda
        fields = '__all__'

class TDemandaAdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaAdjunto
        fields = ['archivo']

class TDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemanda
        fields = '__all__'

class TDemandaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaHistory
        fields = '__all__'

class TTipoCodigoDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TTipoCodigoDemanda
        fields = '__all__'

class TCodigoDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCodigoDemanda
        fields = '__all__'

class TCalificacionDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCalificacionDemanda
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'demanda' in validated_data:
            raise serializers.ValidationError({"demanda": "This field cannot be updated."})
        return super().update(instance, validated_data)

class TCalificacionDemandaHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TCalificacionDemandaHistory
        fields = '__all__'

class TDemandaScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaScore
        fields = '__all__'

class TDemandaScoreHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemandaScoreHistory
        fields = '__all__'
