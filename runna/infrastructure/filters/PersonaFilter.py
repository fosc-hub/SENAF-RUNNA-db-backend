from django_filters import rest_framework as filters
from infrastructure.models import (
    TPersona, 
    TInstitucionEducativa, 
    TNNyAEducacion, 
    TInstitucionSanitaria, 
    TNNyASalud, 
    TNNyAScore, 
    TLocalizacion, 
    TLegajo, 
    TPersonaHistory, 
    TNNyAEducacionHistory, 
    TNNyASaludHistory,
    TLegajoHistory,
    TNNyAScoreHistory
)


class TPersonaFilter(filters.FilterSet):

    class Meta:
        model = TPersona
        fields = '__all__'


class TInstitucionEducativaFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')
    mail = filters.CharFilter(lookup_expr='icontains')
    telefono = filters.NumberFilter()
    localizacion = filters.ModelChoiceFilter(queryset=TLocalizacion.objects.all())

    class Meta:
        model = TInstitucionEducativa
        fields = ['nombre', 'mail', 'telefono', 'localizacion']


class TNNyAEducacionFilter(filters.FilterSet):
    curso = filters.CharFilter(lookup_expr='icontains')
    nivel = filters.ChoiceFilter(choices=TNNyAEducacion.nivel_choices)
    turno = filters.ChoiceFilter(choices=TNNyAEducacion.turno_choices)
    comentarios = filters.CharFilter(lookup_expr='icontains')
    institucion_educativa = filters.ModelChoiceFilter(queryset=TInstitucionEducativa.objects.all())
    nnya = filters.ModelChoiceFilter(queryset=TPersona.objects.all())

    class Meta:
        model = TNNyAEducacion
        fields = ['curso', 'nivel', 'turno', 'comentarios', 'institucion_educativa', 'nnya', 'deleted']


class TInstitucionSanitariaFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')
    mail = filters.CharFilter(lookup_expr='icontains')
    telefono = filters.NumberFilter()
    localizacion = filters.ModelChoiceFilter(queryset=TLocalizacion.objects.all())

    class Meta:
        model = TInstitucionSanitaria
        fields = ['nombre', 'mail', 'telefono', 'localizacion']


class TNNyASaludFilter(filters.FilterSet):
    observaciones = filters.CharFilter(lookup_expr='icontains')
    institucion_sanitaria = filters.ModelChoiceFilter(queryset=TInstitucionSanitaria.objects.all())
    nnya = filters.ModelChoiceFilter(queryset=TPersona.objects.all())

    class Meta:
        model = TNNyASalud
        fields = ['observaciones', 'institucion_sanitaria', 'nnya', 'deleted']


class TNNyAScoreFilter(filters.FilterSet):
    score = filters.RangeFilter()
    score_condiciones_vulnerabilidad = filters.RangeFilter()
    score_vulneracion = filters.RangeFilter()
    nnya = filters.ModelChoiceFilter(queryset=TPersona.objects.all())

    class Meta:
        model = TNNyAScore
        fields = ['score', 'score_condiciones_vulnerabilidad', 'score_vulneracion', 'nnya']


class TLegajoFilter(filters.FilterSet):
    info_legajo = filters.CharFilter(lookup_expr='icontains')
    nnya = filters.ModelChoiceFilter(queryset=TPersona.objects.all())

    class Meta:
        model = TLegajo
        fields = ['info_legajo', 'nnya']

class TPersonaHistoryFilter(filters.FilterSet):
    class Meta:
        model = TPersonaHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }


class TNNyAEducacionHistoryFilter(filters.FilterSet):
    class Meta:
        model = TNNyAEducacionHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }


class TNNyASaludHistoryFilter(filters.FilterSet):
    class Meta:
        model = TNNyASaludHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }


class TLegajoHistoryFilter(filters.FilterSet):
    class Meta:
        model = TLegajoHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }


class TNNyAScoreHistoryFilter(filters.FilterSet):
    class Meta:
        model = TNNyAScoreHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }
