from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from .BaseHistory import BaseHistory

"""

Renombrar '...UsuarioLinea' por '...UsuarioExterno'

"""

class TInstitucionUsuarioExterno(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    mail = models.EmailField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)

    localizacion = models.ForeignKey('TLocalizacion', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Institucion de Usuario Externo')
        verbose_name_plural = _('Instituciones de Usuarios Externos')


class TVinculoUsuarioExterno(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Vinculo del Usuario Externo')
        verbose_name_plural = _('Vinculos de los Usuarios Externos')


class TUsuarioExterno(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero_choices = [
        ('MASCULINO', 'Masculino'),
        ('FEMENINO', 'Femenino'),
        ('OTRO', 'Otro')
    ]
    genero = models.CharField(max_length=10, choices=genero_choices, null=False, blank=False)
    telefono = models.IntegerField(null=False, blank=False)
    mail = models.EmailField(null=False, blank=False, unique=True)

    vinculo = models.ForeignKey('TVinculoUsuarioExterno', on_delete=models.CASCADE, null=False)
    institucion = models.ForeignKey('TInstitucionUsuarioExterno', on_delete=models.CASCADE, null=False)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Usuario Externo del Sistema (Linea 102, etc)')
        verbose_name_plural = _('Usuarios Externos del Sistema (Linea 102, etc)')


class TDemandaBase(models.Model):
    deleted = models.BooleanField(default=False)
    fecha_y_hora_ingreso = models.DateTimeField(null=False, default=datetime.now())
    origen_choices = [
        ('WEB', 'Web'),
        ('TELEFONO', 'Telefono'),
        ('MAIL', 'Mail'),
        ('PERSONAL', 'Personal'),
        ('OTRO', 'Otro')
    ]
    origen = models.CharField(max_length=10, choices=origen_choices, null=False)
    nro_notificacion_102 = models.IntegerField(null=True, blank=True)
    nro_sac = models.IntegerField(null=True, blank=True)
    nro_suac = models.IntegerField(null=True, blank=True)
    nro_historia_clinica = models.IntegerField(null=True, blank=True)
    nro_oficio_web = models.IntegerField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    localizacion = models.ForeignKey('TLocalizacion', on_delete=models.PROTECT, null=False)
    usuario_externo = models.ForeignKey('TUsuarioExterno', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.


class TDemanda(TDemandaBase):

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Demanda')
        verbose_name_plural = _('Demandas')


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


class TPrecalificacionDemanda(TPrecalificacionDemandaBase):

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Precalificacion de Demanda')
        verbose_name_plural = _('Precalificaciones de Demandas')


class TPrecalificacionDemandaHistory(TPrecalificacionDemandaBase, BaseHistory):
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
    score = models.FloatField(null=False, blank=False)
    score_condiciones_vulnerabilidad = models.FloatField(null=False, blank=False)
    score_vulneracion = models.FloatField(null=False, blank=False)
    score_motivos_intervencion = models.FloatField(null=False, blank=False)
    score_indicadores_valoracion = models.FloatField(null=False, blank=False)

    demanda = models.OneToOneField('TDemanda', on_delete=models.CASCADE, unique=True, null=False, blank=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.


class TDemandaScore(TDemandaScoreBase):

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Score de Demanda')
        verbose_name_plural = _('Scores de Demandas')


class TDemandaScoreHistory(TDemandaScoreBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TDemandaScore',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Score de Demanda')
        verbose_name_plural = _('Historial de Scores de Demandas')
