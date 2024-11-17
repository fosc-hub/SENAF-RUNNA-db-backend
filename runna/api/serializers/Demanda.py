from rest_framework import serializers
from infrastructure.models import (
    TInstitucionUsuarioExterno, TVinculoUsuarioExterno, TCargoExterno, TResponsableExterno, TUsuarioExterno, TDemanda, TPrecalificacionDemanda, TScoreDemanda
)


class TInstitucionUsuarioExternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstitucionUsuarioExterno
        fields = '__all__'

        
class TVinculoUsuarioExternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVinculoUsuarioExterno
        fields = '__all__'

        
class TCargoExternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCargoExterno
        fields = '__all__'


class TResponsableExternoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TResponsableExterno
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


class TScoreDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TScoreDemanda
        fields = '__all__'

