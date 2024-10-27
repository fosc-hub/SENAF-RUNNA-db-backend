# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
# from .models import *


# Desregistrar User y Group para personalizarlos
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('username',)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


"""
# Registro de modelos personalizados

admin.site.register(Provincia)
admin.site.register(Localidad)
admin.site.register(Barrio)
admin.site.register(LocalizacionDemanda)
admin.site.register(InstitucionEducativa)
admin.site.register(InstitucionSanitaria)
admin.site.register(Vinculo)
admin.site.register(Responsable)
admin.site.register(UsuarioL)
admin.site.register(EstadoDemanda)
admin.site.register(PrioridadIntervencion)
admin.site.register(Problematica)
admin.site.register(Ambito)
admin.site.register(Operador)
admin.site.register(DDV)
admin.site.register(NNyA)
admin.site.register(Demanda)
admin.site.register(DemandaNNyA)
admin.site.register(ActividadTipo)
admin.site.register(Actividad)
admin.site.register(Evaluacion)
admin.site.register(GravedadTipo)
admin.site.register(UrgenciaTipo)
admin.site.register(EvaluacionAccion)
admin.site.register(Legajo)
admin.site.register(Respuesta)
admin.site.register(DemandaVinculada)

"""
