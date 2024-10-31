from django.contrib import admin
from unfold.admin import ModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from infrastructure.models import (
    CustomUser, Demanda, DemandaAsignado, Provincia, Localidad, Barrio, 
    Cargo, InstitucionUsuarioLinea, VinculoUsuarioLinea, Responsable, 
    UsuarioLinea, Localizacion, EstadoDemanda, PreCalificacionDemanda, 
    PrioridadIntervencion, ProblematicaIdentificada, AmbitoVulneracion, 
    DDV, Operador, Vulneracion, DemandaVinculada, 
    InstitucionSanitaria, NNyA, Persona, InstitucionEducativa, NNyAEducacion, 
    DemandaPersonaConviviente, Vinculo, VinculoPersona, DemandaAutorDV, DemandaNNyA, 
    Legajo, LegajoAsignado, ActividadTipo, InstitucionActividad, Actividad, 
    InstitucionRespuesta, Respuesta, Evaluacion, ValidacionDatos, 
    ActividadesRegistradas, Valoraciones, AccionesNecesarias
)

# ===== Custom User Management ===== #
@admin.action(description='Activate selected users')
def activate_users(modeladmin, request, queryset):
    queryset.update(is_active=True)

@admin.register(CustomUser)
class CustomUserAdmin(SimpleHistoryAdmin, ModelAdmin):
    """Admin for managing users with roles and permissions."""
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('username', 'email')
    ordering = ('email',)
    actions = [activate_users]

# ===== Demand Management ===== #
class DemandaAsignadoInline(admin.TabularInline):
    model = DemandaAsignado
    extra = 1

'''
@admin.action(description='Mark selected demands as processed')
def mark_demands_processed(modeladmin, request, queryset):
    queryset.update(ultima_actualizacion='now')
'''

@admin.register(Demanda)
class DemandaAdmin(SimpleHistoryAdmin, ModelAdmin):
    """Admin for managing demands."""
    list_display = ('notificacion_nro', 'descripcion', 'fecha_ingreso', 'ultima_actualizacion')
    list_filter = ('fecha_ingreso',)#, 'localizacion', 'usuario_linea')
    search_fields = ('descripcion', 'notificacion_nro', 'usuario_linea__nombre')
    inlines = [DemandaAsignadoInline]
    # actions = [mark_demands_processed]

@admin.register(DemandaAsignado)
class DemandaAsignadoAdmin(SimpleHistoryAdmin, ModelAdmin):
    """Admin for managing demand assignments."""
    list_display = ('demanda__notificacion_nro', 'user', 'esta_activo', 'recibido')
    list_filter = ('esta_activo', 'recibido')
    search_fields = ('demanda__descripcion', 'user__username')

# ===== Regional Models ===== #
@admin.register(Provincia)
class ProvinciaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Localidad)
class LocalidadAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre', 'provincia')
    list_filter = ('provincia',)
    search_fields = ('nombre', 'provincia__nombre')

@admin.register(Barrio)
class BarrioAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre', 'localidad')
    list_filter = ('localidad',)
    search_fields = ('nombre', 'localidad__nombre')

@admin.register(Localizacion)
class LocalizacionAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('calle', 'numero', 'barrio')
    list_filter = ('barrio',)
    search_fields = ('calle', 'barrio__nombre')

# ===== User-Related Models ===== #
@admin.register(Cargo)
class CargoAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(InstitucionUsuarioLinea)
class InstitucionUsuarioLineaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre', 'contacto')
    search_fields = ('nombre', 'contacto')

@admin.register(VinculoUsuarioLinea)
class VinculoUsuarioLineaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Responsable)
class ResponsableAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre', 'apellido', 'cargo')
    search_fields = ('nombre', 'apellido', 'cargo__nombre')

@admin.register(UsuarioLinea)
class UsuarioLineaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre', 'apellido', 'sexo', 'telefono')
    search_fields = ('nombre', 'apellido', 'institucion__nombre')
    list_filter = ('sexo',)

# ===== Vulneration Models ===== #
@admin.register(PrioridadIntervencion)
class PrioridadIntervencionAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(ProblematicaIdentificada)
class ProblematicaIdentificadaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(AmbitoVulneracion)
class AmbitoVulneracionAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(DDV)
class DDVAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Operador)
class OperadorAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre', 'apellido')
    search_fields = ('nombre', 'apellido')

@admin.register(Vulneracion)
class VulneracionAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = (
        'motivo', 'principal', 'demanda', 'operador', 
        'prioridad_intervencion', 'problematica_identificada', 'ambito_vulneracion'
    )
    list_filter = ('principal', 'prioridad_intervencion', 'ambito_vulneracion')
    search_fields = ('motivo', 'demanda__descripcion', 'operador__nombre')

# ===== Demand Relationship Models ===== #
@admin.register(DemandaVinculada)
class DemandaVinculadaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('demanda', 'vinculacion')
    search_fields = ('demanda__descripcion', 'vinculacion__descripcion')

@admin.register(EstadoDemanda)
class EstadoDemandaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(PreCalificacionDemanda)
class PreCalificacionDemandaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('fecha', 'hora', 'descripcion', 'estado')
    list_filter = ('fecha', 'estado')
    search_fields = ('descripcion', 'estado__nombre')

# Register models with custom admin configurations

@admin.register(InstitucionSanitaria)
class InstitucionSanitariaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(NNyA)
class NNyAAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('persona', 'educacion', 'institucion_sanitaria')
    search_fields = ('persona__nombre', 'persona__apellido')

@admin.register(Persona)
class PersonaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'sexo', 'adulto')
    list_filter = ('sexo', 'adulto')
    search_fields = ('nombre', 'apellido')

@admin.register(InstitucionEducativa)
class InstitucionEducativaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(NNyAEducacion)
class NNyAEducacionAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('curso', 'nivel', 'turno', 'institucion_educativa')
    search_fields = ('curso', 'nivel', 'institucion_educativa__nombre')

@admin.register(DemandaPersonaConviviente)
class DemandaPersonaConvivienteAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('demanda', 'persona')

@admin.register(Vinculo)
class VinculoAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)

@admin.register(VinculoPersona)
class VinculoPersonaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('persona1', 'persona2', 'vinculo')

@admin.register(DemandaAutorDV)
class DemandaAutorDVAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('demanda', 'persona', 'convive', 'principal')
    list_filter = ('convive', 'principal')

@admin.register(DemandaNNyA)
class DemandaNNyAAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('demanda', 'nnya', 'principal')
    list_filter = ('principal',)

@admin.register(Legajo)
class LegajoAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('info_legajo', 'nnya')

@admin.register(LegajoAsignado)
class LegajoAsignadoAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('legajo', 'user', 'esta_activo', 'recibido')
    list_filter = ('esta_activo', 'recibido')

@admin.register(ActividadTipo)
class ActividadTipoAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)

@admin.register(InstitucionActividad)
class InstitucionActividadAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)

@admin.register(Actividad)
class ActividadAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('fecha', 'hora', 'descripcion', 'demanda', 'actividad_tipo', 'institucion_actividad')
    search_fields = ('descripcion',)

@admin.register(InstitucionRespuesta)
class InstitucionRespuestaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)

@admin.register(Respuesta)
class RespuestaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('fecha', 'hora', 'mail', 'demanda', 'institucion_respuesta')

@admin.register(Evaluacion)
class EvaluacionAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('fecha', 'hora', 'comentarios', 'decision', 'demanda')
    list_filter = ('decision',)

@admin.register(ValidacionDatos)
class ValidacionDatosAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('dropdown', 'bool_value', 'comentarios', 'evaluacion')
    list_filter = ('dropdown', 'bool_value')

@admin.register(ActividadesRegistradas)
class ActividadesRegistradasAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('dropdown', 'bool_value', 'comentarios', 'evaluacion')
    list_filter = ('dropdown', 'bool_value')

@admin.register(Valoraciones)
class ValoracionesAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('dropdown_desc', 'dropdown_options', 'comentarios', 'evaluacion')
    list_filter = ('dropdown_desc', 'dropdown_options')

@admin.register(AccionesNecesarias)
class AccionesNecesariasAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('dropdown', 'bool_value', 'comentarios', 'evaluacion')
    list_filter = ('dropdown', 'bool_value')
