from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords

class TEquipo(models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)


class CustomUser(AbstractUser):
    """Custom user model with additional fields."""
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero_choices = [
        ('MASCULINO', 'Masculino'),
        ('FEMENINO', 'Femenino'),
        ('NO_BINARIO', 'No Binario')
    ]
    genero = models.CharField(max_length=10, choices=genero_choices)
    telefono = models.IntegerField(null=True, blank=True)
    
    localidad = models.ForeignKey('infrastructure.TLocalidad', on_delete=models.SET_NULL, null=True, blank=True)
    equipo = models.ForeignKey('customAuth.TEquipo', on_delete=models.SET_NULL, null=True, blank=True)

    
