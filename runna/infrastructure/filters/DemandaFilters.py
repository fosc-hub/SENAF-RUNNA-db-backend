from django_filters import rest_framework as filters
from infrastructure.models import (
    TInstitucionUsuarioExterno, 
    TVinculoUsuarioExterno, 
    TUsuarioExterno, 
    TDemanda, 
    TPrecalificacionDemanda, 
    TDemandaScore, 
    TLocalizacion, 
    TDemandaHistory, 
    TPrecalificacionDemandaHistory,
    TDemandaScoreHistory
)
 
class TInstitucionUsuarioExternoFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')  # Partial match for nombre
    mail = filters.CharFilter(lookup_expr='icontains')  # Partial match for mail
    telefono = filters.NumberFilter()  # Exact match for telefono
    localizacion = filters.ModelChoiceFilter(queryset=TLocalizacion.objects.all())  # Exact match for localizacion

    class Meta:
        model = TInstitucionUsuarioExterno
        fields = ['nombre', 'mail', 'telefono', 'localizacion']

class TVinculoUsuarioExternoFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')  # Partial match for nombre
    class Meta:
        model = TVinculoUsuarioExterno
        fields = ['nombre']

class TUsuarioExternoFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')  # Partial match for nombre
    apellido = filters.CharFilter(lookup_expr='icontains')  # Partial match for apellido
    fecha_nacimiento = filters.DateFilter()  # Exact match for fecha_nacimiento
    genero = filters.ChoiceFilter(choices=[
        ('MASCULINO', 'Masculino'),
        ('FEMENINO', 'Femenino'),
        ('OTRO', 'Otro')
    ])  # Exact match for genero
    telefono = filters.NumberFilter()  # Exact match for telefono
    mail = filters.CharFilter(lookup_expr='icontains')  # Partial match for mail

    vinculo = filters.ModelChoiceFilter(queryset=TVinculoUsuarioExterno.objects.all())  # Exact match for vinculo

    institucion = filters.ModelChoiceFilter(queryset=TInstitucionUsuarioExterno.objects.all())  # Exact match for institucion

    class Meta:
        model = TUsuarioExterno
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'genero', 'telefono', 'mail', 'vinculo', 'institucion']

class TDemandaFilter(filters.FilterSet):
    
    class Meta:
        model = TDemanda
        fields = '__all__'


class TPrecalificacionDemandaFilter(filters.FilterSet):
    fecha_y_hora = filters.DateTimeFilter()  # Exact match for fecha_y_hora
    descripcion = filters.CharFilter(lookup_expr='icontains')  # Partial match for descripcion
    estado_demanda = filters.ChoiceFilter(choices=[
        ('URGENTE', 'Urgente'),
        ('NO_URGENTE', 'No Urgente'),
        ('COMPLETAR', 'Completar')
    ])  # Exact match for estado_demanda
    ultima_actualizacion = filters.DateTimeFilter()  # Exact match for ultima_actualizacion
    demanda = filters.ModelChoiceFilter(queryset=TDemanda.objects.all())  # Exact match for demanda

    class Meta:
        model = TPrecalificacionDemanda
        fields = ['fecha_y_hora', 'descripcion', 'estado_demanda', 'ultima_actualizacion', 'demanda']



class TDemandaScoreFilter(filters.FilterSet):
    class Meta:
        model = TDemandaScore
        fields = '__all__'

class TDemandaHistoryFilter(filters.FilterSet):
    class Meta:
        model = TDemandaHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }


class TPrecalificacionDemandaHistoryFilter(filters.FilterSet):
    class Meta:
        model = TPrecalificacionDemandaHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }

class TDemandaScoreHistoryFilter(filters.FilterSet):
    class Meta:
        model = TDemandaScoreHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }
