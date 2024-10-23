import random
import datetime
from django.utils.timezone import now
from myApp.models import (
    Provincia, Localidad, Barrio, LocalizacionDemanda, InstitucionEducativa, 
    InstitucionSanitaria, Vinculo, Responsable, UsuarioL, EstadoDemanda, 
    PrioridadIntervencion, Problematica, Ambito, Operador, DDV, NNyA, 
    Demanda, DemandaNNyA, ActividadTipo, Actividad, Evaluacion, GravedadTipo, 
    UrgenciaTipo, EvaluacionAccion, Legajo, Respuesta, DemandaVinculada
)

# Provincias
provincias = ['Cordoba', 'Buenos Aires', 'Mendoza', 'Santa Fe', 'Tucuman']
for nombre in provincias:
    Provincia.objects.create(nombre=nombre)

# Localidades
for i in range(5):
    Localidad.objects.create(
        nombre=f'Localidad {i + 1}',
        provincia=Provincia.objects.order_by('?').first()
    )

# Barrios
for i in range(5):
    Barrio.objects.create(
        nombre=f'Barrio {i + 1}',
        localidad=Localidad.objects.order_by('?').first()
    )

# Instituciones Educativas y Sanitarias
instituciones_educativas = ['Escuela Primaria', 'Colegio Secundario', 'Instituto Tecnico']
instituciones_sanitarias = ['Hospital Regional', 'Centro de Salud', 'Clinica Privada']
for nombre in instituciones_educativas:
    InstitucionEducativa.objects.create(nombre=nombre)

for nombre in instituciones_sanitarias:
    InstitucionSanitaria.objects.create(nombre=nombre)

# Vinculos y Responsables
vinculos = ['Padre', 'Madre', 'Tutor', 'Hermano', 'Abuelo']
for descripcion in vinculos:
    Vinculo.objects.create(descripcion=descripcion)

responsables = ['Lic. Juana Perez', 'Trab. Soc. Carlos Gomez']
for nombre in responsables:
    Responsable.objects.create(nombre=nombre)

# Usuarios Linea
for i in range(5):
    UsuarioL.objects.create(
        nombre_y_apellido=f'Usuario {i + 1}',
        institucion=InstitucionEducativa.objects.order_by('?').first(),
        responsable=Responsable.objects.order_by('?').first(),
        vinculo=Vinculo.objects.order_by('?').first()
    )

# Estados de Demanda y Prioridades
estados = ['Pendiente', 'En Proceso', 'Finalizada']
prioridades = ['Alta', 'Media', 'Baja']
for estado in estados:
    EstadoDemanda.objects.create(estado=estado)

for prioridad in prioridades:
    PrioridadIntervencion.objects.create(descripcion=prioridad)

# Problematicas y ambitos
problemas = ['Maltrato', 'Abuso', 'Abandono']
ambitos = ['Educacion', 'Salud', 'Familiar']
for problema in problemas:
    Problematica.objects.create(descripcion=problema)

for ambito in ambitos:
    Ambito.objects.create(descripcion=ambito)

# Operadores
for i in range(5):
    Operador.objects.create(nombre_y_apellido=f'Operador {i + 1}')

# DDV (Derechos vulnerados)
derechos = ['Derecho a la Educacion', 'Derecho a la Salud']
for derecho in derechos:
    DDV.objects.create(descripcion=derecho)

# NNyA (Niños, Niñas y Adolescentes)
for i in range(5):
    NNyA.objects.create(
        nombre=f'NNyA {i + 1}',
        institucion_sanitaria=InstitucionSanitaria.objects.order_by('?').first(),
        institucion_educativa=InstitucionEducativa.objects.order_by('?').first()
    )

# Demandas
for i in range(5):
    Demanda.objects.create(
        descripcion=f'Demanda {i + 1} por {random.choice(problemas)}',
        estado=EstadoDemanda.objects.order_by('?').first(),
        localizacion=LocalizacionDemanda.objects.create(
            calle=f'Calle {i + 1}',
            numero=str(random.randint(1, 999)),
            barrio=Barrio.objects.order_by('?').first()
        ),
        usuario=UsuarioL.objects.order_by('?').first()
    )

# Demandas y NNyA relacionados
for demanda in Demanda.objects.all():
    nnya = NNyA.objects.order_by('?').first()
    DemandaNNyA.objects.create(demanda=demanda, nnya=nnya)

# Tipos de Actividades
actividades_tipos = ['Evaluacion Inicial', 'Visita al Hogar', 'Seguimiento Telefonico']
for tipo in actividades_tipos:
    ActividadTipo.objects.create(descripcion=tipo)

# Actividades
for i in range(5):
    Actividad.objects.create(
        descripcion=f'Actividad {i + 1}',
        tipo=ActividadTipo.objects.order_by('?').first(),
        demanda=Demanda.objects.order_by('?').first()
    )

# Evaluaciones
for demanda in Demanda.objects.all():
    evaluacion = Evaluacion.objects.create(
        demanda=demanda,
        comentarios='Evaluacion completada.'
    )
    GravedadTipo.objects.create(descripcion='Alta')
    UrgenciaTipo.objects.create(descripcion='Inmediata')
    EvaluacionAccion.objects.create(
        evaluacion=evaluacion,
        descripcion='Apertura de legajo'
    )

# Legajos
for nnya in NNyA.objects.all():
    Legajo.objects.create(nnya=nnya)

# Respuestas
for i in range(5):
    Respuesta.objects.create(
        demanda=Demanda.objects.order_by('?').first(),
        mensaje=f'Respuesta automatica {i + 1}'
    )

# Demandas Vinculadas
for i in range(5):
    DemandaVinculada.objects.create(
        demanda_principal=Demanda.objects.order_by('?').first(),
        demanda_relacionada=Demanda.objects.order_by('?').first()
    )

print("Mock data successfully created.")
