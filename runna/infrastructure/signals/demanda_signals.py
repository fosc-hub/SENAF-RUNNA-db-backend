from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
from django.dispatch import receiver
from infrastructure.models import (
    TDemanda, TDemandaHistory, 
    TCalificacionDemanda, TCalificacionDemandaHistory,
    TDemandaScore, TDemandaScoreHistory,
    ValidacionConfiguracion, TActividad, TRespuesta, TActividadTipo, TRespuestaEtiqueta
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
        config = ValidacionConfiguracion.objects.filter(activo=True).first()
        if not config:
            # Si no hay configuración, se puede permitir o levantar error según la lógica
            return

        missing_fields = []
        for field_name in config.required_fields:
            value = getattr(instance, field_name, None)
            if not value:
                missing_fields.append(field_name)
        
        # Get all activity types for this demand
        registered_activity_types = TActividad.objects.filter(
            demanda=instance
        ).values_list('tipo', flat=True).distinct()
        missing_activities = []
        for activity_type in config.required_activity_types:
            if activity_type not in registered_activity_types:
            # Get the activity type name for better error messages
                try:
                    activity_type_name = TActividadTipo.objects.get(id=activity_type).nombre
                    missing_activities.append(f"{activity_type_name} (ID: {activity_type})")
                except TActividadTipo.DoesNotExist:
                    missing_activities.append(f"ID: {activity_type}")

        # Get all response types for this demand
        registered_response_types = TRespuesta.objects.filter(
            demanda=instance
        ).values_list('etiqueta', flat=True).distinct()
        missing_responses = []
        for response_type in config.required_response_types:
            if response_type not in registered_response_types:
                try:
                    etiqueta_name = TRespuestaEtiqueta.objects.get(id=response_type).nombre
                    missing_responses.append(f"{etiqueta_name} (ID: {response_type})")
                except TRespuestaEtiqueta.DoesNotExist:
                    missing_responses.append(f"ID: {response_type}")

        # Aquí podrías agregar validaciones adicionales: por ejemplo, si existen actividades de tipos
        # requeridos o respuestas, consultando los modelos TActividad y TRespuesta.

        if missing_fields or missing_activities or missing_responses:
            concat_message = f"Faltan campos obligatorios: {', '.join(missing_fields)}. " if missing_fields else ""
            concat_message += f"Faltan actividades requeridas: {', '.join(missing_activities)}. " if missing_activities else ""
            concat_message += f"Faltan respuestas requeridas: {', '.join(missing_responses)}. " if missing_responses else ""
            message = (
                f"El estado de la demanda no se puede cambiar a 'EVALUACION' debido a los siguientes requerimientos: {concat_message}"
                f"Por favor, complete los campos requeridos y asegúrese de que todas las actividades y respuestas necesarias estén presentes. "
            )
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

        try:
            current_user = request.user
            instance.registrado_por_user = current_user
            user_zonas = TCustomUserZona.objects.filter(user=current_user)
            if user_zonas.exists():
                instance.registrado_por_user_zona = user_zonas.first().zona
            else:
                instance.registrado_por_user_zona = None
            print(f"Registrado por: {instance.registrado_por_user} en zona {instance.registrado_por_user_zona}")

        except AttributeError:
            pass
        except Exception as e:
            pass

@receiver(pre_save, sender=TCalificacionDemanda)
def set_estado_demanda(sender, instance, **kwargs):
    estado_demanda = "ARCHIVADA" if instance.estado_calificacion in (
        'PERTINENTE_CONSTATACION_NO_URGENTE',
        'NO_PERTINENTE_NO_CORRESPONDE',
        'NO_PERTINENTE_INCOMPETENCIA',
        'NO_PERTINENTE_NO_CORRESPONDE_LEY',
        'NO_PERTINENTE_NO_VERACIDAD',
    ) else 'ADMITIDA' if instance.estado_calificacion in (
        'PASA_A_LEGAJO',
    ) else 'ENVIO_DE_RESPUESTA'

    if estado_demanda == 'ENVIO_DE_RESPUESTA':
        instance.demanda.envio_de_respuesta = "PENDIENTE"
    else:    
        instance.demanda.estado_demanda = estado_demanda
    instance.demanda.save()

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
