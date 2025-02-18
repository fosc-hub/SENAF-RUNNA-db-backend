from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from infrastructure.models import (
    TLocalizacionPersona, TLocalizacionPersonaHistory,
    TDemandaPersona, TDemandaPersonaHistory,
    TDemandaZona, TDemandaZonaHistory,
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


@receiver(post_save, sender=TDemandaZona)
def set_demanda_asignado(sender, instance, created, **kwargs):
    if created:
        instance.demanda.estado_demanda = "ASIGNADA"
        instance.demanda.save()


@receiver(post_save, sender=TDemandaZona)
def send_mail_to_user_asignado(sender, instance, created, **kwargs):
    """
    Signal triggered after a TDemandaZona instance is created.
    Sends an email notification to the assigned user.
    """
    if created:

        to = [instance.user.email]
        subject = f"Nueva asignación para la Demanda ID {instance.demanda.id}"
        html_content = f"""
            <strong>Estimado {instance.user.username},</strong><br>
            Has sido asignado para una nueva demanda.<br>
            <strong>Details:</strong><br>
            Demanda ID: {instance.demanda.id}<br>
            Comentarios: {instance.comentarios}<br>
            Saludos,<br>
            El equipo
        """

        # Send email and return the response
        email_response = EmailService.send_email(to, subject, html_content)

        return email_response 


@receiver(post_save, sender=TDemandaZona)
def log_demandaAsignado_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    logs(TDemandaZonaHistory, action, instance)


@receiver(post_delete, sender=TDemandaZona)
def log_demandaAsignado_delete(sender, instance, **kwargs):
    action='DELETE'
    logs(TDemandaZonaHistory, action, instance)


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

