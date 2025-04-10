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
    """
    Se marca el usuario que envía la demanda(quien deriva de una zona a otra)
     y el que la recibe.
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

    if instance.pk and current_user is not None:
        previous_values = TDemandaZona.objects.get(pk=instance.pk)
        if previous_values.recibido==False and instance.recibido==True:
            instance.recibido_por = current_user
    elif instance.pk is None and current_user is not None:
        instance.enviado_por = current_user


@receiver(post_save, sender=TDemandaZona)
def set_estado_demanda_and_send_mail_to_User_asignado(sender, instance, created, **kwargs):
    """
    Primero se valida que la derivacion este activa
    Luego se valida que haya un usuario responsable para la derivacion, de haberlo,
     se valida si ha sido asignado en esta modificación de la siguiente manera:
     * instance.demanda.estado_demanda == "SIN_ASIGNAR"
     de ser asi, se cambia el estado de la demanda según el objetivo y se envía un mail al responsable
    Luego, se verifica si el responsable no es nulo y la demanda ya ha sido asignada,
     buscando asi si el responsable ha cambiado,
     de ser asi se envía un mail a ambos responsables
    En caso de no haber responsable, se cambia el estado de la Demanda
    """

    if instance.esta_activo:
        if instance.user_responsable is not None and instance.demanda.estado_demanda=="SIN_ASIGNAR":
            if instance.demanda.objetivo_de_demanda == "PROTECCION":
                instance.demanda.estado_demanda = "CONSTATACION"
                instance.demanda.save()
            if instance.demanda.objetivo_de_demanda == "PETICION_DE_INFORME":
                instance.demanda.estado_demanda = "INFORME_SIN_ENVIAR"
                instance.demanda.save()

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

        elif instance.user_responsable is not None and instance.demanda.estado_demanda != "SIN_ASIGNAR":
            previous_values = TDemandaZonaHistory.objects.filter(parent=instance.id).last()
            if previous_values:
                if previous_values.user_responsable != instance.user_responsable:
                    to = [instance.user_responsable.email, previous_values.user_responsable.email]
                    subject = f"Has sido asignado como responsable de la Demanda ID {instance.demanda.id}"
                    html_content = f"""
                        <strong>Estimado/a {instance.user_responsable.email} {instance.user_responsable.last_name},</strong><br>
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
            else:
                to = [instance.user_responsable.email]
                subject = f"Has sido asignado como responsable de la Demanda ID {instance.demanda.id}"
                html_content = f"""
                    <strong>Estimado/a {instance.user_responsable.email} {instance.user_responsable.last_name},</strong><br>
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

        elif instance.user_responsable is None:
            instance.demanda.estado_demanda = "SIN_ASIGNAR"
            instance.demanda.save()


@receiver(post_save, sender=TDemandaZona)
def send_mail_to_zona_derivada_o_desderivada(sender, instance, created, **kwargs):
    """
    Validar que la derivación esté siendo creada
    Buscar derivaciones activas sobre la demanda, que difieran de la actual creada
     * cambiar sus estados a inactivas
     * enviar mail a los usuarios de la zona de cada una de esas derivaciones
    Enviar mail a los usuarios de la zona de la derivación creada
    A su vez, si es que la derivacion no está siendo creada, sino, modificada
     se valida si la derivación fue desactivada,
     y se envía un mail a los usuarios de la zona
    """
    if created:
        # Obtener todas las derivaciones activas de la demanda
        derivaciones_activas = TDemandaZona.objects.filter(
            demanda=instance.demanda,
            esta_activo=True
        ).exclude(pk=instance.pk)

        # Cambiar el estado a inactivas y enviar mail a los usuarios de la zona
        for derivacion in derivaciones_activas:
            derivacion.esta_activo = False
            derivacion.save()

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

    else:
        previous_values = TDemandaZonaHistory.objects.filter(parent=instance.id).last()
        
        if instance.esta_activo == False and previous_values.esta_activo == True:
            users_zona = TCustomUserZona.objects.filter(zona=instance.zona)

            try:
                to = [user.user.email for user in users_zona]
                subject = f"Demanda ID {instance.demanda.id} ha sido derivada a otra zona"
                html_content = f"""
                    <strong>Estimados,</strong><br>
                    La demanda ID {instance.demanda.id} ha sido derivada a otra zona.<br>
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


# @receiver(post_delete, sender=TDemandaZona)
# def log_demandaAsignado_delete(sender, instance, **kwargs):
#     for frame_record in inspect.stack():
#         if frame_record[3]=='get_response':
#             request = frame_record[0].f_locals['request']
#             break
#     else:
#         request = None

#     try:
#         current_user = request.user
#     except AttributeError:
#         current_user = None

#     action='DELETE'
#     logs(TDemandaZonaHistory, action, instance, current_user=current_user, descripcion_temp=f"Ha eliminado la derivacion de la demanda en la zona {instance.zona.nombre}")


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
