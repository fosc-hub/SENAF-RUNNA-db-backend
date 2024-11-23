from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from infrastructure.models import (
    TPersona, TPersonaHistory,
    TNNyAEducacion, TNNyAEducacionHistory,
    TNNyASalud, TNNyASaludHistory,
)
from .BaseLogs import logs


@receiver(post_save, sender=TPersona)
def log_persona_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TPersonaHistory, action, instance)


@receiver(post_delete, sender=TPersona)
def log_persona_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TPersonaHistory, action, instance)


@receiver(post_save, sender=TNNyAEducacion)
def log_nnyaEducacion_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TNNyAEducacionHistory, action, instance)


@receiver(post_delete, sender=TNNyAEducacion)
def log_nnyaEducacion_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TNNyAEducacionHistory, action, instance)


@receiver(post_save, sender=TNNyASalud)
def log_nnyaSalud_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TNNyASaludHistory, action, instance)


@receiver(post_delete, sender=TNNyASalud)
def log_nnyaSalud_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TNNyASaludHistory, action, instance)

