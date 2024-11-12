from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords


class CustomUser(AbstractUser):
    """Custom user model with additional fields."""
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    telefono = models.CharField(max_length=20, blank=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.username} ({self.email})"

class TProvincia(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()

class TLocalidad(models.Model):
    nombre = models.CharField(max_length=255)
    provincia = models.ForeignKey('TProvincia', on_delete=models.CASCADE)

    history = HistoricalRecords()

class TBarrio(models.Model):
    nombre = models.CharField(max_length=255)
    localidad = models.ForeignKey('TLocalidad', on_delete=models.CASCADE)

    history = HistoricalRecords()

class TLocalizacion(models.Model):
    calle = models.CharField(max_length=255)
    numero = models.IntegerField(null=True, blank=True)
    referencia_geo = models.TextField()
    barrio = models.ForeignKey('TBarrio', on_delete=models.CASCADE)

    history = HistoricalRecords()

class TUsuarioLinea(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    telefono = models.CharField(max_length=15)
    
    vinculo = models.ForeignKey('TVinculoUsuarioLinea', related_name='vinculo', on_delete=models.SET_NULL, null=True, blank=True)
    institucion = models.ForeignKey('TInstitucionUsuarioLinea', related_name='institucion', on_delete=models.SET_NULL, null=True, blank=True)
    responsable = models.ForeignKey('TResponsable', related_name='responsable', on_delete=models.SET_NULL, null=True, blank=True)
    

    history = HistoricalRecords()

class TDemanda(models.Model):
    fecha_ingreso = models.DateField()
    hora_ingreso = models.TimeField()
    n_notificacion_102 = models.IntegerField(null=True, blank=True)
    n_sac = models.IntegerField(null=True, blank=True)
    n_suac = models.IntegerField(null=True, blank=True)
    descripcion = models.TextField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    score = models.IntegerField()
    score_vulneracion = models.IntegerField()
    score_evaluacion = models.IntegerField()
    localizacion = models.ForeignKey('TLocalizacion', on_delete=models.CASCADE)
    usuario_linea = models.ForeignKey('TUsuarioLinea', on_delete=models.CASCADE)

    history = HistoricalRecords()

class TPrecalificacionDemanda(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()
    estado_demanda_choices = [
        ('URGENTE', 'Urgente'),
        ('NO_URGENTE', 'No Urgente'),
        ('COMPLETAR', 'Completar')
    ]
    estado_demanda = models.CharField(max_length=20, choices=estado_demanda_choices)
    demanda = models.OneToOneField('TDemanda', on_delete=models.CASCADE, unique=True, null=False, blank=False)

    history = HistoricalRecords()

class TPersona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    observaciones = models.TextField(blank=True, null=True)
    adulto = models.BooleanField()

    history = HistoricalRecords()

class TDemandaPersona(models.Model):
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    persona = models.ForeignKey('TPersona', on_delete=models.CASCADE)
    conviviente = models.BooleanField()
    autordv = models.BooleanField()
    autordv_principal = models.BooleanField()
    nnya = models.BooleanField()
    nnya_principal = models.BooleanField()

    history = HistoricalRecords()

class TNNyA(models.Model):
    persona = models.ForeignKey('TPersona', on_delete=models.CASCADE)
    educacion = models.OneToOneField('TNNyAEducacion', on_delete=models.SET_NULL, null=True, blank=True)
    
    institucion_sanitaria = models.ForeignKey('TInstitucionSanitaria', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()

class TNNyAEducacion(models.Model):
    curso = models.CharField(max_length=255)
    nivel = models.CharField(max_length=255)
    turno = models.CharField(max_length=255)
    comentarios = models.TextField()
    institucion_educativa = models.ForeignKey('TInstitucionEducativa', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()

class TInstitucionEducativa(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()

class TInstitucionSanitaria(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()

class TVulneracion(models.Model):
    vulneracion_principal_demanda = models.BooleanField(default=False)
    sumatoria_pesos = models.IntegerField(default=0)
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    persona_nnya = models.ForeignKey(
        'TPersona',
        on_delete=models.CASCADE,
        related_name='vulneracion_nnya'
    )
    persona_autordv = models.ForeignKey(
        'TPersona',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vulneracion_autordv'
    )
    categoria_motivo = models.ForeignKey('TCategoriaMotivo', on_delete=models.SET_NULL, null=True, blank=True)
    categoria_submotivo = models.ForeignKey('TCategoriaSubmotivo', on_delete=models.SET_NULL, null=True, blank=True)
    gravedad = models.ForeignKey('TGravedadVulneracion', on_delete=models.SET_NULL, null=True, blank=True)
    urgencia = models.ForeignKey('TUrgenciaVulneracion', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()

class TGravedadVulneracion(models.Model):
    nombre = models.CharField(max_length=255)
    peso = models.IntegerField()

    history = HistoricalRecords()

class TUrgenciaVulneracion(models.Model):
    nombre = models.CharField(max_length=255)
    peso = models.IntegerField()

    history = HistoricalRecords()

class TDecision(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    decision = models.CharField(max_length=255, choices=[('APERTURA', 'Apertura de legajo'), ('RECHAZO', 'Rechazar caso')])
    justificacion = models.TextField()
    demanda = models.OneToOneField('TDemanda', on_delete=models.CASCADE, unique=True, null=False, blank=False)

    history = HistoricalRecords()

# Add other entities based on the schema...

class TInstitucionUsuarioLinea(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)

    history = HistoricalRecords()

class TVinculoUsuarioLinea(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()

class TCargo(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()

class TResponsable(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cargo = models.ForeignKey('TCargo', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()

class TDemandaAsignado(models.Model):
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    esta_activo = models.BooleanField(default=True)
    recibido = models.BooleanField(default=False)
    comentarios = models.TextField(null=True, blank=True)

    history = HistoricalRecords()

class TActividadTipo(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()

class TActividad(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()

    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    tipo = models.ForeignKey('TActividadTipo', on_delete=models.SET_NULL, null=True, blank=True)
    institucion = models.ForeignKey('TInstitucionActividad', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()

class TRespuesta(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    mail = models.EmailField()
    mensaje = models.TextField()
    
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    institucion = models.ForeignKey('TInstitucionRespuesta', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()

class TDemandaVinculada(models.Model):
    demanda_1 = models.ForeignKey('TDemanda', related_name='vinculadas_demanda_1', on_delete=models.CASCADE)
    demanda_2 = models.ForeignKey('TDemanda', related_name='vinculadas_demanda_2', on_delete=models.CASCADE)

    history = HistoricalRecords()

class TLegajoAsignado(models.Model):
    legajo = models.ForeignKey('TLegajo', on_delete=models.CASCADE)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    esta_activo = models.BooleanField(default=True)
    recibido = models.BooleanField(default=False)

    history = HistoricalRecords()

class TIndicadoresValoracion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    peso = models.IntegerField()

    history = HistoricalRecords()

class TEvaluaciones(models.Model):
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    indicador = models.ForeignKey('TIndicadoresValoracion', on_delete=models.CASCADE)
    si_no = models.BooleanField()

    history = HistoricalRecords()

# Further models from schema...


class TCategoriaMotivo(models.Model):
    nombre = models.CharField(max_length=255)
    peso = models.IntegerField()

    history = HistoricalRecords()

class TCategoriaSubmotivo(models.Model):
    nombre = models.CharField(max_length=255)
    peso = models.IntegerField()
    motivo = models.ForeignKey('TCategoriaMotivo', on_delete=models.CASCADE)

    history = HistoricalRecords()

class TLegajo(models.Model):
    info_legajo = models.TextField()
    nnya = models.OneToOneField('TNNyA', on_delete=models.CASCADE, null=False, blank=False)

    history = HistoricalRecords()

class TVinculo(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()

class TVinculoPersona(models.Model):
    vinculo = models.ForeignKey('TVinculo', on_delete=models.SET_NULL, null=True, blank=True)
    persona_1 = models.ForeignKey('TPersona', related_name='persona_1', on_delete=models.CASCADE)
    persona_2 = models.ForeignKey('TPersona', related_name='persona_2', on_delete=models.CASCADE)

    history = HistoricalRecords()

class TInstitucionActividad(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()

class TInstitucionRespuesta(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()
class TMotivoIntervencion(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()

class TDemandaMotivoIntervencion(models.Model):
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    motivo_intervencion = models.ForeignKey('TMotivoIntervencion', on_delete=models.CASCADE)

    history = HistoricalRecords()
