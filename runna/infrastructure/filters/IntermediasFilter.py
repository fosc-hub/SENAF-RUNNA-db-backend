from django_filters import rest_framework as filters
from infrastructure.models import (    
    TLocalizacionPersona,
    TLocalizacionPersonaHistory,
    TDemandaPersona,
    TDemandaPersonaHistory,
    TDemandaZona,
    TDemandaZonaHistory,
    TDemandaVinculada,
    TDemandaVinculadaHistory,
    TPersonaCondicionesVulnerabilidad,
    TPersonaCondicionesVulnerabilidadHistory,
)

class TLocalizacionPersonaFilter(filters.FilterSet):
    class Meta:
        model = TLocalizacionPersona
        fields = '__all__'


class TDemandaPersonaFilter(filters.FilterSet):
    class Meta:
        model = TDemandaPersona
        fields = '__all__'


class TDemandaZonaFilter(filters.FilterSet):
    class Meta:
        model = TDemandaZona
        fields = '__all__'


class TDemandaVinculadaFilter(filters.FilterSet):
    class Meta:
        model = TDemandaVinculada
        fields = '__all__'


class TPersonaCondicionesVulnerabilidadFilter(filters.FilterSet):
    class Meta:
        model = TPersonaCondicionesVulnerabilidad
        fields = '__all__'


class TLocalizacionPersonaHistoryFilter(filters.FilterSet):
    class Meta:
        model = TLocalizacionPersonaHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }

class TDemandaPersonaHistoryFilter(filters.FilterSet):
    class Meta:
        model = TDemandaPersonaHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }


class TDemandaZonaHistoryFilter(filters.FilterSet):
    class Meta:
        model = TDemandaZonaHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }


class TDemandaVinculadaHistoryFilter(filters.FilterSet):
    class Meta:
        model = TDemandaVinculadaHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }


class TPersonaCondicionesVulnerabilidadHistoryFilter(filters.FilterSet):
    class Meta:
        model = TPersonaCondicionesVulnerabilidadHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }

