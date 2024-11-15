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
    User, ActividadTipo, CategoriaMotivo, CategoriaSubmotivo, Decision, DemandaAsignado, DemandaPersona, GravedadVulneracion
    , InstitucionActividad, InstitucionEducativa, InstitucionRespuesta, InstitucionSanitaria, NNyA, NNyAEducacion, Provincia
    , Departamento, Localidad, Barrio, CPC, Localizacion, InstitucionUsuarioLinea, UrgenciaVulneracion, VinculoUsuarioLinea
    , Cargo, Responsable, UsuarioLinea, Demanda, PrecalificacionDemanda, Persona, Vulneracion
    , Actividad, Respuesta, DemandaVinculada, Legajo, LegajoAsignado, IndicadoresValoracion, Evaluaciones, Vinculo
    , VinculoPersonaNNyA, VinculoPersonaNNyA, Score, CondicionesVulnerabilidad, NNyACondicionesVulnerabilidad
    , MotivoIntervencion, NNyAMotivoIntervencion, VinculoPersonaPersona
    )

class UserUseCase:
    def create_custom_user(self, username, email, fecha_nacimiento=None, genero=None, elefono=None):
        return User(username, email, fecha_nacimiento, genero, elefono)

class TProvinciaUseCase:
    def create_provincia(self, nombre):
        return Provincia(nombre)

class TDepartamentoUseCase:
    def create_departamento(self, nombre):
        return Departamento(nombre)

class TLocalidadUseCase:
    def create_localidad(self, nombre, provincia, departamento):
        return Localidad(nombre, provincia, departamento)

class TBarrioUseCase:
    def create_barrio(self, nombre, localidad):
        return Barrio(nombre, localidad)

class TCPCUseCase:
    def create_cpc(self, nombre):
        return CPC(nombre)

class TLocalizacionUseCase:
    def create_localizacion(self, calle, ipo_calle, barrio, localidad, cpc=None, piso_depto=None, lote=None, mza=None, casa_nro=None, referencia_geo=None):
        return Localizacion(calle, ipo_calle, barrio, localidad, cpc, piso_depto, lote, mza, casa_nro, referencia_geo)

class TInstitucionUsuarioLineaUseCase:
    def create_institucion_usuario_linea(self, nombre, contacto):
        return InstitucionUsuarioLinea(nombre, contacto)

class TVinculoUsuarioLineaUseCase:
    def create_vinculo_usuario_linea(self, nombre):
        return VinculoUsuarioLinea(nombre)

class TCargoUseCase:
    def create_cargo(self, nombre):
        return Cargo(nombre)

class TResponsableUseCase:
    def create_responsable(self, nombre, apellido, cargo=None):
        return Responsable(nombre, apellido, cargo)

class TUsuarioLineaUseCase:
    def create_usuario_linea(self, nombre, apellido, genero, vinculo_usuario_linea, institucion_usuario_linea, responsable=None, fecha_nacimiento=None, elefono=None):
        return UsuarioLinea(nombre, apellido, genero, vinculo_usuario_linea, institucion_usuario_linea, responsable, fecha_nacimiento, elefono)

class TDemandaUseCase:
    def create_demanda(self, fecha_ingreso, hora_ingreso, origen, localizacion, usuario_linea, nro_notificacion_102=None, nro_sac=None, nro_suac=None, nro_historia_clinica=None, nro_oficio_web=None, descripcion=None):
        return Demanda(fecha_ingreso, hora_ingreso, origen, localizacion, usuario_linea, nro_notificacion_102, nro_sac, nro_suac, nro_historia_clinica, nro_oficio_web, descripcion)
    
    def update_score(self, demanda, new_score):
        """Updates the score of the Demanda."""
        demanda.score = new_score
        return demanda

class TPrecalificacionDemandaUseCase:
    def create_precalificacion_demanda(self, fecha, hora, descripcion, estado_demanda, demanda):
        return PrecalificacionDemanda(fecha, hora, descripcion, estado_demanda, demanda)

class TPersonaUseCase:
    def create_persona(self, nombre, apellido, fecha_nacimiento, situacion_dni, genero, edad_aproximada=None, dni=None, boton_antipanico=False, observaciones=None, adulto=False, nnya=False):
        return Persona(nombre, apellido, fecha_nacimiento, situacion_dni, genero, edad_aproximada, dni, boton_antipanico, observaciones, adulto, nnya)
    
    def update_persona(self, persona, observaciones):
        """Updates the observaciones of the persona."""
        persona.observaciones = observaciones
        return persona
    
class TDemandaPersonaUseCase:
    def create_demanda_persona(self, demanda, persona, conviviente=False, supuesto_autordv=False, supuesto_autordv_principal=False, nnya=False, nnya_principal=False):
        return DemandaPersona(demanda, persona, conviviente, supuesto_autordv, supuesto_autordv_principal, nnya, nnya_principal)

class TInstitucionEducativaUseCase:
    def create_institucion_educativa(self, nombre, mail=None, elefono=None):
        return InstitucionEducativa(nombre, mail, elefono)

class TNNyAEducacionUseCase:
    def create_nnya_educacion(self, curso, nivel, urno, comentarios=None, institucion_educativa=None):
        return NNyAEducacion(curso, nivel, urno, comentarios, institucion_educativa)

class TInstitucionSanitariaUseCase:
    def create_institucion_sanitaria(self, nombre, mail=None, elefono=None):
        return InstitucionSanitaria(nombre, mail, elefono)

class TNNyAUseCase:
    def create_nnya(self, persona, educacion, institucion_sanitaria):
        return NNyA(persona, educacion, institucion_sanitaria)

