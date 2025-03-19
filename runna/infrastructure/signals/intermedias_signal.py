from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from customAuth.models import (
    CustomUser,
    TCustomUserZona,
    TZona,
)
from infrastructure.models import (
    TLocalizacionPersona, TLocalizacionPersonaHistory,
    TDemandaPersona, TDemandaPersonaHistory,
    TDemandaZona, TDemandaZonaHistory,
    TDemandaVinculada, TDemandaVinculadaHistory,
    # TVinculoPersonaPersona, TVinculoPersonaPersonaHistory,
    TPersonaCondicionesVulnerabilidad, TPersonaCondicionesVulnerabilidadHistory,
    # TDemandaMotivoIntervencion, TDemandaMotivoIntervencionHistory
)
from .BaseLogs import logs
from services.email_service import EmailService
from datetime import datetime
import inspect

# @receiver(post_save, sender=TDemandaPersona)
# def log_demandaPersona_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TDemandaPersonaHistory, action, instance)


# @receiver(post_delete, sender=TDemandaPersona)
# def log_demandaPersona_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TDemandaPersonaHistory, action, instance)


@receiver(pre_save, sender=TDemandaZona)
def set_enviado_recibido(sender, instance, **kwargs):
    
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

    if instance.pk and current_user is not None:
        previous_values = TDemandaZona.objects.get(pk=instance.pk)
        if previous_values.recibido != instance.recibido:
            instance.recibido_por = current_user
        if previous_values.user_responsable != instance.user_responsable:
            instance.enviado_por = current_user
    elif instance.pk is None and current_user is not None:
        instance.enviado_por = current_user

@receiver(post_save, sender=TDemandaZona)
def set_demanda_constatacion(sender, instance, created, **kwargs):
    if created:
        if instance.demanda.objetivo_de_demanda == "CONSTATACION":
            instance.demanda.estado_demanda = "CONSTATACION"
            instance.demanda.save()
        if instance.demanda.objetivo_de_demanda == "ENVÍO_DE_RESPUESTA":
            instance.demanda.estado_demanda = "RESPUESTA_SIN_ENVIAR"
            instance.demanda.save()
        if instance.demanda.objetivo_de_demanda == "PETICION_DE_INFORME":
            instance.demanda.estado_demanda = "INFORME_SIN_ENVIAR"
            instance.demanda.save()


@receiver(post_save, sender=TDemandaZona)
def send_mail_to_zona_derivada(sender, instance, created, **kwargs):
    """
    Signal triggered after a TDemandaZona instance is created.
    Sends an email notification to the assigned user.
    """
    if created:
        users_zona = TCustomUserZona.objects.filter(zona=instance.zona)
        try:
            to = [user.user.email for user in users_zona]
            subject = f"Nueva derivación en zona {instance.zona.nombre} para la Demanda ID {instance.demanda.id}"
            html_content = f"""
                <strong>Estimados,</strong><br>
                Se ha derivado una nueva demanda a su zona.<br>
                <strong>Details:</strong><br>
                Demanda ID: {instance.demanda.id}<br>
                Comentarios: {instance.comentarios}<br>
                Saludos,<br>
                Nuevo RUNNA
            """

            print(f"Email sent to {to} with subject: {subject}")

            if len(to) == 0:
                return None

            # Send email and return the response
            email_response = EmailService.send_email(to, subject, html_content)

            # return {"to": to, "subject": subject, "html_content": html_content}
            
            return email_response
        except AttributeError:
            return None

@receiver(post_save, sender=TDemandaZona)
def send_mail_to_user_responsable(sender, instance, created, **kwargs):
    """
    Signal triggered after a TDemandaZona instance is created.
    Sends an email notification to the assigned user.
    """
    if not created:

        previous_values = TDemandaZonaHistory.objects.filter(parent=instance.id).last()
        
        if instance.esta_activo == False and previous_values.esta_activo == True:
            users_zona = TCustomUserZona.objects.filter(zona=instance.zona)

            try:
                to = [user.user.email for user in users_zona]
                subject = f"Demanda ID {instance.demanda.id} ha sido desactivada"
                html_content = f"""
                    <strong>Estimados,</strong><br>
                    La demanda ID {instance.demanda.id} ha sido desactivada.<br>
                    <strong>Details:</strong><br>
                    Zona: {instance.zona.nombre}<br>
                    Comentarios: {instance.comentarios}<br>
                    Saludos,<br>
                    Nuevo RUNNA
                """
                print(f"Email sent to {to} with subject: {subject}")

                if len(to) == 0:
                    return None

                # Send email and return the response
                email_response = EmailService.send_email(to, subject, html_content)
                
                # return {"to": to, "subject": subject, "html_content": html_content}
                
                return email_response
            except AttributeError:
                return None
        
        if previous_values.user_responsable != instance.user_responsable:
            to = [instance.user_responsable.email]
            subject = f"Has sido asignado como responsable de la Demanda ID {instance.demanda.id}"
            html_content = f"""
                <strong>Estimado/a {instance.user_responsable.first_name} {instance.user_responsable.last_name},</strong><br>
                Has sido asignado/a como responsable de la demanda ID {instance.demanda.id}.<br>
                <strong>Details:</strong><br>
                Zona: {instance.zona.nombre}<br>
                Comentarios: {instance.comentarios}<br>
                Saludos,<br>
                Nuevo RUNNA
            """
            print(f"Email sent to {to} with subject: {subject}")

            if len(to) == 0:
                return None

            # Send email and return the response
            email_response = EmailService.send_email(to, subject, html_content)

            # return {"to": to, "subject": subject, "html_content": html_content}
            
            return email_response


@receiver(post_save, sender=TDemandaZona)
def log_demandaAsignado_save(sender, instance, created, **kwargs):
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

    action = 'CREATE' if created else 'UPDATE'
    descripcion = ""
    previous_values = TDemandaZonaHistory.objects.filter(parent=instance.id).last()
    if previous_values:
        descripcion_dict = {
            'esta_activo': f"Ha quitado la derivacion de la demanda en la zona {previous_values.zona.nombre}" if instance.esta_activo == False and previous_values.esta_activo == True else "",
            'recibido': "Ha recibido la demanda" if instance.recibido == True and previous_values.recibido  == False else "",
            'zona': f"Se ha derivado esta demanda a la zona {instance.zona.nombre}" if instance.zona != previous_values.zona else "",
            'user_responsable': f"Ha cambiado el responsable de esta zona a {instance.user_responsable.first_name}" if instance.user_responsable != previous_values.user_responsable else "",
        }
        descripcion += f"{descripcion_dict['esta_activo']}"
        descripcion += f"{descripcion_dict['recibido']}"
        descripcion += f"{descripcion_dict['zona']}"
        descripcion += f"{descripcion_dict['user_responsable']}"
        
        print(descripcion)
    else:
        descripcion += f"Ha derivado la demanda a la zona {instance.zona.nombre}"
        print(descripcion)

    
    logs(TDemandaZonaHistory, action, instance, current_user=current_user, descripcion_temp=descripcion)


@receiver(post_delete, sender=TDemandaZona)
def log_demandaAsignado_delete(sender, instance, **kwargs):
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

    action='DELETE'
    logs(TDemandaZonaHistory, action, instance, current_user=current_user, descripcion_temp=f"Ha eliminado la derivacion de la demanda en la zona {instance.zona.nombre}")


# @receiver(post_save, sender=TDemandaVinculada)
# def log_demandaVinculada_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TDemandaVinculadaHistory, action, instance)


# @receiver(post_delete, sender=TDemandaVinculada)
# def log_demandaVinculada_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TDemandaVinculadaHistory, action, instance)


# @receiver(post_save, sender=TLocalizacionPersona)
# def log_localizacionPersona_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TLocalizacionPersonaHistory, action, instance)


# @receiver(post_delete, sender=TLocalizacionPersona)
# def log_localizacionPersona_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TLocalizacionPersonaHistory, action, instance)


# @receiver(post_save, sender=TVinculoPersonaPersona)
# def log_vinculoPersonaPersona_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TVinculoPersonaPersonaHistory, action, instance)


# @receiver(post_delete, sender=TVinculoPersonaPersona)
# def log_vinculoPersonaPersona_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TVinculoPersonaPersonaHistory, action, instance)


# @receiver(post_save, sender=TPersonaCondicionesVulnerabilidad)
# def log_personaCondicionesVulnerabilidad_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TPersonaCondicionesVulnerabilidadHistory, action, instance)


# @receiver(post_delete, sender=TPersonaCondicionesVulnerabilidad)
# def log_personaCondicionesVulnerabilidad_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TPersonaCondicionesVulnerabilidadHistory, action, instance)


# @receiver(post_save, sender=TDemandaMotivoIntervencion)
# def log_demandaMotivoIntervencion_save(sender, instance, created, **kwargs):
#     action = 'CREATE' if created else 'UPDATE'
#     logs(TDemandaMotivoIntervencionHistory, action, instance)


# @receiver(post_delete, sender=TDemandaMotivoIntervencion)
# def log_demandaMotivoIntervencion_delete(sender, instance, **kwargs):
#     action='DELETE'
#     logs(TDemandaMotivoIntervencionHistory, action, instance)
