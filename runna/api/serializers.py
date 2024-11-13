# api/serializers.py
'''
class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
'''

from rest_framework import serializers
from infrastructure.models import TLocalizacion, TUsuarioLinea, TDemanda, TPersona, TVulneracion

class LocalizacionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLocalizacion
        fields = '__all__'


class UsuarioLineaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TUsuarioLinea
        fields = '__all__'


class DemandaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemanda
        fields = '__all__'


class PersonaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersona
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'sexo', 'observaciones', 'adulto']


class VulneracionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVulneracion
        fields = '__all__'
