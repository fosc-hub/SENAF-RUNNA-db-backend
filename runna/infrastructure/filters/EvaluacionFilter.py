from django_filters import rest_framework as filters
from infrastructure.models import TActividadTipo, TInstitucionActividad, TActividad, TInstitucionRespuesta, TRespuesta, TIndicadoresValoracion, TEvaluaciones, TDecision, TActividadHistory

class TActividadTipoFilter(filters.FilterSet):
    class Meta:
        model = TActividadTipo
        fields = {
            'nombre': ['exact', 'icontains'],
        }

class TInstitucionActividadFilter(filters.FilterSet):
    class Meta:
        model = TInstitucionActividad
        fields = {
            'nombre': ['exact', 'icontains'],
            'mail': ['exact', 'icontains'],
            'telefono': ['exact', 'gte', 'lte'],
            'localizacion': ['exact'],
        }

class TActividadFilter(filters.FilterSet):
    class Meta:
        model = TActividad
        fields = {
            'fecha_y_hora': ['exact', 'gte', 'lte'],
            'descripcion': ['icontains'],
            'demanda': ['exact'],
            'tipo': ['exact'],
            'institucion': ['exact'],
        }

class TInstitucionRespuestaFilter(filters.FilterSet):
    class Meta:
        model = TInstitucionRespuesta
        fields = {
            'nombre': ['exact', 'icontains'],
            'mail': ['exact', 'icontains'],
            'telefono': ['exact', 'gte', 'lte'],
            'localizacion': ['exact'],
        }

class TRespuestaFilter(filters.FilterSet):
    class Meta:
        model = TRespuesta
        fields = {
            'fecha_y_hora': ['exact', 'gte', 'lte'],
            'mail': ['exact', 'icontains'],
            'mensaje': ['icontains'],
            'demanda': ['exact'],
            'institucion': ['exact'],
        }

class TIndicadoresValoracionFilter(filters.FilterSet):
    class Meta:
        model = TIndicadoresValoracion
        fields = {
            'nombre': ['exact', 'icontains'],
            'descripcion': ['icontains'],
            'peso': ['exact', 'gte', 'lte'],
        }

class TEvaluacionesFilter(filters.FilterSet):
    class Meta:
        model = TEvaluaciones
        fields = {
            'demanda': ['exact'],
            'indicador': ['exact'],
            'si_no': ['exact'],
        }

class TDecisionFilter(filters.FilterSet):
    class Meta:
        model = TDecision
        fields = {
            'fecha_y_hora': ['exact', 'gte', 'lte'],
            'justificacion': ['icontains'],
            'decision': ['exact'],
            'demanda': ['exact'],
        }

class TActividadHistoryFilter(filters.FilterSet):
    class Meta:
        model = TActividadHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }