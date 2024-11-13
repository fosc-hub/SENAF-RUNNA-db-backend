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
