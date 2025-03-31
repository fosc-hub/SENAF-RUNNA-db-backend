from django.db.models.signals import post_save, post_delete, pre_delete, pre_save
from django.dispatch import receiver
from customAuth.models import (
    CustomUser,
    TCustomUserZona,
    TZona,
)
from infrastructure.models import (
    TActividad,
    TEvaluaciones, TEvaluacionesHistory,
    TRespuesta, TDemandaZona
)
from .BaseLogs import logs
from django.contrib.auth.models import AnonymousUser
from services.email_service import EmailService
import inspect


@receiver(pre_save, sender=TRespuesta)
def send_respuesta_mail(sender, instance, **kwargs):
    """
    Signal triggered after a TDemandaZona instance is created.
    Sends an email notification to the assigned user.
    """
    for frame_record in inspect.stack():
        if frame_record[3]=='get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None

    try:
        current_user = request.user
    except AttributeError:
        current_user = None
    except Exception as e:
        current_user = None


    if instance.pk is None:
        try:
            instance.by_user = current_user
            print(f"valores de instance {instance.__dict__}")
            extra_adjuntos = getattr(instance, '_adjuntos', None)
            print(f"Extra adjuntos: {extra_adjuntos}")

            to = instance.to
            subject = f"Nueva respuesta para la Demanda ID {instance.demanda.id} [{instance.etiqueta.nombre}]"
            html_content = f"""
                <strong>Estimada {instance.institucion},</strong><br>
                Se ha enviado una nueva respuesta de la demanda. {instance.demanda.id}<br>
                <strong>Detalles:</strong><br>
                Demanda ID: {instance.demanda.id}<br>
                Mensaje: {instance.mensaje}<br>
                Saludos,<br>
                Nuevo RUNNA
            """
            
            # Send email and return the response
            attachments=[obj['archivo'] for obj in extra_adjuntos] if type(extra_adjuntos) == list else None
            print(f"Attachments: {attachments}")
            email_response = EmailService.send_email(to, subject, html_content, attachments=attachments)

            return email_response 
        except Exception as e:
            print(f"Error sending email: {e}")
            raise e

@receiver(post_save, sender=TActividad)
def remitir_a_jefe(sender, instance, created, **kwargs):
    """
    Signal triggered after a TActividad instance is created.
    Sends an email notification to the assigned user.
    """
    if created and instance.tipo is not None:
        if instance.tipo.remitir_a_jefe:
            try:
                try:                  
                    demanda_zonas = TDemandaZona.objects.filter(demanda=instance.demanda)

                    print(f"Demanda zonas: {demanda_zonas}")
                    jefes_zona = TCustomUserZona.objects.filter(
                        zona__in=[demanda_zona.zona for demanda_zona in demanda_zonas],
                        jefe=True
                    )
                    print(f"Jefes de zona: {jefes_zona}")

                    to = [jefe_zona.user.email for jefe_zona in jefes_zona]
                    print(f"Jefes de zona: {to}")
                    subject = f"Nueva actividad registrada para la demanda {instance.demanda.id}"
                    html_content = f"""
                        <strong>Estimado,</strong><br>
                        Se ha registrado una nueva actividad del tipo {instance.tipo.nombre}.<br>
                        <strong>Detalles:</strong><br>
                        Descripción de la actividad: {instance.descripcion}<br>
                        Saludos,<br>
                        Nuevo RUNNA
                    """
                    # Send email and return the response
                    email_response = EmailService.send_email(to, subject, html_content)

                    return email_response
                except AttributeError:
                    pass
                except Exception as e:
                    pass
            except Exception as e:
                print(f"Error getting request: {e}")
                pass

@receiver(pre_save, sender=TActividad)
def set_by_user_actividad(sender, instance, **kwargs):
    """
    Signal triggered before a TActividad instance is created.
    Sets the by_user field to the current user.
    """
    for frame_record in inspect.stack():
        if frame_record[3]=='get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None

    try:
        current_user = request.user
    except AttributeError:
        current_user = None
    except Exception as e:
        current_user = None

    if instance.pk is None:
        instance.by_user = current_user

# @receiver(post_save, sender=TActividad)
# def log_actividad_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TActividadHistory, action, instance)


# @receiver(post_delete, sender=TActividad)
# def log_actividad_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TActividadHistory, action, instance)


# @receiver(post_save, sender=TEvaluaciones)
# def log_evaluaciones_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TEvaluacionesHistory, action, instance)


# @receiver(post_delete, sender=TEvaluaciones)
# def log_evaluaciones_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TEvaluacionesHistory, action, instance)

