from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from infrastructure.models import (
    TActividad, TActividadHistory,
    TEvaluaciones, TEvaluacionesHistory
)
from .BaseLogs import logs

@receiver(post_save, sender=TActividad)
def log_actividad_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TActividadHistory, action, instance)


@receiver(post_delete, sender=TActividad)
def log_actividad_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TActividadHistory, action, instance)


@receiver(post_save, sender=TEvaluaciones)
def log_evaluaciones_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TEvaluacionesHistory, action, instance)


@receiver(post_delete, sender=TEvaluaciones)
def log_evaluaciones_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TEvaluacionesHistory, action, instance)

