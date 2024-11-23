from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from infrastructure.models import (
    TLocalizacionPersona, TLocalizacionPersonaHistory,
    TDemandaPersona, TDemandaPersonaHistory,
    TDemandaAsignado, TDemandaAsignadoHistory,
    TDemandaVinculada, TDemandaVinculadaHistory,
)
from .BaseLogs import logs


@receiver(post_save, sender=TDemandaPersona)
def log_demandaPersona_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TDemandaPersonaHistory, action, instance)


@receiver(post_delete, sender=TDemandaPersona)
def log_demandaPersona_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TDemandaPersonaHistory, action, instance)


@receiver(post_save, sender=TDemandaAsignado)
def log_demandaAsignado_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TDemandaAsignadoHistory, action, instance)


@receiver(post_delete, sender=TDemandaAsignado)
def log_demandaAsignado_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TDemandaAsignadoHistory, action, instance)


@receiver(post_save, sender=TDemandaVinculada)
def log_demandaVinculada_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TDemandaVinculadaHistory, action, instance)


@receiver(post_delete, sender=TDemandaVinculada)
def log_demandaVinculada_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TDemandaVinculadaHistory, action, instance)


@receiver(post_save, sender=TLocalizacionPersona)
def log_localizacionPersona_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TLocalizacionPersonaHistory, action, instance)


@receiver(post_delete, sender=TLocalizacionPersona)
def log_localizacionPersona_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TLocalizacionPersonaHistory, action, instance)

