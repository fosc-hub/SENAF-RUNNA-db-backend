from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from .BaseHistory import BaseHistory

"""
TLocalizacionPersona
TDemandaPersona
TDemandaAsignado
TDemandaVinculada
TLegajoAsignado
TVinculoPersona
TVinculoPersonaPersona
TDemandaMotivoIntervencion
TPersonaCondicionesVulnerabilidad
"""
class TLocalizacionPersonaBase(models.Model):
    deleted = models.BooleanField(default=False)
    persona = models.ForeignKey('TPersona', on_delete=models.CASCADE)
    localizacion = models.ForeignKey('TLocalizacion', on_delete=models.CASCADE)
    principal = models.BooleanField(null=False, default=False)

    class Meta:
        abstract = True


class TLocalizacionPersona(TLocalizacionPersonaBase):

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        unique_together = ('localizacion', 'persona')
        app_label = 'infrastructure'
        verbose_name = _('Localizacion de Persona')
        verbose_name_plural = _('Localizaciones de Personas')


class TLocalizacionPersonaHistory(TLocalizacionPersonaBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TLocalizacionPersona',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Localizacion de Persona')
        verbose_name_plural = _('Historial de Localizaciones de Personas')


class TDemandaPersona(models.Model):
    conviviente = models.BooleanField(null=False, blank=False)
    supuesto_autordv = models.BooleanField(null=False, blank=False)
    supuesto_autordv_principal = models.BooleanField(null=False, blank=False)
    nnya = models.BooleanField(null=False, blank=False)
    nnya_principal = models.BooleanField(null=False, blank=False)
    
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    persona = models.ForeignKey('TPersona', on_delete=models.CASCADE)

    history = HistoricalRecords()
    
    class Meta:
        unique_together = ('demanda', 'persona')
        app_label = 'infrastructure'
        verbose_name = _('Persona asociada a Demanda')
        verbose_name_plural = _('Personas asociadas a Demandas')


class TDemandaAsignado(models.Model):
    esta_activo = models.BooleanField(default=True)
    recibido = models.BooleanField(default=False)
    comentarios = models.TextField(null=True, blank=True)
    
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    user = models.ForeignKey('customAuth.CustomUser', on_delete=models.CASCADE)

    history = HistoricalRecords()
    
    class Meta:
        unique_together = ('demanda', 'user')
        app_label = 'infrastructure'
        verbose_name = _('Asignacion de Demanda')
        verbose_name_plural = _('Asignaciones de Demandas')


class TDemandaVinculada(models.Model):
    demanda_1 = models.ForeignKey('TDemanda', related_name="demanda_1", on_delete=models.CASCADE)
    demanda_2 = models.ForeignKey('TDemanda', related_name="demanda_2", on_delete=models.CASCADE)

    history = HistoricalRecords()
        
    class Meta:
        unique_together = ('demanda_1', 'demanda_2')
        app_label = 'infrastructure'
        verbose_name = _('Vinculacion de Demandas')
        verbose_name_plural = _('Vinulaciones de Demandas')


class TLegajoAsignado(models.Model):
    esta_activo = models.BooleanField(default=True)
    recibido = models.BooleanField(default=False)
    comentarios = models.TextField(null=True, blank=True)
    
    legajo = models.ForeignKey('TLegajo', on_delete=models.CASCADE)
    user = models.ForeignKey('customAuth.CustomUser', on_delete=models.CASCADE)

    history = HistoricalRecords()
    
    class Meta:
        unique_together = ('legajo', 'user')
        app_label = 'infrastructure'
        verbose_name = _('Asignacion de Legajo')
        verbose_name_plural = _('Asignaciones de Legajos')


class TVinculoPersona(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Vinculo de Personas')
        verbose_name_plural = _('Vinculos de Personas')


class TVinculoPersonaPersona(models.Model):
    conviven = models.BooleanField(null=False, blank=False)
    autordv = models.BooleanField(null=False, blank=False)
    garantiza_proteccion = models.BooleanField(null=False, blank=False)

    persona_1 = models.ForeignKey('TPersona', related_name='persona_1', on_delete=models.CASCADE)
    persona_2 = models.ForeignKey('TPersona', related_name='persona_2', on_delete=models.CASCADE)
    vinculo = models.ForeignKey('TVinculoPersona', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()    
    
    class Meta:
        unique_together = ('persona_1', 'persona_2')
        app_label = 'infrastructure'
        verbose_name = _('Vinculo entre Personas')
        verbose_name_plural = _('Vinculos entre Personas')


class TPersonaCondicionesVulnerabilidad(models.Model):
    si_no = models.BooleanField(null=False, blank=False)
    
    persona = models.ForeignKey('TPersona', on_delete=models.CASCADE)
    condicion_vulnerabilidad = models.ForeignKey('TCondicionesVulnerabilidad', on_delete=models.CASCADE)
    demanda = models.ForeignKey('TDemanda', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()
    
    class Meta:
        unique_together = ('persona', 'condicion_vulnerabilidad')
        app_label = 'infrastructure'
        verbose_name = _('Condicion de Vulnerabilidad de Persona')
        verbose_name_plural = _('Condiciones de Vulnerabilidad de Personas')


class TDemandaMotivoIntervencion(models.Model):
    si_no = models.BooleanField(null=False, blank=False)
    
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    motivo_intervencion = models.ForeignKey('TMotivoIntervencion', on_delete=models.CASCADE)

    history = HistoricalRecords()
    
    class Meta:
        unique_together = ('demanda', 'motivo_intervencion')
        app_label = 'infrastructure'
        verbose_name = _('Motivo de Intervencion de Demanda')
        verbose_name_plural = _('Motivos de Intervencion de Demandas')
