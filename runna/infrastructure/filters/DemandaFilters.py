from django_filters import rest_framework as filters
from infrastructure.models import (
    TInstitucionDemanda, 
    TOrigenDemanda,
    TSubOrigenDemanda, 
    TInformante, 
    TDemanda, 
    TPrecalificacionDemanda, 
    TDemandaScore, 
    TInforme101, 
    TDemandaHistory, 
    TPrecalificacionDemandaHistory,
    TDemandaScoreHistory
)
 
class TInstitucionDemandaFilter(filters.FilterSet):

    class Meta:
        model = TInstitucionDemanda
        fields = '__all__'

class TOrigenDemandaFilter(filters.FilterSet):
    
    class Meta:
        model = TOrigenDemanda
        fields = '__all__'

class TSubOrigenDemandaFilter(filters.FilterSet):
    
    class Meta:
        model = TSubOrigenDemanda
        fields = '__all__'

class TInformanteFilter(filters.FilterSet):

    class Meta:
        model = TInformante
        fields = '__all__'
class TDemandaFilter(filters.FilterSet):
    
    class Meta:
        model = TDemanda
        fields = '__all__'

class TInforme101Filter(filters.FilterSet):
    
    class Meta:
        model = TInforme101
        fields = ['demanda']


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
