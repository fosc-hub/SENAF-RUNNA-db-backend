from django.contrib import admin
from unfold.admin import ModelAdmin
from simple_history.admin import SimpleHistoryAdmin
from django.contrib.auth.admin import UserAdmin

from django.apps import apps

from customAuth.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
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

# ===== Custom User Management ===== #

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

@admin.register(TProvincia)
class TProvinciaAdmin(SimpleHistoryAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(TDepartamento)
class TDepartamentoAdmin(SimpleHistoryAdmin):
    list_display = ('nombre', 'provincia')
    list_filter = ('provincia',)
    search_fields = ('nombre', 'provincia__nombre')


@admin.register(TLocalidad)
class TLocalidadAdmin(SimpleHistoryAdmin):
    list_display = ('nombre', 'departamento')
    list_filter = ('departamento',)
    search_fields = ('nombre', 'departamento__nombre')


@admin.register(TBarrio)
class TBarrioAdmin(SimpleHistoryAdmin):
    list_display = ('nombre', 'localidad')
    list_filter = ('localidad',)
    search_fields = ('nombre', 'localidad__nombre')


@admin.register(TCPC)
class TCPCAdmin(SimpleHistoryAdmin):
    list_display = ('nombre', 'localidad')
    list_filter = ('localidad',)
    search_fields = ('nombre', 'localidad__nombre')


@admin.register(TLocalizacion)
class TLocalizacionAdmin(SimpleHistoryAdmin):
    list_display = ('calle', 'tipo_calle', 'barrio', 'localidad', 'cpc', 'deleted')
    list_filter = ('tipo_calle', 'barrio', 'localidad', 'cpc', 'deleted')
    search_fields = ('calle', 'barrio__nombre', 'localidad__nombre', 'cpc__nombre')



# @admin.register(Demanda)
# class DemandaAdmin(SimpleHistoryAdmin, ModelAdmin):
#     """Admin for managing demands."""
#     list_display = ('notificacion_nro', 'descripcion', 'fecha_ingreso', 'ultima_actualizacion')
#     list_filter = ('fecha_ingreso',)#, 'localizacion', 'usuario_linea')
#     search_fields = ('descripcion', 'notificacion_nro', 'usuario_linea__nombre')
#     inlines = [DemandaAsignadoInline]
#     # actions = [mark_demands_processed]