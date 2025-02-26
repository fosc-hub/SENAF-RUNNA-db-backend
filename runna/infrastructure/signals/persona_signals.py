from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from infrastructure.models import (
    TPersona, TPersonaHistory,
    TEducacion, TEducacionHistory,
    # TNNyASalud, TNNyASaludHistory,
    TLegajo, TLegajoHistory,
    TNNyAScore, TNNyAScoreHistory,   
)
from .BaseLogs import logs

@receiver(post_save, sender=TPersona)
def nnya_create_score(sender, instance, created, **kwargs):
    if created:
        if instance.nnya:
            TNNyAScore.objects.create(nnya=instance)


# @receiver(post_save, sender=TPersona)
# def log_persona_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TPersonaHistory, action, instance)


# @receiver(post_delete, sender=TPersona)
# def log_persona_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TPersonaHistory, action, instance)


# @receiver(post_save, sender=TEducacion)
# def log_nnyaEducacion_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TEducacionHistory, action, instance)


# @receiver(post_delete, sender=TEducacion)
# def log_nnyaEducacion_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TEducacionHistory, action, instance)


# @receiver(post_save, sender=TNNyASalud)
# def log_nnyaSalud_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TNNyASaludHistory, action, instance)


# @receiver(post_delete, sender=TNNyASalud)
# def log_nnyaSalud_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TNNyASaludHistory, action, instance)


# @receiver(post_save, sender=TLegajo)
# def log_legajo_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TLegajoHistory, action, instance)


# @receiver(post_delete, sender=TLegajo)
# def log_legajo_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TLegajoHistory, action, instance)


# @receiver(post_save, sender=TNNyAScore)
# def log_nnyaScore_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TNNyAScoreHistory, action, instance)


# @receiver(post_delete, sender=TNNyAScore)
# def log_nnyaScore_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TNNyAScoreHistory, action, instance)


