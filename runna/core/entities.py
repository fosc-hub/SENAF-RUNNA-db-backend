'''
entity example: 

class Product:
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price

    def apply_discount(self, percentage: float):
        """Apply a discount to the product price."""
        self.price -= self.price * (percentage / 100)

'''

class CustomUser:
    def __init__(self, username: str, email: str, fecha_nacimiento: str = None, genero: str = None, telefono: int = None):
        self.username = username
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.telefono = telefono

    def __str__(self):
        return f"{self.username} ({self.email})"

class Provincia:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Departamento:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Localidad:
    def __init__(self, nombre: str, provincia: Provincia, departamento: Departamento):
        self.nombre = nombre
        self.provincia = provincia
        self.departamento = departamento

class Barrio:
    def __init__(self, nombre: str, localidad: Localidad):
        self.nombre = nombre
        self.localidad = localidad

class CPC:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Localizacion:
    def __init__(self, calle: str, tipo_calle: str, barrio: Barrio, localidad: Localidad, cpc: CPC = None, piso_depto: int = None, lote: int = None, mza: int = None, casa_nro: int = None, referencia_geo: str = None):
        self.calle = calle
        self.tipo_calle = tipo_calle
        self.barrio = barrio
        self.localidad = localidad
        self.cpc = cpc
        self.piso_depto = piso_depto
        self.lote = lote
        self.mza = mza
        self.casa_nro = casa_nro
        self.referencia_geo = referencia_geo

class InstitucionUsuarioLinea:
    def __init__(self, nombre: str, contacto: str):
        self.nombre = nombre
        self.contacto = contacto

class VinculoUsuarioLinea:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Cargo:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Responsable:
    def __init__(self, nombre: str, apellido: str, cargo: Cargo = None):
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo

class UsuarioLinea:
    def __init__(self, nombre: str, apellido: str, genero: str, vinculo_usuario_linea: VinculoUsuarioLinea, institucion_usuario_linea: InstitucionUsuarioLinea, responsable: Responsable = None, fecha_nacimiento: str = None, telefono: int = None):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.vinculo_usuario_linea = vinculo_usuario_linea
        self.institucion_usuario_linea = institucion_usuario_linea
        self.responsable = responsable
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono

class Demanda:
    def __init__(self, fecha_ingreso: str, hora_ingreso: str, origen: str, localizacion: Localizacion, usuario_linea: UsuarioLinea, ultima_actualizacion: str, nro_notificacion_102: int = None, nro_sac: int = None, nro_suac: int = None, nro_historia_clinica: int = None, nro_oficio_web: int = None, descripcion: str = None):
        self.fecha_ingreso = fecha_ingreso
        self.hora_ingreso = hora_ingreso
        self.origen = origen
        self.localizacion = localizacion
        self.usuario_linea = usuario_linea
        self.nro_notificacion_102 = nro_notificacion_102
        self.nro_sac = nro_sac
        self.nro_suac = nro_suac
        self.nro_historia_clinica = nro_historia_clinica
        self.ultima_actualizacion = ultima_actualizacion
        self.nro_oficio_web = nro_oficio_web
        self.descripcion = descripcion

class PrecalificacionDemanda:
    def __init__(self, fecha: str, hora: str, descripcion: str, estado_demanda: str, demanda: Demanda):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion
        self.estado_demanda = estado_demanda
        self.demanda = demanda

class Persona:
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: str, situacion_dni: str, genero: str, edad_aproximada: int = None, dni: int = None, boton_antipanico: bool = False, observaciones: str = None, adulto: bool = False, nnya: bool = False):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.situacion_dni = situacion_dni
        self.genero = genero
        self.edad_aproximada = edad_aproximada
        self.dni = dni
        self.boton_antipanico = boton_antipanico
        self.observaciones = observaciones
        self.adulto = adulto
        self.nnya = nnya

class DemandaPersona:
    def __init__(self, demanda: Demanda, persona: Persona, conviviente: bool = False, supuesto_autordv: bool = False, supuesto_autordv_principal: bool = False, nnya: bool = False, nnya_principal: bool = False):
        self.demanda = demanda
        self.persona = persona
        self.conviviente = conviviente
        self.supuesto_autordv = supuesto_autordv
        self.supuesto_autordv_principal = supuesto_autordv_principal
        self.nnya = nnya
        self.nnya_principal = nnya_principal

class InstitucionEducativa:
    def __init__(self, nombre: str, mail: str = None, telefono: int = None):
        self.nombre = nombre
        self.mail = mail
        self.telefono = telefono

class NNyAEducacion:
    def __init__(self, curso: str, nivel: str, turno: str, comentarios: str = None, institucion_educativa: InstitucionEducativa = None):
        self.curso = curso
        self.nivel = nivel
        self.turno = turno
        self.comentarios = comentarios
        self.institucion_educativa = institucion_educativa

class InstitucionSanitaria:
    def __init__(self, nombre: str, mail: str = None, telefono: int = None):
        self.nombre = nombre
        self.mail = mail
        self.telefono = telefono

class NNyA:
    def __init__(self, persona: Persona, educacion: NNyAEducacion, institucion_sanitaria: InstitucionSanitaria):
        self.persona = persona
        self.educacion = educacion
        self.institucion_sanitaria = institucion_sanitaria

class CategoriaMotivo:
    def __init__(self, nombre: str, descripcion: str = None, peso: int = 0):
        self.nombre = nombre
        self.descripcion = descripcion
        self.peso = peso

