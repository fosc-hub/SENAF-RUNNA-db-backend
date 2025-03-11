import os
from django.db import models
from .helpers import upload_to_adjuntos

class BaseAdjunto(models.Model):
    archivo = models.FileField(upload_to=upload_to_adjuntos, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)    

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.archivo} - {self.fecha}"

    def delete(self, *args, **kwargs):
        if self.archivo:
            if os.path.isfile(self.archivo.path):
                os.remove(self.archivo.path)
        super(BaseAdjunto, self).delete(*args, **kwargs)


class BaseHistory(models.Model):
    descripcion = models.TextField(null=True, blank=True)
    ACTION_CHOICES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    ]

    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    by_user = models.ForeignKey(
        'customAuth.CustomUser',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # This model is abstract and won't create a table.
        
    
    def __str__(self):
        return f"{self.action} - {self.timestamp} - {self.by_user} - {self.parent}"
