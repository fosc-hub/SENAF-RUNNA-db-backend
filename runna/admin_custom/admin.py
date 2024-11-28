from django.contrib import admin
from unfold.admin import ModelAdmin
# from simple_history.admin import SimpleHistoryAdmin
# from unfold.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin

from django.apps import apps

from customAuth.models import CustomUser


# ===== Custom User Admin ===== #

@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin, UserAdmin):
    """Admin for managing users with roles and permissions."""
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('fecha_nacimiento', 'genero', 'telefono', 'localidad')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('fecha_nacimiento', 'genero', 'telefono', 'localidad')}),
    )

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
    TInstitucionUsuarioExterno, 
    TVinculoUsuarioExterno, 
    TUsuarioExterno, 
    TDemanda, 
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
class TLocalizacionAdmin(ModelAdmin):
    list_display = ('calle', 'tipo_calle', 'barrio', 'localidad', 'cpc', 'deleted')
    list_filter = ('tipo_calle', 'barrio', 'localidad', 'cpc', 'deleted')
    search_fields = ('calle', 'barrio__nombre', 'localidad__nombre', 'cpc__nombre')


# ===== Demanda related models ===== #

@admin.register(TInstitucionUsuarioExterno)
class TInstitucionUsuarioExternoAdmin(ModelAdmin):
    list_display = ('nombre', 'mail', 'telefono', 'localizacion')
    list_filter = ('localizacion',)
    search_fields = ('nombre', 'mail', 'telefono', 'localizacion__nombre')


@admin.register(TVinculoUsuarioExterno)
class TVinculoUsuarioExternoAdmin(ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')


@admin.register(TUsuarioExterno)
class TUsuarioExternoAdmin(ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'genero', 'telefono', 'mail', 'vinculo', 'institucion')
    list_filter = ('genero', 'vinculo', 'institucion')
    search_fields = ('nombre', 'apellido', 'mail', 'telefono', 'vinculo__nombre', 'institucion__nombre')


@admin.register(TDemanda)
class TDemandaAdmin(ModelAdmin):
    list_display = ('nro_notificacion_102', 'descripcion', 'fecha_y_hora_ingreso', 'ultima_actualizacion', 'localizacion', 'usuario_externo', 'deleted')
    list_filter = ('fecha_y_hora_ingreso', 'localizacion', 'usuario_externo', 'deleted')
    search_fields = ('descripcion', 'nro_notificacion_102', 'usuario_externo__nombre', 'localizacion__nombre')


@admin.register(TPrecalificacionDemanda)
class TPrecalificacionDemandaAdmin(ModelAdmin):
    list_display = ('fecha_y_hora', 'descripcion', 'estado_demanda', 'ultima_actualizacion', 'demanda')
    list_filter = ('estado_demanda', 'fecha_y_hora')
    search_fields = ('descripcion', 'demanda__nro_notificacion_102')


@admin.register(TDemandaScore)
class TDemandaScoreAdmin(ModelAdmin):
    list_display = ('score', 'score_condiciones_vulnerabilidad', 'score_vulneracion', 'score_motivos_intervencion', 'score_indicadores_valoracion', 'ultima_actualizacion', 'demanda')
    search_fields = ('demanda__nro_notificacion_102',)

# @admin.register(Demanda)
# class DemandaAdmin(SimpleHistoryAdmin, ModelAdmin):
#     """Admin for managing demands."""
#     list_display = ('notificacion_nro', 'descripcion', 'fecha_ingreso', 'ultima_actualizacion')
#     list_filter = ('fecha_ingreso',)#, 'localizacion', 'usuario_linea')
#     search_fields = ('descripcion', 'notificacion_nro', 'usuario_linea__nombre')
#     inlines = [DemandaAsignadoInline]
#     # actions = [mark_demands_processed]