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
    add_fieldsets = UserAdmin.add_fieldsets

    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('username', 'email')
    ordering = ('email',)


"""
DESCOMENTAR ESTO 
Para acelerar el admin register de los models en el DESARROLLO
# Get all models from your app
models = apps.get_models()

for model in models:
    try:
        if model == CustomUser:
            continue
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass  # Skip already registered models
"""

# ===== models ===== #

from infrastructure.models import (
    TProvincia, 
    TDepartamento, 
    TLocalidad, 
    TBarrio, 
    TCPC, 
    TLocalizacion,
)
from infrastructure.models import  (
    TInstitucionDemanda, 
    TOrigenDemanda,
    TSubOrigenDemanda, 
    TInformante, 
    TDemanda,
    TInforme101,
    TPrecalificacionDemanda, 
    TDemandaScore,
)
from infrastructure.models import (
    TPersona,
    TInstitucionEducativa,
    TNNyAEducacion,
    TInstitucionSanitaria,
    TNNyASalud,
    TNNyAScore,
    TLegajo,
)
from infrastructure.models import (
    TCategoriaMotivo,
    TCategoriaSubmotivo,
    TGravedadVulneracion,
    TUrgenciaVulneracion,
    TCondicionesVulnerabilidad,
    TMotivoIntervencion,
    TVulneracion,
)
from infrastructure.models import (
    TLocalizacionPersona, 
    TDemandaPersona, 
    TDemandaAsignado, 
    TDemandaVinculada, 
    TLegajoAsignado, 
    TVinculoPersona, 
    TVinculoPersonaPersona, 
    TDemandaMotivoIntervencion, 
    TPersonaCondicionesVulnerabilidad,
)
from infrastructure.models import (
    TActividadTipo, 
    TInstitucionActividad, 
    TActividad, 
    TInstitucionRespuesta, 
    TRespuesta, 
    TIndicadoresValoracion, 
    TEvaluaciones, 
    TDecision,
)

# ===== Localizacion related models ===== #

@admin.register(TProvincia)
class TProvinciaAdmin(ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(TDepartamento)
class TDepartamentoAdmin(ModelAdmin):
    list_display = ('nombre', 'provincia')
    list_filter = ('provincia',)
    search_fields = ('nombre', 'provincia__nombre')


@admin.register(TLocalidad)
class TLocalidadAdmin(ModelAdmin):
    list_display = ('nombre', 'departamento')
    list_filter = ('departamento',)
    search_fields = ('nombre', 'departamento__nombre')


@admin.register(TBarrio)
class TBarrioAdmin(ModelAdmin):
    list_display = ('nombre', 'localidad')
    list_filter = ('localidad',)
    search_fields = ('nombre', 'localidad__nombre')


@admin.register(TCPC)
class TCPCAdmin(ModelAdmin):
    list_display = ('nombre', 'localidad')
    list_filter = ('localidad',)
    search_fields = ('nombre', 'localidad__nombre')


@admin.register(TLocalizacion)
class TLocalizacionAdmin(NoDeleteAdmin):
    fields = ('calle', 'tipo_calle', 'casa_nro', 'piso_depto', 'lote', 'mza', 'referencia_geo', 'barrio', 'cpc', 'localidad')
    list_display = ('calle', 'tipo_calle', 'barrio', 'localidad', 'cpc')
    list_filter = ('tipo_calle', 'barrio', 'localidad', 'cpc')
    search_fields = ('calle', 'barrio__nombre', 'localidad__nombre', 'cpc__nombre')


# ===== Demanda related models ===== #

@admin.register(TInstitucionDemanda)
class TInstitucionDemandaAdmin(ModelAdmin):
    list_display = ('nombre', 'mail', 'telefono', 'localizacion')
    list_filter = ('localizacion',)
    search_fields = ('nombre', 'mail', 'telefono', 'localizacion__nombre')


@admin.register(TOrigenDemanda)
class TOrigenDemandaAdmin(ModelAdmin):
    list_display = ('nombre', )
    search_fields = ('nombre', )


@admin.register(TSubOrigenDemanda)
class TSubOrigenDemandaAdmin(ModelAdmin):
    list_display = ('nombre', 'origen')
    search_fields = ('nombre', 'origen__nombre')


@admin.register(TInformante)
class TInformanteAdmin(NoDeleteAdmin):
    fields = ('nombre', 'apellido', 'telefono', 'mail')
    list_display = ('nombre', 'apellido', 'telefono', 'mail')
    search_fields = ('nombre', 'apellido', 'mail', 'telefono')


@admin.register(TDemanda)
class TDemandaAdmin(NoDeleteAdmin):
    fields = ( "fecha_y_hora_ingreso", "origen", "sub_origen", "institucion", "localizacion", "informante", "nro_notificacion_102", "nro_sac", "nro_suac", "nro_historia_clinica", "nro_oficio_web", "descripcion", "asignado", "constatacion", "evaluacion", "archivado", "completado")
    list_display = ('id', 'nro_notificacion_102', 'descripcion', 'fecha_y_hora_ingreso', 'ultima_actualizacion', "origen", "sub_origen")
    list_filter = ('fecha_y_hora_ingreso', 'localizacion', 'informante', "origen", "sub_origen")
    search_fields = ('descripcion', 'nro_notificacion_102', 'informante__nombre', 'localizacion__nombre')


@admin.register(TInforme101)
class TInforme101Admin(NoDeleteAdmin):
    fields = ('fecha_y_hora', 'fields', 'demanda')
    list_display = ('fecha_y_hora', 'demanda')
    list_filter = ('demanda',)
    search_fields = ('demanda',)


@admin.register(TPrecalificacionDemanda)
class TPrecalificacionDemandaAdmin(NoDeleteAdmin):
    fields = ('fecha_y_hora', 'descripcion', 'estado_demanda', 'demanda')
    list_display = ('fecha_y_hora', 'descripcion', 'estado_demanda', 'ultima_actualizacion', 'demanda')
    list_filter = ('estado_demanda', 'fecha_y_hora')
    search_fields = ('descripcion', 'demanda__nro_notificacion_102')


@admin.register(TDemandaScore)
class TDemandaScoreAdmin(NoDeleteAdmin):
    fields = ('score', 'score_condiciones_vulnerabilidad', 'score_vulneracion', 'score_motivos_intervencion', 'score_indicadores_valoracion', 'demanda')
    list_display = ('score', 'score_condiciones_vulnerabilidad', 'score_vulneracion', 'score_motivos_intervencion', 'score_indicadores_valoracion', 'ultima_actualizacion', 'demanda')
    search_fields = ('demanda__nro_notificacion_102',)


# ===== Persona related models ===== #

@admin.register(TPersona)
class TPersonaAdmin(NoDeleteAdmin):
    fields = ('nombre', 'apellido', 'fecha_nacimiento', 'edad_aproximada', 'dni', 'situacion_dni', 'genero', 'boton_antipanico', 'observaciones', 'adulto', 'nnya', 'cautelar')
    list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'dni', 'genero', 'adulto', 'nnya', 'deleted')
    list_filter = ('genero', 'adulto', 'nnya', 'deleted')
    search_fields = ('nombre', 'apellido', 'dni')


@admin.register(TInstitucionEducativa)
class TInstitucionEducativaAdmin(ModelAdmin):
    fields = ('nombre', 'mail', 'telefono', 'localizacion')
    list_display = ('nombre', 'mail', 'telefono', 'localizacion')
    list_filter = ('localizacion',)
    search_fields = ('nombre', 'mail', 'telefono', 'localizacion__nombre')


@admin.register(TNNyAEducacion)
class TNNyAEducacionAdmin(NoDeleteAdmin):
    fields = ('curso', 'nivel', 'turno', 'comentarios', 'institucion_educativa', 'nnya')
    list_display = ('curso', 'nivel', 'turno', 'institucion_educativa', 'nnya', 'deleted')
    list_filter = ('nivel', 'turno', 'institucion_educativa', 'deleted')
    search_fields = ('curso', 'institucion_educativa__nombre', 'nnya__nombre')


@admin.register(TInstitucionSanitaria)
class TInstitucionSanitariaAdmin(ModelAdmin):
    fields = ('nombre', 'mail', 'telefono', 'localizacion')
    list_display = ('nombre', 'mail', 'telefono', 'localizacion')
    list_filter = ('localizacion',)
    search_fields = ('nombre', 'mail', 'telefono', 'localizacion__nombre')


@admin.register(TNNyASalud)
class TNNyASaludAdmin(NoDeleteAdmin):
    fields = ('observaciones', 'institucion_sanitaria', 'nnya')
    list_display = ('institucion_sanitaria', 'nnya', 'deleted')
    list_filter = ('institucion_sanitaria', 'deleted')
    search_fields = ('institucion_sanitaria__nombre', 'nnya__nombre')


@admin.register(TNNyAScore)
class TNNyAScoreAdmin(NoDeleteAdmin):
    fields = ('score', 'score_condiciones_vulnerabilidad', 'score_vulneracion', 'nnya')
    list_display = ('score', 'score_condiciones_vulnerabilidad', 'score_vulneracion', 'nnya')
    search_fields = ('nnya__nombre',)


@admin.register(TLegajo)
class TLegajoAdmin(NoDeleteAdmin):
    fields = ('info_legajo', 'nnya')
    list_display = ('info_legajo', 'nnya')
    search_fields = ('nnya__nombre',)


# ===== Vulneracion related models ===== #

@admin.register(TCategoriaMotivo)
class TCategoriaMotivoAdmin(ModelAdmin):
    fields = ('nombre', 'descripcion', 'peso')
    list_display = ('nombre', 'descripcion', 'peso')
    list_filter = ('peso',)
    search_fields = ('nombre', 'descripcion')


@admin.register(TCategoriaSubmotivo)
class TCategoriaSubmotivoAdmin(ModelAdmin):
    fields = ('nombre', 'descripcion', 'peso', 'motivo')
    list_display = ('nombre', 'descripcion', 'peso', 'motivo')
    list_filter = ('peso', 'motivo')
    search_fields = ('nombre', 'descripcion', 'motivo__nombre')


@admin.register(TGravedadVulneracion)
class TGravedadVulneracionAdmin(ModelAdmin):
    fields = ('nombre', 'descripcion', 'peso')
    list_display = ('nombre', 'descripcion', 'peso')
    list_filter = ('peso',)
    search_fields = ('nombre', 'descripcion')


@admin.register(TUrgenciaVulneracion)
class TUrgenciaVulneracionAdmin(ModelAdmin):
    fields = ('nombre', 'descripcion', 'peso')
    list_display = ('nombre', 'descripcion', 'peso')
    list_filter = ('peso',)
    search_fields = ('nombre', 'descripcion')


@admin.register(TCondicionesVulnerabilidad)
class TCondicionesVulnerabilidadAdmin(ModelAdmin):
    fields = ('nombre', 'descripcion', 'peso', 'nnya', 'adulto')
    list_display = ('nombre', 'descripcion', 'peso', 'nnya', 'adulto')
    list_filter = ('peso', 'nnya', 'adulto')
    search_fields = ('nombre', 'descripcion')


@admin.register(TMotivoIntervencion)
class TMotivoIntervencionAdmin(ModelAdmin):
    fields = ('nombre', 'descripcion', 'peso')
    list_display = ('nombre', 'descripcion', 'peso')
    list_filter = ('peso',)
    search_fields = ('nombre', 'descripcion')


@admin.register(TVulneracion)
class TVulneracionAdmin(NoDeleteAdmin):
    fields = ('principal_demanda', 'transcurre_actualidad', 'sumatoria_de_pesos', 'demanda', 'nnya', 'autor_dv', 'categoria_motivo', 'categoria_submotivo', 'gravedad_vulneracion', 'urgencia_vulneracion')
    list_display = ('principal_demanda', 'transcurre_actualidad', 'sumatoria_de_pesos', 'demanda', 'nnya', 'autor_dv', 'categoria_motivo', 'categoria_submotivo', 'gravedad_vulneracion', 'urgencia_vulneracion')
    list_filter = ('principal_demanda', 'transcurre_actualidad', 'demanda', 'nnya', 'autor_dv', 'categoria_motivo', 'categoria_submotivo', 'gravedad_vulneracion', 'urgencia_vulneracion')
    search_fields = ('demanda__nro_notificacion_102', 'nnya__nombre', 'autor_dv__nombre', 'categoria_motivo__nombre', 'categoria_submotivo__nombre', 'gravedad_vulneracion__nombre', 'urgencia_vulneracion__nombre')



# ===== Intermedias related models ===== #


@admin.register(TLocalizacionPersona)
class TLocalizacionPersonaAdmin(NoDeleteAdmin):
    fields = ('persona', 'localizacion', 'principal')
    list_display = ('persona', 'localizacion', 'principal', 'deleted')
    list_filter = ('principal', 'deleted')
    search_fields = ('persona__nombre', 'localizacion__nombre')


@admin.register(TDemandaPersona)
class TDemandaPersonaAdmin(NoDeleteAdmin):
    fields = ('conviviente', 'supuesto_autordv', 'supuesto_autordv_principal', 'nnya_principal', 'demanda', 'persona')
    list_display = ('conviviente', 'supuesto_autordv', 'supuesto_autordv_principal', 'nnya_principal', 'demanda', 'persona', 'deleted')
    list_filter = ('conviviente', 'supuesto_autordv', 'supuesto_autordv_principal', 'nnya_principal', 'deleted')
    search_fields = ('demanda__nro_notificacion_102', 'persona__nombre')


@admin.register(TDemandaAsignado)
class TDemandaAsignadoAdmin(NoDeleteAdmin):
    fields = ('esta_activo', 'recibido', 'comentarios', 'demanda', 'user')
    list_display = ('esta_activo', 'recibido', 'demanda', 'user')
    list_filter = ('esta_activo', 'recibido')
    search_fields = ('demanda__nro_notificacion_102', 'user__username')


@admin.register(TDemandaVinculada)
class TDemandaVinculadaAdmin(NoDeleteAdmin):
    fields = ('demanda_1', 'demanda_2')
    list_display = ('demanda_1', 'demanda_2', 'deleted')
    list_filter = ('deleted',)
    search_fields = ('demanda_1__nro_notificacion_102', 'demanda_2__nro_notificacion_102')


@admin.register(TLegajoAsignado)
class TLegajoAsignadoAdmin(NoDeleteAdmin):
    fields = ('esta_activo', 'recibido', 'comentarios', 'legajo', 'user')
    list_display = ('esta_activo', 'recibido', 'legajo', 'user')
    list_filter = ('esta_activo', 'recibido')
    search_fields = ('legajo__info_legajo', 'user__username')


@admin.register(TVinculoPersona)
class TVinculoPersonaAdmin(ModelAdmin):
    fields = ('nombre',)
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(TVinculoPersonaPersona)
class TVinculoPersonaPersonaAdmin(NoDeleteAdmin):
    fields = ('conviven', 'autordv', 'garantiza_proteccion', 'persona_1', 'persona_2', 'vinculo')
    list_display = ('conviven', 'autordv', 'garantiza_proteccion', 'persona_1', 'persona_2', 'vinculo', 'deleted')
    list_filter = ('conviven', 'autordv', 'garantiza_proteccion', 'deleted')
    search_fields = ('persona_1__nombre', 'persona_2__nombre', 'vinculo__nombre')


@admin.register(TPersonaCondicionesVulnerabilidad)
class TPersonaCondicionesVulnerabilidadAdmin(NoDeleteAdmin):
    fields = ('si_no', 'persona', 'condicion_vulnerabilidad', 'demanda')
    list_display = ('si_no', 'persona', 'condicion_vulnerabilidad', 'demanda')
    list_filter = ('si_no', 'condicion_vulnerabilidad')
    search_fields = ('persona__nombre', 'condicion_vulnerabilidad__nombre', 'demanda__nro_notificacion_102')


@admin.register(TDemandaMotivoIntervencion)
class TDemandaMotivoIntervencionAdmin(NoDeleteAdmin):
    fields = ('si_no', 'demanda', 'motivo_intervencion')
    list_display = ('si_no', 'demanda', 'motivo_intervencion')
    list_filter = ('si_no', 'motivo_intervencion')
    search_fields = ('demanda__nro_notificacion_102', 'motivo_intervencion__nombre')



# ===== Actividad related models ===== #

@admin.register(TActividadTipo)
class TActividadTipoAdmin(ModelAdmin):
    fields = ('nombre',)
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(TInstitucionActividad)
class TInstitucionActividadAdmin(ModelAdmin):
    fields = ('nombre', 'mail', 'telefono', 'localizacion')
    list_display = ('nombre', 'mail', 'telefono', 'localizacion')
    list_filter = ('localizacion',)
    search_fields = ('nombre', 'mail', 'telefono', 'localizacion__nombre')


@admin.register(TActividad)
class TActividadAdmin(NoDeleteAdmin):
    fields = ('descripcion', 'demanda', 'tipo', 'institucion')
    list_display = ('fecha_y_hora', 'descripcion', 'demanda', 'tipo', 'institucion')
    list_filter = ('fecha_y_hora', 'tipo', 'institucion')
    search_fields = ('descripcion', 'demanda__nro_notificacion_102', 'tipo__nombre', 'institucion__nombre')


@admin.register(TInstitucionRespuesta)
class TInstitucionRespuestaAdmin(ModelAdmin):
    fields = ('nombre', 'mail', 'telefono', 'localizacion')
    list_display = ('nombre', 'mail', 'telefono', 'localizacion')
    list_filter = ('localizacion',)
    search_fields = ('nombre', 'mail', 'telefono', 'localizacion__nombre')


@admin.register(TRespuesta)
class TRespuestaAdmin(NoDeleteAdmin):
    fields = ('mail', 'mensaje', 'demanda', 'institucion')
    list_display = ('fecha_y_hora', 'mail', 'mensaje', 'demanda', 'institucion')
    list_filter = ('fecha_y_hora', 'institucion')
    search_fields = ('mail', 'mensaje', 'demanda__nro_notificacion_102', 'institucion__nombre')


@admin.register(TIndicadoresValoracion)
class TIndicadoresValoracionAdmin(ModelAdmin):
    fields = ('nombre', 'descripcion', 'peso')
    list_display = ('nombre', 'descripcion', 'peso')
    list_filter = ('peso',)
    search_fields = ('nombre', 'descripcion')


@admin.register(TEvaluaciones)
class TEvaluacionesAdmin(NoDeleteAdmin):
    fields = ('demanda', 'indicador', 'si_no')
    list_display = ('demanda', 'indicador', 'si_no')
    list_filter = ('si_no', 'indicador')
    search_fields = ('demanda__nro_notificacion_102', 'indicador__nombre')


@admin.register(TDecision)
class TDecisionAdmin(NoDeleteAdmin):
    fields = ('justificacion', 'decision', 'demanda', 'nnya')
    list_display = ('fecha_y_hora', 'justificacion', 'decision', 'demanda', 'nnya')
    list_filter = ('decision', 'fecha_y_hora')
    search_fields = ('justificacion', 'demanda__nro_notificacion_102', 'nnya')


# @admin.register(Demanda)
# class DemandaAdmin(SimpleHistoryAdmin, ModelAdmin):
#     """Admin for managing demands."""
#     list_display = ('notificacion_nro', 'descripcion', 'fecha_ingreso', 'ultima_actualizacion')
#     list_filter = ('fecha_ingreso',)#, 'localizacion', 'usuario_linea')
#     search_fields = ('descripcion', 'notificacion_nro', 'usuario_linea__nombre')
#     inlines = [DemandaAsignadoInline]
#     # actions = [mark_demands_processed]