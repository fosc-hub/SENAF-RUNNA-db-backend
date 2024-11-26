from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from .BaseHistory import BaseHistory

# The following models are used to represent the location of a user in the system.
class TProvincia(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Provincia')
        verbose_name_plural = _('Provincias')

class TDepartamento(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)

    provincia = models.ForeignKey('infrastructure.TProvincia', on_delete=models.CASCADE)

    history = HistoricalRecords()

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Departamento')
        verbose_name_plural = _('Departamentos')

class TLocalidad(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)

    departamento = models.ForeignKey('infrastructure.TDepartamento', on_delete=models.CASCADE)

    history = HistoricalRecords()

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Localidad')
        verbose_name_plural = _('Localidades')

class TBarrio(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    localidad = models.ForeignKey('infrastructure.TLocalidad', on_delete=models.CASCADE)

    history = HistoricalRecords()

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Barrio')
        verbose_name_plural = _('Barrios')

class TCPC(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    localidad = models.ForeignKey('infrastructure.TLocalidad', on_delete=models.CASCADE)

    history = HistoricalRecords()

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('CPC')
        verbose_name_plural = _('CPCs')

class TLocalizacionBase(models.Model):
    deleted = models.BooleanField(default=False)
    calle = models.CharField(max_length=255, null=False, blank=False)
    tipo_calle_choices = [
        ('CALLE', 'Calle'),
        ('AVENIDA', 'Avenida'),
        ('PASAJE', 'Pasaje'),
        ('RUTA', 'Ruta'),
        ('BOULEVARD', 'Boulevard'),
        ('OTRO', 'Otro')
    ]
    tipo_calle = models.CharField(max_length=10, choices=tipo_calle_choices, null=False, blank=False)
    piso_depto = models.IntegerField(null=True, blank=True)
    lote = models.IntegerField(null=True, blank=True)
    mza = models.IntegerField(null=True, blank=True)
    casa_nro = models.IntegerField(null=True, blank=True)
    referencia_geo = models.TextField(null=False, blank=False)
    barrio = models.ForeignKey('infrastructure.TBarrio', on_delete=models.SET_NULL, null=True, blank=True)
    localidad = models.ForeignKey('infrastructure.TLocalidad', on_delete=models.CASCADE, null=False)
    cpc = models.ForeignKey('infrastructure.TCPC', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True

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
