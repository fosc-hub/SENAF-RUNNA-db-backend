from datetime import datetime



class Provincia:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

class Departamento:
    def __init__(self, id: int, nombre: str, provincia: Provincia):
        self.id = id
        self.nombre = nombre
        self.provincia = provincia

class Localidad:
    def __init__(self, id: int,nombre: str, departamento: Departamento):
        self.id = id
        self.nombre = nombre
        self.departamento = departamento

class Barrio:
    def __init__(self, id: int ,nombre: str, localidad: Localidad):
        self.id = id
        self.nombre = nombre
        self.localidad = localidad

class CPC:
    def __init__(self, id: int ,nombre: str, localidad: Localidad):
        self.id = id
        self.nombre = nombre
        self.localidad = localidad

class Localizacion:
    def __init__(self, id: int, calle: str, tipo_calle: str, localidad: Localidad, barrio: Barrio = None, cpc: CPC = None, piso_depto: int = None, lote: int = None, mza: int = None, casa_nro: int = None, referencia_geo: str = None):
        self.id = id
        self.calle = calle
        self.tipo_calle = tipo_calle
        self.localidad = localidad
        self.barrio = barrio
        self.cpc = cpc
        self.piso_depto = piso_depto
        self.lote = lote
        self.mza = mza
        self.casa_nro = casa_nro
        self.referencia_geo = referencia_geo

class Demanda:
    def __init__(self, id: int, deleted: bool, fecha_y_hora_ingreso: datetime, origen: str, nro_notificacion_102: int = None, nro_sac: int = None, nro_suac: int = None, nro_historia_clinica: int = None, nro_oficio_web: int = None, descripcion: str = None, ultima_actualizacion: datetime = None, localizacion: 'Localizacion' = None, usuario_externo: 'TInformante' = None):
        self.id = id
        self.deleted = deleted
        self.fecha_y_hora_ingreso = fecha_y_hora_ingreso
        self.origen = origen
        self.nro_notificacion_102 = nro_notificacion_102
        self.nro_sac = nro_sac
        self.nro_suac = nro_suac
        self.nro_historia_clinica = nro_historia_clinica
        self.nro_oficio_web = nro_oficio_web
        self.descripcion = descripcion
        self.ultima_actualizacion = ultima_actualizacion
        self.localizacion = localizacion
        self.usuario_externo = usuario_externo

class Persona:
    def __init__(self, id: int, deleted: bool, nombre: str, apellido: str, fecha_nacimiento: datetime = None, edad_aproximada: int = None, dni: int = None, situacion_dni: str = None, genero: str = None, boton_antipanico: bool = False, observaciones: str = None, adulto: bool = False, nnya: bool = False):
        self.id = id
        self.deleted = deleted
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.edad_aproximada = edad_aproximada
        self.dni = dni
        self.situacion_dni = situacion_dni
        self.genero = genero
        self.boton_antipanico = boton_antipanico
        self.observaciones = observaciones
        self.adulto = adulto
        self.nnya = nnya        

class NNyAScore:
    def __init__(self, id: int, ultima_actualizacion: datetime, score: float, score_condiciones_vulnerabilidad: float, score_vulneracion: float, score_motivos_intervencion: float, nnya: Persona):
        self.id = id
        self.ultima_actualizacion = ultima_actualizacion
        self.score = score
        self.score_condiciones_vulnerabilidad = score_condiciones_vulnerabilidad
        self.score_vulneracion = score_vulneracion
        self.score_motivos_intervencion = score_motivos_intervencion
        self.nnya = nnya

class DemandaScore:
    def __init__(self, id: int, ultima_actualizacion: datetime, score: float, score_condiciones_vulnerabilidad: float, score_vulneracion: float, score_motivos_intervencion: float, score_indicadores_valoracion: float, demanda: Demanda):
        self.id = id
        self.ultima_actualizacion = ultima_actualizacion
        self.score = score
        self.score_condiciones_vulnerabilidad = score_condiciones_vulnerabilidad
        self.score_vulneracion = score_vulneracion
        self.score_motivos_intervencion = score_motivos_intervencion
        self.score_indicadores_valoracion = score_indicadores_valoracion
        self.demanda = demanda