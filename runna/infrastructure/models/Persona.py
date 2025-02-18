from datetime import datetime
from django.db import models
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from .BaseHistory import BaseHistory
from django.core.exceptions import ValidationError


"""
# List of models in this file:
# 1. TPersonaBase
# 2. TPersona
# 3. TPersonaHistory
# 4. TInstitucionEducativa
# 5. TEducacionBase
# 6. TEducacion
# 7. TEducacionHistory
# 8. TInstitucionSanitaria
# 9. TSituacionSalud
# 10. TEnfermedad
# 11. TMedico
# 12. TCoberturaMedicaBase
# 13. TCoberturaMedica
# 14. TCoberturaMedicaHistory
# 15. TPersonaEnfermedadesBase
# 16. TPersonaEnfermedades
# 17. TPersonaEnfermedadesHistory
# 18. TNNyAScoreBase
# 19. TNNyAScore
# 20. TNNyAScoreHistory
# 21. TLegajoBase
# 22. TLegajo
# 23. TLegajoHistory

"""

class TPersonaBase(models.Model):
    deleted = models.BooleanField(default=False)
    nombre = models.CharField(max_length=255, null=False, blank=False)
    nombre_autopercibido = models.CharField(max_length=255, null=True, blank=True)
    apellido = models.CharField(max_length=255, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    edad_aproximada = models.IntegerField(null=True, blank=True)

    NACIONALIDAD_CHOICES = [
        ('ARGENTINA', 'Argentina'),
        ('EXTRANJERA', 'Extranjera')
    ]
    nacionalidad = models.CharField(max_length=10, choices=NACIONALIDAD_CHOICES, null=False, blank=False)

    dni = models.IntegerField(null=True, blank=True)
    SITUACION_DNI_CHOICES = [
        ('EN_TRAMITE', 'En Trámite'),
        ('VENCIDO', 'Vencido'),
        ('EXTRAVIADO', 'Extraviado'),
        ('INEXISTENTE', 'Inexistente'),
        ('VALIDO', 'Válido'),
        ('OTRO', 'Otro')
    ]
    situacion_dni = models.CharField(max_length=20, choices=SITUACION_DNI_CHOICES, null=False, blank=False)
    GENERO_CHOICES = [
        ('MASCULINO', 'Masculino'),
        ('FEMENINO', 'Femenino'),
        ('NO_BINARIO', 'No Binario')
    ]
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, null=False, blank=False)

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

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Institucion Educativa')
        verbose_name_plural = _('Instituciones Educativas')
        
    def __str__(self):
        return f"{self.nombre} - {self.mail} - {self.telefono}"


