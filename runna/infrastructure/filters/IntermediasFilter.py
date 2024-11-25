from django_filters import rest_framework as filters
from infrastructure.models import (
    TLocalizacionPersona, 
    TDemandaPersona, 
    TDemandaAsignado, 
    TDemandaVinculada, 
    TLegajoAsignado, 
    TVinculoPersona, 
    TVinculoPersonaPersona, 
    TDemandaMotivoIntervencion, 
    TPersonaCondicionesVulnerabilidad, 
    TLocalizacionPersonaHistory, 
    TDemandaPersonaHistory, 
    TDemandaAsignadoHistory, 
    TDemandaVinculadaHistory,
    TVinculoPersonaPersonaHistory,
    TPersonaCondicionesVulnerabilidadHistory,
    TDemandaMotivoIntervencionHistory
)

class TLocalizacionPersonaFilter(filters.FilterSet):
    class Meta:
        model = TLocalizacionPersona
        fields = '__all__'


class TDemandaPersonaFilter(filters.FilterSet):
    class Meta:
        model = TDemandaPersona
        fields = '__all__'


class TDemandaAsignadoFilter(filters.FilterSet):
    class Meta:
        model = TDemandaAsignado
        fields = '__all__'


class TDemandaVinculadaFilter(filters.FilterSet):
    class Meta:
        model = TDemandaVinculada
        fields = '__all__'


class TLegajoAsignadoFilter(filters.FilterSet):
    class Meta:
        model = TLegajoAsignado
        fields = '__all__'


class TVinculoPersonaFilter(filters.FilterSet):
    class Meta:
        model = TVinculoPersona
        fields = '__all__'


class TVinculoPersonaPersonaFilter(filters.FilterSet):
    class Meta:
        model = TVinculoPersonaPersona
        fields = '__all__'


class TPersonaCondicionesVulnerabilidadFilter(filters.FilterSet):
    class Meta:
        model = TPersonaCondicionesVulnerabilidad
        fields = '__all__'


class TDemandaMotivoIntervencionFilter(filters.FilterSet):
    class Meta:
        model = TDemandaMotivoIntervencion
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


class TDemandaAsignadoHistoryFilter(filters.FilterSet):
    class Meta:
        model = TDemandaAsignadoHistory
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


class TVinculoPersonaPersonaHistoryFilter(filters.FilterSet):
    class Meta:
        model = TVinculoPersonaPersonaHistory
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


class TDemandaMotivoIntervencionHistoryFilter(filters.FilterSet):
    class Meta:
        model = TDemandaMotivoIntervencionHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }
