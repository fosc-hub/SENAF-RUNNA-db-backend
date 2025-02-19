from django.contrib import admin
from unfold.admin import ModelAdmin
# from simple_history.admin import SimpleHistoryAdmin
# from unfold.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin

from django.apps import apps

from customAuth.models import CustomUser


class NoDeleteAdmin(ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

# ===== Custom User Admin ===== #
@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin, UserAdmin):
    """Admin for managing users with roles and permissions."""
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('fecha_nacimiento', 'genero', 'telefono', 'localidad')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'email',
                'fecha_nacimiento',
                'genero',
                'telefono',
                'localidad',
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
    )

    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('username', 'email')
    ordering = ('email',)

"""
DESCOMENTAR ESTO 
Para acelerar el admin register de los models en el DESARROLLO
# Get all models from your app
"""
models = apps.get_models()
for model in models:
    try:
        if model == CustomUser:
            continue
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass  # Skip already registered models


# # ===== models ===== #

# from infrastructure.models import ( 
#     TLocalidad, 
#     TBarrio, 
#     TCPC, 
#     TLocalizacion,
# )
# from infrastructure.models import  (
#     TBloqueDatosRemitente,
#     TTipoInstitucionDemanda,
#     TAmbitoVulneracion,
#     TTipoPresuntoDelito,
#     TInstitucionDemanda,
#     TDemanda,
#     TDemandaHistory,
#     TTipoCodigoDemanda,
#     TCodigoDemanda,
#     TCalificacionDemanda,
#     TCalificacionDemandaHistory,
#     TDemandaScore, 
#     TDemandaScoreHistory,
# )
# from infrastructure.models import (
#     TPersona,
#     TPersonaHistory,
#     TInstitucionEducativa,
#     TEducacion,
#     TEducacionHistory,
#     TInstitucionSanitaria,
#     TSituacionSalud,
#     TEnfermedad,
#     TMedico,
#     TCoberturaMedica,
#     TCoberturaMedicaHistory,
#     TPersonaEnfermedades,
#     TPersonaEnfermedadesHistory,
#     TNNyAScore,
#     TNNyAScoreHistory,
#     TLegajo,
#     TLegajoHistory,
# )
# from infrastructure.models import (
#     TCategoriaMotivo,
#     TCategoriaSubmotivo,
#     TGravedadVulneracion,
#     TUrgenciaVulneracion,
#     TCondicionesVulnerabilidad,
#     TMotivoIntervencion,
#     TVulneracion,
# )
# from infrastructure.models import (
#     TLocalizacionPersona, 
#     TDemandaPersona, 
#     TDemandaZona, 
#     TDemandaVinculada, 
#     TLegajoAsignado, 
#     TVinculoPersona, 
#     TVinculoPersonaPersona, 
#     TDemandaMotivoIntervencion, 
#     TPersonaCondicionesVulnerabilidad,
# )
# from infrastructure.models import (
#     TActividadTipo, 
#     TInstitucionActividad, 
#     TActividad, 
#     TRespuesta, 
#     TIndicadoresValoracion, 
#     TEvaluaciones, 
#     TDecision,
# )

# # ===== Localizacion related models ===== #


# @admin.register(TLocalidad)
# class TLocalidadAdmin(ModelAdmin):
#     list_display = ('nombre',)
#     search_fields = ('nombre',)


# @admin.register(TBarrio)
# class TBarrioAdmin(ModelAdmin):
#     list_display = ('nombre', 'localidad')
#     list_filter = ('localidad',)
#     search_fields = ('nombre', 'localidad__nombre')


# @admin.register(TCPC)
# class TCPCAdmin(ModelAdmin):
#     list_display = ('nombre', 'localidad')
#     list_filter = ('localidad',)
#     search_fields = ('nombre', 'localidad__nombre')


# @admin.register(TLocalizacion)
# class TLocalizacionAdmin(NoDeleteAdmin):
#     fields = ('calle', 'tipo_calle', 'casa_nro', 'piso_depto', 'lote', 'mza', 'referencia_geo', 'barrio', 'cpc', 'localidad')
#     list_display = ('calle', 'tipo_calle', 'barrio', 'localidad', 'cpc')
#     list_filter = ('tipo_calle', 'barrio', 'localidad', 'cpc')
#     search_fields = ('calle', 'barrio__nombre', 'localidad__nombre', 'cpc__nombre')


