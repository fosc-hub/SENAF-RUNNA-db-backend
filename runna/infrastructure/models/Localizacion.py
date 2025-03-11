from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from .BaseClass import BaseHistory


class TLocalidad(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Localidad')
        verbose_name_plural = _('Localidades')
    
    def __str__(self):
        return f"{self.nombre}"


class TBarrio(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    localidad = models.ForeignKey('infrastructure.TLocalidad', on_delete=models.CASCADE)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Barrio')
        verbose_name_plural = _('Barrios')

    def __str__(self):
        return f"{self.nombre} - {self.localidad}"


class TCPC(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    localidad = models.ForeignKey('infrastructure.TLocalidad', on_delete=models.CASCADE)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('CPC')
        verbose_name_plural = _('CPCs')
        
    def __str__(self):
        return f"{self.nombre} - {self.localidad}"


class TLocalizacionBase(models.Model):
    deleted = models.BooleanField(default=False)

    calle = models.CharField(max_length=255, null=False, blank=False)
    TIPO_CALLE_CHOICES = [
        ('CALLE', 'Calle'),
        ('AVENIDA', 'Avenida'),
        ('PASAJE', 'Pasaje'),
        ('RUTA', 'Ruta'),
        ('BOULEVARD', 'Boulevard'),
        ('OTRO', 'Otro')
    ]
    tipo_calle = models.CharField(max_length=10, choices=TIPO_CALLE_CHOICES, null=True, blank=True)

    piso_depto = models.IntegerField(null=True, blank=True)
    lote = models.IntegerField(null=True, blank=True)
    mza = models.IntegerField(null=True, blank=True)
    casa_nro = models.IntegerField(null=False, blank=False)

    referencia_geo = models.TextField(null=False, blank=False)
    geolocalizacion = models.CharField(max_length=255, null=True, blank=True)

    barrio = models.ForeignKey('infrastructure.TBarrio', on_delete=models.SET_NULL, null=True, blank=True)
    localidad = models.ForeignKey('infrastructure.TLocalidad', on_delete=models.PROTECT, null=False)
    cpc = models.ForeignKey('infrastructure.TCPC', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return f"{self.calle} - {self.tipo_calle} - {self.piso_depto} - {self.lote} - {self.mza} - {self.casa_nro} - {self.referencia_geo} - {self.barrio} - {self.localidad} - {self.cpc}"

class TLocalizacion(TLocalizacionBase):


    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Localizacion')
        verbose_name_plural = _('Localizaciones')

class TLocalizacionHistory(TLocalizacionBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TLocalizacion',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Localizacion')
        verbose_name_plural = _('Historial de Localizaciones')

    def __str__(self):
        return f"{self.action} - {self.timestamp} - {self.by_user} - {self.parent}"
