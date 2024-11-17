from django_filters import rest_framework as filters
from infrastructure.models import TLocalizacionPersona, TDemandaPersona, TDemandaAsignado, TDemandaVinculada, TLegajoAsignado, TVinculoPersona, TVinculoPersonaPersona, TDemandaMotivoIntervencion, TPersonaCondicionesVulnerabilidad

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
