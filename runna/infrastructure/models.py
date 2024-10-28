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
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    history = HistoricalRecords()

class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)

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
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    history = HistoricalRecords()

class UsuarioLinea(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)
    telefono = models.CharField(max_length=20)
    vinculo = models.ForeignKey(VinculoUsuarioLinea, on_delete=models.CASCADE)
    institucion = models.ForeignKey(InstitucionUsuarioLinea, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)

    history = HistoricalRecords()

# Location Model
class Localizacion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    referencia_geo = models.TextField()
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)

    history = HistoricalRecords()

# Demand-Related Models
class EstadoDemanda(models.Model):
    nombre = models.CharField(max_length=100)

    history = HistoricalRecords()

class PreCalificacionDemanda(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()
    estado = models.ForeignKey(EstadoDemanda, on_delete=models.CASCADE)

    history = HistoricalRecords()

class Demanda(models.Model):
    fecha_ingreso = models.DateField()
    hora_ingreso = models.TimeField()
    id_notificacion_manual = models.CharField(max_length=100, null=True, blank=True)
    notificacion_nro = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    precalificacion = models.OneToOneField(
        PreCalificacionDemanda, on_delete=models.SET_NULL, null=True, blank=True
    )
    localizacion = models.ForeignKey(Localizacion, on_delete=models.CASCADE)
    usuario_linea = models.ForeignKey(UsuarioLinea, on_delete=models.CASCADE)

    history = HistoricalRecords()

class DemandaAsignado(models.Model):
    esta_activo = models.BooleanField(default=True)
    recibido = models.BooleanField(default=False)
    comentarios = models.TextField(null=True, blank=True)
    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

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
    demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE)
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    prioridad_intervencion = models.ForeignKey(PrioridadIntervencion, on_delete=models.CASCADE)
    problematica_identificada = models.ForeignKey(ProblematicaIdentificada, on_delete=models.CASCADE)
    ambito_vulneracion = models.ForeignKey(AmbitoVulneracion, on_delete=models.CASCADE)
    ddv = models.ForeignKey(DDV, on_delete=models.CASCADE)

    history = HistoricalRecords()

class DemandaVinculada(models.Model):
    demanda = models.ForeignKey(Demanda, related_name='vinculadas', on_delete=models.CASCADE)
    vinculacion = models.ForeignKey(Demanda, related_name='demandas', on_delete=models.CASCADE)

    history = HistoricalRecords()
