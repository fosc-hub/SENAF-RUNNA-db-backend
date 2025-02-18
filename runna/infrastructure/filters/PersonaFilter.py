from django_filters import rest_framework as filters
from infrastructure.models import (
    TPersona,
    TPersonaHistory,
    TInstitucionEducativa,
    TEducacion,
    TEducacionHistory,
    TInstitucionSanitaria,
    TSituacionSalud,
    TEnfermedad,
    TMedico,
    TCoberturaMedica,
    TCoberturaMedicaHistory,
    TPersonaEnfermedades,
    TPersonaEnfermedadesHistory,
    TNNyAScore,
    TNNyAScoreHistory,
    TLegajo,
    TLegajoHistory,
)
class TPersonaFilter(filters.FilterSet):
    class Meta:
        model = TPersona
        fields = '__all__'

class TPersonaHistoryFilter(filters.FilterSet):
    class Meta:
        model = TPersonaHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }

class TInstitucionEducativaFilter(filters.FilterSet):
    class Meta:
        model = TInstitucionEducativa
        fields = '__all__'

class TEducacionFilter(filters.FilterSet):
    class Meta:
        model = TEducacion
        fields = '__all__'

class TEducacionHistoryFilter(filters.FilterSet):
    class Meta:
        model = TEducacionHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }

class TInstitucionSanitariaFilter(filters.FilterSet):
    class Meta:
        model = TInstitucionSanitaria
        fields = '__all__'

class TSituacionSaludFilter(filters.FilterSet):
    class Meta:
        model = TSituacionSalud
        fields = '__all__'

class TEnfermedadFilter(filters.FilterSet):
    class Meta:
        model = TEnfermedad
        fields = '__all__'

class TMedicoFilter(filters.FilterSet):
    class Meta:
        model = TMedico
        fields = '__all__'

class TCoberturaMedicaFilter(filters.FilterSet):
    class Meta:
        model = TCoberturaMedica
        fields = '__all__'

class TCoberturaMedicaHistoryFilter(filters.FilterSet):
    class Meta:
        model = TCoberturaMedicaHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }

class TPersonaEnfermedadesFilter(filters.FilterSet):
    class Meta:
        model = TPersonaEnfermedades
        fields = '__all__'

class TPersonaEnfermedadesHistoryFilter(filters.FilterSet):
    class Meta:
        model = TPersonaEnfermedadesHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }

class TNNyAScoreFilter(filters.FilterSet):
    class Meta:
        model = TNNyAScore
        fields = '__all__'

class TNNyAScoreHistoryFilter(filters.FilterSet):
    class Meta:
        model = TNNyAScoreHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }

class TLegajoFilter(filters.FilterSet):
    class Meta:
        model = TLegajo
        fields = '__all__'

class TLegajoHistoryFilter(filters.FilterSet):
    class Meta:
        model = TLegajoHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'by_user': ['exact'],
        }
