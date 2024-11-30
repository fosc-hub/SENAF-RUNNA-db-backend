from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from .BaseHistory import BaseHistory

"""

Renombrar '...UsuarioLinea' por '...UsuarioExterno'

"""

class TInstitucionDemanda(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    mail = models.EmailField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)

    localizacion = models.ForeignKey('TLocalizacion', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Institucion de las Demandas')
        verbose_name_plural = _('Instituciones de las Demandas')
    
    def __str__(self):
        return self.nombre


class TInformante(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    telefono = models.IntegerField(null=False, blank=False)
    mail = models.EmailField(null=False, blank=False, unique=True)    
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Informante de la Demanda')
        verbose_name_plural = _('Informantes de las Demandas')
        
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.mail}"


class TOrigenDemanda(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Origen de Demanda')
        verbose_name_plural = _('Origenes de Demandas')
        
    def __str__(self):
        return f"{self.nombre}"


class TSubOrigenDemanda(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    origen = models.ForeignKey('TOrigenDemanda', on_delete=models.CASCADE, null=False)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Sub-Origen de Demanda')
        verbose_name_plural = _('Sub-Origenes de Demandas')
        
    def __str__(self):
        return f"{self.nombre} - {self.origen}"


class TDemandaBase(models.Model):
    fecha_y_hora_ingreso = models.DateTimeField(null=False, default=datetime.now())
    nro_notificacion_102 = models.IntegerField(null=True, blank=True)
    nro_sac = models.IntegerField(null=True, blank=True)
    nro_suac = models.IntegerField(null=True, blank=True)
    nro_historia_clinica = models.IntegerField(null=True, blank=True)
    nro_oficio_web = models.IntegerField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    asignado = models.BooleanField(default=False)
    constatacion = models.BooleanField(default=False)
    evaluacion = models.BooleanField(default=False)
    archivado = models.BooleanField(default=False)
    completado = models.BooleanField(default=False)

    localizacion = models.ForeignKey('TLocalizacion', on_delete=models.PROTECT, null=False)
    informante = models.ForeignKey('TInformante', on_delete=models.SET_NULL, null=True, blank=True)
    origen = models.ForeignKey('TOrigenDemanda', on_delete=models.PROTECT, null=False)
    sub_origen = models.ForeignKey('TSubOrigenDemanda', on_delete=models.PROTECT, null=False)
    institucion = models.ForeignKey('TInstitucionDemanda', on_delete=models.CASCADE, null=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.


class TDemanda(TDemandaBase):

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.archivado = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Demanda')
        verbose_name_plural = _('Demandas')
        
    def __str__(self):
        return f"{self.origen} - {self.descripcion} - {self.fecha_y_hora_ingreso}"


class TDemandaHistory(TDemandaBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TDemanda',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Demanda')
        verbose_name_plural = _('Historial de Demandas')

class TInforme101(models.Model):
    fecha_y_hora = models.DateTimeField(null=False, default=datetime.now())
    fields = models.JSONField(null=False, blank=False)
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE, null=False)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Informe 101')
        verbose_name_plural = _('Informes 101')
        
    def __str__(self):
        return f"{self.fecha_y_hora} - {self.demanda}"


class TPrecalificacionDemandaBase(models.Model):
    fecha_y_hora = models.DateTimeField(null=False, default=datetime.now())
    descripcion = models.TextField(null=False, blank=False)
    estado_demanda_choices = [
        ('URGENTE', 'Urgente'),
        ('NO_URGENTE', 'No Urgente'),
        ('COMPLETAR', 'Completar')
    ]
    estado_demanda = models.CharField(max_length=20, choices=estado_demanda_choices, null=False, blank=False)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    demanda = models.OneToOneField('TDemanda', on_delete=models.CASCADE, unique=True, null=False, blank=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.
        
    def __str__(self):
        return f"{self.fecha_y_hora} - {self.descripcion} - {self.estado_demanda}"


class TPrecalificacionDemanda(TPrecalificacionDemandaBase):

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Precalificacion de Demanda')
        verbose_name_plural = _('Precalificaciones de Demandas')


class TPrecalificacionDemandaHistory(TPrecalificacionDemandaBase, BaseHistory):
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE, null=False, blank=False)
    parent = models.ForeignKey(
        'infrastructure.TPrecalificacionDemanda',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Precalificacion de Demanda')
        verbose_name_plural = _('Historial de Precalificaciones de Demandas')

class TDemandaScoreBase(models.Model):
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    score = models.FloatField(default=0)
    score_condiciones_vulnerabilidad = models.FloatField(default=0)
    score_vulneracion = models.FloatField(default=0)
    score_motivos_intervencion = models.FloatField(default=0)
    score_indicadores_valoracion = models.FloatField(default=0)

    demanda = models.OneToOneField('TDemanda', on_delete=models.CASCADE, unique=True, null=False, blank=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.
        
    def __str__(self):
        return f"{self.score} - {self.demanda}"


class TDemandaScore(TDemandaScoreBase):

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Score de Demanda')
        verbose_name_plural = _('Scores de Demandas')


class TDemandaScoreHistory(TDemandaScoreBase, BaseHistory):
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE, unique=False, null=False, blank=False)
    parent = models.ForeignKey(
        'infrastructure.TDemandaScore',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Score de Demanda')
        verbose_name_plural = _('Historial de Scores de Demandas')
