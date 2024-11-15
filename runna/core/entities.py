
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