class TCategoriaMotivoUseCase:
    def create_categoria_motivo(self, nombre, descripcion=None, peso=0):
        return CategoriaMotivo(nombre, descripcion, peso)

class TCategoriaSubmotivoUseCase:
    def create_categoria_submotivo(self, nombre, descripcion=None, peso=0, motivo=None):
        return CategoriaSubmotivo(nombre, descripcion, peso, motivo)

class TGravedadVulneracionUseCase:
    def create_gravedad_vulneracion(self, nombre, descripcion=None, peso=0):
        return GravedadVulneracion(nombre, descripcion, peso)

class TUrgenciaVulneracionUseCase:
    def create_urgencia_vulneracion(self, nombre, descripcion=None, peso=0):
        return UrgenciaVulneracion(nombre, descripcion, peso)

class TVulneracionUseCase:
    def create_vulneracion(self, principal_demanda, ranscurre_actualidad, sumatoria_de_pesos, demanda, nnya, autor_dv=None, categoria_motivo=None, categoria_submotivo=None, gravedad_vulneracion=None, urgencia_vulneracion=None):
        return Vulneracion(principal_demanda, ranscurre_actualidad, sumatoria_de_pesos, demanda, nnya, autor_dv, categoria_motivo, categoria_submotivo, gravedad_vulneracion, urgencia_vulneracion)

    def calculate_vulneracion_score(self, vulneracion):
        """Calculates and returns the score of a Vulneracion based on its properties."""
        return vulneracion.sumatoria_pesos

class TDecisionUseCase:
    def create_decision(self, fecha, hora, justificacion, decision, demanda):
        return Decision(fecha, hora, justificacion, decision, demanda)
    
    def make_decision(self, fecha, hora, decision, justificacion, demanda):
        """Creates a new Decision entity."""
        return Decision(fecha, hora, decision, justificacion, demanda)

class TDemandaAsignadoUseCase:
    def create_demanda_asignado(self, demanda, user, esta_activo=True, recibido=False, comentarios=None):
        return DemandaAsignado(demanda, user, esta_activo, recibido, comentarios)

class TActividadTipoUseCase:
    def create_actividad_tipo(self, nombre):
        return ActividadTipo(nombre)

class TInstitucionActividadUseCase:
    def create_institucion_actividad(self, nombre):
        return InstitucionActividad(nombre)

class TInstitucionRespuestaUseCase:
    def create_institucion_respuesta(self, nombre):
        return InstitucionRespuesta(nombre)


class TActividadUseCase:
    def create_actividad(self, fecha, hora, descripcion, demanda, ipo=None, institucion=None):
        return Actividad(fecha, hora, descripcion, demanda, ipo, institucion)

class TRespuestaUseCase:
    def create_respuesta(self, fecha, hora, mail, mensaje, demanda, institucion=None):
        return Respuesta(fecha, hora, mail, mensaje, demanda, institucion)

class TDemandaVinculadaUseCase:
    def create_demanda_vinculada(self, demanda_1, demanda_2):
        return DemandaVinculada(demanda_1, demanda_2)

class TLegajoUseCase:
    def create_legajo(self, info_legajo, nnya):
        return Legajo(info_legajo, nnya)

class TLegajoAsignadoUseCase:
    def create_legajo_asignado(self, legajo, user, esta_activo=True, recibido=False):
        return LegajoAsignado(legajo, user, esta_activo, recibido)

class TIndicadoresValoracionUseCase:
    def create_indicadores_valoracion(self, nombre, descripcion=None, peso=0):
        return IndicadoresValoracion(nombre, descripcion, peso)

class TEvaluacionesUseCase:
    def create_evaluaciones(self, demanda, indicador, si_no=False):
        return Evaluaciones(demanda, indicador, si_no)

class TVinculoUseCase:
    def create_vinculo(self, nombre):
        return Vinculo(nombre)

class TVinculoPersonaPersonaUseCase:
    def create_vinculo_persona_persona(self, conviven, vinculo, persona_1, persona_2):
        return VinculoPersonaPersona(conviven, vinculo, persona_1, persona_2)

class TVinculoPersonaNNyAUseCase:
    def create_vinculo_persona_nnya(self, conviven, autordv, garantiza_proteccion, vinculo, nnya, persona):
        return VinculoPersonaNNyA(conviven, autordv, garantiza_proteccion, vinculo, nnya, persona)

class TScoreUseCase:
    def create_score(self, demanda, nnya, score, score_vulneracion, score_evaluacion, score_condiciones_vulnerabilidad, score_motivo_intervencion):
        return Score(demanda, nnya, score, score_vulneracion, score_evaluacion, score_condiciones_vulnerabilidad, score_motivo_intervencion)

class TCondicionesVulnerabilidadUseCase:
    def create_condiciones_vulnerabilidad(self, nombre, descripcion, peso):
        return CondicionesVulnerabilidad(nombre, descripcion, peso)

class TNNyACondicionesVulnerabilidadUseCase:
    def create_nnya_condiciones_vulnerabilidad(self, nnya, condiciones_vulnerabilidad, si_no):
        return NNyACondicionesVulnerabilidad(nnya, condiciones_vulnerabilidad, si_no)

class TMotivoIntervencionUseCase:
    def create_motivo_intervencion(self, nombre, descripcion, peso):
        return MotivoIntervencion(nombre, descripcion, peso)

class TNNyAMotivoIntervencionUseCase:
    def create_nnya_motivo_intervencion(self, nnya, motivo_intervencion):
        return NNyAMotivoIntervencion(nnya, motivo_intervencion)
