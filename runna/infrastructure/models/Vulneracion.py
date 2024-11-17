from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _


"""
TCategoriaMotivo
TCategoriaSubmotivo
TGravedadVulneracion
TUrgenciaVulneracion
TVulneracion
TCondicionesVulnerabilidad
TMotivoIntervencion
"""

class TCategoriaMotivo(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField(null=False, blank=False)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Categoria de Motivo')
        verbose_name_plural = _('Categorias de Motivo')

class TCategoriaSubmotivo(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField(null=False, blank=False)

    motivo = models.ForeignKey('TCategoriaMotivo', on_delete=models.CASCADE)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Categoria de Sub-Motivo')
        verbose_name_plural = _('Categorias de Sub-Motivo')


class TGravedadVulneracion(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField(null=False, blank=False)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Gravedad de Vulneracion')
        verbose_name_plural = _('Gravedades de Vulneracion')


class TUrgenciaVulneracion(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField(null=False, blank=False)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Urgencia de Vulneracion')
        verbose_name_plural = _('Urgencias de Vulneracion')


class TCondicionesVulnerabilidad(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField(null=False, blank=False)
    nnya = models.BooleanField(null=False, blank=False)
    adulto = models.BooleanField(null=False, blank=False)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Condicion de Vulnerabilidad')
        verbose_name_plural = _('Condiciones de Vulnerabilidad')


class TMotivoIntervencion(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField(null=False, blank=False)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Condicion de Vulnerabilidad')
        verbose_name_plural = _('Condiciones de Vulnerabilidad')


class TVulneracion(models.Model):
    principal_demanda = models.BooleanField(default=False)
    transcurre_actualidad = models.BooleanField(default=False)
    sumatoria_de_pesos = models.IntegerField(default=0)

    demanda = models.ForeignKey('TDemanda', on_delete=models.SET_NULL, null=True, blank=True)
    nnya = models.ForeignKey('TPersona', on_delete=models.CASCADE, null=False, blank=False, related_name='vulneracion_nnya')
    autor_dv = models.ForeignKey('TPersona', on_delete=models.SET_NULL, null=True, blank=True, related_name='vulneracion_autordv')

    categoria_motivo = models.ForeignKey('TCategoriaMotivo', on_delete=models.CASCADE, null=False)
    categoria_submotivo = models.ForeignKey('TCategoriaSubmotivo', on_delete=models.CASCADE, null=False)
    gravedad_vulneracion = models.ForeignKey('TGravedadVulneracion', on_delete=models.CASCADE, null=False)
    urgencia_vulneracion = models.ForeignKey('TUrgenciaVulneracion', on_delete=models.CASCADE, null=False)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Vulneracion')
        verbose_name_plural = _('Vulneraciones')