class CategoriaSubmotivo:
    def __init__(self, nombre: str, descripcion: str = None, peso: int = 0, motivo: CategoriaMotivo = None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.peso = peso
        self.motivo = motivo

class GravedadVulneracion:
    def __init__(self, nombre: str, descripcion: str = None, peso: int = 0):
        self.nombre = nombre
        self.descripcion = descripcion
        self.peso = peso

class UrgenciaVulneracion:
    def __init__(self, nombre: str, descripcion: str = None, peso: int = 0):
        self.nombre = nombre
        self.descripcion = descripcion
        self.peso = peso

class Vulneracion:
    def __init__(self, principal_demanda: bool, transcurre_actualidad: bool, sumatoria_de_pesos: int, demanda: Demanda, nnya: Persona, autor_dv: Persona = None, categoria_motivo: CategoriaMotivo = None, categoria_submotivo: CategoriaSubmotivo = None, gravedad_vulneracion: GravedadVulneracion = None, urgencia_vulneracion: UrgenciaVulneracion = None):
        self.principal_demanda = principal_demanda
        self.transcurre_actualidad = transcurre_actualidad
        self.sumatoria_de_pesos = sumatoria_de_pesos
        self.demanda = demanda
        self.nnya = nnya
        self.autor_dv = autor_dv
        self.categoria_motivo = categoria_motivo
        self.categoria_submotivo = categoria_submotivo
        self.gravedad_vulneracion = gravedad_vulneracion
        self.urgencia_vulneracion = urgencia_vulneracion

class Decision:
    def __init__(self, fecha: str, hora: str, justificacion: str, decision: str, demanda: Demanda):
        self.fecha = fecha
        self.hora = hora
        self.justificacion = justificacion
        self.decision = decision
        self.demanda = demanda

class DemandaAsignado:
    def __init__(self, demanda: Demanda, user: CustomUser, esta_activo: bool = True, recibido: bool = False, comentarios: str = None):
        self.demanda = demanda
        self.user = user
        self.esta_activo = esta_activo
        self.recibido = recibido
        self.comentarios = comentarios

class ActividadTipo:
    def __init__(self, nombre: str):
        self.nombre = nombre

class InstitucionActividad:
    def __init__(self, nombre: str):
        self.nombre = nombre

class InstitucionRespuesta:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Actividad:
    def __init__(self, fecha: str, hora: str, descripcion: str, demanda: Demanda, tipo: ActividadTipo = None, institucion: InstitucionActividad = None):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion
        self.demanda = demanda
        self.tipo = tipo
        self.institucion = institucion

class Respuesta:
    def __init__(self, fecha: str, hora: str, mail: str, mensaje: str, demanda: Demanda, institucion: InstitucionRespuesta = None):
        self.fecha = fecha
        self.hora = hora
        self.mail = mail
        self.mensaje = mensaje
        self.demanda = demanda
        self.institucion = institucion

class DemandaVinculada:
    def __init__(self, demanda_1: Demanda, demanda_2: Demanda):
        self.demanda_1 = demanda_1
        self.demanda_2 = demanda_2

class Legajo:
    def __init__(self, info_legajo: str, nnya: NNyA):
        self.info_legajo = info_legajo
        self.nnya = nnya

class LegajoAsignado:
    def __init__(self, legajo: Legajo, user: CustomUser, esta_activo: bool = True, recibido: bool = False):
        self.legajo = legajo
        self.user = user
        self.esta_activo = esta_activo
        self.recibido = recibido

class IndicadoresValoracion:
    def __init__(self, nombre: str, descripcion: str = None, peso: int = 0):
        self.nombre = nombre
        self.descripcion = descripcion
        self.peso = peso

class Evaluaciones:
    def __init__(self, demanda: Demanda, indicador: IndicadoresValoracion, si_no: bool = False):
        self.demanda = demanda
        self.indicador = indicador
        self.si_no = si_no

class Vinculo:
    def __init__(self, nombre: str):
        self.nombre = nombre

class VinculoPersonaPersona:
    def __init__(self, conviven: bool, vinculo: Vinculo, persona_1: Persona, persona_2: Persona):
        self.conviven = conviven
        self.vinculo = vinculo
        self.persona_1 = persona_1
        self.persona_2 = persona_2

class VinculoPersonaNNyA:
    def __init__(self, conviven: bool, autordv: bool, garantiza_proteccion: bool, vinculo: Vinculo, nnya: NNyA, persona: Persona):
        self.conviven = conviven
        self.autordv = autordv
        self.garantiza_proteccion = garantiza_proteccion
        self.vinculo = vinculo
        self.nnya = nnya
        self.persona = persona

class Score:
    def __init__(self, demanda: Demanda, nnya: NNyA, score: int, score_vulneracion: int, score_evaluacion: int, score_condiciones_vulnerabilidad: int, score_motivo_intervencion: int):
        self.demanda = demanda
        self.nnya = nnya
        self.score = score
        self.score_vulneracion = score_vulneracion
        self.score_evaluacion = score_evaluacion
        self.score_condiciones_vulnerabilidad = score_condiciones_vulnerabilidad
        self.score_motivo_intervencion = score_motivo_intervencion

class CondicionesVulnerabilidad:
    def __init__(self, nombre: str, descripcion: str, peso: int):
        self.nombre = nombre
        self.descripcion = descripcion
        self.peso = peso

class NNyACondicionesVulnerabilidad:
    def __init__(self, nnya: NNyA, condiciones_vulnerabilidad: CondicionesVulnerabilidad, si_no: bool):
        self.nnya = nnya
        self.condiciones_vulnerabilidad = condiciones_vulnerabilidad
        self.si_no = si_no

class MotivoIntervencion:
    def __init__(self, nombre: str, descripcion: str, peso: int):
        self.nombre = nombre
        self.descripcion = descripcion
        self.peso = peso

class NNyAMotivoIntervencion:
    def __init__(self, nnya: NNyA, motivo_intervencion: MotivoIntervencion):
        self.nnya = nnya
        self.motivo_intervencion = motivo_intervencion
