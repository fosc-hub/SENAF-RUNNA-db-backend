from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from infrastructure.models import TLocalizacion, TLocalizacionHistory
from .BaseLogs import logs

@receiver(post_save, sender=TLocalizacion)
def log_localizacion_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TLocalizacionHistory, action, instance)


@receiver(post_delete, sender=TLocalizacion)
def log_localizacion_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TLocalizacionHistory, action, instance)
