from rest_framework import status, viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from .BaseView import BaseViewSet

from infrastructure.models import (
    TLocalizacion, TLocalizacionHistory
)

from core.use_cases import (
    TProvinciaUseCase, TDepartamentoUseCase, TLocalidadUseCase, TBarrioUseCase, TCPCUseCase
)

from api.serializers import (
    TProvinciaSerializer, TDepartamentoSerializer, TLocalidadSerializer, TBarrioSerializer, TCPCSerializer, TLocalizacionSerializer, TLocalizacionHistorySerializer
)

from infrastructure.repositories import (
    TProvinciaRepository, TDepartamentoRepository, TLocalidadRepository, TBarrioRepository, TCPCRepository, TLocalizacionRepository
)

from infrastructure.filters import (
    TProvinciaFilter, TDepartamentoFilter, TLocalidadFilter, TBarrioFilter, TCPCFilter, TLocalizacionFilter, TLocalizacionHistoryFilter
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

class TLocalizacionViewSet(BaseViewSet):
    model = TLocalizacion
    serializer_class = TLocalizacionSerializer
    filterset_class = TLocalizacionFilter
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    
    @extend_schema(
        request=TLocalizacionSerializer,
        responses=TLocalizacionSerializer,
        description="Create a new TLocalizacion entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TLocalizacionSerializer,
        responses=TLocalizacionSerializer,
        description="Partially update an existing TLocalizacion entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TLocalizacionSerializer(many=True),
        description="Retrieve a list of TLocalizacion entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TLocalizacionSerializer,
        description="Retrieve a single TLocalizacion entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)

    @extend_schema(
        responses=None,
        description="Delete an existing TLocalizacion entry"
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)

class TLocalizacionHistoryViewSet(BaseViewSet):
    model = TLocalizacionHistory
    serializer_class = TLocalizacionHistorySerializer
    filterset_class = TLocalizacionHistoryFilter
    
    http_method_names = ['get']

    @extend_schema(
        responses=TLocalizacionHistorySerializer(many=True),
        description="Retrieve a list of TLocalizacionHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TLocalizacionHistorySerializer,
        description="Retrieve a single TLocalizacionHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)

