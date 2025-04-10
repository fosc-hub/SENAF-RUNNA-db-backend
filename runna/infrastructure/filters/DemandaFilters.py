from django_filters import rest_framework as filters
from infrastructure.models import (
    TBloqueDatosRemitente,
    TTipoInstitucionDemanda,
    TAmbitoVulneracion,
    TInstitucionDemanda,
    TDemanda,
    TDemandaHistory,
    TTipoCodigoDemanda,
    TCodigoDemanda,
    TCalificacionDemanda,
    TCalificacionDemandaHistory,
    TDemandaScore, 
    TDemandaScoreHistory,
)

class TBloqueDatosRemitenteFilter(filters.FilterSet):
    class Meta:
        model = TBloqueDatosRemitente
        fields = '__all__'

class TTipoInstitucionDemandaFilter(filters.FilterSet):
    class Meta:
        model = TTipoInstitucionDemanda
        fields = '__all__'

class TAmbitoVulneracionFilter(filters.FilterSet):
    class Meta:
        model = TAmbitoVulneracion
        fields = '__all__'

class TInstitucionDemandaFilter(filters.FilterSet):
    class Meta:
        model = TInstitucionDemanda
        fields = '__all__'

class TDemandaFilter(filters.FilterSet):
    class Meta:
        model = TDemanda
        fields = '__all__'

class TDemandaHistoryFilter(filters.FilterSet):
    class Meta:
        model = TDemandaHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }

class TTipoCodigoDemandaFilter(filters.FilterSet):
    class Meta:
        model = TTipoCodigoDemanda
        fields = '__all__'

class TCodigoDemandaFilter(filters.FilterSet):
    class Meta:
        model = TCodigoDemanda
        fields = '__all__'

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

class TDemandaScoreFilter(filters.FilterSet):
    class Meta:
        model = TDemandaScore
        fields = '__all__'

class TDemandaScoreHistoryFilter(filters.FilterSet):
    class Meta:
        model = TDemandaScoreHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }