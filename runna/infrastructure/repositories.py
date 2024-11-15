from infrastructure.models import (
    User, TProvincia, TDepartamento, TLocalidad, TBarrio, TCPC, TLocalizacion
    , TVinculoUsuarioLinea, TInstitucionUsuarioLinea, TCargo, TResponsable, TUsuarioLinea
    , TDemanda, TPrecalificacionDemanda, TPersona, TDemandaPersona, TInstitucionEducativa, TNNyAEducacion
    , TInstitucionSanitaria, TNNyA, TCategoriaMotivo, TCategoriaSubmotivo, TGravedadVulneracion, TUrgenciaVulneracion, TVulneracion
    , TInstitucionRespuesta, TRespuesta, TDemandaAsignado, TActividadTipo, TInstitucionActividad, TActividad
    , TDemandaVinculada, TLegajo, TLegajoAsignado, TIndicadoresValoracion, TEvaluaciones, TDecision
    , TVinculo, TVinculoPersonaPersona, TVinculoPersonaNNyA, TScore, TCondicionesVulnerabilidad
    , TNNyACondicionesVulnerabilidad, TMotivoIntervencion, TNNyAMotivoIntervencion
)
from core.entities import (
    CPC, Cargo, User, Departamento, InstitucionUsuarioLinea, Provincia, Localidad, Barrio, Localizacion, Responsable, UsuarioLinea, Demanda, PrecalificacionDemanda, Persona
    , DemandaPersona, NNyA, NNyAEducacion, InstitucionEducativa, InstitucionSanitaria, CategoriaMotivo, CategoriaSubmotivo
    , GravedadVulneracion, UrgenciaVulneracion, VinculoUsuarioLinea, Vulneracion, InstitucionRespuesta, Respuesta, DemandaAsignado, ActividadTipo
    , InstitucionActividad, Actividad, DemandaVinculada, Legajo, LegajoAsignado, IndicadoresValoracion, Evaluaciones, Decision
    , Vinculo, VinculoPersonaPersona, VinculoPersonaNNyA, Score, CondicionesVulnerabilidad, NNyACondicionesVulnerabilidad
    , MotivoIntervencion, NNyAMotivoIntervencion
)

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

class UserRepository:
    def create(self, user: User):
        User.objects.create(
            username=user.username,
            email=user.email,
            fecha_nacimiento=user.fecha_nacimiento,
            genero=user.genero,
            telefono=user.telefono,
        )

    def get_all(self):
        users = User.objects.all()
        return [User(u.username, u.email, u.fecha_nacimiento, u.genero, u.telefono) for u in users]

class TProvinciaRepository:
    def create(self, provincia: Provincia):
        TProvincia.objects.create(nombre=provincia.nombre)

    def get_all(self):
        provincias = TProvincia.objects.all()
        return [Provincia(p.nombre) for p in provincias]

class TLocalidadRepository:
    def create(self, localidad: Localidad):
        TLocalidad.objects.create(
            nombre=localidad.nombre,
            provincia=localidad.provincia,
            departamento=localidad.departamento,
        )

    def get_all(self):
        localidades = TLocalidad.objects.all()
        return [Localidad(l.nombre, l.provincia, l.departamento) for l in localidades]

class TBarrioRepository:
    def create(self, barrio: Barrio):
        TBarrio.objects.create(
            nombre=barrio.nombre,
            localidad=barrio.localidad,
        )

    def get_all(self):
        barrios = TBarrio.objects.all()
        return [Barrio(b.nombre, b.localidad) for b in barrios]

class TLocalizacionRepository:
    def create(self, localizacion: Localizacion):
        """Save a Localizacion entity to the database."""
        TLocalizacion.objects.create(
            calle=localizacion.calle,
            tipo_calle=localizacion.tipo_calle,
            piso_depto=localizacion.piso_depto,
            lote=localizacion.lote,
            mza=localizacion.mza,
            casa_nro=localizacion.casa_nro,
            referencia_geo=localizacion.referencia_geo,
            barrio=localizacion.barrio,
            localidad=localizacion.localidad,
            cpc=localizacion.cpc,
        )

    def get_all(self):
        """Retrieve all Localizacion entries from the database."""
        localizaciones = TLocalizacion.objects.all()
        return [Localizacion(l.calle, l.tipo_calle, l.piso_depto, l.lote, l.mza, l.casa_nro, l.referencia_geo, l.barrio, l.localidad, l.cpc) for l in localizaciones]

class TUsuarioLineaRepository:
    def create(self, usuario_linea: UsuarioLinea):
        """Save a UsuarioLinea entity to the database."""
        TUsuarioLinea.objects.create(
            nombre=usuario_linea.nombre,
            apellido=usuario_linea.apellido,
            fecha_nacimiento=usuario_linea.fecha_nacimiento,
            genero=usuario_linea.genero,
            telefono=usuario_linea.telefono,
            vinculo_usuario_linea=usuario_linea.vinculo_usuario_linea,
            institucion_usuario_linea=usuario_linea.institucion_usuario_linea,
            responsable=usuario_linea.responsable,
        )

    def get_all(self):
        """Retrieve all UsuarioLinea entries from the database."""
        usuarios_linea = TUsuarioLinea.objects.all()
        return [UsuarioLinea(u.nombre, u.apellido, u.fecha_nacimiento, u.genero, u.telefono, u.vinculo_usuario_linea, u.institucion_usuario_linea, u.responsable) for u in usuarios_linea]

class TDemandaRepository:
    def create(self, demanda: Demanda):
        """Save a Demanda entity to the database."""
        TDemanda.objects.create(
            fecha_ingreso=demanda.fecha_ingreso,
            hora_ingreso=demanda.hora_ingreso,
            origen=demanda.origen,
            nro_notificacion_102=demanda.nro_notificacion_102,
            nro_sac=demanda.nro_sac,
            nro_suac=demanda.nro_suac,
            nro_historia_clinica=demanda.nro_historia_clinica,
            nro_oficio_web=demanda.nro_oficio_web,
            descripcion=demanda.descripcion,
            ultima_actualizacion=demanda.ultima_actualizacion,
            localizacion=demanda.localizacion,
            usuario_linea=demanda.usuario_linea,
        )

    def get_all(self):
        """Retrieve all Demanda entries from the database."""
        demandas = TDemanda.objects.all()
        return [Demanda(d.fecha_ingreso, d.hora_ingreso, d.origen, d.localizacion, d.usuario_linea, d.ultima_actualizacion, d.nro_notificacion_102, d.nro_sac, d.nro_suac, d.nro_historia_clinica, d.nro_oficio_web, d.descripcion) for d in demandas]

class TPrecalificacionDemandaRepository:
    def create(self, precalificacion_demanda: PrecalificacionDemanda):
        TPrecalificacionDemanda.objects.create(
            fecha=precalificacion_demanda.fecha,
            hora=precalificacion_demanda.hora,
            descripcion=precalificacion_demanda.descripcion,
            estado_demanda=precalificacion_demanda.estado_demanda,
            demanda=precalificacion_demanda.demanda,
        )

    def get_all(self):
        precalificaciones = TPrecalificacionDemanda.objects.all()
        return [PrecalificacionDemanda(p.fecha, p.hora, p.descripcion, p.estado_demanda, p.demanda) for p in precalificaciones]

class TPersonaRepository:
    def create(self, persona: Persona):
        """Save a Persona entity to the database."""
        TPersona.objects.create(
            nombre=persona.nombre,
            apellido=persona.apellido,
            fecha_nacimiento=persona.fecha_nacimiento,
            edad_aproximada=persona.edad_aproximada,
            dni=persona.dni,
            situacion_dni=persona.situacion_dni,
            genero=persona.genero,
            boton_antipanico=persona.boton_antipanico,
            observaciones=persona.observaciones,
            adulto=persona.adulto,
            nnya=persona.nnya,
        )

    def get_all(self):
        """Retrieve all Persona entries from the database."""
        personas = TPersona.objects.all()
        return [Persona(p.nombre, p.apellido, p.fecha_nacimiento, p.edad_aproximada, p.dni, p.situacion_dni, p.genero, p.boton_antipanico, p.observaciones, p.adulto, p.nnya) for p in personas]

class TDemandaPersonaRepository:
    def create(self, demanda_persona: DemandaPersona):
        TDemandaPersona.objects.create(
            demanda=demanda_persona.demanda,
            persona=demanda_persona.persona,
            conviviente=demanda_persona.conviviente,
            supuesto_autordv=demanda_persona.supuesto_autordv,
            supuesto_autordv_principal=demanda_persona.supuesto_autordv_principal,
            nnya=demanda_persona.nnya,
            nnya_principal=demanda_persona.nnya_principal,
        )

    def get_all(self):
        demandas_personas = TDemandaPersona.objects.all()
        return [DemandaPersona(dp.demanda, dp.persona, dp.conviviente, dp.supuesto_autordv, dp.supuesto_autordv_principal, dp.nnya, dp.nnya_principal) for dp in demandas_personas]

class TNNyARepository:
    def create(self, nnya: NNyA):
        TNNyA.objects.create(
            persona=nnya.persona,
            educacion=nnya.educacion,
            institucion_sanitaria=nnya.institucion_sanitaria,
        )

    def get_all(self):
        nnyas = TNNyA.objects.all()
        return [NNyA(n.persona, n.educacion, n.institucion_sanitaria) for n in nnyas]

class TNNyAEducacionRepository:
    def create(self, nnya_educacion: NNyAEducacion):
        TNNyAEducacion.objects.create(
            curso=nnya_educacion.curso,
            nivel=nnya_educacion.nivel,
            turno=nnya_educacion.turno,
            comentarios=nnya_educacion.comentarios,
            institucion_educativa=nnya_educacion.institucion_educativa,
        )

    def get_all(self):
        nnyas_educacion = TNNyAEducacion.objects.all()
        return [NNyAEducacion(ne.curso, ne.nivel, ne.turno, ne.comentarios, ne.institucion_educativa) for ne in nnyas_educacion]

class TInstitucionEducativaRepository:
    def create(self, institucion_educativa: InstitucionEducativa):
        TInstitucionEducativa.objects.create(
            nombre=institucion_educativa.nombre,
            mail=institucion_educativa.mail,
            telefono=institucion_educativa.telefono,
        )

    def get_all(self):
        instituciones_educativas = TInstitucionEducativa.objects.all()
        return [InstitucionEducativa(ie.nombre, ie.mail, ie.telefono) for ie in instituciones_educativas]

class TInstitucionSanitariaRepository:
    def create(self, institucion_sanitaria: InstitucionSanitaria):
        TInstitucionSanitaria.objects.create(
            nombre=institucion_sanitaria.nombre,
            mail=institucion_sanitaria.mail,
            telefono=institucion_sanitaria.telefono,
        )

    def get_all(self):
        instituciones_sanitarias = TInstitucionSanitaria.objects.all()
        return [InstitucionSanitaria(isa.nombre, isa.mail, isa.telefono) for isa in instituciones_sanitarias]

class TVulneracionRepository:
    def create(self, vulneracion: Vulneracion):
        TVulneracion.objects.create(
            principal_demanda=vulneracion.principal_demanda,
            transcurre_actualidad=vulneracion.transcurre_actualidad,
            sumatoria_de_pesos=vulneracion.sumatoria_de_pesos,
            demanda=vulneracion.demanda,
            nnya=vulneracion.nnya,
            autor_dv=vulneracion.autor_dv,
            categoria_motivo=vulneracion.categoria_motivo,
            categoria_submotivo=vulneracion.categoria_submotivo,
            gravedad_vulneracion=vulneracion.gravedad_vulneracion,
            urgencia_vulneracion=vulneracion.urgencia_vulneracion,
        )

    def get_all(self):
        vulneraciones = TVulneracion.objects.all()
        return [Vulneracion(v.principal_demanda, v.transcurre_actualidad, v.sumatoria_de_pesos, v.demanda, v.nnya, v.autor_dv, v.categoria_motivo, v.categoria_submotivo, v.gravedad_vulneracion, v.urgencia_vulneracion) for v in vulneraciones]

class TGravedadVulneracionRepository:
    def create(self, gravedad_vulneracion: GravedadVulneracion):
        TGravedadVulneracion.objects.create(
            nombre=gravedad_vulneracion.nombre,
            descripcion=gravedad_vulneracion.descripcion,
            peso=gravedad_vulneracion.peso,
        )

    def get_all(self):
        gravedades_vulneracion = TGravedadVulneracion.objects.all()
        return [GravedadVulneracion(gv.nombre, gv.descripcion, gv.peso) for gv in gravedades_vulneracion]

class TUrgenciaVulneracionRepository:
    def create(self, urgencia_vulneracion: UrgenciaVulneracion):
        TUrgenciaVulneracion.objects.create(
            nombre=urgencia_vulneracion.nombre,
            descripcion=urgencia_vulneracion.descripcion,
            peso=urgencia_vulneracion.peso,
        )

    def get_all(self):
        urgencias_vulneracion = TUrgenciaVulneracion.objects.all()
        return [UrgenciaVulneracion(uv.nombre, uv.descripcion, uv.peso) for uv in urgencias_vulneracion]

class TDecisionRepository:
    def create(self, decision: Decision):
        TDecision.objects.create(
            fecha=decision.fecha,
            hora=decision.hora,
            justificacion=decision.justificacion,
            decision=decision.decision,
            demanda=decision.demanda,
        )

    def get_all(self):
        decisiones = TDecision.objects.all()
        return [Decision(d.fecha, d.hora, d.justificacion, d.decision, d.demanda) for d in decisiones]

class TInstitucionUsuarioLineaRepository:
    def create(self, institucion_usuario_linea: InstitucionUsuarioLinea):
        TInstitucionUsuarioLinea.objects.create(
            nombre=institucion_usuario_linea.nombre,
            contacto=institucion_usuario_linea.contacto,
        )

    def get_all(self):
        instituciones_usuario_linea = TInstitucionUsuarioLinea.objects.all()
        return [InstitucionUsuarioLinea(iul.nombre, iul.contacto) for iul in instituciones_usuario_linea]

class TVinculoUsuarioLineaRepository:
    def create(self, vinculo_usuario_linea: VinculoUsuarioLinea):
        TVinculoUsuarioLinea.objects.create(nombre=vinculo_usuario_linea.nombre)

    def get_all(self):
        vinculos_usuario_linea = TVinculoUsuarioLinea.objects.all()
        return [VinculoUsuarioLinea(vul.nombre) for vul in vinculos_usuario_linea]

class TCargoRepository:
    def create(self, cargo: Cargo):
        TCargo.objects.create(nombre=cargo.nombre)

    def get_all(self):
        cargos = TCargo.objects.all()
        return [Cargo(c.nombre) for c in cargos]

class TResponsableRepository:
    def create(self, responsable: Responsable):
        TResponsable.objects.create(
            nombre=responsable.nombre,
            apellido=responsable.apellido,
            cargo=responsable.cargo,
        )

    def get_all(self):
        responsables = TResponsable.objects.all()
        return [Responsable(r.nombre, r.apellido, r.cargo) for r in responsables]

class TDemandaAsignadoRepository:
    def create(self, demanda_asignado: DemandaAsignado):
        TDemandaAsignado.objects.create(
            demanda=demanda_asignado.demanda,
            user=demanda_asignado.user,
            esta_activo=demanda_asignado.esta_activo,
            recibido=demanda_asignado.recibido,
            comentarios=demanda_asignado.comentarios,
        )

    def get_all(self):
        demandas_asignadas = TDemandaAsignado.objects.all()
        return [DemandaAsignado(da.demanda, da.user, da.esta_activo, da.recibido, da.comentarios) for da in demandas_asignadas]

class TActividadTipoRepository:
    def create(self, actividad_tipo: ActividadTipo):
        TActividadTipo.objects.create(nombre=actividad_tipo.nombre)

    def get_all(self):
        actividades_tipo = TActividadTipo.objects.all()
        return [ActividadTipo(at.nombre) for at in actividades_tipo]

class TActividadRepository:
    def create(self, actividad: Actividad):
        TActividad.objects.create(
            fecha=actividad.fecha,
            hora=actividad.hora,
            descripcion=actividad.descripcion,
            demanda=actividad.demanda,
            tipo=actividad.tipo,
            institucion=actividad.institucion,
        )

    def get_all(self):
        actividades = TActividad.objects.all()
        return [Actividad(a.fecha, a.hora, a.descripcion, a.demanda, a.tipo, a.institucion) for a in actividades]

class TRespuestaRepository:
    def create(self, respuesta: Respuesta):
        TRespuesta.objects.create(
            fecha=respuesta.fecha,
            hora=respuesta.hora,
            mail=respuesta.mail,
            mensaje=respuesta.mensaje,
            demanda=respuesta.demanda,
            institucion=respuesta.institucion,
        )

    def get_all(self):
        respuestas = TRespuesta.objects.all()
        return [Respuesta(r.fecha, r.hora, r.mail, r.mensaje, r.demanda, r.institucion) for r in respuestas]

class TDemandaVinculadaRepository:
    def create(self, demanda_vinculada: DemandaVinculada):
        TDemandaVinculada.objects.create(
            demanda_1=demanda_vinculada.demanda_1,
            demanda_2=demanda_vinculada.demanda_2,
        )

    def get_all(self):
        demandas_vinculadas = TDemandaVinculada.objects.all()
        return [DemandaVinculada(dv.demanda_1, dv.demanda_2) for dv in demandas_vinculadas]

class TLegajoAsignadoRepository:
    def create(self, legajo_asignado: LegajoAsignado):
        TLegajoAsignado.objects.create(
            legajo=legajo_asignado.legajo,
            user=legajo_asignado.user,
            esta_activo=legajo_asignado.esta_activo,
            recibido=legajo_asignado.recibido,
        )

    def get_all(self):
        legajos_asignados = TLegajoAsignado.objects.all()
        return [LegajoAsignado(la.legajo, la.user, la.esta_activo, la.recibido) for la in legajos_asignados]

class TIndicadoresValoracionRepository:
    def create(self, indicador_valoracion: IndicadoresValoracion):
        TIndicadoresValoracion.objects.create(
            nombre=indicador_valoracion.nombre,
            descripcion=indicador_valoracion.descripcion,
            peso=indicador_valoracion.peso,
        )

    def get_all(self):
        indicadores_valoracion = TIndicadoresValoracion.objects.all()
        return [IndicadoresValoracion(iv.nombre, iv.descripcion, iv.peso) for iv in indicadores_valoracion]

class TEvaluacionesRepository:
    def create(self, evaluacion: Evaluaciones):
        TEvaluaciones.objects.create(
            demanda=evaluacion.demanda,
            indicador=evaluacion.indicador,
            si_no=evaluacion.si_no,
        )

    def get_all(self):
        evaluaciones = TEvaluaciones.objects.all()
        return [Evaluaciones(e.demanda, e.indicador, e.si_no) for e in evaluaciones]

class TCategoriaMotivoRepository:
    def create(self, categoria_motivo: CategoriaMotivo):
        TCategoriaMotivo.objects.create(
            nombre=categoria_motivo.nombre,
            descripcion=categoria_motivo.descripcion,
            peso=categoria_motivo.peso,
        )

    def get_all(self):
        categorias_motivo = TCategoriaMotivo.objects.all()
        return [CategoriaMotivo(cm.nombre, cm.descripcion, cm.peso) for cm in categorias_motivo]

class TCategoriaSubmotivoRepository:
    def create(self, categoria_submotivo: CategoriaSubmotivo):
        TCategoriaSubmotivo.objects.create(
            nombre=categoria_submotivo.nombre,
            descripcion=categoria_submotivo.descripcion,
            peso=categoria_submotivo.peso,
            motivo=categoria_submotivo.motivo,
        )

    def get_all(self):
        categorias_submotivo = TCategoriaSubmotivo.objects.all()
        return [CategoriaSubmotivo(cs.nombre, cs.descripcion, cs.peso, cs.motivo) for cs in categorias_submotivo]

class TLegajoRepository:
    def create(self, legajo: Legajo):
        TLegajo.objects.create(
            info_legajo=legajo.info_legajo,
            nnya=legajo.nnya,
        )

    def get_all(self):
        legajos = TLegajo.objects.all()
        return [Legajo(l.info_legajo, l.nnya) for l in legajos]

class TVinculoRepository:
    def create(self, vinculo: Vinculo):
        TVinculo.objects.create(nombre=vinculo.nombre)

    def get_all(self):
        vinculos = TVinculo.objects.all()
        return [Vinculo(v.nombre) for v in vinculos]

class TVinculoPersonaPersonaRepository:
    def create(self, vinculo_persona_persona: VinculoPersonaPersona):
        TVinculoPersonaPersona.objects.create(
            conviven=vinculo_persona_persona.conviven,
            vinculo=vinculo_persona_persona.vinculo,
            persona_1=vinculo_persona_persona.persona_1,
            persona_2=vinculo_persona_persona.persona_2,
        )

    def get_all(self):
        vinculos_persona_persona = TVinculoPersonaPersona.objects.all()
        return [VinculoPersonaPersona(vpp.conviven, vpp.vinculo, vpp.persona_1, vpp.persona_2) for vpp in vinculos_persona_persona]

class TVinculoPersonaNNyARepository:
    def create(self, vinculo_persona_nnya: VinculoPersonaNNyA):
        TVinculoPersonaNNyA.objects.create(
            conviven=vinculo_persona_nnya.conviven,
            autordv=vinculo_persona_nnya.autordv,
            garantiza_proteccion=vinculo_persona_nnya.garantiza_proteccion,
            vinculo=vinculo_persona_nnya.vinculo,
            nnya=vinculo_persona_nnya.nnya,
            persona=vinculo_persona_nnya.persona,
        )

    def get_all(self):
        vinculos_persona_nnya = TVinculoPersonaNNyA.objects.all()
        return [VinculoPersonaNNyA(vpn.conviven, vpn.autordv, vpn.garantiza_proteccion, vpn.vinculo, vpn.nnya, vpn.persona) for vpn in vinculos_persona_nnya]

class TInstitucionActividadRepository:
    def create(self, institucion_actividad: InstitucionActividad):
        TInstitucionActividad.objects.create(nombre=institucion_actividad.nombre)

    def get_all(self):
        instituciones_actividad = TInstitucionActividad.objects.all()
        return [InstitucionActividad(ia.nombre) for ia in instituciones_actividad]

class TInstitucionRespuestaRepository:
    def create(self, institucion_respuesta: InstitucionRespuesta):
        TInstitucionRespuesta.objects.create(nombre=institucion_respuesta.nombre)

    def get_all(self):
        instituciones_respuesta = TInstitucionRespuesta.objects.all()
        return [InstitucionRespuesta(ir.nombre) for ir in instituciones_respuesta]

class TScoreRepository:
    def create(self, score: Score):
        TScore.objects.create(
            demanda=score.demanda,
            nnya=score.nnya,
            score=score.score,
            score_vulneracion=score.score_vulneracion,
            score_evaluacion=score.score_evaluacion,
            score_condiciones_vulnerabilidad=score.score_condiciones_vulnerabilidad,
            score_motivo_intervencion=score.score_motivo_intervencion,
        )

    def get_all(self):
        scores = TScore.objects.all()
        return [Score(s.demanda, s.nnya, s.score, s.score_vulneracion, s.score_evaluacion, s.score_condiciones_vulnerabilidad, s.score_motivo_intervencion) for s in scores]

class TCondicionesVulnerabilidadRepository:
    def create(self, condiciones_vulnerabilidad: CondicionesVulnerabilidad):
        TCondicionesVulnerabilidad.objects.create(
            nombre=condiciones_vulnerabilidad.nombre,
            descripcion=condiciones_vulnerabilidad.descripcion,
            peso=condiciones_vulnerabilidad.peso,
        )

    def get_all(self):
        condiciones_vulnerabilidad = TCondicionesVulnerabilidad.objects.all()
        return [CondicionesVulnerabilidad(cv.nombre, cv.descripcion, cv.peso) for cv in condiciones_vulnerabilidad]

class TNNyACondicionesVulnerabilidadRepository:
    def create(self, nnya_condiciones_vulnerabilidad: NNyACondicionesVulnerabilidad):
        TNNyACondicionesVulnerabilidad.objects.create(
            nnya=nnya_condiciones_vulnerabilidad.nnya,
            condiciones_vulnerabilidad=nnya_condiciones_vulnerabilidad.condiciones_vulnerabilidad,
            si_no=nnya_condiciones_vulnerabilidad.si_no,
        )

    def get_all(self):
        nnya_condiciones_vulnerabilidad = TNNyACondicionesVulnerabilidad.objects.all()
        return [NNyACondicionesVulnerabilidad(ncv.nnya, ncv.condiciones_vulnerabilidad, ncv.si_no) for ncv in nnya_condiciones_vulnerabilidad]

class TMotivoIntervencionRepository:
    def create(self, motivo_intervencion: MotivoIntervencion):
        TMotivoIntervencion.objects.create(
            nombre=motivo_intervencion.nombre,
            descripcion=motivo_intervencion.descripcion,
            peso=motivo_intervencion.peso,
        )

    def get_all(self):
        motivos_intervencion = TMotivoIntervencion.objects.all()
        return [MotivoIntervencion(mi.nombre, mi.descripcion, mi.peso) for mi in motivos_intervencion]

class TNNyAMotivoIntervencionRepository:
    def create(self, nnya_motivo_intervencion: NNyAMotivoIntervencion):
        TNNyAMotivoIntervencion.objects.create(
            nnya=nnya_motivo_intervencion.nnya,
            motivo_intervencion=nnya_motivo_intervencion.motivo_intervencion,
        )

    def get_all(self):
        nnya_motivos_intervencion = TNNyAMotivoIntervencion.objects.all()
        return [NNyAMotivoIntervencion(nmi.nnya, nmi.motivo_intervencion) for nmi in nnya_motivos_intervencion]

class TCPCRepository:
    def create(self, cpc: CPC):
        TCPC.objects.create(nombre=cpc.nombre)

    def get_all(self):
        cpcs = TCPC.objects.all()
        return [CPC(c.nombre) for c in cpcs]

class TDepartamentoRepository:
    def create(self, departamento: Departamento):
        TDepartamento.objects.create(nombre=departamento.nombre)

    def get_all(self):
        departamentos = TDepartamento.objects.all()
        return [Departamento(d.nombre) for d in departamentos]