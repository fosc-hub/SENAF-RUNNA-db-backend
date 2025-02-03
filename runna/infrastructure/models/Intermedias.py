from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from .BaseHistory import BaseHistory
from django.core.exceptions import ValidationError

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
        # unique_together = ('localizacion', 'persona')
        app_label = 'infrastructure'
        verbose_name = _('Localizacion de Persona')
        verbose_name_plural = _('Localizaciones de Personas')
    
    def save(self, *args, **kwargs):
        if self.principal:
            TLocalizacionPersona.objects.filter(persona=self.persona, principal=True).update(principal=False)
        super().save(*args, **kwargs)


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


class TDemandaPersonaBase(models.Model):
    deleted = models.BooleanField(default=False)
    conviviente = models.BooleanField(null=False, blank=False)
    
    supuesto_autordv_choices = [
        ('NO_CORRESPONDE', 'No corresponde'),
        ('CORRESPONDE', 'Corresponde'),
        ('SE_DESCONOCE', 'Se desconoce')
    ]
    supuesto_autordv = models.CharField(
        max_length=20,
        choices=supuesto_autordv_choices,
        default="Corresponde",
        null=False,
        blank=False
    )
        
    supuesto_autordv_principal = models.BooleanField(null=False, blank=False)
    nnya_principal = models.BooleanField(null=False, blank=False)
    
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    persona = models.ForeignKey('TPersona', on_delete=models.CASCADE)
    
    class Meta:
        abstract = True


class TDemandaPersona(TDemandaPersonaBase):

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        # unique_together = ('demanda', 'persona')
        app_label = 'infrastructure'
        verbose_name = _('Persona asociada a Demanda')
        verbose_name_plural = _('Personas asociadas a Demandas')
        
    def save(self, *args, **kwargs):
        if self.supuesto_autordv_principal:
            if TDemandaPersona.objects.filter(demanda=self.demanda, supuesto_autordv_principal=True).exclude(pk=self.pk).exists():
                raise ValidationError("Ya existe un supuesto autor principal para esta demanda.")
        if self.supuesto_autordv=="CORRESPONDE" or self.supuesto_autordv_principal:
            if self.persona.nnya:
                raise ValidationError("La persona seleccionada como supuesto autor debe ser un adulto.")
        if self.nnya_principal:
            if TDemandaPersona.objects.filter(demanda=self.demanda, nnya_principal=True).exclude(pk=self.pk).exists():
                raise ValidationError("Ya existe un NNyA principal para esta demanda.")
            if not self.persona.nnya:
                raise ValidationError("La persona seleccionada como nnya principal debe ser un NNyA.")
        super().save(*args, **kwargs)


class TDemandaPersonaHistory(TDemandaPersonaBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TDemandaPersona',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Persona asociada a Demanda')
        verbose_name_plural = _('Historial de Personas asociadas a Demandas')


class TDemandaAsignadoBase(models.Model):
    esta_activo = models.BooleanField(default=True)
    recibido = models.BooleanField(default=False)
    comentarios = models.TextField(null=True, blank=True)
    
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    user = models.ForeignKey('customAuth.CustomUser', on_delete=models.CASCADE,  related_name='%(class)s_user')

    class Meta:
        abstract = True


class TDemandaAsignado(TDemandaAsignadoBase):

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.esta_activo = False
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        unique_together = ('demanda', 'user')
        app_label = 'infrastructure'
        verbose_name = _('Asignacion de Demanda')
        verbose_name_plural = _('Asignaciones de Demandas')


class TDemandaAsignadoHistory(TDemandaAsignadoBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TDemandaAsignado',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Asignacion de Demanda')
        verbose_name_plural = _('Historial de Asignaciones de Demandas')


class TDemandaVinculadaBase(models.Model):
    deleted = models.BooleanField(default=False)
    demanda_1 = models.ForeignKey('TDemanda', related_name="%(class)sdemanda_1", on_delete=models.CASCADE)
    demanda_2 = models.ForeignKey('TDemanda', related_name="%(class)sdemanda_2", on_delete=models.CASCADE)

    class Meta:
        abstract = True


class TDemandaVinculada(TDemandaVinculadaBase):

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        # unique_together = ('demanda_1', 'demanda_2')
        app_label = 'infrastructure'
        verbose_name = _('Vinculacion de Demandas')
        verbose_name_plural = _('Vinculaciones de Demandas')


class TDemandaVinculadaHistory(TDemandaVinculadaBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TDemandaVinculada',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Vinculacion de Demandas')
        verbose_name_plural = _('Historial de Vinculaciones de Demandas')


