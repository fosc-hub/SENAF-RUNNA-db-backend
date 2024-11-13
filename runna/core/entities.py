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

class Localizacion:
    def __init__(self, calle: str, numero: int, referencia_geo: str, barrio):
        self.calle = calle
        self.numero = numero
        self.referencia_geo = referencia_geo
        self.barrio = barrio

class UsuarioLinea:
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento, sexo: str, telefono: str, vinculo=None, institucion=None, responsable=None):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.telefono = telefono
        self.vinculo = vinculo
        self.institucion = institucion
        self.responsable = responsable

class Demanda:
    def __init__(self, fecha_ingreso, hora_ingreso, descripcion: str, ultima_actualizacion, score: int, score_vulneracion: int, score_evaluacion: int, localizacion, usuario_linea):
        self.fecha_ingreso = fecha_ingreso
        self.hora_ingreso = hora_ingreso
        self.descripcion = descripcion
        self.ultima_actualizacion = ultima_actualizacion
        self.score = score
        self.score_vulneracion = score_vulneracion
        self.score_evaluacion = score_evaluacion
        self.localizacion = localizacion
        self.usuario_linea = usuario_linea

class PrecalificacionDemanda:
    def __init__(self, fecha, hora, descripcion: str, estado_demanda: str, demanda):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion
        self.estado_demanda = estado_demanda
        self.demanda = demanda

class Persona:
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento, sexo: str, observaciones=None, adulto: bool = False):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.observaciones = observaciones
        self.adulto = adulto

class DemandaPersona:
    def __init__(self, demanda, persona, conviviente: bool, autordv: bool, autordv_principal: bool, nnya: bool, nnya_principal: bool):
        self.demanda = demanda
        self.persona = persona
        self.conviviente = conviviente
        self.autordv = autordv
        self.autordv_principal = autordv_principal
        self.nnya = nnya
        self.nnya_principal = nnya_principal

class NNyA:
    def __init__(self, persona, educacion=None, institucion_sanitaria=None):
        self.persona = persona
        self.educacion = educacion
        self.institucion_sanitaria = institucion_sanitaria

class NNyAEducacion:
    def __init__(self, curso: str, nivel: str, turno: str, comentarios: str, institucion_educativa=None):
        self.curso = curso
        self.nivel = nivel
        self.turno = turno
        self.comentarios = comentarios
        self.institucion_educativa = institucion_educativa

class Vulneracion:
    def __init__(self, vulneracion_principal_demanda: bool, sumatoria_pesos: int, demanda, persona_nnya, persona_autordv=None, categoria_motivo=None, categoria_submotivo=None, gravedad=None, urgencia=None):
        self.vulneracion_principal_demanda = vulneracion_principal_demanda
        self.sumatoria_pesos = sumatoria_pesos
        self.demanda = demanda
        self.persona_nnya = persona_nnya
        self.persona_autordv = persona_autordv
        self.categoria_motivo = categoria_motivo
        self.categoria_submotivo = categoria_submotivo
        self.gravedad = gravedad
        self.urgencia = urgencia

class Decision:
    def __init__(self, fecha, hora, decision: str, justificacion: str, demanda):
        self.fecha = fecha
        self.hora = hora
        self.decision = decision
        self.justificacion = justificacion
        self.demanda = demanda

