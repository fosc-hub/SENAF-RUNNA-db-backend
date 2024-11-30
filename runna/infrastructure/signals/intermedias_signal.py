from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from infrastructure.models import (
    TLocalizacionPersona, TLocalizacionPersonaHistory,
    TDemandaPersona, TDemandaPersonaHistory,
    TDemandaAsignado, TDemandaAsignadoHistory,
    TDemandaVinculada, TDemandaVinculadaHistory,
    TVinculoPersonaPersona, TVinculoPersonaPersonaHistory,
    TPersonaCondicionesVulnerabilidad, TPersonaCondicionesVulnerabilidadHistory,
    TDemandaMotivoIntervencion, TDemandaMotivoIntervencionHistory
)
from .BaseLogs import logs
from services.email_service import EmailService


@receiver(post_save, sender=TDemandaPersona)
def log_demandaPersona_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TDemandaPersonaHistory, action, instance)


@receiver(post_delete, sender=TDemandaPersona)
def log_demandaPersona_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TDemandaPersonaHistory, action, instance)


@receiver(post_save, sender=TDemandaAsignado)
def set_demanda_asignado(sender, instance, created, **kwargs):
    if created:
        instance.demanda.asignado = True
        instance.demanda.save()


@receiver(post_save, sender=TDemandaAsignado)
def send_mail_to_user_asignado(sender, instance, created, **kwargs):
    """
    Signal triggered after a TDemandaAsignado instance is created.
    Sends an email notification to the assigned user.
    """
    if created:

        to = [instance.user.email]
        subject = f"New Assignment for Demanda ID {instance.demanda.id}"
        html_content = f"""
            <strong>Dear {instance.user.username},</strong><br>
            You have been assigned to a new Demanda.<br>
            <strong>Details:</strong><br>
            Demanda ID: {instance.demanda.id}<br>
            Comments: {instance.comentarios}<br>
            Regards,<br>
            The Team
        """

        # Send email and return the response
        email_response = EmailService.send_email(to, subject, html_content)

        return email_response 


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


@receiver(post_save, sender=TVinculoPersonaPersona)
def log_vinculoPersonaPersona_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TVinculoPersonaPersonaHistory, action, instance)


@receiver(post_delete, sender=TVinculoPersonaPersona)
def log_vinculoPersonaPersona_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TVinculoPersonaPersonaHistory, action, instance)


@receiver(post_save, sender=TPersonaCondicionesVulnerabilidad)
def log_personaCondicionesVulnerabilidad_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TPersonaCondicionesVulnerabilidadHistory, action, instance)


@receiver(post_delete, sender=TPersonaCondicionesVulnerabilidad)
def log_personaCondicionesVulnerabilidad_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TPersonaCondicionesVulnerabilidadHistory, action, instance)


@receiver(post_save, sender=TDemandaMotivoIntervencion)
def log_demandaMotivoIntervencion_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TDemandaMotivoIntervencionHistory, action, instance)


@receiver(post_delete, sender=TDemandaMotivoIntervencion)
def log_demandaMotivoIntervencion_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TDemandaMotivoIntervencionHistory, action, instance)

