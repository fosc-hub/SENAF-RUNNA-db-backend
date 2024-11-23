from django_filters import rest_framework as filters
from infrastructure.models import  TInstitucionUsuarioExterno, TVinculoUsuarioExterno, TUsuarioExterno, TDemanda, TPrecalificacionDemanda, TScoreDemanda, TLocalizacion, TDemandaHistory, TPrecalificacionDemandaHistory
 
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
    fecha_y_hora_ingreso = filters.DateTimeFilter()  # Exact match for fecha_y_hora_ingreso
    origen = filters.ChoiceFilter(choices=[
        ('WEB', 'Web'),
        ('TELEFONO', 'Telefono'),
        ('MAIL', 'Mail'),
        ('PERSONAL', 'Personal'),
        ('OTRO', 'Otro')
    ])  # Exact match for origen
    nro_notificacion_102 = filters.NumberFilter()  # Exact match for nro_notificacion_102
    nro_sac = filters.NumberFilter()  # Exact match for nro_sac
    nro_suac = filters.NumberFilter()  # Exact match for nro_suac
    nro_historia_clinica = filters.NumberFilter()  # Exact match for nro_historia_clinica
    nro_oficio_web = filters.NumberFilter()  # Exact match for nro_oficio_web
    descripcion = filters.CharFilter(lookup_expr='icontains')  # Partial match for descripcion
    ultima_actualizacion = filters.DateTimeFilter()  # Exact match for ultima_actualizacion

    localizacion = filters.ModelChoiceFilter(queryset=TLocalizacion.objects.all())  # Exact match for localizacion

    usuario_externo = filters.ModelChoiceFilter(queryset=TUsuarioExterno.objects.all())  # Exact match for usuario_externo

    class Meta:
        model = TDemanda
        fields = [
            'fecha_y_hora_ingreso', 'origen', 'nro_notificacion_102', 'nro_sac', 'nro_suac',
            'nro_historia_clinica', 'nro_oficio_web', 'descripcion', 'ultima_actualizacion',
            'localizacion', 'usuario_externo', 'deleted'
        ]


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
        fields = ['fecha_y_hora', 'descripcion', 'estado_demanda', 'ultima_actualizacion', 'demanda', 'deleted']



class TScoreDemandaFilter(filters.FilterSet):
    ultima_actualizacion = filters.DateTimeFilter()  # Exact match for ultima_actualizacion
    score = filters.NumberFilter()  # Exact match for score
    score_condiciones_vulnerabilidad = filters.NumberFilter()  # Exact match for score_condiciones_vulnerabilidad
    score_vulneracion = filters.NumberFilter()  # Exact match for score_vulneracion
    score_motivo_vulneracion = filters.NumberFilter()  # Exact match for score_motivo_vulneracion

    demanda = filters.ModelChoiceFilter(queryset=TDemanda.objects.all())  # Exact match for demanda

    class Meta:
        model = TScoreDemanda
        fields = [
            'ultima_actualizacion', 'score', 'score_condiciones_vulnerabilidad',
            'score_vulneracion', 'score_motivo_vulneracion', 'demanda'
        ]

class TDemandaHistoryFilter(filters.FilterSet):
    class Meta:
        model = TDemandaHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'user': ['exact'],
        }


class TPrecalificacionDemandaHistoryFilter(filters.FilterSet):
    class Meta:
        model = TPrecalificacionDemandaHistory
        fields = {
            'parent': ['exact'],
            'action': ['exact'],
            'user': ['exact'],
        }
