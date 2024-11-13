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

from core.entities import Decision, Demanda, DemandaPersona, NNyA, Persona, Localizacion, PrecalificacionDemanda, UsuarioLinea, Vulneracion

class LocalizacionUseCase:
    def create_localizacion(self, calle, numero, referencia_geo, barrio):
        """Creates a new Localizacion entity."""
        return Localizacion(calle, numero, referencia_geo, barrio)

class UsuarioLineaUseCase:
    def create_usuario_linea(self, nombre, apellido, fecha_nacimiento, sexo, telefono, vinculo=None, institucion=None, responsable=None):
        """Creates a new UsuarioLinea entity."""
        return UsuarioLinea(nombre, apellido, fecha_nacimiento, sexo, telefono, vinculo, institucion, responsable)

class DemandaUseCase:
    def create_demanda(self, fecha_ingreso, hora_ingreso, descripcion, ultima_actualizacion, score, score_vulneracion, score_evaluacion, localizacion, usuario_linea):
        """Creates a new Demanda entity."""
        return Demanda(fecha_ingreso, hora_ingreso, descripcion, ultima_actualizacion, score, score_vulneracion, score_evaluacion, localizacion, usuario_linea)

    def update_score(self, demanda, new_score):
        """Updates the score of the Demanda."""
        demanda.score = new_score
        return demanda

class PrecalificacionDemandaUseCase:
    def create_precalificacion_demanda(self, fecha, hora, descripcion, estado_demanda, demanda):
        """Creates a new PrecalificacionDemanda entity."""
        return PrecalificacionDemanda(fecha, hora, descripcion, estado_demanda, demanda)

class PersonaUseCase:
    def create_persona(self, nombre, apellido, fecha_nacimiento, sexo, observaciones=None, adulto=False):
        """Creates a new Persona entity."""
        return Persona(nombre, apellido, fecha_nacimiento, sexo, observaciones, adulto)

    def update_persona(self, persona, observaciones):
        """Updates the observaciones of the persona."""
        persona.observaciones = observaciones
        return persona

class DemandaPersonaUseCase:
    def link_persona_to_demanda(self, demanda, persona, conviviente, autordv, autordv_principal, nnya, nnya_principal):
        """Links a Persona to a Demanda."""
        return DemandaPersona(demanda, persona, conviviente, autordv, autordv_principal, nnya, nnya_principal)

class NNyAUseCase:
    def create_nnya(self, persona, educacion=None, institucion_sanitaria=None):
        """Creates a new NNyA entity."""
        return NNyA(persona, educacion, institucion_sanitaria)

class VulneracionUseCase:
    def create_vulneracion(self, vulneracion_principal_demanda, sumatoria_pesos, demanda, persona_nnya, persona_autordv=None, categoria_motivo=None, categoria_submotivo=None, gravedad=None, urgencia=None):
        """Creates a new Vulneracion entity."""
        return Vulneracion(vulneracion_principal_demanda, sumatoria_pesos, demanda, persona_nnya, persona_autordv, categoria_motivo, categoria_submotivo, gravedad, urgencia)

    def calculate_vulneracion_score(self, vulneracion):
        """Calculates and returns the score of a Vulneracion based on its properties."""
        return vulneracion.sumatoria_pesos

class DecisionUseCase:
    def make_decision(self, fecha, hora, decision, justificacion, demanda):
        """Creates a new Decision entity."""
        return Decision(fecha, hora, decision, justificacion, demanda)
