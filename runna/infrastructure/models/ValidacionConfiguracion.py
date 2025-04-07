from django.db import models

class ValidacionConfiguracion(models.Model):
    # Estos campos se llenarán mediante el formulario personalizado del admin
    required_fields = models.JSONField(default=list, help_text="Lista de nombres de campos obligatorios en la Demanda")
    required_activity_types = models.JSONField(default=list, help_text="Lista de IDs de los tipos de actividad requeridos")
    required_response_types = models.JSONField(default=list, help_text="Lista de IDs de los tipos de respuesta requeridos")
    
    activo = models.BooleanField(default=True, help_text="Indica si esta configuración es la activa")

    def save(self, *args, **kwargs):
        # Impedir la creación de más de una instancia
        if not self.pk and ValidacionConfiguracion.objects.exists():
            raise ValueError("Ya existe una configuración. Solo se permite un único objeto.")
        super().save(*args, **kwargs)

    def __str__(self):
        return "Configuración de Validación"
    
    class Meta:
        verbose_name = "Configuración de Validación"
        verbose_name_plural = "Configuración de Validación"
