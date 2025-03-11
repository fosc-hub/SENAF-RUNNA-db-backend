from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from .BaseClass import BaseHistory, BaseAdjunto
from django.core.exceptions import ValidationError
from .Persona import TLegajo

"""
TActividadTipo
TInstitucionActividad
TActividad
TRespuesta
TIndicadoresValoracion
TEvaluaciones
TDecision
"""

class TActividadTipo(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Tipo de Actividad')
        verbose_name_plural = _('Tipos de Actividades')

    def __str__(self):
        return f"{self.nombre}"

class TActividadTipoModelo(BaseAdjunto):
    actividad_tipo = models.ForeignKey('TActividadTipo', on_delete=models.CASCADE)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Modelo de Tipo de Actividad')
        verbose_name_plural = _('Modelos de Tipos de Actividades')

class TInstitucionActividad(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Institucion de Actividad')
        verbose_name_plural = _('Instituciones de Actividades')

    def __str__(self):
        return f"{self.nombre}"


class TActividadBase(models.Model):
    fecha_y_hora = models.DateTimeField(null=False, blank=False, auto_now=True) 
    fecha_y_hora_manual = models.DateTimeField(null=False, blank=False)
    descripcion = models.TextField(blank=False, null=False)

    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    tipo = models.ForeignKey('TActividadTipo', on_delete=models.SET_NULL, null=True, blank=True)
    institucion = models.ForeignKey('TInstitucionActividad', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.

    def __str__(self):
        return f"{self.fecha_y_hora} - {self.descripcion} - {self.demanda} - {self.tipo} - {self.institucion}"


class TActividad(TActividadBase):
    # adjuntos = models.FileField(upload_to=file_directory('actividad-adjuntos', 'actividad_', 'infrastructure.TActividad'), null=True, blank=True)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Actividad')
        verbose_name_plural = _('Actividades')


class TActividadHistory(TActividadBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TActividad',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Actividad')
        verbose_name_plural = _('Historial de Actividades')

class TActividadAdjunto(BaseAdjunto):
    actividad = models.ForeignKey('TActividad', on_delete=models.CASCADE)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Adjunto de Actividad')
        verbose_name_plural = _('Adjuntos de Actividades')

class TRespuesta(models.Model):
    fecha_y_hora = models.DateTimeField(auto_now=True)
    mail = models.EmailField(null=False, blank=False)
    mensaje = models.TextField(null=False, blank=False)
    
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    institucion = models.CharField(max_length=255, null=False, blank=False)
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Respuesta')
        verbose_name_plural = _('Respuestas')
    
    def __str__(self):
        return f"{self.fecha_y_hora} - {self.mail} - {self.mensaje} - {self.demanda} - {self.institucion}"

class TRespuestaAdjunto(BaseAdjunto):
    respuesta = models.ForeignKey('TRespuesta', on_delete=models.CASCADE)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Adjunto de Respuesta')
        verbose_name_plural = _('Adjuntos de Respuestas')

class TIndicadoresValoracion(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField(default=0)
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Indicador de Valoracion')
        verbose_name_plural = _('Indicadores de Valoracion')

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.peso}"

class TEvaluacionesBase(models.Model):
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    indicador = models.ForeignKey('TIndicadoresValoracion', on_delete=models.CASCADE)
    si_no = models.BooleanField(null=False, blank=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.
    
    def __str__(self):
        return f"{self.demanda} {self.indicador} - {self.si_no}"


class TEvaluaciones(TEvaluacionesBase):

    class Meta:
        # unique_together = ('demanda', 'indicador')
        app_label = 'infrastructure'
        verbose_name = _('Evaluacion')
        verbose_name_plural = _('Evaluaciones')


class TEvaluacionesHistory(TEvaluacionesBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TEvaluaciones',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Evaluacion')
        verbose_name_plural = _('Historial de Evaluaciones')


class TDecision(models.Model):
    fecha_y_hora = models.DateTimeField(auto_now=True)
    justificacion = models.TextField(null=False, blank=False)
    decision_choices = [
        ('APERTURA DE LEGAJO', 'Apertura de Legajo'),
        ('RECHAZAR CASO', 'Rechazar Caso'),
        ('MPI_MPE', 'MPI_MPE')
    ]
    decision = models.CharField(max_length=20, choices=decision_choices, null=False)

    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE, null=False)
    nnya = models.ForeignKey('TPersona', on_delete=models.CASCADE, null=False)
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Decision')
        verbose_name_plural = _('Decisiones')
        
    def save(self, *args, **kwargs):
        if self.nnya.nnya==False:
            raise ValidationError("La persona debe ser un NNyA")

        if self.decision == 'APERTURA DE LEGAJO':
            if TLegajo.objects.filter(nnya=self.nnya).exists():
                raise ValidationError("Ya existe un legajo para este NNyA")
            else:
                TLegajo.objects.create(nnya=self.nnya)
                self.demanda.completado = True
                self.demanda.save()
                
        if self.decision == 'MPI_MPE':
            if TLegajo.objects.filter(nnya=self.nnya).exists():
                self.demanda.completado = True
                self.demanda.save()
            else:
                raise ValidationError("No se puede crear una MPI_MPE sin un legajo")

        if self.decision == 'RECHAZAR CASO':
            self.demanda.archivado = True
            self.demanda.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fecha_y_hora} - {self.justificacion} - {self.decision} - {self.demanda} - {self.nnya}"
