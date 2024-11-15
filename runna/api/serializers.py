# api/serializers.py
'''
class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
'''

from rest_framework import serializers
from infrastructure.models import (
    TProvincia, TDepartamento, TLocalidad, TBarrio, TCPC, TLocalizacion
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
