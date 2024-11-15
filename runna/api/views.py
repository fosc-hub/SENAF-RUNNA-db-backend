from rest_framework import status, viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend

from core.use_cases import (
    TProvinciaUseCase, TDepartamentoUseCase, TLocalidadUseCase, TBarrioUseCase, TCPCUseCase, TLocalizacionUseCase
)

from api.serializers import (
    TProvinciaSerializer, TDepartamentoSerializer, TLocalidadSerializer, TBarrioSerializer, TCPCSerializer, TLocalizacionSerializer
)

from infrastructure.repositories import (
    TProvinciaRepository, TDepartamentoRepository, TLocalidadRepository, TBarrioRepository, TCPCRepository, TLocalizacionRepository
)

from infrastructure.filters import (
    TProvinciaFilter, TDepartamentoFilter, TLocalidadFilter, TBarrioFilter, TCPCFilter, TLocalizacionFilter
)

class TProvinciaViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TProvinciaFilter

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tprovincia_use_case = TProvinciaUseCase()
        self.tprovincia_repo = TProvinciaRepository()

    @extend_schema(
        responses=TProvinciaSerializer(many=True),
        description="Retrieve a list of all Provincia entries with optional filtering."
    )
    def list(self, request):
        """List all TProvincia."""
        queryset = self.tprovincia_repo.get_all()
        filtered_queryset = self.filter_queryset(queryset)  # Apply filters
        serializer = TProvinciaSerializer(filtered_queryset, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        request=TProvinciaSerializer,
        responses=TProvinciaSerializer,
        description="Retrieve a single TProvincia"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TProvincia."""
        tprovincia = self.tprovincia_repo.get_provincia(pk)
        serializer = TProvinciaSerializer(tprovincia)
        return Response(serializer.data)
    
    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)



class TDepartamentoViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TDepartamentoFilter    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tdepartamento_use_case = TDepartamentoUseCase()
        self.tdepartamento_repo = TDepartamentoRepository()

    @extend_schema(
        responses=TDepartamentoSerializer(many=True),
        description="Retrieve a list of all TDepartamento entries with optional filtering."
    )
    def list(self, request):
        """List all TDepartamento."""
        queryset = self.tdepartamento_repo.get_all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = TDepartamentoSerializer(filtered_queryset, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        request=TDepartamentoSerializer,
        responses=TDepartamentoSerializer,
        description="Retrieve a single TDepartamento"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TDepartamento."""
        tdepartamento = self.tdepartamento_repo.get_departamento(pk)
        serializer = TDepartamentoSerializer(tdepartamento)
        return Response(serializer.data)

    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)


class TLocalidadViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TLocalidadFilter

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tlocalidad_use_case = TLocalidadUseCase()
        self.tlocalidad_repo = TLocalidadRepository()

    @extend_schema(
        responses=TLocalidadSerializer(many=True),
        description="Retrieve a list of all TLocalidad entries with optional filtering."
    )
    def list(self, request):
        """List all TLocalidad."""
        queryset = self.tlocalidad_repo.get_all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = TLocalidadSerializer(filtered_queryset, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        request=TLocalidadSerializer,
        responses=TLocalidadSerializer,
        description="Retrieve a single TLocalidad"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TLocalidad."""
        tlocalidad = self.tlocalidad_repo.get_localidad(pk)
        serializer = TLocalidadSerializer(tlocalidad)
        return Response(serializer.data)
    
    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)

class TBarrioViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TBarrioFilter

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tbarrio_use_case = TBarrioUseCase()
        self.tbarrio_repo = TBarrioRepository()

    @extend_schema(
        responses=TBarrioSerializer(many=True),
        description="Retrieve a list of all TBarrio entries with optional filtering."
    )
    def list(self, request):
        """List all TBarrio."""
        queryset = self.tbarrio_repo.get_all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = TBarrioSerializer(filtered_queryset, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        request=TBarrioSerializer,
        responses=TBarrioSerializer,
        description="Retrieve a single TBarrio"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TBarrio."""
        tbarrio = self.tbarrio_repo.get_barrio(pk)
        serializer = TBarrioSerializer(tbarrio)
        return Response(serializer.data)
    
    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)

class TCPCViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TCPCFilter

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tcpc_use_case = TCPCUseCase()
        self.tcpc_repo = TCPCRepository()

    @extend_schema(
        responses=TCPCSerializer(many=True),
        description="Retrieve a list of all TCPC entries with optional filtering."
    )
    def list(self, request):
        """List all TCPC."""
        queryset = self.tcpc_repo.get_all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = TCPCSerializer(filtered_queryset, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        request=TCPCSerializer,
        responses=TCPCSerializer,
        description="Retrieve a single TCPC"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TCPC."""
        tcpc = self.tcpc_repo.get_cpc(pk)
        serializer = TCPCSerializer(tcpc)
        return Response(serializer.data)
    
    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)

class TLocalizacionViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TLocalizacionFilter

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tlocalizacion_use_case = TLocalizacionUseCase()
        self.tlocalizacion_repo = TLocalizacionRepository()
        
    @extend_schema(
        responses=TLocalizacionSerializer(many=True),
        description="Retrieve a list of all TLocalizacion entries with optional filtering."
    )
    def list(self, request):
        """List all TLocalizacion."""
        queryset = self.tlocalizacion_repo.get_all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = TLocalizacionSerializer(filtered_queryset, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        request=TLocalizacionSerializer,
        responses=TLocalizacionSerializer,
        description="Retrieve a single TLocalizacion"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TLocalizacion."""
        tlocalizacion = self.tlocalizacion_repo.get_localizacion(pk)
        serializer = TLocalizacionSerializer(tlocalizacion)
        return Response(serializer.data)
    
    @extend_schema(
        request=TLocalizacionSerializer,
        responses=TLocalizacionSerializer,
        description="Create a new TLocalizacion"
    )
    def create(self, request):
        """Create a new TLocalizacion."""
        serializer = TLocalizacionSerializer(data=request.data)
        if serializer.is_valid():
            tlocalizacion = self.tlocalizacion_use_case.create_localizacion(**serializer.validated_data)
            new_localizacion =  self.tlocalizacion_repo.create(tlocalizacion)

            return Response(TLocalizacionSerializer(new_localizacion).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        request=TLocalizacionSerializer,
        responses=TLocalizacionSerializer,
        description="Partially update an existing TLocalizacion"
    )
    def partial_update(self, request, pk=None):
        """Partially update an existing TLocalizacion."""
        tlocalizacion = self.tlocalizacion_repo.get_localizacion(pk)
        serializer = TLocalizacionSerializer(tlocalizacion, data=request.data, partial=True)
        if serializer.is_valid():
            updated_localizacion = self.tlocalizacion_use_case.update_localizacion(tlocalizacion, **serializer.validated_data)
            final_localizacion = self.tlocalizacion_repo.update(updated_localizacion)
            return Response(TLocalizacionSerializer(final_localizacion).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)