from .BaseLogs import logs
# from .localizacion_signal import (
#     log_localizacion_save, log_localizacion_delete
# )
# from .demanda_signals import (
#     demanda_create_score,
#     log_demanda_save, log_demanda_delete, 
#     log_preCalificacionDemanda_save, log_preCalificacionDemanda_delete,
#     log_scoreDemanda_save, log_scoreDemanda_delete,
# )
# from .persona_signals import (
#     log_persona_save, log_persona_delete, 
#     log_nnyaEducacion_save, log_nnyaEducacion_delete, 
#     # log_nnyaSalud_save, log_nnyaSalud_delete,
#     log_legajo_save, log_legajo_delete,
#     log_nnyaScore_save, log_nnyaScore_delete
# )
# from .vulneracion_signal import (
#     log_vulneracion_save, log_vulneracion_delete
# )
from .intermedias_signal import (
    # log_localizacionPersona_save, log_localizacionPersona_delete, 
    # log_demandaPersona_save, log_demandaPersona_delete, 
    # set_demanda_asignado, send_mail_to_user_asignado,
    # log_demandaAsignado_save, log_demandaAsignado_delete, 
    # log_demandaVinculada_save, log_demandaVinculada_delete,
    # log_vinculoPersonaPersona_save, log_vinculoPersonaPersona_delete,
    # log_personaCondicionesVulnerabilidad_save, log_personaCondicionesVulnerabilidad_delete,
    # log_demandaMotivoIntervencion_save, log_demandaMotivoIntervencion_delete
    set_demanda_constatacion, send_mail_to_zona_derivada, send_mail_to_user_responsable,
    log_demandaAsignado_save, log_demandaAsignado_delete, set_enviado_recibido,
)
# from .evaluacion_signals import (
#     send_respuesta_mail,
#     log_actividad_save, log_actividad_delete,
#     log_evaluaciones_save, log_evaluaciones_delete
# )
# from .score_signals import (
#     vulneracion_track_old_peso_values,
#     vulneracion_update_sumatoria_and_score,
#     personaCondicionVulnerabilidad_track_old_values,
#     personaCondicionVulnerabilidad_update_sumatoria_and_score,
#     demandaMotivoIntervencion_track_old_values,
#     demandaMotivoIntervencion_update_sumatoria_and_score,
#     evaluaciones_track_old_values,
#     evaluaciones_update_sumatoria_and_score
# )