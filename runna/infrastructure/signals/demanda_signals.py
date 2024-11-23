from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from infrastructure.models import (
    TDemanda, TDemandaHistory, 
    TPrecalificacionDemanda, TPrecalificacionDemandaHistory,
)
from .BaseLogs import logs

@receiver(post_save, sender=TDemanda)
def log_demanda_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TDemandaHistory, action, instance)


@receiver(post_delete, sender=TDemanda)
def log_demanda_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TDemandaHistory, action, instance)


@receiver(post_save, sender=TPrecalificacionDemanda)
def log_preCalificacionDemanda_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TPrecalificacionDemandaHistory, action, instance)


@receiver(post_delete, sender=TPrecalificacionDemanda)
def log_preCalificacionDemanda_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TPrecalificacionDemandaHistory, action, instance)