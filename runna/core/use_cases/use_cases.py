'''
use case example

from core.entities import Product

class ProductUseCase:
    def create_product(self, name, description, price):
        """Creates a new product entity."""
        return Product(name, description, price)

    def discount_product(self, product, percentage):
        """Applies discount to the product."""
        product.apply_discount(percentage)
        return product

'''

from core.entities import (
    Provincia, Departamento, Localidad, Barrio, CPC, Localizacion
    )

class TProvinciaUseCase:
    def list_provincias(self, queryset):
        return [Provincia(provincia.id, provincia.nombre) for provincia in queryset]
    
    def get_provincia(self, provincia):
        return Provincia(provincia.id, provincia.nombre)


class TDepartamentoUseCase:
    def list_departamentos(self, queryset):
        return [Departamento(departamento.id, departamento.nombre, departamento.provincia) for departamento in queryset]
    
    def get_departamento(self, departamento):
        return Departamento(departamento.id, departamento.nombre, departamento.provincia)

class TLocalidadUseCase:
    def list_localidades(self, queryset):
        return [Localidad(localidad.id, localidad.nombre, localidad.departamento) for localidad in queryset]
    
    def get_localidad(self, localidad):
        return Localidad(localidad.id, localidad.nombre, localidad.departamento)

class TBarrioUseCase:
    def list_barrios(self, queryset):
        return [Barrio(barrio.id, barrio.nombre, barrio.localidad) for barrio in queryset]
    
    def get_barrio(self, barrio):
        return Barrio(barrio.id, barrio.nombre, barrio.localidad)

class TCPCUseCase:
    def list_cpcs(self, queryset):
        return [CPC(cpc.id, cpc.nombre, cpc.localidad) for cpc in queryset]
    
    def get_cpc(self, cpc):
        return CPC(cpc.id, cpc.nombre, cpc.localidad)

class TLocalizacionUseCase:
    def create_localizacion(self, calle, tipo_calle, localidad, barrio=None, cpc=None, piso_depto=None, lote=None, mza=None, casa_nro=None, referencia_geo=None):
        return Localizacion(None, calle, tipo_calle, localidad, barrio, cpc, piso_depto, lote, mza, casa_nro, referencia_geo)
    
    def list_localizaciones(self, queryset):
        return [Localizacion(localizacion.id, localizacion.calle, localizacion.tipo_calle, localizacion.localidad, localizacion.barrio, localizacion.cpc, localizacion.piso_depto, localizacion.lote, localizacion.mza, localizacion.casa_nro, localizacion.referencia_geo) for localizacion in queryset]
    
    def get_localizacion(self, localizacion):
        return Localizacion(localizacion.id, localizacion.calle, localizacion.tipo_calle, localizacion.localidad, localizacion.barrio, localizacion.cpc, localizacion.piso_depto, localizacion.lote, localizacion.mza, localizacion.casa_nro, localizacion.referencia_geo)
    
    def update_localizacion(self, localizacion, **kwargs):
        for key, value in kwargs.items():
            if hasattr(localizacion, key):
                setattr(localizacion, key, value)
        
        return localizacion
