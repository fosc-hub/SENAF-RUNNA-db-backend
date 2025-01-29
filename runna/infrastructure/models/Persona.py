from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from .BaseHistory import BaseHistory
from django.core.exceptions import ValidationError


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
        ('NO_BINARIO', 'No Binario')
    ]
    genero = models.CharField(max_length=10, choices=genero_choices, null=False, blank=False)
    observaciones = models.TextField(null=True, blank=True)
    adulto = models.BooleanField(null=False, blank=False)
    nnya = models.BooleanField(null=False, blank=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.

    def save(self, *args, **kwargs):
        if not self.nnya and not self.adulto:
            raise ValidationError(f"({self.nombre} {self.apellido})  Debe ser adulto o NNyA")
        if self.nnya and self.adulto:
            raise ValidationError(f"({self.nombre} {self.apellido}) No puede ser adulto y NNyA a la vez")
        if self.situacion_dni == 'VALIDO' and self.dni is None:
            raise ValidationError(f"({self.nombre} {self.apellido}) El DNI no puede ser nulo si la situacion es valido")
        if self.situacion_dni != 'VALIDO' and self.dni is not None:
            raise ValidationError(f"({self.nombre} {self.apellido}) El DNI debe ser nulo si la situacion no es valido")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.fecha_nacimiento} - {self.edad_aproximada} - {self.dni} - {self.situacion_dni} - {self.genero} - {self.observaciones} - {self.adulto} - {self.nnya}"

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

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Institucion Educativa')
        verbose_name_plural = _('Instituciones Educativas')
        
    def __str__(self):
        return f"{self.nombre} - {self.mail} - {self.telefono}"


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

    def __str__(self):
        return f"{self.curso} - {self.nivel} - {self.turno} - {self.comentarios}"

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
    nnya = models.ForeignKey('TPersona', on_delete=models.CASCADE, null=False, blank=False)
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
        
    def __str__(self):
        return f"{self.observaciones} - {self.institucion_sanitaria} - {self.nnya}"


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
    nnya = models.ForeignKey('TPersona', on_delete=models.CASCADE, null=False, blank=False)
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
    score = models.FloatField(default=0)
    score_condiciones_vulnerabilidad = models.FloatField(default=0)
    score_vulneracion = models.FloatField(default=0)
    nnya = models.OneToOneField('TPersona', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.

    def __str__(self):
        return f"{self.ultima_actualizacion} - {self.score} - {self.score_condiciones_vulnerabilidad} - {self.score_vulneracion} - {self.nnya}"


class TNNyAScore(TNNyAScoreBase):

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Score del NNyA')
        verbose_name_plural = _('Scores de los NNyAs')


class TNNyAScoreHistory(TNNyAScoreBase, BaseHistory):
    nnya = models.ForeignKey('TPersona', on_delete=models.CASCADE, null=False, blank=False)
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
    
    def __str__(self):
        return f"{self.info_legajo} - {self.nnya}"


class TLegajo(TLegajoBase):

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Legajo')
        verbose_name_plural = _('Legajos')


class TLegajoHistory(TLegajoBase, BaseHistory):
    nnya = models.ForeignKey('TPersona', on_delete=models.CASCADE, null=False, blank=False)
    parent = models.ForeignKey(
        'infrastructure.TLegajo',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Legajo')
        verbose_name_plural = _('Historial de Legajos')