# # ===== Demanda related models ===== #

# @admin.register(TBloqueDatosRemitente)
# class TBloqueDatosRemitenteAdmin(ModelAdmin):
#     list_display = ('nombre', )
#     search_fields = ('nombre', )


# @admin.register(TTipoInstitucionDemanda)
# class TTipoInstitucionDemandaAdmin(ModelAdmin):
#     list_display = ('nombre', 'bloque_datos_remitente')
#     search_fields = ('nombre', 'bloque_datos_remitente__nombre')


# @admin.register(TDemanda)
# class TDemandaAdmin(NoDeleteAdmin):
#     list_display = ('fecha_ingreso_senaf', 'fecha_oficio_documento', 'descripcion', 'estado_demanda', 'envio_de_respuesta', 'tipo_demanda', 'localizacion', 'ambito_vulneracion', 'tipos_presuntos_delitos', 'bloque_datos_remitente', 'tipo_institucion', 'institucion', 'motivo_ingreso', 'submotivo_ingreso', 'registrado_por_user', 'registrado_por_user_zona', 'zona_asignada', 'user_responsable')
#     list_filter = ('estado_demanda', 'envio_de_respuesta', 'tipo_demanda', 'localizacion', 'ambito_vulneracion', 'tipos_presuntos_delitos', 'tipo_institucion', 'motivo_ingreso', 'submotivo_ingreso', 'zona_asignada')
#     search_fields = ('descripcion', 'localizacion__nombre', 'ambito_vulneracion__nombre', 'tipos_presuntos_delitos__nombre', 'bloque_datos_remitente__nombre', 'tipo_institucion__nombre', 'institucion__nombre', 'motivo_ingreso__nombre', 'submotivo_ingreso__nombre', 'registrado_por_user__username', 'zona_asignada__nombre', 'user_responsable__username')

# @admin.register(TDemandaScore)
# class TDemandaScoreAdmin(NoDeleteAdmin):
#     list_display = ('score', 'score_condiciones_vulnerabilidad', 'score_vulneracion', 'score_motivos_intervencion', 'score_indicadores_valoracion', 'ultima_actualizacion', 'demanda')
#     search_fields = ('demanda__nro_notificacion_102',)


# # ===== Persona related models ===== #

# @admin.register(TPersona)
# class TPersonaAdmin(NoDeleteAdmin):
#     list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'dni', 'genero', 'adulto', 'nnya', 'deleted')
#     list_filter = ('genero', 'adulto', 'nnya', 'deleted')
#     search_fields = ('nombre', 'apellido', 'dni')


# @admin.register(TInstitucionEducativa)
# class TInstitucionEducativaAdmin(ModelAdmin):
#     list_display = ('nombre', 'mail', 'telefono', 'localizacion')
#     list_filter = ('localizacion',)
#     search_fields = ('nombre', 'mail', 'telefono', 'localizacion__nombre')


# @admin.register(TEducacion)
# class TEducacionAdmin(NoDeleteAdmin):
#     list_display = ('curso', 'nivel', 'turno', 'institucion_educativa', 'nnya', 'deleted')
#     list_filter = ('nivel', 'turno', 'institucion_educativa', 'deleted')
#     search_fields = ('curso', 'institucion_educativa__nombre', 'nnya__nombre')


# @admin.register(TInstitucionSanitaria)
# class TInstitucionSanitariaAdmin(ModelAdmin):
#     list_display = ('nombre', 'mail', 'telefono', 'localizacion')
#     list_filter = ('localizacion',)
#     search_fields = ('nombre', 'mail', 'telefono', 'localizacion__nombre')


# @admin.register(TNNyAScore)
# class TNNyAScoreAdmin(NoDeleteAdmin):
#     list_display = ('score', 'score_condiciones_vulnerabilidad', 'score_vulneracion', 'nnya')
#     search_fields = ('nnya__nombre',)


# @admin.register(TLegajo)
# class TLegajoAdmin(NoDeleteAdmin):
#     list_display = ('info_legajo', 'nnya')
#     search_fields = ('nnya__nombre',)


# # ===== Vulneracion related models ===== #

# @admin.register(TCategoriaMotivo)
# class TCategoriaMotivoAdmin(ModelAdmin):
#     list_display = ('nombre', 'descripcion', 'peso')
#     list_filter = ('peso',)
#     search_fields = ('nombre', 'descripcion')


# @admin.register(TCategoriaSubmotivo)
# class TCategoriaSubmotivoAdmin(ModelAdmin):
#     list_display = ('nombre', 'descripcion', 'peso', 'motivo')
#     list_filter = ('peso', 'motivo')
#     search_fields = ('nombre', 'descripcion', 'motivo__nombre')


# @admin.register(TGravedadVulneracion)
# class TGravedadVulneracionAdmin(ModelAdmin):
#     list_display = ('nombre', 'descripcion', 'peso')
#     list_filter = ('peso',)
#     search_fields = ('nombre', 'descripcion')


# @admin.register(TUrgenciaVulneracion)
# class TUrgenciaVulneracionAdmin(ModelAdmin):
#     list_display = ('nombre', 'descripcion', 'peso')
#     list_filter = ('peso',)
#     search_fields = ('nombre', 'descripcion')


# @admin.register(TCondicionesVulnerabilidad)
# class TCondicionesVulnerabilidadAdmin(ModelAdmin):
#     list_display = ('nombre', 'descripcion', 'peso', 'nnya', 'adulto')
#     list_filter = ('peso', 'nnya', 'adulto')
#     search_fields = ('nombre', 'descripcion')


# @admin.register(TMotivoIntervencion)
# class TMotivoIntervencionAdmin(ModelAdmin):
#     list_display = ('nombre', 'descripcion', 'peso')
#     list_filter = ('peso',)
#     search_fields = ('nombre', 'descripcion')


# @admin.register(TVulneracion)
# class TVulneracionAdmin(NoDeleteAdmin):
#     list_display = ('principal_demanda', 'transcurre_actualidad', 'sumatoria_de_pesos', 'demanda', 'nnya', 'autor_dv', 'categoria_motivo', 'categoria_submotivo', 'gravedad_vulneracion', 'urgencia_vulneracion')
#     list_filter = ('principal_demanda', 'transcurre_actualidad', 'demanda', 'nnya', 'autor_dv', 'categoria_motivo', 'categoria_submotivo', 'gravedad_vulneracion', 'urgencia_vulneracion')
#     search_fields = ('demanda__nro_notificacion_102', 'nnya__nombre', 'autor_dv__nombre', 'categoria_motivo__nombre', 'categoria_submotivo__nombre', 'gravedad_vulneracion__nombre', 'urgencia_vulneracion__nombre')



# # ===== Intermedias related models ===== #


# @admin.register(TLocalizacionPersona)
# class TLocalizacionPersonaAdmin(NoDeleteAdmin):
#     list_display = ('persona', 'localizacion', 'principal', 'deleted')
#     list_filter = ('principal', 'deleted')
#     search_fields = ('persona__nombre', 'localizacion__nombre')


# @admin.register(TDemandaPersona)
# class TDemandaPersonaAdmin(NoDeleteAdmin):
#     list_display = ('conviviente', 'supuesto_autordv', 'supuesto_autordv_principal', 'nnya_principal', 'demanda', 'persona', 'deleted')
#     list_filter = ('conviviente', 'supuesto_autordv', 'supuesto_autordv_principal', 'nnya_principal', 'deleted')
#     search_fields = ('demanda__nro_notificacion_102', 'persona__nombre')


# @admin.register(TDemandaZona)
# class TDemandaZonaAdmin(NoDeleteAdmin):
#     list_display = ('esta_activo', 'recibido', 'demanda', 'user')
#     list_filter = ('esta_activo', 'recibido')
#     search_fields = ('demanda__nro_notificacion_102', 'user__username')


# @admin.register(TDemandaVinculada)
# class TDemandaVinculadaAdmin(NoDeleteAdmin):
#     list_display = ('demanda_1', 'demanda_2', 'deleted')
#     list_filter = ('deleted',)
#     search_fields = ('demanda_1__nro_notificacion_102', 'demanda_2__nro_notificacion_102')


# @admin.register(TLegajoAsignado)
# class TLegajoAsignadoAdmin(NoDeleteAdmin):
#     list_display = ('esta_activo', 'recibido', 'legajo', 'user')
#     list_filter = ('esta_activo', 'recibido')
#     search_fields = ('legajo__info_legajo', 'user__username')


# @admin.register(TVinculoPersona)
# class TVinculoPersonaAdmin(ModelAdmin):
#     list_display = ('nombre',)
#     search_fields = ('nombre',)


# @admin.register(TVinculoPersonaPersona)
# class TVinculoPersonaPersonaAdmin(NoDeleteAdmin):
#     list_display = ('conviven', 'autordv', 'garantiza_proteccion', 'persona_1', 'persona_2', 'vinculo', 'deleted')
#     list_filter = ('conviven', 'autordv', 'garantiza_proteccion', 'deleted')
#     search_fields = ('persona_1__nombre', 'persona_2__nombre', 'vinculo__nombre')


# @admin.register(TPersonaCondicionesVulnerabilidad)
# class TPersonaCondicionesVulnerabilidadAdmin(NoDeleteAdmin):
#     list_display = ('si_no', 'persona', 'condicion_vulnerabilidad', 'demanda')
#     list_filter = ('si_no', 'condicion_vulnerabilidad')
#     search_fields = ('persona__nombre', 'condicion_vulnerabilidad__nombre', 'demanda__nro_notificacion_102')


# @admin.register(TDemandaMotivoIntervencion)
# class TDemandaMotivoIntervencionAdmin(NoDeleteAdmin):
#     list_display = ('si_no', 'demanda', 'motivo_intervencion')
#     list_filter = ('si_no', 'motivo_intervencion')
#     search_fields = ('demanda__nro_notificacion_102', 'motivo_intervencion__nombre')



# # ===== Actividad related models ===== #

# @admin.register(TActividadTipo)
# class TActividadTipoAdmin(ModelAdmin):
#     list_display = ('nombre',)
#     search_fields = ('nombre',)


# @admin.register(TInstitucionActividad)
# class TInstitucionActividadAdmin(ModelAdmin):
#     list_display = ('nombre', 'mail', 'telefono', 'localizacion')
#     list_filter = ('localizacion',)
#     search_fields = ('nombre', 'mail', 'telefono', 'localizacion__nombre')


# @admin.register(TActividad)
# class TActividadAdmin(NoDeleteAdmin):
#     list_display = ('fecha_y_hora', 'descripcion', 'demanda', 'tipo', 'institucion')
#     list_filter = ('fecha_y_hora', 'tipo', 'institucion')
#     search_fields = ('descripcion', 'demanda__nro_notificacion_102', 'tipo__nombre', 'institucion__nombre')


# @admin.register(TRespuesta)
# class TRespuestaAdmin(NoDeleteAdmin):
#     list_display = ('fecha_y_hora', 'mail', 'mensaje', 'demanda', 'institucion')
#     list_filter = ('fecha_y_hora', 'institucion')
#     search_fields = ('mail', 'mensaje', 'demanda__nro_notificacion_102')


# @admin.register(TIndicadoresValoracion)
# class TIndicadoresValoracionAdmin(ModelAdmin):
#     list_display = ('nombre', 'descripcion', 'peso')
#     list_filter = ('peso',)
#     search_fields = ('nombre', 'descripcion')


# @admin.register(TEvaluaciones)
# class TEvaluacionesAdmin(NoDeleteAdmin):
#     list_display = ('demanda', 'indicador', 'si_no')
#     list_filter = ('si_no', 'indicador')
#     search_fields = ('demanda__nro_notificacion_102', 'indicador__nombre')


# @admin.register(TDecision)
# class TDecisionAdmin(NoDeleteAdmin):
#     list_display = ('fecha_y_hora', 'justificacion', 'decision', 'demanda', 'nnya')
#     list_filter = ('decision', 'fecha_y_hora')
#     search_fields = ('justificacion', 'demanda__nro_notificacion_102', 'nnya')


# # @admin.register(Demanda)
# # class DemandaAdmin(SimpleHistoryAdmin, ModelAdmin):
# #     """Admin for managing demands."""
# #     list_display = ('notificacion_nro', 'descripcion', 'fecha_ingreso', 'ultima_actualizacion')
# #     list_filter = ('fecha_ingreso',)#, 'localizacion', 'usuario_linea')
# #     search_fields = ('descripcion', 'notificacion_nro', 'usuario_linea__nombre')
# #     inlines = [DemandaAsignadoInline]
# #     # actions = [mark_demands_processed]