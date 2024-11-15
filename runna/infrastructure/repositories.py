from infrastructure.models import (
    TProvincia, TDepartamento, TLocalidad, TBarrio, TCPC, TLocalizacion
)
from core.entities import (
    CPC, Departamento, Provincia, Localidad, Barrio, Localizacion,
)

class TProvinciaRepository:
    def get_all(self):
        return TProvincia.objects.all() # returns a QuerySet (not a list) to be used in filtering

    def get_provincia(self, id):
        return TProvincia.objects.get(id=id)

class TDepartamentoRepository:
    def get_all(self):
        return TDepartamento.objects.all()
    
    def get_departamento(self, id):
        return TDepartamento.objects.get(id=id)

class TLocalidadRepository:
    def get_all(self):
        return TLocalidad.objects.all()
    
    def get_localidad(self, id):
        return TLocalidad.objects.get(id=id)
    
class TBarrioRepository:
    def get_all(self):
        return TBarrio.objects.all()
    
    def get_barrio(self, id):
        return TBarrio.objects.get(id=id)

class TCPCRepository:
    def get_all(self):
        return TCPC.objects.all()
    
    def get_cpc(self, id):
        return TCPC.objects.get(id=id)


class TLocalizacionRepository:
    def create(self, localizacion: Localizacion):
        """Save a Localizacion entity to the database."""
        new_localizacion = TLocalizacion.objects.create(
            calle=localizacion.calle,
            tipo_calle=localizacion.tipo_calle,
            piso_depto=localizacion.piso_depto,
            lote=localizacion.lote,
            mza=localizacion.mza,
            casa_nro=localizacion.casa_nro,
            referencia_geo=localizacion.referencia_geo,
            barrio=localizacion.barrio,
            localidad=localizacion.localidad,
            cpc=localizacion.cpc
        )
        return Localizacion(new_localizacion.id, new_localizacion.calle, new_localizacion.tipo_calle, new_localizacion.localidad, new_localizacion.barrio, new_localizacion.cpc, new_localizacion.piso_depto, new_localizacion.lote, new_localizacion.mza, new_localizacion.casa_nro, new_localizacion.referencia_geo)

    def update(self, localizacion: Localizacion):
        """Update a Localizacion entity in the database."""
        localizacion_model = TLocalizacion.objects.get(id=localizacion.id)
        localizacion_model.calle = localizacion.calle
        localizacion_model.tipo_calle = localizacion.tipo_calle
        localizacion_model.piso_depto = localizacion.piso_depto
        localizacion_model.lote = localizacion.lote
        localizacion_model.mza = localizacion.mza
        localizacion_model.casa_nro = localizacion.casa_nro
        localizacion_model.referencia_geo = localizacion.referencia_geo
        localizacion_model.barrio = localizacion.barrio
        localizacion_model.localidad = localizacion.localidad
        localizacion_model.cpc = localizacion.cpc
        localizacion_model.save()
        return Localizacion(localizacion_model.id, localizacion_model.calle, localizacion_model.tipo_calle, localizacion_model.localidad, localizacion_model.barrio, localizacion_model.cpc, localizacion_model.piso_depto, localizacion_model.lote, localizacion_model.mza, localizacion_model.casa_nro, localizacion_model.referencia_geo)

    def get_all(self):
        return TLocalizacion.objects.all()
    
    def get_localizacion(self, id):
        return TLocalizacion.objects.get(id=id)
