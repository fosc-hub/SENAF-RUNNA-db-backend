from django.shortcuts import render

# Create your views here.

'''
view example:

from rest_framework import status, viewsets
from rest_framework.response import Response

from core.use_cases import ProductUseCase
from api.serializers import ProductSerializer
from infrastructure.repositories import ProductRepository

class ProductViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_use_case = ProductUseCase()
        self.product_repo = ProductRepository()

    def list(self, request):
        """List all products."""
        products = self.product_repo.get_all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new product."""
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = self.product_use_case.create_product(**serializer.validated_data)
            self.product_repo.create(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
'''

from rest_framework import status, viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from core.use_cases import (
    CustomUserUseCase, TProvinciaUseCase, TDepartamentoUseCase, TLocalidadUseCase, TBarrioUseCase, TCPCUseCase, TLocalizacionUseCase
    , TVinculoUsuarioLineaUseCase, TInstitucionUsuarioLineaUseCase, TCargoUseCase, TResponsableUseCase, TUsuarioLineaUseCase
    , TDemandaUseCase, TPrecalificacionDemandaUseCase, TPersonaUseCase, TDemandaPersonaUseCase, TInstitucionEducativaUseCase, TNNyAEducacionUseCase
    , TInstitucionSanitariaUseCase, TNNyAUseCase, TCategoriaMotivoUseCase, TCategoriaSubmotivoUseCase, TGravedadVulneracionUseCase, TUrgenciaVulneracionUseCase, TVulneracionUseCase
    , TInstitucionRespuestaUseCase, TRespuestaUseCase, TDemandaAsignadoUseCase, TActividadTipoUseCase, TInstitucionActividadUseCase, TActividadUseCase
    , TDemandaVinculadaUseCase, TLegajoUseCase, TLegajoAsignadoUseCase, TIndicadoresValoracionUseCase, TEvaluacionesUseCase, TDecisionUseCase
    , TVinculoUseCase, TVinculoPersonaPersonaUseCase, TVinculoPersonaNNyAUseCase, TScoreUseCase, TCondicionesVulnerabilidadUseCase
    , TNNyACondicionesVulnerabilidadUseCase, TMotivoIntervencionUseCase, TNNyAMotivoIntervencionUseCase
)

from api.serializers import (
    CustomUserSerializer, TProvinciaSerializer, TDepartamentoSerializer, TLocalidadSerializer, TBarrioSerializer, TCPCSerializer, TLocalizacionSerializer
    , TVinculoUsuarioLineaSerializer, TInstitucionUsuarioLineaSerializer, TCargoSerializer, TResponsableSerializer, TUsuarioLineaSerializer
    , TDemandaSerializer, TPrecalificacionDemandaSerializer, TPersonaSerializer, TDemandaPersonaSerializer, TInstitucionEducativaSerializer, TNNyAEducacionSerializer
    , TInstitucionSanitariaSerializer, TNNyASerializer, TCategoriaMotivoSerializer, TCategoriaSubmotivoSerializer, TGravedadVulneracionSerializer, TUrgenciaVulneracionSerializer, TVulneracionSerializer
    , TInstitucionRespuestaSerializer, TRespuestaSerializer, TDemandaAsignadoSerializer, TActividadTipoSerializer, TInstitucionActividadSerializer, TActividadSerializer
    , TDemandaVinculadaSerializer, TLegajoSerializer, TLegajoAsignadoSerializer, TIndicadoresValoracionSerializer, TEvaluacionesSerializer, TDecisionSerializer
    , TVinculoSerializer, TVinculoPersonaPersonaSerializer, TVinculoPersonaNNyASerializer, TScoreSerializer, TCondicionesVulnerabilidadSerializer
    , TNNyACondicionesVulnerabilidadSerializer, TMotivoIntervencionSerializer, TNNyAMotivoIntervencionSerializer
)

from infrastructure.repositories import (
    CustomUserRepository, TProvinciaRepository, TDepartamentoRepository, TLocalidadRepository, TBarrioRepository, TCPCRepository, TLocalizacionRepository
    , TVinculoUsuarioLineaRepository, TInstitucionUsuarioLineaRepository, TCargoRepository, TResponsableRepository, TUsuarioLineaRepository
    , TDemandaRepository, TPrecalificacionDemandaRepository, TPersonaRepository, TDemandaPersonaRepository, TInstitucionEducativaRepository, TNNyAEducacionRepository
    , TInstitucionSanitariaRepository, TNNyARepository, TCategoriaMotivoRepository, TCategoriaSubmotivoRepository, TGravedadVulneracionRepository, TUrgenciaVulneracionRepository, TVulneracionRepository
    , TInstitucionRespuestaRepository, TRespuestaRepository, TDemandaAsignadoRepository, TActividadTipoRepository, TInstitucionActividadRepository, TActividadRepository
    , TDemandaVinculadaRepository, TLegajoRepository, TLegajoAsignadoRepository, TIndicadoresValoracionRepository, TEvaluacionesRepository, TDecisionRepository
    , TVinculoRepository, TVinculoPersonaPersonaRepository, TVinculoPersonaNNyARepository, TScoreRepository, TCondicionesVulnerabilidadRepository
    , TNNyACondicionesVulnerabilidadRepository, TMotivoIntervencionRepository, TNNyAMotivoIntervencionRepository
)

class CustomUserViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.custom_user_use_case = CustomUserUseCase()
        self.custom_user_repo = CustomUserRepository()

    @extend_schema(
        responses=CustomUserSerializer(many=True),
        description="Retrieve a list of all CustomUser entries."
    )
    def list(self, request):
        """List all CustomUser."""
        custom_users = self.custom_user_repo.get_all()
        serializer = CustomUserSerializer(custom_users, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=CustomUserSerializer,
        responses=CustomUserSerializer,
        description="Create a new CustomUser entry."
    )
    def create(self, request):
        """Create a new CustomUser."""
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            custom_user = self.custom_user_use_case.create_custom_user(**serializer.validated_data)
            self.custom_user_repo.create(custom_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TProvinciaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tprovincia_use_case = TProvinciaUseCase()
        self.tprovincia_repo = TProvinciaRepository()

    @extend_schema(
        responses=TProvinciaSerializer(many=True),
        description="Retrieve a list of all TProvincia entries."
    )
    def list(self, request):
        """List all TProvincia."""
        tprovincias = self.tprovincia_repo.get_all()
        serializer = TProvinciaSerializer(tprovincias, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TProvinciaSerializer,
        responses=TProvinciaSerializer,
        description="Create a new TProvincia entry."
    )
    def create(self, request):
        """Create a new TProvincia."""
        serializer = TProvinciaSerializer(data=request.data)
        if serializer.is_valid():
            tprovincia = self.tprovincia_use_case.create_provincia(**serializer.validated_data)
            self.tprovincia_repo.create(tprovincia)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TDepartamentoViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tdepartamento_use_case = TDepartamentoUseCase()
        self.tdepartamento_repo = TDepartamentoRepository()

    @extend_schema(
        responses=TDepartamentoSerializer(many=True),
        description="Retrieve a list of all TDepartamento entries."
    )
    def list(self, request):
        """List all TDepartamento."""
        tdepartamentos = self.tdepartamento_repo.get_all()
        serializer = TDepartamentoSerializer(tdepartamentos, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TDepartamentoSerializer,
        responses=TDepartamentoSerializer,
        description="Create a new TDepartamento entry."
    )
    def create(self, request):
        """Create a new TDepartamento."""
        serializer = TDepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            tdepartamento = self.tdepartamento_use_case.create_departamento(**serializer.validated_data)
            self.tdepartamento_repo.create(tdepartamento)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TLocalidadViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tlocalidad_use_case = TLocalidadUseCase()
        self.tlocalidad_repo = TLocalidadRepository()

    @extend_schema(
        responses=TLocalidadSerializer(many=True),
        description="Retrieve a list of all TLocalidad entries."
    )
    def list(self, request):
        """List all TLocalidad."""
        tlocalidades = self.tlocalidad_repo.get_all()
        serializer = TLocalidadSerializer(tlocalidades, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TLocalidadSerializer,
        responses=TLocalidadSerializer,
        description="Create a new TLocalidad entry."
    )
    def create(self, request):
        """Create a new TLocalidad."""
        serializer = TLocalidadSerializer(data=request.data)
        if serializer.is_valid():
            tlocalidad = self.tlocalidad_use_case.create_localidad(**serializer.validated_data)
            self.tlocalidad_repo.create(tlocalidad)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TBarrioViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tbarrio_use_case = TBarrioUseCase()
        self.tbarrio_repo = TBarrioRepository()

    @extend_schema(
        responses=TBarrioSerializer(many=True),
        description="Retrieve a list of all TBarrio entries."
    )
    def list(self, request):
        """List all TBarrio."""
        tbarrios = self.tbarrio_repo.get_all()
        serializer = TBarrioSerializer(tbarrios, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TBarrioSerializer,
        responses=TBarrioSerializer,
        description="Create a new TBarrio entry."
    )
    def create(self, request):
        """Create a new TBarrio."""
        serializer = TBarrioSerializer(data=request.data)
        if serializer.is_valid():
            tbarrio = self.tbarrio_use_case.create_barrio(**serializer.validated_data)
            self.tbarrio_repo.create(tbarrio)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TCPCViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tcpc_use_case = TCPCUseCase()
        self.tcpc_repo = TCPCRepository()

    @extend_schema(
        responses=TCPCSerializer(many=True),
        description="Retrieve a list of all TCPC entries."
    )
    def list(self, request):
        """List all TCPC."""
        tcpcs = self.tcpc_repo.get_all()
        serializer = TCPCSerializer(tcpcs, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TCPCSerializer,
        responses=TCPCSerializer,
        description="Create a new TCPC entry."
    )
    def create(self, request):
        """Create a new TCPC."""
        serializer = TCPCSerializer(data=request.data)
        if serializer.is_valid():
            tcpc = self.tcpc_use_case.create_cpc(**serializer.validated_data)
            self.tcpc_repo.create(tcpc)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TLocalizacionViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tlocalizacion_use_case = TLocalizacionUseCase()
        self.tlocalizacion_repo = TLocalizacionRepository()

    @extend_schema(
        responses=TLocalizacionSerializer(many=True),
        description="Retrieve a list of all TLocalizacion entries."
    )
    def list(self, request):
        """List all TLocalizacion."""
        tlocalizaciones = self.tlocalizacion_repo.get_all()
        serializer = TLocalizacionSerializer(tlocalizaciones, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TLocalizacionSerializer,
        responses=TLocalizacionSerializer,
        description="Create a new TLocalizacion entry."
    )
    def create(self, request):
        """Create a new TLocalizacion."""
        serializer = TLocalizacionSerializer(data=request.data)
        if serializer.is_valid():
            tlocalizacion = self.tlocalizacion_use_case.create_localizacion(**serializer.validated_data)
            self.tlocalizacion_repo.create(tlocalizacion)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TVinculoUsuarioLineaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tvinculo_usuario_linea_use_case = TVinculoUsuarioLineaUseCase()
        self.tvinculo_usuario_linea_repo = TVinculoUsuarioLineaRepository()

    @extend_schema(
        responses=TVinculoUsuarioLineaSerializer(many=True),
        description="Retrieve a list of all TVinculoUsuarioLinea entries."
    )
    def list(self, request):
        """List all TVinculoUsuarioLinea."""
        tvinculo_usuario_lineas = self.tvinculo_usuario_linea_repo.get_all()
        serializer = TVinculoUsuarioLineaSerializer(tvinculo_usuario_lineas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TVinculoUsuarioLineaSerializer,
        responses=TVinculoUsuarioLineaSerializer,
        description="Create a new TVinculoUsuarioLinea entry."
    )
    def create(self, request):
        """Create a new TVinculoUsuarioLinea."""
        serializer = TVinculoUsuarioLineaSerializer(data=request.data)
        if serializer.is_valid():
            tvinculo_usuario_linea = self.tvinculo_usuario_linea_use_case.create_vinculo_usuario_linea(**serializer.validated_data)
            self.tvinculo_usuario_linea_repo.create(tvinculo_usuario_linea)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TInstitucionUsuarioLineaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tinstitucion_usuario_linea_use_case = TInstitucionUsuarioLineaUseCase()
        self.tinstitucion_usuario_linea_repo = TInstitucionUsuarioLineaRepository()

    @extend_schema(
        responses=TInstitucionUsuarioLineaSerializer(many=True),
        description="Retrieve a list of all TInstitucionUsuarioLinea entries."
    )
    def list(self, request):
        """List all TInstitucionUsuarioLinea."""
        tinstitucion_usuario_lineas = self.tinstitucion_usuario_linea_repo.get_all()
        serializer = TInstitucionUsuarioLineaSerializer(tinstitucion_usuario_lineas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TInstitucionUsuarioLineaSerializer,
        responses=TInstitucionUsuarioLineaSerializer,
        description="Create a new TInstitucionUsuarioLinea entry."
    )
    def create(self, request):
        """Create a new TInstitucionUsuarioLinea."""
        serializer = TInstitucionUsuarioLineaSerializer(data=request.data)
        if serializer.is_valid():
            tinstitucion_usuario_linea = self.tinstitucion_usuario_linea_use_case.create_institucion_usuario_linea(**serializer.validated_data)
            self.tinstitucion_usuario_linea_repo.create(tinstitucion_usuario_linea)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TCargoViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tcargo_use_case = TCargoUseCase()
        self.tcargo_repo = TCargoRepository()

    @extend_schema(
        responses=TCargoSerializer(many=True),
        description="Retrieve a list of all TCargo entries."
    )
    def list(self, request):
        """List all TCargo."""
        tcargos = self.tcargo_repo.get_all()
        serializer = TCargoSerializer(tcargos, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TCargoSerializer,
        responses=TCargoSerializer,
        description="Create a new TCargo entry."
    )
    def create(self, request):
        """Create a new TCargo."""
        serializer = TCargoSerializer(data=request.data)
        if serializer.is_valid():
            tcargo = self.tcargo_use_case.create_cargo(**serializer.validated_data)
            self.tcargo_repo.create(tcargo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TResponsableViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tresponsable_use_case = TResponsableUseCase()
        self.tresponsable_repo = TResponsableRepository()

    @extend_schema(
        responses=TResponsableSerializer(many=True),
        description="Retrieve a list of all TResponsable entries."
    )
    def list(self, request):
        """List all TResponsable."""
        tresponsables = self.tresponsable_repo.get_all()
        serializer = TResponsableSerializer(tresponsables, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TResponsableSerializer,
        responses=TResponsableSerializer,
        description="Create a new TResponsable entry."
    )
    def create(self, request):
        """Create a new TResponsable."""
        serializer = TResponsableSerializer(data=request.data)
        if serializer.is_valid():
            tresponsable = self.tresponsable_use_case.create_responsable(**serializer.validated_data)
            self.tresponsable_repo.create(tresponsable)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TUsuarioLineaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tusuario_linea_use_case = TUsuarioLineaUseCase()
        self.tusuario_linea_repo = TUsuarioLineaRepository()

    @extend_schema(
        responses=TUsuarioLineaSerializer(many=True),
        description="Retrieve a list of all TUsuarioLinea entries."
    )
    def list(self, request):
        """List all TUsuarioLinea."""
        tusuario_lineas = self.tusuario_linea_repo.get_all()
        serializer = TUsuarioLineaSerializer(tusuario_lineas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TUsuarioLineaSerializer,
        responses=TUsuarioLineaSerializer,
        description="Create a new TUsuarioLinea entry."
    )
    def create(self, request):
        """Create a new TUsuarioLinea."""
        serializer = TUsuarioLineaSerializer(data=request.data)
        if serializer.is_valid():
            tusuario_linea = self.tusuario_linea_use_case.create_usuario_linea(**serializer.validated_data)
            self.tusuario_linea_repo.create(tusuario_linea)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TDemandaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tdemanda_use_case = TDemandaUseCase()
        self.tdemanda_repo = TDemandaRepository()

    @extend_schema(
        responses=TDemandaSerializer(many=True),
        description="Retrieve a list of all TDemanda entries."
    )
    def list(self, request):
        """List all TDemanda."""
        tdemandas = self.tdemanda_repo.get_all()
        serializer = TDemandaSerializer(tdemandas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TDemandaSerializer,
        responses=TDemandaSerializer,
        description="Create a new TDemanda entry."
    )
    def create(self, request):
        """Create a new TDemanda."""
        serializer = TDemandaSerializer(data=request.data)
        if serializer.is_valid():
            tdemanda = self.tdemanda_use_case.create_demanda(**serializer.validated_data)
            self.tdemanda_repo.create(tdemanda)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TPrecalificacionDemandaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tprecalificacion_demanda_use_case = TPrecalificacionDemandaUseCase()
        self.tprecalificacion_demanda_repo = TPrecalificacionDemandaRepository()

    @extend_schema(
        responses=TPrecalificacionDemandaSerializer(many=True),
        description="Retrieve a list of all TPrecalificacionDemanda entries."
    )
    def list(self, request):
        """List all TPrecalificacionDemanda."""
        tprecalificacion_demandas = self.tprecalificacion_demanda_repo.get_all()
        serializer = TPrecalificacionDemandaSerializer(tprecalificacion_demandas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TPrecalificacionDemandaSerializer,
        responses=TPrecalificacionDemandaSerializer,
        description="Create a new TPrecalificacionDemanda entry."
    )
    def create(self, request):
        """Create a new TPrecalificacionDemanda."""
        serializer = TPrecalificacionDemandaSerializer(data=request.data)
        if serializer.is_valid():
            tprecalificacion_demanda = self.tprecalificacion_demanda_use_case.create_precalificacion_demanda(**serializer.validated_data)
            self.tprecalificacion_demanda_repo.create(tprecalificacion_demanda)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TPersonaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tpersona_use_case = TPersonaUseCase()
        self.tpersona_repo = TPersonaRepository()

    @extend_schema(
        responses=TPersonaSerializer(many=True),
        description="Retrieve a list of all TPersona entries."
    )
    def list(self, request):
        """List all TPersona."""
        tpersonas = self.tpersona_repo.get_all()
        serializer = TPersonaSerializer(tpersonas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TPersonaSerializer,
        responses=TPersonaSerializer,
        description="Create a new TPersona entry."
    )
    def create(self, request):
        """Create a new TPersona."""
        serializer = TPersonaSerializer(data=request.data)
        if serializer.is_valid():
            tpersona = self.tpersona_use_case.create_persona(**serializer.validated_data)
            self.tpersona_repo.create(tpersona)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TDemandaPersonaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tdemanda_persona_use_case = TDemandaPersonaUseCase()
        self.tdemanda_persona_repo = TDemandaPersonaRepository()

    @extend_schema(
        responses=TDemandaPersonaSerializer(many=True),
        description="Retrieve a list of all TDemandaPersona entries."
    )
    def list(self, request):
        """List all TDemandaPersona."""
        tdemanda_personas = self.tdemanda_persona_repo.get_all()
        serializer = TDemandaPersonaSerializer(tdemanda_personas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TDemandaPersonaSerializer,
        responses=TDemandaPersonaSerializer,
        description="Create a new TDemandaPersona entry."
    )
    def create(self, request):
        """Create a new TDemandaPersona."""
        serializer = TDemandaPersonaSerializer(data=request.data)
        if serializer.is_valid():
            tdemanda_persona = self.tdemanda_persona_use_case.create_demanda_persona(**serializer.validated_data)
            self.tdemanda_persona_repo.create(tdemanda_persona)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TInstitucionEducativaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tinstitucion_educativa_use_case = TInstitucionEducativaUseCase()
        self.tinstitucion_educativa_repo = TInstitucionEducativaRepository()

    @extend_schema(
        responses=TInstitucionEducativaSerializer(many=True),
        description="Retrieve a list of all TInstitucionEducativa entries."
    )
    def list(self, request):
        """List all TInstitucionEducativa."""
        tinstitucion_educativas = self.tinstitucion_educativa_repo.get_all()
        serializer = TInstitucionEducativaSerializer(tinstitucion_educativas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TInstitucionEducativaSerializer,
        responses=TInstitucionEducativaSerializer,
        description="Create a new TInstitucionEducativa entry."
    )
    def create(self, request):
        """Create a new TInstitucionEducativa."""
        serializer = TInstitucionEducativaSerializer(data=request.data)
        if serializer.is_valid():
            tinstitucion_educativa = self.tinstitucion_educativa_use_case.create_institucion_educativa(**serializer.validated_data)
            self.tinstitucion_educativa_repo.create(tinstitucion_educativa)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TNNyAEducacionViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tnnya_educacion_use_case = TNNyAEducacionUseCase()
        self.tnnya_educacion_repo = TNNyAEducacionRepository()

    @extend_schema(
        responses=TNNyAEducacionSerializer(many=True),
        description="Retrieve a list of all TNNyAEducacion entries."
    )
    def list(self, request):
        """List all TNNyAEducacion."""
        tnnya_educaciones = self.tnnya_educacion_repo.get_all()
        serializer = TNNyAEducacionSerializer(tnnya_educaciones, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TNNyAEducacionSerializer,
        responses=TNNyAEducacionSerializer,
        description="Create a new TNNyAEducacion entry."
    )
    def create(self, request):
        """Create a new TNNyAEducacion."""
        serializer = TNNyAEducacionSerializer(data=request.data)
        if serializer.is_valid():
            tnnya_educacion = self.tnnya_educacion_use_case.create_nnya_educacion(**serializer.validated_data)
            self.tnnya_educacion_repo.create(tnnya_educacion)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TInstitucionSanitariaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tinstitucion_sanitaria_use_case = TInstitucionSanitariaUseCase()
        self.tinstitucion_sanitaria_repo = TInstitucionSanitariaRepository()

    @extend_schema(
        responses=TInstitucionSanitariaSerializer(many=True),
        description="Retrieve a list of all TInstitucionSanitaria entries."
    )
    def list(self, request):
        """List all TInstitucionSanitaria."""
        tinstitucion_sanitarias = self.tinstitucion_sanitaria_repo.get_all()
        serializer = TInstitucionSanitariaSerializer(tinstitucion_sanitarias, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TInstitucionSanitariaSerializer,
        responses=TInstitucionSanitariaSerializer,
        description="Create a new TInstitucionSanitaria entry."
    )
    def create(self, request):
        """Create a new TInstitucionSanitaria."""
        serializer = TInstitucionSanitariaSerializer(data=request.data)
        if serializer.is_valid():
            tinstitucion_sanitaria = self.tinstitucion_sanitaria_use_case.create_institucion_sanitaria(**serializer.validated_data)
            self.tinstitucion_sanitaria_repo.create(tinstitucion_sanitaria)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TNNyAViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tnnya_use_case = TNNyAUseCase()
        self.tnnya_repo = TNNyARepository()

    @extend_schema(
        responses=TNNyASerializer(many=True),
        description="Retrieve a list of all TNNyA entries."
    )
    def list(self, request):
        """List all TNNyA."""
        tnnyas = self.tnnya_repo.get_all()
        serializer = TNNyASerializer(tnnyas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TNNyASerializer,
        responses=TNNyASerializer,
        description="Create a new TNNyA entry."
    )
    def create(self, request):
        """Create a new TNNyA."""
        serializer = TNNyASerializer(data=request.data)
        if serializer.is_valid():
            tnnya = self.tnnya_use_case.create_nnya(**serializer.validated_data)
            self.tnnya_repo.create(tnnya)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TCategoriaMotivoViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tcategoria_motivo_use_case = TCategoriaMotivoUseCase()
        self.tcategoria_motivo_repo = TCategoriaMotivoRepository()

    @extend_schema(
        responses=TCategoriaMotivoSerializer(many=True),
        description="Retrieve a list of all TCategoriaMotivo entries."
    )
    def list(self, request):
        """List all TCategoriaMotivo."""
        tcategoria_motivos = self.tcategoria_motivo_repo.get_all()
        serializer = TCategoriaMotivoSerializer(tcategoria_motivos, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TCategoriaMotivoSerializer,
        responses=TCategoriaMotivoSerializer,
        description="Create a new TCategoriaMotivo entry."
    )
    def create(self, request):
        """Create a new TCategoriaMotivo."""
        serializer = TCategoriaMotivoSerializer(data=request.data)
        if serializer.is_valid():
            tcategoria_motivo = self.tcategoria_motivo_use_case.create_categoria_motivo(**serializer.validated_data)
            self.tcategoria_motivo_repo.create(tcategoria_motivo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TCategoriaSubmotivoViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tcategoria_submotivo_use_case = TCategoriaSubmotivoUseCase()
        self.tcategoria_submotivo_repo = TCategoriaSubmotivoRepository()

    @extend_schema(
        responses=TCategoriaSubmotivoSerializer(many=True),
        description="Retrieve a list of all TCategoriaSubmotivo entries."
    )
    def list(self, request):
        """List all TCategoriaSubmotivo."""
        tcategoria_submotivos = self.tcategoria_submotivo_repo.get_all()
        serializer = TCategoriaSubmotivoSerializer(tcategoria_submotivos, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TCategoriaSubmotivoSerializer,
        responses=TCategoriaSubmotivoSerializer,
        description="Create a new TCategoriaSubmotivo entry."
    )
    def create(self, request):
        """Create a new TCategoriaSubmotivo."""
        serializer = TCategoriaSubmotivoSerializer(data=request.data)
        if serializer.is_valid():
            tcategoria_submotivo = self.tcategoria_submotivo_use_case.create_categoria_submotivo(**serializer.validated_data)
            self.tcategoria_submotivo_repo.create(tcategoria_submotivo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TGravedadVulneracionViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tgravedad_vulneracion_use_case = TGravedadVulneracionUseCase()
        self.tgravedad_vulneracion_repo = TGravedadVulneracionRepository()

    @extend_schema(
        responses=TGravedadVulneracionSerializer(many=True),
        description="Retrieve a list of all TGravedadVulneracion entries."
    )
    def list(self, request):
        """List all TGravedadVulneracion."""
        tgravedad_vulneraciones = self.tgravedad_vulneracion_repo.get_all()
        serializer = TGravedadVulneracionSerializer(tgravedad_vulneraciones, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TGravedadVulneracionSerializer,
        responses=TGravedadVulneracionSerializer,
        description="Create a new TGravedadVulneracion entry."
    )
    def create(self, request):
        """Create a new TGravedadVulneracion."""
        serializer = TGravedadVulneracionSerializer(data=request.data)
        if serializer.is_valid():
            tgravedad_vulneracion = self.tgravedad_vulneracion_use_case.create_gravedad_vulneracion(**serializer.validated_data)
            self.tgravedad_vulneracion_repo.create(tgravedad_vulneracion)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TUrgenciaVulneracionViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.turgencia_vulneracion_use_case = TUrgenciaVulneracionUseCase()
        self.turgencia_vulneracion_repo = TUrgenciaVulneracionRepository()

    @extend_schema(
        responses=TUrgenciaVulneracionSerializer(many=True),
        description="Retrieve a list of all TUrgenciaVulneracion entries."
    )
    def list(self, request):
        """List all TUrgenciaVulneracion."""
        turgencia_vulneraciones = self.turgencia_vulneracion_repo.get_all()
        serializer = TUrgenciaVulneracionSerializer(turgencia_vulneraciones, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TUrgenciaVulneracionSerializer,
        responses=TUrgenciaVulneracionSerializer,
        description="Create a new TUrgenciaVulneracion entry."
    )
    def create(self, request):
        """Create a new TUrgenciaVulneracion."""
        serializer = TUrgenciaVulneracionSerializer(data=request.data)
        if serializer.is_valid():
            turgencia_vulneracion = self.turgencia_vulneracion_use_case.create_urgencia_vulneracion(**serializer.validated_data)
            self.turgencia_vulneracion_repo.create(turgencia_vulneracion)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TVulneracionViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tvulneracion_use_case = TVulneracionUseCase()
        self.tvulneracion_repo = TVulneracionRepository()

    @extend_schema(
        responses=TVulneracionSerializer(many=True),
        description="Retrieve a list of all TVulneracion entries."
    )
    def list(self, request):
        """List all TVulneracion."""
        tvulneraciones = self.tvulneracion_repo.get_all()
        serializer = TVulneracionSerializer(tvulneraciones, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TVulneracionSerializer,
        responses=TVulneracionSerializer,
        description="Create a new TVulneracion entry."
    )
    def create(self, request):
        """Create a new TVulneracion."""
        serializer = TVulneracionSerializer(data=request.data)
        if serializer.is_valid():
            tvulneracion = self.tvulneracion_use_case.create_vulneracion(**serializer.validated_data)
            self.tvulneracion_repo.create(tvulneracion)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TInstitucionRespuestaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tinstitucion_respuesta_use_case = TInstitucionRespuestaUseCase()
        self.tinstitucion_respuesta_repo = TInstitucionRespuestaRepository()

    @extend_schema(
        responses=TInstitucionRespuestaSerializer(many=True),
        description="Retrieve a list of all TInstitucionRespuesta entries."
    )
    def list(self, request):
        """List all TInstitucionRespuesta."""
        tinstitucion_respuestas = self.tinstitucion_respuesta_repo.get_all()
        serializer = TInstitucionRespuestaSerializer(tinstitucion_respuestas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TInstitucionRespuestaSerializer,
        responses=TInstitucionRespuestaSerializer,
        description="Create a new TInstitucionRespuesta entry."
    )
    def create(self, request):
        """Create a new TInstitucionRespuesta."""
        serializer = TInstitucionRespuestaSerializer(data=request.data)
        if serializer.is_valid():
            tinstitucion_respuesta = self.tinstitucion_respuesta_use_case.create_institucion_respuesta(**serializer.validated_data)
            self.tinstitucion_respuesta_repo.create(tinstitucion_respuesta)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TRespuestaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.trespuesta_use_case = TRespuestaUseCase()
        self.trespuesta_repo = TRespuestaRepository()

    @extend_schema(
        responses=TRespuestaSerializer(many=True),
        description="Retrieve a list of all TRespuesta entries."
    )
    def list(self, request):
        """List all TRespuesta."""
        trespuestas = self.trespuesta_repo.get_all()
        serializer = TRespuestaSerializer(trespuestas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TRespuestaSerializer,
        responses=TRespuestaSerializer,
        description="Create a new TRespuesta entry."
    )
    def create(self, request):
        """Create a new TRespuesta."""
        serializer = TRespuestaSerializer(data=request.data)
        if serializer.is_valid():
            trespuesta = self.trespuesta_use_case.create_respuesta(**serializer.validated_data)
            self.trespuesta_repo.create(trespuesta)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TDemandaAsignadoViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tdemanda_asignado_use_case = TDemandaAsignadoUseCase()
        self.tdemanda_asignado_repo = TDemandaAsignadoRepository()

    @extend_schema(
        responses=TDemandaAsignadoSerializer(many=True),
        description="Retrieve a list of all TDemandaAsignado entries."
    )
    def list(self, request):
        """List all TDemandaAsignado."""
        tdemanda_asignados = self.tdemanda_asignado_repo.get_all()
        serializer = TDemandaAsignadoSerializer(tdemanda_asignados, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TDemandaAsignadoSerializer,
        responses=TDemandaAsignadoSerializer,
        description="Create a new TDemandaAsignado entry."
    )
    def create(self, request):
        """Create a new TDemandaAsignado."""
        serializer = TDemandaAsignadoSerializer(data=request.data)
        if serializer.is_valid():
            tdemanda_asignado = self.tdemanda_asignado_use_case.create_demanda_asignado(**serializer.validated_data)
            self.tdemanda_asignado_repo.create(tdemanda_asignado)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TActividadTipoViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tactividad_tipo_use_case = TActividadTipoUseCase()
        self.tactividad_tipo_repo = TActividadTipoRepository()

    @extend_schema(
        responses=TActividadTipoSerializer(many=True),
        description="Retrieve a list of all TActividadTipo entries."
    )
    def list(self, request):
        """List all TActividadTipo."""
        tactividad_tipos = self.tactividad_tipo_repo.get_all()
        serializer = TActividadTipoSerializer(tactividad_tipos, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TActividadTipoSerializer,
        responses=TActividadTipoSerializer,
        description="Create a new TActividadTipo entry."
    )
    def create(self, request):
        """Create a new TActividadTipo."""
        serializer = TActividadTipoSerializer(data=request.data)
        if serializer.is_valid():
            tactividad_tipo = self.tactividad_tipo_use_case.create_actividad_tipo(**serializer.validated_data)
            self.tactividad_tipo_repo.create(tactividad_tipo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TInstitucionActividadViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tinstitucion_actividad_use_case = TInstitucionActividadUseCase()
        self.tinstitucion_actividad_repo = TInstitucionActividadRepository()

    @extend_schema(
        responses=TInstitucionActividadSerializer(many=True),
        description="Retrieve a list of all TInstitucionActividad entries."
    )
    def list(self, request):
        """List all TInstitucionActividad."""
        tinstitucion_actividades = self.tinstitucion_actividad_repo.get_all()
        serializer = TInstitucionActividadSerializer(tinstitucion_actividades, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TInstitucionActividadSerializer,
        responses=TInstitucionActividadSerializer,
        description="Create a new TInstitucionActividad entry."
    )
    def create(self, request):
        """Create a new TInstitucionActividad."""
        serializer = TInstitucionActividadSerializer(data=request.data)
        if serializer.is_valid():
            tinstitucion_actividad = self.tinstitucion_actividad_use_case.create_institucion_actividad(**serializer.validated_data)
            self.tinstitucion_actividad_repo.create(tinstitucion_actividad)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TActividadViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tactividad_use_case = TActividadUseCase()
        self.tactividad_repo = TActividadRepository()

    @extend_schema(
        responses=TActividadSerializer(many=True),
        description="Retrieve a list of all TActividad entries."
    )
    def list(self, request):
        """List all TActividad."""
        tactividades = self.tactividad_repo.get_all()
        serializer = TActividadSerializer(tactividades, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TActividadSerializer,
        responses=TActividadSerializer,
        description="Create a new TActividad entry."
    )
    def create(self, request):
        """Create a new TActividad."""
        serializer = TActividadSerializer(data=request.data)
        if serializer.is_valid():
            tactividad = self.tactividad_use_case.create_actividad(**serializer.validated_data)
            self.tactividad_repo.create(tactividad)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TDemandaVinculadaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tdemanda_vinculada_use_case = TDemandaVinculadaUseCase()
        self.tdemanda_vinculada_repo = TDemandaVinculadaRepository()

    @extend_schema(
        responses=TDemandaVinculadaSerializer(many=True),
        description="Retrieve a list of all TDemandaVinculada entries."
    )
    def list(self, request):
        """List all TDemandaVinculada."""
        tdemanda_vinculadas = self.tdemanda_vinculada_repo.get_all()
        serializer = TDemandaVinculadaSerializer(tdemanda_vinculadas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TDemandaVinculadaSerializer,
        responses=TDemandaVinculadaSerializer,
        description="Create a new TDemandaVinculada entry."
    )
    def create(self, request):
        """Create a new TDemandaVinculada."""
        serializer = TDemandaVinculadaSerializer(data=request.data)
        if serializer.is_valid():
            tdemanda_vinculada = self.tdemanda_vinculada_use_case.create_demanda_vinculada(**serializer.validated_data)
            self.tdemanda_vinculada_repo.create(tdemanda_vinculada)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TLegajoViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tlegajo_use_case = TLegajoUseCase()
        self.tlegajo_repo = TLegajoRepository()

    @extend_schema(
        responses=TLegajoSerializer(many=True),
        description="Retrieve a list of all TLegajo entries."
    )
    def list(self, request):
        """List all TLegajo."""
        tlegajos = self.tlegajo_repo.get_all()
        serializer = TLegajoSerializer(tlegajos, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TLegajoSerializer,
        responses=TLegajoSerializer,
        description="Create a new TLegajo entry."
    )
    def create(self, request):
        """Create a new TLegajo."""
        serializer = TLegajoSerializer(data=request.data)
        if serializer.is_valid():
            tlegajo = self.tlegajo_use_case.create_legajo(**serializer.validated_data)
            self.tlegajo_repo.create(tlegajo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TLegajoAsignadoViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tlegajo_asignado_use_case = TLegajoAsignadoUseCase()
        self.tlegajo_asignado_repo = TLegajoAsignadoRepository()

    @extend_schema(
        responses=TLegajoAsignadoSerializer(many=True),
        description="Retrieve a list of all TLegajoAsignado entries."
    )
    def list(self, request):
        """List all TLegajoAsignado."""
        tlegajo_asignados = self.tlegajo_asignado_repo.get_all()
        serializer = TLegajoAsignadoSerializer(tlegajo_asignados, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TLegajoAsignadoSerializer,
        responses=TLegajoAsignadoSerializer,
        description="Create a new TLegajoAsignado entry."
    )
    def create(self, request):
        """Create a new TLegajoAsignado."""
        serializer = TLegajoAsignadoSerializer(data=request.data)
        if serializer.is_valid():
            tlegajo_asignado = self.tlegajo_asignado_use_case.create_legajo_asignado(**serializer.validated_data)
            self.tlegajo_asignado_repo.create(tlegajo_asignado)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TIndicadoresValoracionViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tindicadores_valoracion_use_case = TIndicadoresValoracionUseCase()
        self.tindicadores_valoracion_repo = TIndicadoresValoracionRepository()

    @extend_schema(
        responses=TIndicadoresValoracionSerializer(many=True),
        description="Retrieve a list of all TIndicadoresValoracion entries."
    )
    def list(self, request):
        """List all TIndicadoresValoracion."""
        tindicadores_valoraciones = self.tindicadores_valoracion_repo.get_all()
        serializer = TIndicadoresValoracionSerializer(tindicadores_valoraciones, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TIndicadoresValoracionSerializer,
        responses=TIndicadoresValoracionSerializer,
        description="Create a new TIndicadoresValoracion entry."
    )
    def create(self, request):
        """Create a new TIndicadoresValoracion."""
        serializer = TIndicadoresValoracionSerializer(data=request.data)
        if serializer.is_valid():
            tindicadores_valoracion = self.tindicadores_valoracion_use_case.create_indicadores_valoracion(**serializer.validated_data)
            self.tindicadores_valoracion_repo.create(tindicadores_valoracion)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TEvaluacionesViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tevaluaciones_use_case = TEvaluacionesUseCase()
        self.tevaluaciones_repo = TEvaluacionesRepository()

    @extend_schema(
        responses=TEvaluacionesSerializer(many=True),
        description="Retrieve a list of all TEvaluaciones entries."
    )
    def list(self, request):
        """List all TEvaluaciones."""
        tevaluaciones = self.tevaluaciones_repo.get_all()
        serializer = TEvaluacionesSerializer(tevaluaciones, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TEvaluacionesSerializer,
        responses=TEvaluacionesSerializer,
        description="Create a new TEvaluaciones entry."
    )
    def create(self, request):
        """Create a new TEvaluaciones."""
        serializer = TEvaluacionesSerializer(data=request.data)
        if serializer.is_valid():
            tevaluaciones = self.tevaluaciones_use_case.create_evaluaciones(**serializer.validated_data)
            self.tevaluaciones_repo.create(tevaluaciones)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TDecisionViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tdecision_use_case = TDecisionUseCase()
        self.tdecision_repo = TDecisionRepository()

    @extend_schema(
        responses=TDecisionSerializer(many=True),
        description="Retrieve a list of all TDecision entries."
    )
    def list(self, request):
        """List all TDecision."""
        tdecisions = self.tdecision_repo.get_all()
        serializer = TDecisionSerializer(tdecisions, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TDecisionSerializer,
        responses=TDecisionSerializer,
        description="Create a new TDecision entry."
    )
    def create(self, request):
        """Create a new TDecision."""
        serializer = TDecisionSerializer(data=request.data)
        if serializer.is_valid():
            tdecision = self.tdecision_use_case.create_decision(**serializer.validated_data)
            self.tdecision_repo.create(tdecision)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TVinculoViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tvinculo_use_case = TVinculoUseCase()
        self.tvinculo_repo = TVinculoRepository()

    @extend_schema(
        responses=TVinculoSerializer(many=True),
        description="Retrieve a list of all TVinculo entries."
    )
    def list(self, request):
        """List all TVinculo."""
        tvinculos = self.tvinculo_repo.get_all()
        serializer = TVinculoSerializer(tvinculos, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TVinculoSerializer,
        responses=TVinculoSerializer,
        description="Create a new TVinculo entry."
    )
    def create(self, request):
        """Create a new TVinculo."""
        serializer = TVinculoSerializer(data=request.data)
        if serializer.is_valid():
            tvinculo = self.tvinculo_use_case.create_vinculo(**serializer.validated_data)
            self.tvinculo_repo.create(tvinculo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TVinculoPersonaPersonaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tvinculo_persona_persona_use_case = TVinculoPersonaPersonaUseCase()
        self.tvinculo_persona_persona_repo = TVinculoPersonaPersonaRepository()

    @extend_schema(
        responses=TVinculoPersonaPersonaSerializer(many=True),
        description="Retrieve a list of all TVinculoPersonaPersona entries."
    )
    def list(self, request):
        """List all TVinculoPersonaPersona."""
        tvinculo_persona_personas = self.tvinculo_persona_persona_repo.get_all()
        serializer = TVinculoPersonaPersonaSerializer(tvinculo_persona_personas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TVinculoPersonaPersonaSerializer,
        responses=TVinculoPersonaPersonaSerializer,
        description="Create a new TVinculoPersonaPersona entry."
    )
    def create(self, request):
        """Create a new TVinculoPersonaPersona."""
        serializer = TVinculoPersonaPersonaSerializer(data=request.data)
        if serializer.is_valid():
            tvinculo_persona_persona = self.tvinculo_persona_persona_use_case.create_vinculo_persona_persona(**serializer.validated_data)
            self.tvinculo_persona_persona_repo.create(tvinculo_persona_persona)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TVinculoPersonaNNyAViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tvinculo_persona_nnya_use_case = TVinculoPersonaNNyAUseCase()
        self.tvinculo_persona_nnya_repo = TVinculoPersonaNNyARepository()

    @extend_schema(
        responses=TVinculoPersonaNNyASerializer(many=True),
        description="Retrieve a list of all TVinculoPersonaNNyA entries."
    )
    def list(self, request):
        """List all TVinculoPersonaNNyA."""
        tvinculo_persona_nnyas = self.tvinculo_persona_nnya_repo.get_all()
        serializer = TVinculoPersonaNNyASerializer(tvinculo_persona_nnyas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TVinculoPersonaNNyASerializer,
        responses=TVinculoPersonaNNyASerializer,
        description="Create a new TVinculoPersonaNNyA entry."
    )
    def create(self, request):
        """Create a new TVinculoPersonaNNyA."""
        serializer = TVinculoPersonaNNyASerializer(data=request.data)
        if serializer.is_valid():
            tvinculo_persona_nnya = self.tvinculo_persona_nnya_use_case.create_vinculo_persona_nnya(**serializer.validated_data)
            self.tvinculo_persona_nnya_repo.create(tvinculo_persona_nnya)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TScoreViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tscore_use_case = TScoreUseCase()
        self.tscore_repo = TScoreRepository()

    @extend_schema(
        responses=TScoreSerializer(many=True),
        description="Retrieve a list of all TScore entries."
    )
    def list(self, request):
        """List all TScore."""
        tscores = self.tscore_repo.get_all()
        serializer = TScoreSerializer(tscores, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TScoreSerializer,
        responses=TScoreSerializer,
        description="Create a new TScore entry."
    )
    def create(self, request):
        """Create a new TScore."""
        serializer = TScoreSerializer(data=request.data)
        if serializer.is_valid():
            tscore = self.tscore_use_case.create_score(**serializer.validated_data)
            self.tscore_repo.create(tscore)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TCondicionesVulnerabilidadViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tcondiciones_vulnerabilidad_use_case = TCondicionesVulnerabilidadUseCase()
        self.tcondiciones_vulnerabilidad_repo = TCondicionesVulnerabilidadRepository()

    @extend_schema(
        responses=TCondicionesVulnerabilidadSerializer(many=True),
        description="Retrieve a list of all TCondicionesVulnerabilidad entries."
    )
    def list(self, request):
        """List all TCondicionesVulnerabilidad."""
        tcondiciones_vulnerabilidades = self.tcondiciones_vulnerabilidad_repo.get_all()
        serializer = TCondicionesVulnerabilidadSerializer(tcondiciones_vulnerabilidades, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=TCondicionesVulnerabilidadSerializer,
        responses=TCondicionesVulnerabilidadSerializer,
        description="Create a new TCondicionesVulnerabilidad entry."
    )
    def create(self, request):
        """Create a new TCondicionesVulnerabilidad."""
        serializer = TCondicionesVulnerabilidadSerializer(data=request.data)
        if serializer.is_valid():
            tcondiciones_vulnerabilidad = self.tcondiciones_vulnerabilidad_use_case.create_condiciones_vulnerabilidad(**serializer.validated_data)
            self.tcondiciones_vulnerabilidad_repo.create(tcondiciones_vulnerabilidad)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
