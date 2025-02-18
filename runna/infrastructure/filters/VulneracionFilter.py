from django_filters import rest_framework as filters
from infrastructure.models import (
    TDerechoAfectado,
    TCategoriaMotivo,
    TCategoriaSubmotivo,
    TGravedadVulneracion,
    TUrgenciaVulneracion,
    TCondicionesVulnerabilidad, 
    TVulneracion,
    TVulneracionHistory,
)


class TDerechoAfectadoFilter(filters.FilterSet):
    class Meta:
        model = TDerechoAfectado
        fields = "__all__"


class TCategoriaMotivoFilter(filters.FilterSet):
    class Meta:
        model = TCategoriaMotivo
        fields = "__all__"


class TCategoriaSubmotivoFilter(filters.FilterSet):
    class Meta:
        model = TCategoriaSubmotivo
        fields = "__all__"


class TGravedadVulneracionFilter(filters.FilterSet):
    class Meta:
        model = TGravedadVulneracion
        fields = "__all__"

class TUrgenciaVulneracionFilter(filters.FilterSet):
    class Meta:
        model = TUrgenciaVulneracion
        fields = "__all__"


class TCondicionesVulnerabilidadFilter(filters.FilterSet):
    class Meta:
        model = TCondicionesVulnerabilidad
        fields = "__all__"

class TVulneracionFilter(filters.FilterSet):
    class Meta:
        model = TVulneracion
        fields = "__all__"


class TVulneracionHistoryFilter(filters.FilterSet):
    class Meta:
        model = TVulneracionHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }
