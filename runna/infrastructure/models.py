from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords


class CustomUser(AbstractUser):
    """Custom user model with additional fields."""
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.username} ({self.email})"

# Region and Location Models
class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    
    history = HistoricalRecords()

class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey('Provincia', on_delete=models.CASCADE)

    history = HistoricalRecords()

class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    localidad = models.ForeignKey('Localidad', on_delete=models.CASCADE)

    history = HistoricalRecords()

# CustomUser and Institution Models
class Cargo(models.Model):
    nombre = models.CharField(max_length=100)

    history = HistoricalRecords()

class InstitucionUsuarioLinea(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    history = HistoricalRecords()

class VinculoUsuarioLinea(models.Model):
    nombre = models.CharField(max_length=100)

    history = HistoricalRecords()

class Responsable(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)

    history = HistoricalRecords()

class UsuarioLinea(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    telefono = models.CharField(max_length=20)
    vinculo = models.ForeignKey('VinculoUsuarioLinea', on_delete=models.CASCADE)
    institucion = models.ForeignKey('InstitucionUsuarioLinea', on_delete=models.CASCADE)
    responsable = models.ForeignKey('Responsable', on_delete=models.CASCADE)

    history = HistoricalRecords()

# Location Model
class Localizacion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    referencia_geo = models.TextField()
    barrio = models.ForeignKey('Barrio', on_delete=models.CASCADE)

    history = HistoricalRecords()

# Demand-Related Models
class EstadoDemanda(models.Model):
    nombre = models.CharField(max_length=100)

    history = HistoricalRecords()

class PreCalificacionDemanda(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()
    estado = models.ForeignKey('EstadoDemanda', on_delete=models.CASCADE)

    history = HistoricalRecords()

class Demanda(models.Model):
    fecha_ingreso = models.DateField()
    hora_ingreso = models.TimeField()
    id_notificacion_manual = models.CharField(max_length=100, null=True, blank=True)
    notificacion_nro = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    precalificacion = models.OneToOneField(
        'PreCalificacionDemanda', on_delete=models.SET_NULL, null=True, blank=True
    )
    localizacion = models.ForeignKey('Localizacion', on_delete=models.CASCADE)
    usuario_linea = models.ForeignKey('UsuarioLinea', on_delete=models.CASCADE)

    history = HistoricalRecords()

class DemandaAsignado(models.Model):
    esta_activo = models.BooleanField(default=True)
    recibido = models.BooleanField(default=False)
    comentarios = models.TextField(null=True, blank=True)
    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    history = HistoricalRecords()

# Vulneracion and Related Models
class PrioridadIntervencion(models.Model):
    nombre = models.CharField(max_length=100)

    history = HistoricalRecords()

class ProblematicaIdentificada(models.Model):
    nombre = models.CharField(max_length=100)

    history = HistoricalRecords()

class AmbitoVulneracion(models.Model):
    nombre = models.CharField(max_length=100)

    history = HistoricalRecords()

class DDV(models.Model):
    nombre = models.CharField(max_length=100)

    history = HistoricalRecords()

class Operador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    history = HistoricalRecords()

class Vulneracion(models.Model):
    motivo = models.TextField()
    principal = models.BooleanField()
    demanda = models.ForeignKey('Demanda', on_delete=models.CASCADE)
    nnya = models.ForeignKey('NNyA', on_delete=models.CASCADE)
    operador = models.ForeignKey('Operador', on_delete=models.CASCADE)
    prioridad_intervencion = models.ForeignKey('PrioridadIntervencion', on_delete=models.CASCADE)
    problematica_identificada = models.ForeignKey('ProblematicaIdentificada', on_delete=models.CASCADE)
    ambito_vulneracion = models.ForeignKey('AmbitoVulneracion', on_delete=models.CASCADE)
    ddv = models.ForeignKey('DDV', on_delete=models.CASCADE)

    history = HistoricalRecords()

class DemandaVinculada(models.Model):
    demanda = models.ForeignKey(Demanda, related_name='vinculadas', on_delete=models.CASCADE)
    vinculacion = models.ForeignKey(Demanda, related_name='demandas', on_delete=models.CASCADE)

    history = HistoricalRecords()

class InstitucionSanitaria(models.Model):
    nombre = models.CharField(max_length=100)

    history = HistoricalRecords()

class NNyA(models.Model):
    persona = models.OneToOneField('Persona', on_delete=models.CASCADE)
    educacion = models.OneToOneField(
        'NNyAEducacion', on_delete=models.SET_NULL, null=True, blank=True
    )
    institucion_sanitaria = models.ForeignKey('InstitucionSanitaria', on_delete=models.CASCADE)

    history = HistoricalRecords()

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    observaciones = models.TextField(blank=True)
    adulto = models.BooleanField(default=False)

    history = HistoricalRecords()

class InstitucionEducativa(models.Model):
    nombre = models.CharField(max_length=100)

    history = HistoricalRecords()

class NNyAEducacion(models.Model):
    curso = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50)
    turno = models.CharField(max_length=50)
    comentarios = models.TextField(blank=True)
    institucion_educativa = models.ForeignKey('InstitucionEducativa', on_delete=models.CASCADE)

    history = HistoricalRecords()

class DemandaPersonaConviviente(models.Model):
    demanda = models.ForeignKey('Demanda', on_delete=models.CASCADE)
    persona = models.ForeignKey('Persona', on_delete=models.CASCADE)

    history = HistoricalRecords()

class Vinculo(models.Model):
    nombre = models.CharField(max_length=100)

    history = HistoricalRecords()

class VinculoPersona(models.Model):
    persona1 = models.ForeignKey('Persona', on_delete=models.CASCADE, related_name='persona1')
    persona2 = models.ForeignKey('Persona', on_delete=models.CASCADE, related_name='persona2')
    vinculo = models.ForeignKey('Vinculo', on_delete=models.CASCADE)

    history = HistoricalRecords()

class DemandaAutorDV(models.Model):
    demanda = models.ForeignKey('Demanda', on_delete=models.CASCADE)
    persona = models.ForeignKey('Persona', on_delete=models.CASCADE)
    convive = models.BooleanField()
    principal = models.BooleanField()

    history = HistoricalRecords()

class DemandaNNyA(models.Model):
    demanda = models.ForeignKey('Demanda', on_delete=models.CASCADE)
    nnya = models.ForeignKey('NNyA', on_delete=models.CASCADE)
    principal = models.BooleanField()

    history = HistoricalRecords()

class Legajo(models.Model):
    info_legajo = models.TextField()
    nnya = models.OneToOneField('NNyA', on_delete=models.CASCADE)

    history = HistoricalRecords()

class LegajoAsignado(models.Model):
    legajo = models.ForeignKey('Legajo', on_delete=models.CASCADE)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    esta_activo = models.BooleanField(default=True)
    recibido = models.BooleanField(default=False)

    history = HistoricalRecords()

class ActividadTipo(models.Model):
    nombre = models.CharField(max_length=100)

    history = HistoricalRecords()

class InstitucionActividad(models.Model):
    nombre = models.CharField(max_length=100)

    history = HistoricalRecords()

class Actividad(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()
    demanda = models.ForeignKey('Demanda', on_delete=models.CASCADE)
    actividad_tipo = models.ForeignKey('ActividadTipo', on_delete=models.CASCADE)
    institucion_actividad = models.ForeignKey('InstitucionActividad', on_delete=models.CASCADE)

    history = HistoricalRecords()

class InstitucionRespuesta(models.Model):
    nombre = models.CharField(max_length=100)

    history = HistoricalRecords()

class Respuesta(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    mail = models.EmailField()
    mensaje = models.TextField()
    demanda = models.ForeignKey('Demanda', on_delete=models.CASCADE)
    institucion_respuesta = models.ForeignKey('InstitucionRespuesta', on_delete=models.CASCADE)

    history = HistoricalRecords()

class Evaluacion(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    comentarios = models.TextField()
    decision = models.CharField(max_length=50, choices=[('APERTURA DE LEGAJO', 'Apertura'), ('RECHAZAR CASO', 'Rechazar')])
    demanda = models.ForeignKey('Demanda', on_delete=models.CASCADE)

    history = HistoricalRecords()

class ValidacionDatos(models.Model):
    dropdown = models.CharField(
        max_length=100, 
        choices=[
            ("La informacion es veridica ?", "Veridica"),
            ("La informacion es fue corroborada ?", "Corroborada")
        ]
    )
    bool_value = models.BooleanField()
    comentarios = models.TextField(blank=True)
    evaluacion = models.ForeignKey('Evaluacion', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('evaluacion', 'dropdown')

    history = HistoricalRecords()

class ActividadesRegistradas(models.Model):
    dropdown = models.CharField(
        max_length=100, 
        choices=[
            ("La informacion es veridica ?", "Veridica"),
            ("La informacion es fue corroborada ?", "Corroborada")
        ]
    )
    bool_value = models.BooleanField()
    comentarios = models.TextField(blank=True)
    evaluacion = models.ForeignKey('Evaluacion', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('evaluacion', 'dropdown')

    history = HistoricalRecords()

class Valoraciones(models.Model):
    dropdown_desc = models.CharField(
        max_length=100,
        choices=[
            ("Gravedad de la situacion", "Gravedad"),
            ("Urgencia de la situacion", "Urgencia")
        ]
    )
    dropdown_options = models.CharField(
        max_length=50,
        choices=[("Baja", "Baja"), ("Media", "Media"), ("Alta", "Alta")]
    )
    comentarios = models.TextField(blank=True)
    evaluacion = models.ForeignKey('Evaluacion', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('evaluacion', 'dropdown_desc')

    history = HistoricalRecords()

class AccionesNecesarias(models.Model):
    dropdown = models.CharField(
        max_length=100,
        choices=[
            ("Apertura de legajo", "Apertura"),
            ("Acciones MPI / MPE", "MPI/MPE"),
            ("Archivar el caso", "Archivar"),
            ("Rechazar el caso", "Rechazar")
        ]
    )
    bool_value = models.BooleanField()
    comentarios = models.TextField(blank=True)
    evaluacion = models.ForeignKey('Evaluacion', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('evaluacion', 'dropdown')

    history = HistoricalRecords()

    # Signals for Custom Logic Based on Dropdown Choice
    @staticmethod
    def post_save_handler(sender, instance, **kwargs):
        if instance.dropdown == "Apertura de legajo" and instance.bool_value:
            # Custom logic for legajo creation
            print("Legajo creation triggered")
        elif instance.dropdown == "Archivar el caso" and instance.bool_value:
            # Logic for archiving case
            print("Case archived")
        elif instance.dropdown == "Rechazar el caso" and instance.bool_value:
            # Logic for rejecting case
            print("Case rejected")

# Connect post_save signal
from django.db.models.signals import post_save
post_save.connect(AccionesNecesarias.post_save_handler, sender=AccionesNecesarias)
