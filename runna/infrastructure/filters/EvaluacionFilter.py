from django_filters import rest_framework as filters
from infrastructure.models import (
    TActividadTipo, 
    TInstitucionActividad, 
    TActividad,
    TRespuesta, 
    TIndicadoresValoracion, 
    TEvaluaciones, 
    TDecision, 
    TActividadHistory,
    TEvaluacionesHistory
)

class TActividadTipoFilter(filters.FilterSet):
    class Meta:
        model = TActividadTipo
        fields = "__all__"

class TInstitucionActividadFilter(filters.FilterSet):
    class Meta:
        model = TInstitucionActividad
        fields = "__all__"
class TActividadFilter(filters.FilterSet):
    class Meta:
        model = TActividad
        fields = ["demanda", "tipo", "institucion"]

class TRespuestaFilter(filters.FilterSet):
    class Meta:
        model = TRespuesta
        fields = ["demanda", "institucion", "etiqueta"]

class TIndicadoresValoracionFilter(filters.FilterSet):
    class Meta:
        model = TIndicadoresValoracion
        fields = "__all__"

class TEvaluacionesFilter(filters.FilterSet):
    class Meta:
        model = TEvaluaciones
        fields = "__all__"

class TDecisionFilter(filters.FilterSet):
    class Meta:
        model = TDecision
        fields = "__all__"

class TActividadHistoryFilter(filters.FilterSet):
    class Meta:
        model = TActividadHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }


class TEvaluacionesHistoryFilter(filters.FilterSet):
    class Meta:
        model = TEvaluacionesHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }
    