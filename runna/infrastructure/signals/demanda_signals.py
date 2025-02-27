from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
from django.dispatch import receiver
from infrastructure.models import (
    TDemanda, TDemandaHistory, 
    TCalificacionDemanda, TCalificacionDemandaHistory,
    TDemandaScore, TDemandaScoreHistory,
)
from customAuth.models import (
    CustomUser,
    TCustomUserZona,
    TZona,
)
from .BaseLogs import logs
from django.db import IntegrityError
import inspect

@receiver(pre_save, sender=TDemanda)
def set_evaluacion_validar(sender, instance, **kwargs):
    if instance.estado_demanda == 'EVALUACION':
        not_null_fields = {
            "motivo de ingreso": instance.motivo_ingreso,
            "submotivo de ingreso": instance.submotivo_ingreso,
            "referencia geografica de la demanda": instance.localizacion.referencia_geo if instance.localizacion else None,
            "geolocalizacion de la demanda": instance.localizacion.geolocalizacion if instance.localizacion else None,
        }
        if not all(not_null_fields.values()):
            message = f'Faltan campos obligatorios para la evaluación de la demanda: {[k for k, v in not_null_fields.items() if not v]}'
            raise ValueError(message)


@receiver(post_save, sender=TDemanda)
def demanda_create_score(sender, instance, created, **kwargs):
    if created:
        try:
            TDemandaScore.objects.create(demanda=instance)
        except IntegrityError:
            # Handle the exception (e.g., log the error, notify someone, etc.)
            pass

@receiver(pre_save, sender=TDemanda)
def set_demanda_registrado(sender, instance, **kwargs):
    action = 'CREATE' if instance.pk is None else 'UPDATE'
    if action == 'CREATE':
        for frame_record in inspect.stack():
            if frame_record[3]=='get_response':
                request = frame_record[0].f_locals['request']
                break
        else:
            request = None
        print(f"Request: {request.user}")

        current_user = request.user
        instance.registrado_por_user = current_user
        
        user_zonas = TCustomUserZona.objects.filter(user=current_user)
        if user_zonas.exists():
            instance.registrado_por_user_zona = user_zonas.first().zona
        else:
            instance.registrado_por_user_zona = None
        print(f"Registrado por: {instance.registrado_por_user} en zona {instance.registrado_por_user_zona}")


# @receiver(post_save, sender=TDemanda)
# def log_demanda_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TDemandaHistory, action, instance)


# @receiver(post_delete, sender=TDemanda)
# def log_demanda_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TDemandaHistory, action, instance)


# @receiver(post_save, sender=TCalificacionDemanda)
# def log_preCalificacionDemanda_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TCalificacionDemandaHistory, action, instance)


# @receiver(post_delete, sender=TCalificacionDemanda)
# def log_preCalificacionDemanda_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TCalificacionDemandaHistory, action, instance)

# @receiver(post_save, sender=TDemandaScore)
# def log_scoreDemanda_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TDemandaScoreHistory, action, instance)


# @receiver(post_delete, sender=TDemandaScore)
# def log_scoreDemanda_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TDemandaScoreHistory, action, instance)
