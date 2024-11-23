from rest_framework import serializers
from infrastructure.models import (
    TProvincia, TDepartamento, TLocalidad, TBarrio, TCPC, TLocalizacion, TLocalizacionHistory
)

class TProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TProvincia
        fields = '__all__'

class TDepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDepartamento
        fields = '__all__'

class TLocalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLocalidad
        fields = '__all__'

class TBarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBarrio
        fields = '__all__'

class TCPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCPC
        fields = '__all__'

class TLocalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLocalizacion
        fields = '__all__'

    def create(self, validated_data):
        if 'deleted' in validated_data:
            raise serializers.ValidationError({"delete": "This field cannot be created."})
        return super().create(validated_data)
    

class TLocalizacionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TLocalizacionHistory
        fields = '__all__'
