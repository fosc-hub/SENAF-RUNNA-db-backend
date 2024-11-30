from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
from django.dispatch import receiver
from infrastructure.models import (
    TDemanda, TDemandaHistory, 
    TPrecalificacionDemanda, TPrecalificacionDemandaHistory,
    TDemandaScore, TDemandaScoreHistory
)
from .BaseLogs import logs
from django.db import IntegrityError

@receiver(post_save, sender=TDemanda)
def demanda_create_score(sender, instance, created, **kwargs):
    if created:
        try:
            TDemandaScore.objects.create(demanda=instance)
        except IntegrityError:
            # Handle the exception (e.g., log the error, notify someone, etc.)
            pass


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
    

@receiver(post_save, sender=TDemandaScore)
def log_scoreDemanda_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TDemandaScoreHistory, action, instance)


@receiver(post_delete, sender=TDemandaScore)
def log_scoreDemanda_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TDemandaScoreHistory, action, instance)
