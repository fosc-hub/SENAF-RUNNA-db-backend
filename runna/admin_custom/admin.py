# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from unfold.admin import ModelAdmin
from infrastructure.models import CustomUser, Demanda, DemandaAsignado
from simple_history.admin import SimpleHistoryAdmin

@admin.action(description='Activate selected users')
def activate_users(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin, ModelAdmin):
    """Customized admin for managing users with roles and permissions."""
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('username', 'email')
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
    ordering = ('email',)
    
    actions = [activate_users]


class DemandaAsignadoInline(admin.TabularInline):
    model = DemandaAsignado
    extra = 1


@admin.register(Demanda)
class DemandaAdmin(SimpleHistoryAdmin, ModelAdmin):
    """Admin interface for managing demands with related assignments."""
    list_display = ('descripcion', 'fecha_ingreso', 'ultima_actualizacion')
    list_filter = ('fecha_ingreso',)
    search_fields = ('descripcion', 'notificacion_nro')
    inlines = [DemandaAsignadoInline]
