from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _

"""
TPersona
TInstitucionEducativa
TNNyAEducacion
TInstitucionSanitaria
TNNyASalud
TNNyAScore
"""

class TPersona(models.Model):
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

    history = HistoricalRecords()
    
    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Persona')
        verbose_name_plural = _('Personas')


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


class TNNyAEducacion(models.Model):
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

    history = HistoricalRecords()

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Educación del NNyA')
        verbose_name_plural = _('Educacion de los NNyAs')


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


class TNNyASalud(models.Model):
    observaciones = models.TextField(null=True, blank=True)

    institucion_sanitaria = models.ForeignKey('TInstitucionSanitaria', on_delete=models.CASCADE, null=False, blank=False)
    nnya = models.OneToOneField('TPersona', on_delete=models.CASCADE, null=False, blank=False)

    history = HistoricalRecords()

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Salud del NNyA')
        verbose_name_plural = _('Salud de los NNyAs')


class TNNyAScore(models.Model):
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    score = models.FloatField(null=False, blank=False)
    score_condiciones_vulnerabilidad = models.FloatField(null=False, blank=False)
    score_vulneracion = models.FloatField(null=False, blank=False)
    score_motivo_intervencion = models.FloatField(null=False, blank=False)

    nnya = models.OneToOneField('TPersona', on_delete=models.CASCADE, null=False, blank=False)

    history = HistoricalRecords()

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Score del NNyA')
        verbose_name_plural = _('Scores de los NNyAs')

