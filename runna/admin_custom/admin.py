from django.contrib import admin
from unfold.admin import ModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from infrastructure.models import (
    CustomUser, Demanda, DemandaAsignado, Provincia, Localidad, Barrio, 
    Cargo, InstitucionUsuarioLinea, VinculoUsuarioLinea, Responsable, 
    UsuarioLinea, Localizacion, EstadoDemanda, PreCalificacionDemanda, 
    PrioridadIntervencion, ProblematicaIdentificada, AmbitoVulneracion, 
    DDV, Operador, Vulneracion, DemandaVinculada
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
    fieldsets = (
        ('Personal Info', {
            'fields': ('username', 'password', 'email', 'first_name', 'last_name')
        }),
        ('Additional Info', {
            'fields': ('fecha_nacimiento', 'sexo', 'telefono')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
    actions = [activate_users]

# ===== Demand Management ===== #
class DemandaAsignadoInline(admin.TabularInline):
    model = DemandaAsignado
    extra = 1

@admin.register(Demanda)
class DemandaAdmin(SimpleHistoryAdmin, ModelAdmin):
    """Admin for managing demands."""
    list_display = ('descripcion', 'fecha_ingreso', 'ultima_actualizacion')
    list_filter = ('fecha_ingreso',)
    search_fields = ('descripcion', 'notificacion_nro')
    inlines = [DemandaAsignadoInline]

@admin.register(DemandaAsignado)
class DemandaAsignadoAdmin(SimpleHistoryAdmin, ModelAdmin):
    """Admin for managing demand assignments."""
    list_display = ('demanda', 'user', 'esta_activo', 'recibido')
    list_filter = ('esta_activo', 'recibido')

# ===== Regional Models ===== #
@admin.register(Provincia)
class ProvinciaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)

@admin.register(Localidad)
class LocalidadAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre', 'provincia')

@admin.register(Barrio)
class BarrioAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre', 'localidad')

@admin.register(Localizacion)
class LocalizacionAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('calle', 'numero', 'barrio')

# ===== User-Related Models ===== #
@admin.register(Cargo)
class CargoAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)

@admin.register(InstitucionUsuarioLinea)
class InstitucionUsuarioLineaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre', 'contacto')

@admin.register(VinculoUsuarioLinea)
class VinculoUsuarioLineaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)

@admin.register(Responsable)
class ResponsableAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre', 'apellido', 'cargo')

@admin.register(UsuarioLinea)
class UsuarioLineaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre', 'apellido', 'sexo', 'telefono')

# ===== Vulneration Models ===== #
@admin.register(PrioridadIntervencion)
class PrioridadIntervencionAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)

@admin.register(ProblematicaIdentificada)
class ProblematicaIdentificadaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)

@admin.register(AmbitoVulneracion)
class AmbitoVulneracionAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)

@admin.register(DDV)
class DDVAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre',)

@admin.register(Operador)
class OperadorAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('nombre', 'apellido')

@admin.register(Vulneracion)
class VulneracionAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = (
        'motivo', 'principal', 'demanda', 'operador', 
        'prioridad_intervencion', 'problematica_identificada', 'ambito_vulneracion'
    )
    list_filter = ('principal',)

# ===== Demand Relationship Models ===== #
@admin.register(DemandaVinculada)
class DemandaVinculadaAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('demanda', 'vinculacion')


@admin.register(EstadoDemanda)
class EstadoDemandaAdmin(SimpleHistoryAdmin, ModelAdmin):
    """Admin for managing demand states."""
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(PreCalificacionDemanda)
class PreCalificacionDemandaAdmin(SimpleHistoryAdmin, ModelAdmin):
    """Admin for managing demand prequalifications."""
    list_display = ('fecha', 'hora', 'descripcion', 'estado')
    list_filter = ('fecha', 'estado')
    search_fields = ('descripcion',)

