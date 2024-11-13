'''
repositorie example: 

from infrastructure.models import ProductModel
from core.entities import Product

class ProductRepository:
    def create(self, product: Product):
        """Save a product entity to the database."""
        ProductModel.objects.create(
            name=product.name,
            description=product.description,
            price=product.price,
        )

    def get_all(self):
        """Retrieve all products from the database."""
        products = ProductModel.objects.all()
        return [Product(p.name, p.description, p.price) for p in products]
'''

from infrastructure.models import TLocalizacion, TUsuarioLinea, TDemanda, TPersona, TVulneracion
from core.entities import Localizacion, UsuarioLinea, Demanda, Persona, Vulneracion

class LocalizacionRepository:
    def create(self, localizacion: Localizacion):
        """Save a Localizacion entity to the database."""
        TLocalizacion.objects.create(
            calle=localizacion.calle,
            numero=localizacion.numero,
            referencia_geo=localizacion.referencia_geo,
            barrio=localizacion.barrio
        )

    def get_all(self):
        """Retrieve all Localizacion entries from the database."""
        localizaciones = TLocalizacion.objects.all()
        return [Localizacion(l.calle, l.numero, l.referencia_geo, l.barrio) for l in localizaciones]

class UsuarioLineaRepository:
    def create(self, usuario: UsuarioLinea):
        """Save a UsuarioLinea entity to the database."""
        TUsuarioLinea.objects.create(
            nombre=usuario.nombre,
            apellido=usuario.apellido,
            fecha_nacimiento=usuario.fecha_nacimiento,
            sexo=usuario.sexo,
            telefono=usuario.telefono,
            vinculo=usuario.vinculo,
            institucion=usuario.institucion,
            responsable=usuario.responsable
        )

    def get_all(self):
        """Retrieve all UsuarioLinea entries from the database."""
        usuarios = TUsuarioLinea.objects.all()
        return [UsuarioLinea(u.nombre, u.apellido, u.fecha_nacimiento, u.sexo, u.telefono, u.vinculo, u.institucion, u.responsable) for u in usuarios]

class DemandaRepository:
    def create(self, demanda: Demanda):
        """Save a Demanda entity to the database."""
        TDemanda.objects.create(
            fecha_ingreso=demanda.fecha_ingreso,
            hora_ingreso=demanda.hora_ingreso,
            descripcion=demanda.descripcion,
            ultima_actualizacion=demanda.ultima_actualizacion,
            score=demanda.score,
            score_vulneracion=demanda.score_vulneracion,
            score_evaluacion=demanda.score_evaluacion,
            localizacion=demanda.localizacion,
            usuario_linea=demanda.usuario_linea
        )

    def get_all(self):
        """Retrieve all Demanda entries from the database."""
        demandas = TDemanda.objects.all()
        return [Demanda(d.fecha_ingreso, d.hora_ingreso, d.descripcion, d.ultima_actualizacion, d.score, d.score_vulneracion, d.score_evaluacion, d.localizacion, d.usuario_linea) for d in demandas]

class PersonaRepository:
    def create(self, persona: Persona):
        """Save a Persona entity to the database."""
        TPersona.objects.create(
            nombre=persona.nombre,
            apellido=persona.apellido,
            fecha_nacimiento=persona.fecha_nacimiento,
            sexo=persona.sexo,
            observaciones=persona.observaciones,
            adulto=persona.adulto
        )

    def get_all(self):
        """Retrieve all Persona entries from the database."""
        personas = TPersona.objects.all()
        return [Persona(p.nombre, p.apellido, p.fecha_nacimiento, p.sexo, p.observaciones, p.adulto) for p in personas]

class VulneracionRepository:
    def create(self, vulneracion: Vulneracion):
        """Save a Vulneracion entity to the database."""
        TVulneracion.objects.create(
            vulneracion_principal_demanda=vulneracion.vulneracion_principal_demanda,
            sumatoria_pesos=vulneracion.sumatoria_pesos,
            demanda=vulneracion.demanda,
            persona_nnya=vulneracion.persona_nnya,
            persona_autordv=vulneracion.persona_autordv,
            categoria_motivo=vulneracion.categoria_motivo,
            categoria_submotivo=vulneracion.categoria_submotivo,
            gravedad=vulneracion.gravedad,
            urgencia=vulneracion.urgencia
        )

    def get_all(self):
        """Retrieve all Vulneracion entries from the database."""
        vulneraciones = TVulneracion.objects.all()
        return [Vulneracion(v.vulneracion_principal_demanda, v.sumatoria_pesos, v.demanda, v.persona_nnya, v.persona_autordv, v.categoria_motivo, v.categoria_submotivo, v.gravedad, v.urgencia) for v in vulneraciones]


