from django_filters import rest_framework as filters
from infrastructure.models import TCategoriaMotivo, TCategoriaSubmotivo, TGravedadVulneracion, TUrgenciaVulneracion, TCondicionesVulnerabilidad, TMotivoIntervencion, TVulneracion, TVulneracionHistory


class TCategoriaMotivoFilter(filters.FilterSet):
    class Meta:
        model = TCategoriaMotivo
        fields = {
            'nombre': ['exact', 'icontains'],
            'descripcion': ['icontains'],
            'peso': ['exact', 'gte', 'lte'],
        }

class TCategoriaSubmotivoFilter(filters.FilterSet):
    class Meta:
        model = TCategoriaSubmotivo
        fields = {
            'nombre': ['exact', 'icontains'],
            'descripcion': ['icontains'],
            'peso': ['exact', 'gte', 'lte'],
            'motivo': ['exact'],
        }


class TGravedadVulneracionFilter(filters.FilterSet):
    class Meta:
        model = TGravedadVulneracion
        fields = {
            'nombre': ['exact', 'icontains'],
            'descripcion': ['icontains'],
            'peso': ['exact', 'gte', 'lte'],
        }

class TUrgenciaVulneracionFilter(filters.FilterSet):
    class Meta:
        model = TUrgenciaVulneracion
        fields = {
            'nombre': ['exact', 'icontains'],
            'descripcion': ['icontains'],
            'peso': ['exact', 'gte', 'lte'],
        }

class TCondicionesVulnerabilidadFilter(filters.FilterSet):
    class Meta:
        model = TCondicionesVulnerabilidad
        fields = {
            'nombre': ['exact', 'icontains'],
            'descripcion': ['icontains'],
            'peso': ['exact', 'gte', 'lte'],
            'nnya': ['exact'],
            'adulto': ['exact'],
        }

class TMotivoIntervencionFilter(filters.FilterSet):
    class Meta:
        model = TMotivoIntervencion
        fields = {
            'nombre': ['exact', 'icontains'],
            'descripcion': ['icontains'],
            'peso': ['exact', 'gte', 'lte'],
        }

class TVulneracionFilter(filters.FilterSet):
    class Meta:
        model = TVulneracion
        fields = {
            'principal_demanda': ['exact'],
            'transcurre_actualidad': ['exact'],
            'deleted': ['exact'],
            'sumatoria_de_pesos': ['exact', 'gte', 'lte'],
            'demanda': ['exact'],
            'nnya': ['exact'],
            'autor_dv': ['exact'],
            'categoria_motivo': ['exact'],
            'categoria_submotivo': ['exact'],
            'gravedad_vulneracion': ['exact'],
            'urgencia_vulneracion': ['exact'],
        }


class TVulneracionHistoryFilter(filters.FilterSet):
    class Meta:
        model = TVulneracionHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'user': ['exact'],
        }
