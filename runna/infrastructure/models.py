from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords


class CustomUser(AbstractUser):
    """Custom user model with additional fields."""
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero_choices = [
        ('MASCULINO', 'Masculino'),
        ('FEMENINO', 'Femenino'),
        ('OTRO', 'Otro')
    ]
    genero = models.CharField(max_length=10, choices=genero_choices)
    telefono = models.IntegerField(null=True, blank=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.username} ({self.email})"

class TProvincia(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()

class TLocalidad(models.Model):
    nombre = models.CharField(max_length=255)
    provincia = models.ForeignKey('TProvincia', on_delete=models.CASCADE)
    departamento = models.ForeignKey('TDepartamento', on_delete=models.CASCADE)

    history = HistoricalRecords()

class TBarrio(models.Model):
    nombre = models.CharField(max_length=255)
    localidad = models.ForeignKey('TLocalidad', on_delete=models.CASCADE)

    history = HistoricalRecords()

class TLocalizacion(models.Model):
    calle = models.CharField(max_length=255, null=False)
    tipo_calle_choices = [
        ('CALLE', 'Calle'),
        ('AVENIDA', 'Avenida'),
        ('PASAJE', 'Pasaje'),
        ('RUTA', 'Ruta'),
        ('BOULEVAR', 'Boulevard'),
        ('OTRO', 'Otro')
    ]
    tipo_calle = models.CharField(max_length=10, choices=tipo_calle_choices, null=False)
    piso_depto = models.IntegerField(null=True, blank=True)
    lote = models.IntegerField(null=True, blank=True)
    mza = models.IntegerField(null=True, blank=True)
    casa_nro = models.IntegerField(null=True, blank=True)
    referencia_geo = models.TextField(null=True, blank=True)
    barrio = models.ForeignKey('TBarrio', on_delete=models.CASCADE, null=False)
    localidad = models.ForeignKey('TLocalidad', on_delete=models.CASCADE, null=False)
    cpc = models.ForeignKey('TCPC', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()

class TUsuarioLinea(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero_choices = [
        ('MASCULINO', 'Masculino'),
        ('FEMENINO', 'Femenino'),
        ('OTRO', 'Otro')
    ]
    genero = models.CharField(max_length=10, choices=genero_choices, null=False)
    telefono = models.IntegerField(null=True, blank=True)
    vinculo_usuario_linea = models.ForeignKey('TVinculoUsuarioLinea', on_delete=models.CASCADE, null=False)
    institucion_usuario_linea = models.ForeignKey('TInstitucionUsuarioLinea', on_delete=models.CASCADE, null=False)
    responsable = models.ForeignKey('TResponsable', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()

class TDemanda(models.Model):
    fecha_ingreso = models.DateField(null=False)
    hora_ingreso = models.TimeField(null=False)
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
    ultima_actualizacion = models.DateField(auto_now=True)
    localizacion = models.ForeignKey('TLocalizacion', on_delete=models.CASCADE, null=False)
    usuario_linea = models.ForeignKey('TUsuarioLinea', on_delete=models.CASCADE, null=False)

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
    nombre = models.CharField(max_length=255, null=False)
    apellido = models.CharField(max_length=255, null=False)
    fecha_nacimiento = models.DateField(null=False)
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
    situacion_dni = models.CharField(max_length=20, choices=situacion_dni_choices, null=False)
    genero_choices = [
        ('MASCULINO', 'Masculino'),
        ('FEMENINO', 'Femenino'),
        ('OTRO', 'Otro')
    ]
    genero = models.CharField(max_length=10, choices=genero_choices, null=False)
    boton_antipanico = models.BooleanField(default=False)
    observaciones = models.TextField(null=True, blank=True)
    adulto = models.BooleanField(default=False)
    nnya = models.BooleanField(default=False)

    history = HistoricalRecords()

class TDemandaPersona(models.Model):
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    persona = models.ForeignKey('TPersona', on_delete=models.CASCADE)
    conviviente = models.BooleanField(default=False)
    supuesto_autordv = models.BooleanField(default=False)
    supuesto_autordv_principal = models.BooleanField(default=False)
    nnya = models.BooleanField(default=False)
    nnya_principal = models.BooleanField(default=False)

    class Meta:
        unique_together = ('demanda', 'persona')

    history = HistoricalRecords()

class TNNyA(models.Model):
    persona = models.OneToOneField('TPersona', on_delete=models.CASCADE, primary_key=True)
    educacion = models.OneToOneField('TNNyAEducacion', on_delete=models.CASCADE, null=False)
    institucion_sanitaria = models.ForeignKey('TInstitucionSanitaria', on_delete=models.CASCADE, null=False)

    history = HistoricalRecords()

    """
    def save(self, *args, **kwargs):
        if self.persona.adulto:
            raise ValueError("La persona no puede ser un adulto.")
        super().save(*args, **kwargs)
    """

class TNNyAEducacion(models.Model):
    curso = models.CharField(max_length=255, null=False)
    nivel_choices = [
        ('PRIMARIO', 'Primario'),
        ('SECUNDARIO', 'Secundario'),
        ('TERCIARIO', 'Terciario'),
        ('UNIVERSITARIO', 'Universitario'),
        ('OTRO', 'Otro')
    ]
    nivel = models.CharField(max_length=15, choices=nivel_choices, null=False)
    turno_choices = [
        ('MANIANA', 'Mañana'),
        ('TARDE', 'Tarde'),
        ('NOCHE', 'Noche'),
        ('OTRO', 'Otro')
    ]
    turno = models.CharField(max_length=10, choices=turno_choices, null=False)
    comentarios = models.TextField(null=True, blank=True)
    institucion_educativa = models.ForeignKey('TInstitucionEducativa', on_delete=models.CASCADE, null=False)

    history = HistoricalRecords()

class TInstitucionEducativa(models.Model):
    nombre = models.CharField(max_length=255)
    mail = models.EmailField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)

    history = HistoricalRecords()

class TInstitucionSanitaria(models.Model):
    nombre = models.CharField(max_length=255)
    mail = models.EmailField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)

    history = HistoricalRecords()

class TVulneracion(models.Model):
    principal_demanda = models.BooleanField(default=False)
    transcurre_actualidad = models.BooleanField(default=False)
    sumatoria_de_pesos = models.IntegerField(default=0)
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE, null=False)
    nnya = models.ForeignKey('TPersona', on_delete=models.CASCADE, null=False, blank=False, related_name='vulneracion_nnya')
    autor_dv = models.ForeignKey('TPersona', on_delete=models.SET_NULL, null=True, blank=True, related_name='vulneracion_autordv')
    categoria_motivo = models.ForeignKey('TCategoriaMotivo', on_delete=models.CASCADE, null=False)
    categoria_submotivo = models.ForeignKey('TCategoriaSubmotivo', on_delete=models.CASCADE, null=False)
    gravedad_vulneracion = models.ForeignKey('TGravedadVulneracion', on_delete=models.CASCADE, null=False)
    urgencia_vulneracion = models.ForeignKey('TUrgenciaVulneracion', on_delete=models.CASCADE, null=False)

    history = HistoricalRecords()

class TGravedadVulneracion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField()

    history = HistoricalRecords()

class TUrgenciaVulneracion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField()

    history = HistoricalRecords()

class TDecision(models.Model):
    fecha = models.DateField(null=False)
    hora = models.TimeField(null=False)
    justificacion = models.TextField(null=False)
    decision_choices = [
        ('APERTURA DE LEGAJO', 'Apertura de Legajo'),
        ('RECHAZAR CASO', 'Rechazar Caso')
    ]
    decision = models.CharField(max_length=20, choices=decision_choices, null=False)
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE, null=False)

    history = HistoricalRecords()

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
    descripcion = models.TextField(blank=False, null=False)

    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    tipo = models.ForeignKey('TActividadTipo', on_delete=models.SET_NULL, null=True, blank=True)
    institucion = models.ForeignKey('TInstitucionActividad', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()

class TRespuesta(models.Model):
    fecha = models.DateField(null=False)
    hora = models.TimeField(null=False)
    mail = models.EmailField(null=False)
    mensaje = models.TextField(null=False)
    
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    institucion = models.ForeignKey('TInstitucionRespuesta', on_delete=models.SET_NULL, null=True, blank=True)

    history = HistoricalRecords()

class TDemandaVinculada(models.Model):
    demanda_1 = models.ForeignKey('TDemanda', related_name='vinculadas_demanda_1', on_delete=models.CASCADE)
    demanda_2 = models.ForeignKey('TDemanda', related_name='vinculadas_demanda_2', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('demanda_1', 'demanda_2')

    history = HistoricalRecords()

class TLegajoAsignado(models.Model):
    legajo = models.ForeignKey('TLegajo', on_delete=models.CASCADE)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    esta_activo = models.BooleanField(default=True)
    recibido = models.BooleanField(default=False)

    history = HistoricalRecords()

class TIndicadoresValoracion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField(default=0)

    history = HistoricalRecords()

class TEvaluaciones(models.Model):
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    indicador = models.ForeignKey('TIndicadoresValoracion', on_delete=models.CASCADE)
    si_no = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('demanda', 'indicador')

    history = HistoricalRecords()

class TCategoriaMotivo(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField()

    history = HistoricalRecords()

class TCategoriaSubmotivo(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
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

class TVinculoPersonaPersona(models.Model):
    conviven = models.BooleanField(default=False)
    vinculo = models.ForeignKey('TVinculo', on_delete=models.SET_NULL, null=True, blank=True)
    persona_1 = models.ForeignKey('TPersona', related_name='persona_1', on_delete=models.CASCADE)
    persona_2 = models.ForeignKey('TPersona', related_name='persona_2', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('persona_1', 'persona_2')

    history = HistoricalRecords()

class TVinculoPersonaNNyA(models.Model):
    conviven = models.BooleanField(default=False)
    autordv = models.BooleanField(default=False)
    garantiza_proteccion = models.BooleanField(default=False)
    vinculo = models.ForeignKey('TVinculo', on_delete=models.SET_NULL, null=True, blank=True)
    nnya = models.ForeignKey('TNNyA', related_name='nnya', on_delete=models.CASCADE)
    persona = models.ForeignKey('TPersona', related_name='persona', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('nnya', 'persona')

    history = HistoricalRecords()

class TInstitucionActividad(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()

class TInstitucionRespuesta(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()

class TScore(models.Model):
    demanda = models.ForeignKey('TDemanda', on_delete=models.CASCADE)
    nnya = models.ForeignKey('TNNyA', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    score_vulneracion = models.IntegerField(default=0)
    score_evaluacion = models.IntegerField(default=0)
    score_condiciones_vulnerabilidad = models.IntegerField(default=0)
    score_motivo_intervencion = models.IntegerField(default=0)

    class Meta:
        unique_together = ('demanda', 'nnya')

    history = HistoricalRecords()

class TCondicionesVulnerabilidad(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField(null=False)

    history = HistoricalRecords()

class TNNyACondicionesVulnerabilidad(models.Model):
    nnya = models.ForeignKey('TNNyA', on_delete=models.CASCADE)
    condiciones_vulnerabilidad = models.ForeignKey('TCondicionesVulnerabilidad', on_delete=models.CASCADE)
    si_no = models.BooleanField(default=False)

    class Meta:
        unique_together = ('nnya', 'condiciones_vulnerabilidad')

    history = HistoricalRecords()

class TMotivoIntervencion(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    descripcion = models.TextField(null=True, blank=True)
    peso = models.IntegerField(null=False)

    history = HistoricalRecords()

class TNNyAMotivoIntervencion(models.Model):
    nnya = models.ForeignKey('TNNyA', on_delete=models.CASCADE)
    motivo_intervencion = models.ForeignKey('TMotivoIntervencion', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('nnya', 'motivo_intervencion')

    history = HistoricalRecords()

class TCPC(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()

class TDepartamento(models.Model):
    nombre = models.CharField(max_length=255)

    history = HistoricalRecords()