class TLegajoAsignado(models.Model):
    esta_activo = models.BooleanField(default=True)
    recibido = models.BooleanField(default=False)
    comentarios = models.TextField(null=True, blank=True)
    
    legajo = models.ForeignKey('TLegajo', on_delete=models.CASCADE)
    user = models.ForeignKey('customAuth.CustomUser', on_delete=models.CASCADE)

    
    
    class Meta:
        # unique_together = ('legajo', 'user')
        app_label = 'infrastructure'
        verbose_name = _('Asignacion de Legajo')
        verbose_name_plural = _('Asignaciones de Legajos')


class TVinculoPersona(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)

    
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Vinculo de Personas')
        verbose_name_plural = _('Vinculos de Personas')


class TVinculoPersonaPersonaBase(models.Model):
    deleted = models.BooleanField(default=False)
    conviven = models.BooleanField(null=False, blank=False)
    autordv = models.BooleanField(null=False, blank=False)
    garantiza_proteccion = models.BooleanField(null=False, blank=False)

    persona_1 = models.ForeignKey('TPersona', related_name='%(class)s_persona_1', on_delete=models.CASCADE)
    persona_2 = models.ForeignKey('TPersona', related_name='%(class)s_persona_2', on_delete=models.CASCADE)
    vinculo = models.ForeignKey('TVinculoPersona', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True


class TVinculoPersonaPersona(TVinculoPersonaPersonaBase):

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        # unique_together = ('persona_1', 'persona_2')
        app_label = 'infrastructure'
        verbose_name = _('Vinculo entre Personas')
        verbose_name_plural = _('Vinculos entre Personas')

    def save(self, *args, **kwargs):
        if self.garantiza_proteccion and self.autordv:
            raise ValidationError("No puede garantizar proteccion y ser supuesto autor a la vez")
        if self.garantiza_proteccion and (self.persona_1.nnya and self.persona_2.nnya):
            raise ValidationError("Un nnya no puede garantizar proteccion a otro nnya")
        super().save(*args, **kwargs)


class TVinculoPersonaPersonaHistory(TVinculoPersonaPersonaBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TVinculoPersonaPersona',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Vinculo entre Personas')
        verbose_name_plural = _('Historial de Vinculos entre Personas')


class TPersonaCondicionesVulnerabilidadBase(models.Model):
    si_no = models.BooleanField(null=False, blank=False)

    persona = models.ForeignKey('TPersona', on_delete=models.CASCADE)
    condicion_vulnerabilidad = models.ForeignKey('TCondicionesVulnerabilidad', on_delete=models.CASCADE)
    demanda = models.ForeignKey('TDemanda', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True


class TPersonaCondicionesVulnerabilidad(TPersonaCondicionesVulnerabilidadBase):

    class Meta:
        # unique_together = ('persona', 'condicion_vulnerabilidad')
        app_label = 'infrastructure'
        verbose_name = _('Condicion de Vulnerabilidad de Persona')
        verbose_name_plural = _('Condiciones de Vulnerabilidad de Personas')

        
    def save(self, *args, **kwargs):
        if self.condicion_vulnerabilidad.nnya and not self.persona.nnya:
            raise ValidationError(f"La persona debe ser un NNyA para esta Condicion de Vulnerabilidad {self.condicion_vulnerabilidad}")
        if self.condicion_vulnerabilidad.adulto and not self.persona.adulto:
            raise ValidationError(f"La persona debe ser un adulto para esta Condicion de Vulnerabilidad {self.condicion_vulnerabilidad}")
        super().save(*args, **kwargs)


class TPersonaCondicionesVulnerabilidadHistory(TPersonaCondicionesVulnerabilidadBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TPersonaCondicionesVulnerabilidad',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Condicion de Vulnerabilidad de Persona')
        verbose_name_plural = _('Historial de Condiciones de Vulnerabilidad de Personas')

class TDemandaMotivoIntervencionBase(models.Model):
    si_no = models.BooleanField(null=False, blank=False)
    
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    motivo_intervencion = models.ForeignKey('TMotivoIntervencion', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class TDemandaMotivoIntervencion(TDemandaMotivoIntervencionBase):

    class Meta:
        # unique_together = ('demanda', 'motivo_intervencion')
        app_label = 'infrastructure'
        verbose_name = _('Motivo de Intervencion de Demanda')
        verbose_name_plural = _('Motivos de Intervencion de Demandas')


class TDemandaMotivoIntervencionHistory(TDemandaMotivoIntervencionBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TDemandaMotivoIntervencion',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Motivo de Intervencion de Demanda')
        verbose_name_plural = _('Historial de Motivos de Intervencion de Demandas')
