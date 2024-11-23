from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from infrastructure.models import TLocalizacionPersona, TLocalizacionPersonaHistory
from .BaseLogs import logs

@receiver(post_save, sender=TLocalizacionPersona)
def log_localizacionPersona_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TLocalizacionPersonaHistory, action, instance)


@receiver(post_delete, sender=TLocalizacionPersona)
def log_localizacionPersona_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TLocalizacionPersonaHistory, action, instance)

