from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _


"""
TActividadTipo
TInstitucionActividad
TActividad
TInstitucionRespuesta
TRespuesta
TIndicadoresValoracion
TEvaluaciones
TDecision
"""

class TActividadTipo(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Tipo de Actividad')
        verbose_name_plural = _('Tipos de Actividades')


class TInstitucionActividad(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    mail = models.EmailField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)

    localizacion = models.ForeignKey('TLocalizacion', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Institucion de Actividad')
        verbose_name_plural = _('Instituciones de Actividades')


class TActividad(models.Model):
    fecha_y_hora = models.DateTimeField(auto_now=True)
    descripcion = models.TextField(blank=False, null=False)

    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    tipo = models.ForeignKey('TActividadTipo', on_delete=models.SET_NULL, null=True, blank=True)
    institucion = models.ForeignKey('TInstitucionActividad', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Actividad')
        verbose_name_plural = _('Actividades')


class TInstitucionRespuesta(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    mail = models.EmailField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)

    localizacion = models.ForeignKey('TLocalizacion', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Institucion de Respuesta')
        verbose_name_plural = _('Instituciones de Respuestas')


class TRespuesta(models.Model):
    fecha_y_hora = models.DateTimeField(auto_now=True)
    mail = models.EmailField(null=False, blank=False)
    mensaje = models.TextField(null=False, blank=False)
    
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    institucion = models.ForeignKey('TInstitucionRespuesta', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Respuesta')
        verbose_name_plural = _('Respuestas')


class TIndicadoresValoracion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField(default=0)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Indicador de Valoracion')
        verbose_name_plural = _('Indicadores de Valoracion')


class TEvaluaciones(models.Model):
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    indicador = models.ForeignKey('TIndicadoresValoracion', on_delete=models.CASCADE)
    si_no = models.BooleanField(null=False, blank=False)

    history = HistoricalRecords()
    
    class Meta:
        unique_together = ('demanda', 'indicador')
        app_label = 'infrastructure'
        verbose_name = _('Evaluacion')
        verbose_name_plural = _('Evaluaciones')


class TDecision(models.Model):
    fecha_y_hora = models.DateTimeField(auto_now=True)
    justificacion = models.TextField(null=False, blank=False)
    decision_choices = [
        ('APERTURA DE LEGAJO', 'Apertura de Legajo'),
        ('RECHAZAR CASO', 'Rechazar Caso')
    ]
    decision = models.CharField(max_length=20, choices=decision_choices, null=False)

    demanda = models.OneToOneField('TDemanda', on_delete=models.CASCADE, null=False)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Decision')
        verbose_name_plural = _('Decisiones')

