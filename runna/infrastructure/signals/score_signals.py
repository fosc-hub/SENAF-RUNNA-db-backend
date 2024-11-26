from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from jsonschema import ValidationError
from infrastructure.models import (
    TDemandaScore, TNNyAScore,
    TVulneracion,
    TPersonaCondicionesVulnerabilidad,
    TVinculoPersonaPersona,
    TDemandaMotivoIntervencion,
    TEvaluaciones
)


# To track old values
@receiver(pre_save, sender=TVulneracion)
def vulneracion_track_old_peso_values(sender, instance, **kwargs):
    """
    Before saving, track the old 'peso' values of related fields for adjustment.
    """
    if instance.pk:  # Only for updates, not creates
        old_instance = TVulneracion.objects.get(pk=instance.pk)
        instance._old_categoria_motivo_peso = old_instance.categoria_motivo.peso
        instance._old_categoria_submotivo_peso = old_instance.categoria_submotivo.peso
        instance._old_gravedad_vulneracion_peso = old_instance.gravedad_vulneracion.peso
        instance._old_urgencia_vulneracion_peso = old_instance.urgencia_vulneracion.peso
        instance._old_nnya = old_instance.nnya
        instance._old_demanda = old_instance.demanda

    else:
        # For new instances, no old values
        instance._old_categoria_motivo_peso = 0
        instance._old_categoria_submotivo_peso = 0
        instance._old_gravedad_vulneracion_peso = 0
        instance._old_urgencia_vulneracion_peso = 0
        instance._old_nnya = None
        instance._old_demanda = None

@receiver(post_save, sender=TVulneracion)
def vulneracion_update_sumatoria_and_score(sender, instance, created, **kwargs):
    """
    On creation or update of a TVulneracion object:
    1. Calculate the new sum of the 'peso' fields from related objects.
    2. Adjust the 'sumatoria_de_pesos' field.
    3. Adjust the 'total_score' field of the associated TDemandaScore.
    """
    # Relevant fields for recalculating `sumatoria_de_pesos`
    relevant_fields = {
        'categoria_motivo_id',
        'categoria_submotivo_id',
        'gravedad_vulneracion_id',
        'urgencia_vulneracion_id',
    }

    # Check if relevant fields are updated
    update_fields = kwargs.get('update_fields', None)
    if update_fields and not relevant_fields.intersection(update_fields):
        return  # Skip if none of the relevant fields were updated

    # Calculate new sumatoria_de_pesos
    new_sumatoria_de_pesos = (
        instance.categoria_motivo.peso +
        instance.categoria_submotivo.peso +
        instance.gravedad_vulneracion.peso +
        instance.urgencia_vulneracion.peso
    )

    # Adjust TDemandaScore
    # Calculate the difference in scores
    old_sumatoria_de_pesos = (
        instance._old_categoria_motivo_peso +
        instance._old_categoria_submotivo_peso +
        instance._old_gravedad_vulneracion_peso +
        instance._old_urgencia_vulneracion_peso
    )
    if instance.demanda:
        if instance._old_demanda == instance.demanda or instance._old_demanda is None:
            demanda_score, created = TDemandaScore.objects.get_or_create(demanda=instance.demanda)

            score_difference = new_sumatoria_de_pesos - old_sumatoria_de_pesos
            demanda_score.score += score_difference
            demanda_score.score_vulneracion += score_difference

            demanda_score.save()
        else:
            demanda_score_old, created = TDemandaScore.objects.get_or_create(demanda=instance._old_demanda)
            
            demanda_score_old.score -= old_sumatoria_de_pesos
            demanda_score_old.score_vulneracion -= old_sumatoria_de_pesos
            demanda_score_old.save()

            demanda_score_new, created = TDemandaScore.objects.get_or_create(demanda=instance.demanda)
            
            demanda_score_new.score += new_sumatoria_de_pesos
            demanda_score_new.score_vulneracion += new_sumatoria_de_pesos
            demanda_score_new.save()


    # Adjust TDemandaScore
    if instance.nnya:
        if instance._old_nnya == instance.nnya or instance._old_nnya is None:
            nnya_score, created = TNNyAScore.objects.get_or_create(nnya=instance.nnya)

            score_difference = new_sumatoria_de_pesos - old_sumatoria_de_pesos
            nnya_score.score += score_difference
            nnya_score.score_vulneracion += score_difference

            nnya_score.save()
        else:
            nnya_score_old, created = TNNyAScore.objects.get_or_create(nnya=instance._old_nnya)
            
            nnya_score_old.score -= old_sumatoria_de_pesos
            nnya_score_old.score_vulneracion -= old_sumatoria_de_pesos
            nnya_score_old.save()

            nnya_score_new, created = TNNyAScore.objects.get_or_create(nnya=instance.nnya)
            
            nnya_score_new.score += new_sumatoria_de_pesos
            nnya_score_new.score_vulneracion += new_sumatoria_de_pesos
            nnya_score_new.save()

    # Update sumatoria_de_pesos on the instance
    if new_sumatoria_de_pesos != instance.sumatoria_de_pesos:
        instance.sumatoria_de_pesos = new_sumatoria_de_pesos
        instance.save(update_fields=['sumatoria_de_pesos'])


