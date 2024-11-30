from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from infrastructure.models import (
    TActividad, TActividadHistory,
    TEvaluaciones, TEvaluacionesHistory,
    TRespuesta
)
from .BaseLogs import logs
from services.email_service import EmailService


@receiver(post_save, sender=TRespuesta)
def send_respuesta_mail(sender, instance, created, **kwargs):
    """
    Signal triggered after a TDemandaAsignado instance is created.
    Sends an email notification to the assigned user.
    """
    if created:

        to = [instance.mail]
        subject = f"New Answer for Demanda ID {instance.demanda.id}"
        html_content = f"""
            <strong>Dear {instance.institucion},</strong><br>
            You have been assigned to a new Demanda.<br>
            <strong>Details:</strong><br>
            Demanda ID: {instance.demanda.id}<br>
            Comments: {instance.mensaje}<br>
            Regards,<br>
            The Team
        """

        # Send email and return the response
        email_response = EmailService.send_email(to, subject, html_content)

        return email_response 

@receiver(post_save, sender=TActividad)
def log_actividad_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TActividadHistory, action, instance)


@receiver(post_delete, sender=TActividad)
def log_actividad_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TActividadHistory, action, instance)


@receiver(post_save, sender=TEvaluaciones)
def log_evaluaciones_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TEvaluacionesHistory, action, instance)


@receiver(post_delete, sender=TEvaluaciones)
def log_evaluaciones_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TEvaluacionesHistory, action, instance)

