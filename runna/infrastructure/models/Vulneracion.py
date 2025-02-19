from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from .BaseHistory import BaseHistory
from django.core.exceptions import ValidationError

"""
TCategoriaMotivo
TCategoriaSubmotivo
TGravedadVulneracion
TUrgenciaVulneracion
TVulneracion
TCondicionesVulnerabilidad
"""


class TCategoriaMotivo(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False, blank=False)
    peso = models.IntegerField(null=False, blank=False)
 
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Categoria de Motivo')
        verbose_name_plural = _('Categorias de Motivo')
    
    def __str__(self):
        return f"{self.nombre} - {self.peso}"
        

class TCategoriaSubmotivo(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False, blank=False)
    peso = models.IntegerField(null=False, blank=False)

    motivo = models.ForeignKey('TCategoriaMotivo', on_delete=models.CASCADE)
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Categoria de Sub-Motivo')
        verbose_name_plural = _('Categorias de Sub-Motivo')

    def __str__(self):
        return f"{self.nombre} - {self.motivo} - {self.peso}"


class TGravedadVulneracion(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False, blank=False)
    peso = models.IntegerField(null=False, blank=False)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Gravedad de Vulneracion')
        verbose_name_plural = _('Gravedades de Vulneracion')

    def __str__(self):
        return f"{self.nombre} - {self.peso}"


class TUrgenciaVulneracion(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False, blank=False)
    peso = models.IntegerField(null=False, blank=False)
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Urgencia de Vulneracion')
        verbose_name_plural = _('Urgencias de Vulneracion')
    
    def __str__(self):
        return f"{self.nombre} - {self.peso}"


class TCondicionesVulnerabilidad(models.Model):
    nombre = models.CharField(max_length=255, unique=True, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField(null=False, blank=False)
    nnya = models.BooleanField(null=False, blank=False)
    adulto = models.BooleanField(null=False, blank=False)
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Condicion de Vulnerabilidad')
        verbose_name_plural = _('Condiciones de Vulnerabilidad')
    
    def __str__(self):
        return f"{self.nombre} - {self.peso} - {self.nnya} - {self.adulto}"


class TVulneracionBase(models.Model):
    deleted = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    principal_demanda = models.BooleanField(default=False)
    transcurre_actualidad = models.BooleanField(default=False)
    sumatoria_de_pesos = models.IntegerField(default=0)

    demanda = models.ForeignKey('TDemanda', on_delete=models.SET_NULL, null=True, blank=True)
    nnya = models.ForeignKey(
        'TPersona',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='%(class)s_nnya'
    )
    autor_dv = models.ForeignKey(
        'TPersona',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_autordv'
    )

    categoria_motivo = models.ForeignKey('TCategoriaMotivo', on_delete=models.CASCADE, null=False)
    categoria_submotivo = models.ForeignKey('TCategoriaSubmotivo', on_delete=models.CASCADE, null=False)
    gravedad_vulneracion = models.ForeignKey('TGravedadVulneracion', on_delete=models.CASCADE, null=False)
    urgencia_vulneracion = models.ForeignKey('TUrgenciaVulneracion', on_delete=models.CASCADE, null=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.
    
    def __str__(self):
        return f"{self.categoria_motivo} {self.categoria_submotivo} - {self.nnya} - {self.autor_dv}"

class TVulneracion(TVulneracionBase):

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Vulneracion')
        verbose_name_plural = _('Vulneraciones')
        
    def save(self, *args, **kwargs):
        if self.principal_demanda:
            if TVulneracion.objects.filter(demanda=self.demanda, principal_demanda=True).exclude(id=self.id).exists():
                raise ValidationError(f"(vulneracion - {self.categoria_motivo} {self.categoria_submotivo}) Ya existe una vulneracion principal para esta Demanda.")
        if self.nnya == self.autor_dv:
            raise ValidationError("El NNyA no puede ser el supuesto autor de la vulneración.")
        
        super().save(*args, **kwargs)


class TVulneracionHistory(TVulneracionBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TVulneracion',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Vulneracion')
        verbose_name_plural = _('Historial de Vulneraciones')
