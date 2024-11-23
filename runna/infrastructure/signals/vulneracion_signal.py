from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from infrastructure.models import TVulneracion, TVulneracionHistory
from runna.middleware import get_current_authenticated_user


@receiver(post_save, sender=TVulneracion)
def log_vulneracion_save(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    TVulneracionHistory.objects.create(
        vulneracion_parent=instance,
        action=action,
        user=get_current_authenticated_user(),  # Replace with logic to get the current user
        principal_demanda=instance.principal_demanda,
        transcurre_actualidad=instance.transcurre_actualidad,
        sumatoria_de_pesos=instance.sumatoria_de_pesos,
        demanda=instance.demanda,
        nnya=instance.nnya,
        autor_dv=instance.autor_dv,
        categoria_motivo=instance.categoria_motivo,
        categoria_submotivo=instance.categoria_submotivo,
        gravedad_vulneracion=instance.gravedad_vulneracion,
        urgencia_vulneracion=instance.urgencia_vulneracion,
    )

@receiver(post_delete, sender=TVulneracion)
def log_vulneracion_delete(sender, instance, **kwargs):
    TVulneracionHistory.objects.create(
        vulneracion_parent=instance,
        action='DELETE',
        user=get_current_authenticated_user(),  # Replace with logic to get the current user
        principal_demanda=instance.principal_demanda,
        transcurre_actualidad=instance.transcurre_actualidad,
        sumatoria_de_pesos=instance.sumatoria_de_pesos,
        demanda=instance.demanda,
        nnya=instance.nnya,
        autor_dv=instance.autor_dv,
        categoria_motivo=instance.categoria_motivo,
        categoria_submotivo=instance.categoria_submotivo,
        gravedad_vulneracion=instance.gravedad_vulneracion,
        urgencia_vulneracion=instance.urgencia_vulneracion,
    )
