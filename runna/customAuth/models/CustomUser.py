from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords

class TZona(models.Model):
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


class TCustomUserZona(models.Model):
    jefe = models.BooleanField(default=False)
    
    user = models.ForeignKey('customAuth.CustomUser', on_delete=models.CASCADE)
    zona = models.ForeignKey('customAuth.TZona', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ['user', 'zona']
        verbose_name = 'Usuario en Zona'
        verbose_name_plural = 'Usuarios en Zonas'

    def save(self, *args, **kwargs):
        if self.jefe:
            if TCustomUserZona.objects.filter(zona=self.zona, jefe=True).exists():
                raise ValueError("Solo puede haber un jefe por zona.")
        super(TCustomUserZona, self).save(*args, **kwargs)

