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

