from django.db.models.signals import post_save, post_delete, pre_delete, pre_save
from django.dispatch import receiver
from infrastructure.models import (
    TActividad, TActividadHistory,
    TEvaluaciones, TEvaluacionesHistory,
    TRespuesta
)
from .BaseLogs import logs
from services.email_service import EmailService


@receiver(pre_save, sender=TRespuesta)
def send_respuesta_mail(sender, instance, **kwargs):
    """
    Signal triggered after a TDemandaZona instance is created.
    Sends an email notification to the assigned user.
    """
    if instance.pk is None:
        try:
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
            
            print(type(extra_adjuntos))
            print([obj['archivo'] for obj in extra_adjuntos])
            # Send email and return the response
            email_response = EmailService.send_email(to, subject, html_content, attachments=[obj['archivo'] for obj in extra_adjuntos])

            return email_response 
        except Exception as e:
            print(f"Error sending email: {e}")
            raise e

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

