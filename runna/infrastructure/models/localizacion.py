from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _

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

class TLocalizacion(models.Model):
    calle = models.CharField(max_length=255, null=False, blank=False)
    tipo_calle_choices = [
        ('CALLE', 'Calle'),
        ('AVENIDA', 'Avenida'),
        ('PASAJE', 'Pasaje'),
        ('RUTA', 'Ruta'),
        ('BOULEVAR', 'Boulevard'),
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

    history = HistoricalRecords()

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Localizacion')
        verbose_name_plural = _('Localizaciones')