@receiver(pre_save, sender=TPersonaCondicionesVulnerabilidad)
def personaCondicionVulnerabilidad_track_old_values(sender, instance, **kwargs):
    """
    On creation or update of a TVulneracion object:
    1. Check if the 'persona.adulto' field is true, so condicion_vulnerabilidad.adulto' field must be true
    Elif the 'persona.nnya' field is true, so condicion_vulnerabilidad.nnya' field must be true.
    Else, raise a validation error.
    """
    if instance.persona.adulto:
        if not instance.condicion_vulnerabilidad.adulto:
            raise ValidationError("El campo 'adulto' debe ser verdadero si la persona es adulta.")
    elif instance.persona.nnya:
        if not instance.condicion_vulnerabilidad.nnya:
            raise ValidationError("El campo 'nnya' debe ser verdadero si la persona es un NNyA.")
    else:
        raise ValidationError("La persona debe ser adulta o un NNyA.")
    
    if instance.pk:  # Only for updates, not creates
        old_instance = TPersonaCondicionesVulnerabilidad.objects.get(pk=instance.pk)
        instance._old_persona = old_instance.persona
        instance._old_condicion_vulnerabilidad = old_instance.condicion_vulnerabilidad
        instance._old_demanda = old_instance.demanda
        instance._old_si_no = old_instance.si_no

    else:
        # For new instances, no old values
        instance._old_persona = None
        instance._old_condicion_vulnerabilidad = None
        instance._old_demanda = None
        instance._old_si_no = None

@receiver(post_save, sender=TPersonaCondicionesVulnerabilidad)
def personaCondicionVulnerabilidad_update_sumatoria_and_score(sender, instance, created, **kwargs):
    """
    On creation or update of a TVulneracion object:
    1. Check if the 'persona.adulto' field is true, so all the TVinculoPersonaPersona related
    to the persona must be filtered by the 'TVinculoPersonaPersona.persona_1' andor 'TVinculoPersonaPersona.persona_2' fields.
    2. For those filtered_objects in which 'persona.nnya' is true, sum the 'conidicion_vulnerabilidad.peso' value .
    to its related TNNyAScore object
    """
    if instance._old_si_no == instance.si_no:
        return

    condicion_vulnerabilidad_peso = instance.condicion_vulnerabilidad.peso if instance.si_no else instance.condicion_vulnerabilidad.peso*(-1)
    if instance.persona.adulto:
        # Filter TVinculoPersonaPersona related to the persona
        related_vinculos = TVinculoPersonaPersona.objects.filter(
            persona_1=instance.persona
        ) | TVinculoPersonaPersona.objects.filter(
            persona_2=instance.persona
        )

        for vinculo in related_vinculos:
            if vinculo.persona_1.nnya:
                nnya_score, created = TNNyAScore.objects.get_or_create(nnya=vinculo.persona_1)
                nnya_score.score += condicion_vulnerabilidad_peso
                nnya_score.score_condiciones_vulnerabilidad += condicion_vulnerabilidad_peso
                nnya_score.save()
            if vinculo.persona_2.nnya:
                nnya_score, created = TNNyAScore.objects.get_or_create(nnya=vinculo.persona_2)
                nnya_score.score += condicion_vulnerabilidad_peso
                nnya_score.score_condiciones_vulnerabilidad += condicion_vulnerabilidad_peso
                nnya_score.save()
    if instance.persona.nnya:
        nnya_score, created = TNNyAScore.objects.get_or_create(nnya=instance.persona)
        nnya_score.score += condicion_vulnerabilidad_peso
        nnya_score.score_condiciones_vulnerabilidad += condicion_vulnerabilidad_peso
        nnya_score.save()
        
    if instance.demanda:
        demanda_score, created = TDemandaScore.objects.get_or_create(demanda=instance.demanda)
        demanda_score.score += condicion_vulnerabilidad_peso
        demanda_score.score_condiciones_vulnerabilidad += condicion_vulnerabilidad_peso
        demanda_score.save()

