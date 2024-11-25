from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from .BaseHistory import BaseHistory

"""
TPersona
TInstitucionEducativa
TNNyAEducacion
TInstitucionSanitaria
TNNyASalud
TNNyAScore
TLegajo
"""

class TPersonaBase(models.Model):
    deleted = models.BooleanField(default=False)
    nombre = models.CharField(max_length=255, null=False, blank=False)
    apellido = models.CharField(max_length=255, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    edad_aproximada = models.IntegerField(null=True, blank=True)
    dni = models.IntegerField(null=True, blank=True)
    situacion_dni_choices = [
        ('EN_TRAMITE', 'En Trámite'),
        ('VENCIDO', 'Vencido'),
        ('EXTRAVIADO', 'Extraviado'),
        ('INEXISTENTE', 'Inexistente'),
        ('VALIDO', 'Válido'),
        ('OTRO', 'Otro')
    ]
    situacion_dni = models.CharField(max_length=20, choices=situacion_dni_choices, null=False, blank=False)
    genero_choices = [
        ('MASCULINO', 'Masculino'),
        ('FEMENINO', 'Femenino'),
        ('OTRO', 'Otro')
    ]
    genero = models.CharField(max_length=10, choices=genero_choices, null=False, blank=False)
    boton_antipanico = models.BooleanField(default=False)
    observaciones = models.TextField(null=True, blank=True)
    adulto = models.BooleanField(null=False, blank=False)
    nnya = models.BooleanField(null=False, blank=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.


class TPersona(TPersonaBase):

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Persona')
        verbose_name_plural = _('Personas')


class TPersonaHistory(TPersonaBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TPersona',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Persona')
        verbose_name_plural = _('Historial de Personas')

class TInstitucionEducativa(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    mail = models.EmailField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)

    localizacion = models.ForeignKey('TLocalizacion', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Institucion Educativa')
        verbose_name_plural = _('Instituciones Educativas')


class TNNyAEducacionBase(models.Model):
    deleted = models.BooleanField(default=False)
    curso = models.CharField(max_length=255, null=False, blank=False)
    nivel_choices = [
        ('PRIMARIO', 'Primario'),
        ('SECUNDARIO', 'Secundario'),
        ('TERCIARIO', 'Terciario'),
        ('UNIVERSITARIO', 'Universitario'),
        ('OTRO', 'Otro')
    ]
    nivel = models.CharField(max_length=15, choices=nivel_choices, null=False, blank=False)
    turno_choices = [
        ('MANIANA', 'Mañana'),
        ('TARDE', 'Tarde'),
        ('NOCHE', 'Noche'),
        ('OTRO', 'Otro')
    ]
    turno = models.CharField(max_length=10, choices=turno_choices, null=False, blank=False)
    comentarios = models.TextField(null=True, blank=True)

    institucion_educativa = models.ForeignKey('TInstitucionEducativa', on_delete=models.CASCADE, null=False, blank=False)
    nnya = models.OneToOneField('TPersona', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.


class TNNyAEducacion(TNNyAEducacionBase):

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Educación del NNyA')
        verbose_name_plural = _('Educacion de los NNyAs')


class TNNyAEducacionHistory(TNNyAEducacionBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TNNyAEducacion',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Educación del NNyA')
        verbose_name_plural = _('Historial de Educación de los NNyAs')

class TInstitucionSanitaria(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    mail = models.EmailField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)

    localizacion = models.ForeignKey('TLocalizacion', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Institucion Sanitaria')
        verbose_name_plural = _('Instituciones Sanitarias')


class TNNyASaludBase(models.Model):
    deleted = models.BooleanField(default=False)
    observaciones = models.TextField(null=True, blank=True)

    institucion_sanitaria = models.ForeignKey('TInstitucionSanitaria', on_delete=models.CASCADE, null=False, blank=False)
    nnya = models.OneToOneField('TPersona', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.


class TNNyASalud(TNNyASaludBase):

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Salud del NNyA')
        verbose_name_plural = _('Salud de los NNyAs')


class TNNyASaludHistory(TNNyASaludBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TNNyASalud',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Salud del NNyA')
        verbose_name_plural = _('Historial de Salud de los NNyAs')


class TNNyAScoreBase(models.Model):
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    score = models.FloatField(null=False, blank=False)
    score_condiciones_vulnerabilidad = models.FloatField(null=False, blank=False)
    score_vulneracion = models.FloatField(null=False, blank=False)
    score_motivos_intervencion = models.FloatField(null=False, blank=False)
    nnya = models.OneToOneField('TPersona', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.


class TNNyAScore(TNNyAScoreBase):

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Score del NNyA')
        verbose_name_plural = _('Scores de los NNyAs')


class TNNyAScoreHistory(TNNyAScoreBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TNNyAScore',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Score del NNyA')
        verbose_name_plural = _('Historial de Scores de los NNyAs')


class TLegajoBase(models.Model):
    info_legajo = models.TextField()
    nnya = models.OneToOneField('TPersona', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.


class TLegajo(TLegajoBase):

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Legajo')
        verbose_name_plural = _('Legajos')


class TLegajoHistory(TLegajoBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TLegajo',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Legajo')
        verbose_name_plural = _('Historial de Legajos')