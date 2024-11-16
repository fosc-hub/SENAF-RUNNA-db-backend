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
    provincia__nombre = filters.CharFilter(field_name='provincia__nombre', lookup_expr='icontains')

    class Meta:
        model = TDepartamento
        fields = ['nombre', 'provincia']

class TLocalidadFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')
    departamento = filters.NumberFilter(field_name='departamento__id')
    departamento__nombre = filters.CharFilter(field_name='departamento__nombre', lookup_expr='icontains')

    class Meta:
        model = TLocalidad
        fields = ['nombre', 'departamento']

class TBarrioFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')
    localidad = filters.NumberFilter(field_name='localidad__id')
    localidad__nombre = filters.CharFilter(field_name='localidad__nombre', lookup_expr='icontains')

    class Meta:
        model = TBarrio
        fields = ['nombre', 'localidad']

class TCPCFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')
    localidad = filters.NumberFilter(field_name='localidad__id')
    localidad__nombre = filters.CharFilter(field_name='localidad__nombre', lookup_expr='icontains')

    class Meta:
        model = TCPC
        fields = ['nombre', 'localidad']

class TLocalizacionFilter(filters.FilterSet):
    calle = filters.CharFilter(lookup_expr='icontains')
    tipo_calle = filters.CharFilter(lookup_expr='icontains')
    
    localidad = filters.NumberFilter(field_name='localidad__id')
    localidad__nombre = filters.CharFilter(field_name='localidad__nombre', lookup_expr='icontains')
    
    barrio = filters.NumberFilter(field_name='barrio__id')
    barrio__nombre = filters.CharFilter(field_name='barrio__nombre', lookup_expr='icontains')
    
    cpc = filters.NumberFilter(field_name='cpc__id')
    cpc__nombre = filters.CharFilter(field_name='cpc__nombre', lookup_expr='icontains')

    class Meta:
        model = TLocalizacion
        fields = ['calle', 'localidad', 'barrio', 'cpc']