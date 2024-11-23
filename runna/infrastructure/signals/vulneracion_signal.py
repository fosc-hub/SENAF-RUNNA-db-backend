from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from infrastructure.models import TVulneracion, TVulneracionHistory
from .BaseLogs import logs

@receiver(post_save, sender=TVulneracion)
def log_vulneracion_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TVulneracionHistory, action, instance)


@receiver(post_delete, sender=TVulneracion)
def log_vulneracion_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TVulneracionHistory, action, instance)

