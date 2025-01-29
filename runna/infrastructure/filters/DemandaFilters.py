from django_filters import rest_framework as filters
from infrastructure.models import (
    TOrigenDemanda,
    TSubOrigenDemanda, 
    TInformante, 
    TDemanda, 
    TPrecalificacionDemanda, 
    TDemandaScore, 
    TInforme101, 
    TDemandaHistory, 
    TPrecalificacionDemandaHistory,
    TCalificacionDemanda,
    TCalificacionDemandaHistory,
    TDemandaScoreHistory
)

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

    class Meta:
        model = TPrecalificacionDemanda
        fields = '__all__'


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


class TCalificacionDemandaFilter(filters.FilterSet):
    class Meta:
        model = TCalificacionDemanda
        fields = '__all__'

class TCalificacionDemandaHistoryFilter(filters.FilterSet):
    class Meta:
        model = TCalificacionDemandaHistory
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
