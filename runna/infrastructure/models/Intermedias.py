from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from .BaseHistory import BaseHistory
from django.core.exceptions import ValidationError

"""
TLocalizacionPersona
TDemandaPersona
TDemandaZona
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

    def __str__(self):
        return f"{self.persona} {self.localizacion} - {self.principal}"    


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
    vinculo_demanda_choices = [
        ('NNYA_PRINCIPAL', 'NNYA Principal'),
        ('NNYA_SECUNDARIO', 'NNYA Secundario'),
        ('SUPUESTO_AUTOR_DV', 'Supuesto Autor DV'),
        ('SUPUESTO_AUTOR_DV_PRINCIPAL', 'Supuesto Autor DV Principal'),
        ('GARANTIZA_PROTECCION', 'Garantiza Protección'),
        ('SE_DESCONOCE', 'Se Desconoce'),
    ]
    vinculo_demanda = models.CharField(
        max_length=30,
        choices=vinculo_demanda_choices,
        default='SE_DESCONOCE',
        null=False,
        blank=False
    )
    vinculo_con_nnya_principal_choices = [
        ('MADRE', 'Madre'),
        ('PADRE', 'Padre'),
        ('TUTOR', 'Tutor'),
        ('HERMANO', 'Hermano'),
        ('ABUELO', 'Abuelo'),
        ('OTRO', 'Otro'),
        ('NO_CORRESPONDE', 'No Corresponde'),
    ]
    vinculo_con_nnya_principal = models.CharField(
        max_length=30,
        choices=vinculo_con_nnya_principal_choices,
        null=False,
        blank=False
    )

    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    persona = models.ForeignKey('TPersona', on_delete=models.CASCADE)
    
    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.demanda} {self.persona} - {self.supuesto_autordv} - {self.supuesto_autordv_principal} - {self.nnya_principal}"


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
        if self.vinculo_demanda == 'NNYA_PRINCIPAL':
            if TDemandaPersona.objects.filter(demanda=self.demanda, persona=self.persona, vinculo_demanda='NNYA_PRINCIPAL').exists():
                raise ValidationError("Ya existe un NNYA Principal para esta demanda y persona")
            if self.vinculo_con_nnya_principal != 'NO_CORRESPONDE':
                raise ValidationError("El nnya ingresante es un NNyA principal, no corresponde ingresar un vinculo con si mismo")
        if self.vinculo_demanda == 'SUPUESTO_AUTOR_DV_PRINCIPAL':
            if TDemandaPersona.objects.filter(demanda=self.demanda, persona=self.persona, vinculo_demanda='SUPUESTO_AUTOR_DV_PRINCIPAL').exists():
                raise ValidationError("Ya existe un Supuesto Autor DV Principal para esta demanda y persona")
        if (self.vinculo_demanda in ['NNYA_PRINCIPAL', 'NNYA_SECUNDARIO']) and not self.persona.nnya:
            raise ValidationError("La persona seleccionada como nnya debe ser un NNyA")
        if (self.vinculo_demanda in ['SUPUESTO_AUTOR_DV', 'SUPUESTO_AUTOR_DV_PRINCIPAL']) and self.persona.nnya:
            raise ValidationError("La persona seleccionada como supuesto autor debe ser un adulto")
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


class TDemandaZonaBase(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_recibido = models.DateTimeField(null=True, blank=True)
    esta_activo = models.BooleanField(default=True)
    recibido = models.BooleanField(default=False)
    comentarios = models.TextField(null=True, blank=True)
    
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    enviado_por = models.ForeignKey('customAuth.CustomUser', related_name="%(class)senviado_por", on_delete=models.PROTECT, null=True)
    recibido_por = models.ForeignKey('customAuth.CustomUser', related_name="%(class)srecibido_por", on_delete=models.PROTECT, null=True)
    zona = models.ForeignKey('customAuth.TZona', on_delete=models.CASCADE)

    class Meta:
        abstract = True
    
    def __str__(self):
        return f"{self.demanda} {self.user} - {self.esta_activo}"


class TDemandaZona(TDemandaZonaBase):

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.esta_activo = False
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Asignacion de Demanda')
        verbose_name_plural = _('Asignaciones de Demandas')


class TDemandaZonaHistory(TDemandaZonaBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TDemandaZona',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Asignacion de Demanda')
        verbose_name_plural = _('Historial de Asignaciones de Demandas')


class TDemandaVinculadaBase(models.Model):
    deleted = models.BooleanField(default=False)
    demanda_padre = models.ForeignKey('TDemanda', related_name="%(class)sdemanda_padre", on_delete=models.CASCADE)
    demanda_hijo = models.ForeignKey('TDemanda', related_name="%(class)sdemanda_hijo", on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.demanda_padre} {self.demanda_hijo}"

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


class TPersonaCondicionesVulnerabilidadBase(models.Model):
    si_no = models.BooleanField(null=False, blank=False)

    persona = models.ForeignKey('TPersona', on_delete=models.CASCADE)
    condicion_vulnerabilidad = models.ForeignKey('TCondicionesVulnerabilidad', on_delete=models.CASCADE)
    demanda = models.ForeignKey('TDemanda', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return f"{self.persona} {self.condicion_vulnerabilidad} - {self.si_no} - {self.demanda}"


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

