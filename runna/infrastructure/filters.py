from django_filters import rest_framework as filters
from infrastructure.models import TProvincia, TDepartamento, TLocalidad, TBarrio, TCPC, TLocalizacion

class TProvinciaFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TProvincia
        fields = ['nombre']

class TDepartamentoFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')
    provincia = filters.NumberFilter(field_name='provincia__id')

    class Meta:
        model = TDepartamento
        fields = ['nombre', 'provincia']

class TLocalidadFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')
    departamento = filters.NumberFilter(field_name='departamento__id')

    class Meta:
        model = TLocalidad
        fields = ['nombre', 'departamento']

class TBarrioFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')
    localidad = filters.NumberFilter(field_name='localidad__id')

    class Meta:
        model = TBarrio
        fields = ['nombre', 'localidad']

class TCPCFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')
    localidad = filters.NumberFilter(field_name='localidad__id')

    class Meta:
        model = TCPC
        fields = ['nombre', 'localidad']

class TLocalizacionFilter(filters.FilterSet):
    calle = filters.CharFilter(lookup_expr='icontains')
    localidad = filters.NumberFilter(field_name='localidad__id')

    class Meta:
        model = TLocalizacion
        fields = ['calle', 'localidad', 'barrio', 'cpc']