class TEducacionBase(models.Model):
    deleted = models.BooleanField(default=False)

    NIVEL_ALCANZADO_CHOICES = [
        ('PRIMARIO', 'Primario'),
        ('SECUNDARIO', 'Secundario'),
        ('TERCIARIO', 'Terciario'),
        ('UNIVERSITARIO', 'Universitario'),
        ('OTRO', 'Otro')
    ]
    nivel_alcanzado = models.CharField(max_length=20, choices=NIVEL_ALCANZADO_CHOICES, null=False, blank=False)
    esta_escolarizado = models.BooleanField(null=False, blank=False)
    
    ULTIMO_CURSADO_CHOICES = [
        ('PRIMERO', 'Primero'),
        ('SEGUNDO', 'Segundo'),
        ('TERCERO', 'Tercero'),
        ('CUARTO', 'Cuarto'),
        ('QUINTO', 'Quinto'),
        ('SEXTO', 'Sexto'),
        ('SEPTIMO', 'Séptimo'),
        ('OCTAVO', 'Octavo'),
        ('NOVENO', 'Noveno'),
        ('PRIMERO_SECUNDARIO', 'Primero Secundario'),
        ('SEGUNDO_SECUNDARIO', 'Segundo Secundario'),
        ('TERCERO_SECUNDARIO', 'Tercero Secundario'),
        ('CUARTO_SECUNDARIO', 'Cuarto Secundario'),
        ('QUINTO_SECUNDARIO', 'Quinto Secundario'),
        ('OTRO', 'Otro')
    ]
    ultimo_cursado = models.CharField(max_length=20, choices=ULTIMO_CURSADO_CHOICES, null=True, blank=True)
    
    TIPO_ESCUELA_CHOICES = [
        ('PUBLICA', 'Pública'),
        ('PRIVADA', 'Privada'),
        ('ESTATAL', 'Estatal'),
        ('COMUN', 'Común'),
        ('ESPECIAL', 'Especial'),
        ('OTRO', 'Otro')
    ]
    tipo_escuela = models.CharField(max_length=20, choices=TIPO_ESCUELA_CHOICES, null=True, blank=True)
    
    comentarios_educativos = models.TextField(null=True, blank=True)
    
    institucion_educativa = models.ForeignKey('TInstitucionEducativa', on_delete=models.CASCADE, null=False, blank=False)
    
    persona = models.OneToOneField('TPersona',related_name="%(class)spersona", on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.

    def __str__(self):
        return f"{self.ultimo_cursado} - {self.nivel_alcanzado} - {self.tipo_escuela} - {self.comentarios}"

class TEducacion(TEducacionBase):

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


class TEducacionHistory(TEducacionBase, BaseHistory):
    parent = models.ForeignKey(
        'infrastructure.TEducacion',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Educación del NNyA')
        verbose_name_plural = _('Historial de Educación de los NNyAs')


class TInstitucionSanitaria(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Institucion Sanitaria')
        verbose_name_plural = _('Instituciones Sanitarias')


class TSituacionSalud(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Situación de Salud')
        verbose_name_plural = _('Situaciones de Salud')

    def __str__(self):
        return self.nombre


class TEnfermedad(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    situacion_salud_categoria = models.ForeignKey('TSituacionSalud', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Enfermedad')
        verbose_name_plural = _('Enfermedades')

    def __str__(self):
        return f"{self.nombre} - {self.situacion_salud_categoria}"


class TMedico(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    mail = models.EmailField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Medico')
        verbose_name_plural = _('Medicos')

    def __str__(self):
        return f"{self.nombre} - {self.mail} - {self.telefono}"


class TCoberturaMedicaBase(models.Model):
    deleted = models.BooleanField(default=False)

    OBRA_SOCIAL_CHOICES = [
        ('NO_POSEE', 'No Posee'),
        ('PAMI', 'PAMI'),
        ('IOMA', 'IOMA'),
        ('OSECAC', 'OSECAC'),
        ('OSDE', 'OSDE'),
        ('OTRA', 'Otra')
    ]
    obra_social = models.CharField(max_length=20, choices=OBRA_SOCIAL_CHOICES, null=False, blank=False)

    INTERVENCION_CHOICES = [
        ('AUH', 'AUH'),
        ('OBRA_SOCIAL', 'Obra Social'),
        ('AMBAS', 'Ambas'),
        ('NINGUNA', 'Ninguna')
    ]
    intervencion = models.CharField(max_length=20, choices=INTERVENCION_CHOICES, null=False, blank=False)

    auh = models.BooleanField(null=False, blank=False)
    observaciones = models.TextField(null=True, blank=True)

    institucion_sanitaria = models.ForeignKey('TInstitucionSanitaria', on_delete=models.CASCADE, null=False, blank=False)
    persona = models.OneToOneField('TPersona', on_delete=models.CASCADE, null=False, blank=False)
    medico_cabecera = models.ForeignKey('TMedico', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.

    def __str__(self):
        return f"{self.obra_social} - {self.auh} - {self.intervencion} - {self.observaciones} - {self.institucion_sanitaria} - {self.persona} - {self.medico_cabecera}"


class TCoberturaMedica(TCoberturaMedicaBase):
    
    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Cobertura Médica')
        verbose_name_plural = _('Coberturas Médicas')


class TCoberturaMedicaHistory(TCoberturaMedicaBase, BaseHistory):
    persona = models.ForeignKey('TPersona', on_delete=models.CASCADE, null=False, blank=False)
    parent = models.ForeignKey(
        'infrastructure.TCoberturaMedica',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Cobertura Médica')
        verbose_name_plural = _('Historial de Coberturas Médicas')


class TPersonaEnfermedadesBase(models.Model):
    deleted = models.BooleanField(default=False)

    CERTIFICACION_CHOICES = [
        ('TIENE', 'Tiene'),
        ('NO_TIENE', 'No Tiene'),
        ('EN_TRAMITE', 'En Trámite'),
        ('SE_INTERVIENE_EN_SU_GESTION', 'Se Interviene en su Gestión'),
        ('EN_PERIODO_DE_EVALUACION', 'En Período de Evaluación')
    ]
    certificacion = models.CharField(max_length=30, choices=CERTIFICACION_CHOICES, null=True, blank=True)

    BENEFICIOS_CHOICES = [
        ('BOLETO_DE_COLECTIVO', 'Boleto de Colectivo'),
        ('PROTESIS', 'Prótesis'),
        ('PENSION', 'Pensión')
    ]
    beneficios_gestionados = models.CharField(max_length=20, choices=BENEFICIOS_CHOICES, null=True, blank=True)

    recibe_tratamiento = models.BooleanField(null=False, blank=False)
    informacion_tratamiento = models.TextField(null=True, blank=True)

    persona = models.ForeignKey('TPersona', on_delete=models.CASCADE, null=False)
    situacion_salud = models.ForeignKey('TSituacionSalud', on_delete=models.CASCADE, null=False)
    enfermedad = models.ForeignKey('TEnfermedad', on_delete=models.CASCADE, null=False)
    institucion_sanitaria_interviniente = models.ForeignKey('TInstitucionSanitaria', on_delete=models.SET_NULL, null=True, blank=True)
    medico_tratamiento = models.ForeignKey('TMedico', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.

    def __str__(self):
        return f"{self.persona} - {self.enfermedad} - {self.recibe_tratamiento} - {self.certificacion}"


class TPersonaEnfermedades(TPersonaEnfermedadesBase):

    def delete(self, *args, **kwargs):
        """Override delete to implement soft delete."""
        self.deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        """Permanently delete the object."""
        super().delete(*args, **kwargs)

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Enfermedad de Persona')
        verbose_name_plural = _('Enfermedades de Personas')


class TPersonaEnfermedadesHistory(TPersonaEnfermedadesBase, BaseHistory):
    persona = models.ForeignKey('TPersona', on_delete=models.CASCADE, null=False, blank=False)
    parent = models.ForeignKey(
        'infrastructure.TPersonaEnfermedades',
        on_delete=models.CASCADE,
        related_name='history'
    )

    class Meta:
        app_label = 'infrastructure'
        verbose_name = _('Historial de Enfermedad de Persona')
        verbose_name_plural = _('Historial de Enfermedades de Personas')


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
