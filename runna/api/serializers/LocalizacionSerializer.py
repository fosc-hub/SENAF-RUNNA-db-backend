from rest_framework import serializers
from infrastructure.models import (
    TLocalidad, TBarrio, TCPC, TLocalizacion, TLocalizacionHistory
)


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

class TLocalizacionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TLocalizacionHistory
        fields = '__all__'
