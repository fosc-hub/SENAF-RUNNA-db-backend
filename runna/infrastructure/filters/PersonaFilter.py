from django_filters import rest_framework as filters
from infrastructure.models import TPersona, TInstitucionEducativa, TNNyAEducacion, TInstitucionSanitaria, TNNyASalud, TNNyAScore, TLocalizacion, TLegajo, TPersonaHistory, TNNyAEducacionHistory, TNNyASaludHistory


class TPersonaFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')
    apellido = filters.CharFilter(lookup_expr='icontains')
    dni = filters.NumberFilter()
    situacion_dni = filters.ChoiceFilter(choices=TPersona.situacion_dni_choices)
    genero = filters.ChoiceFilter(choices=TPersona.genero_choices)
    adulto = filters.BooleanFilter()
    nnya = filters.BooleanFilter()

    class Meta:
        model = TPersona
        fields = ['nombre', 'apellido', 'dni', 'situacion_dni', 'genero', 'adulto', 'nnya', 'deleted']


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
    score_motivo_intervencion = filters.RangeFilter()
    nnya = filters.ModelChoiceFilter(queryset=TPersona.objects.all())

    class Meta:
        model = TNNyAScore
        fields = ['score', 'score_condiciones_vulnerabilidad', 'score_vulneracion', 'score_motivo_intervencion', 'nnya']


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
            'user': ['exact'],
        }


class TNNyAEducacionHistoryFilter(filters.FilterSet):
    class Meta:
        model = TNNyAEducacionHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'user': ['exact'],
        }


class TNNyASaludHistoryFilter(filters.FilterSet):
    class Meta:
        model = TNNyASaludHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'user': ['exact'],
        }