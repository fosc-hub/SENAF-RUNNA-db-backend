from drf_spectacular.utils import extend_schema

from .BaseView import BaseViewSet

from infrastructure.models import (
    TCategoriaMotivo, TCategoriaSubmotivo, TGravedadVulneracion, TUrgenciaVulneracion, TCondicionesVulnerabilidad, TMotivoIntervencion, TVulneracion, TVulneracionHistory
)
from api.serializers import (
    TCategoriaMotivoSerializer, TCategoriaSubmotivoSerializer, TGravedadVulneracionSerializer, TUrgenciaVulneracionSerializer, TCondicionesVulnerabilidadSerializer, TMotivoIntervencionSerializer, TVulneracionSerializer, TVulneracionHistorySerializer
)
from infrastructure.filters import (
    TCategoriaMotivoFilter, TCategoriaSubmotivoFilter, TGravedadVulneracionFilter, TUrgenciaVulneracionFilter, TCondicionesVulnerabilidadFilter, TMotivoIntervencionFilter, TVulneracionFilter, TVulneracionHistoryFilter
)

class TCategoriaMotivoViewSet(BaseViewSet):
    model = TCategoriaMotivo
    serializer_class = TCategoriaMotivoSerializer
    filterset_class = TCategoriaMotivoFilter
    
    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TCategoriaMotivoSerializer(many=True),
        description="Retrieve a list of TCategoriaMotivo entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TCategoriaMotivoSerializer,
        description="Retrieve a single TCategoriaMotivo entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TCategoriaSubmotivoViewSet(BaseViewSet):
    model = TCategoriaSubmotivo
    serializer_class = TCategoriaSubmotivoSerializer
    filterset_class = TCategoriaSubmotivoFilter
    
    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TCategoriaSubmotivoSerializer(many=True),
        description="Retrieve a list of TCategoriaSubmotivo entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TCategoriaSubmotivoSerializer,
        description="Retrieve a single TCategoriaSubmotivo entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TGravedadVulneracionViewSet(BaseViewSet):
    model = TGravedadVulneracion
    serializer_class = TGravedadVulneracionSerializer
    filterset_class = TGravedadVulneracionFilter
    
    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TGravedadVulneracionSerializer(many=True),
        description="Retrieve a list of TGravedadVulneracion entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TGravedadVulneracionSerializer,
        description="Retrieve a single TGravedadVulneracion entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TUrgenciaVulneracionViewSet(BaseViewSet):
    model = TUrgenciaVulneracion
    serializer_class = TUrgenciaVulneracionSerializer
    filterset_class = TUrgenciaVulneracionFilter

    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TUrgenciaVulneracionSerializer(many=True),
        description="Retrieve a list of TUrgenciaVulneracion entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TUrgenciaVulneracionSerializer,
        description="Retrieve a single TUrgenciaVulneracion entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TCondicionesVulnerabilidadViewSet(BaseViewSet):
    model = TCondicionesVulnerabilidad
    serializer_class = TCondicionesVulnerabilidadSerializer
    filterset_class = TCondicionesVulnerabilidadFilter

    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TCondicionesVulnerabilidadSerializer(many=True),
        description="Retrieve a list of TCondicionesVulnerabilidad entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TCondicionesVulnerabilidadSerializer,
        description="Retrieve a single TCondicionesVulnerabilidad entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TMotivoIntervencionViewSet(BaseViewSet):
    model = TMotivoIntervencion
    serializer_class = TMotivoIntervencionSerializer
    filterset_class = TMotivoIntervencionFilter

    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TMotivoIntervencionSerializer(many=True),
        description="Retrieve a list of TMotivoIntervencion entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TMotivoIntervencionSerializer,
        description="Retrieve a single TMotivoIntervencion entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TVulneracionViewSet(BaseViewSet):
    model = TVulneracion
    serializer_class = TVulneracionSerializer
    filterset_class = TVulneracionFilter
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    @extend_schema(
        request=TVulneracionSerializer,
        responses=TVulneracionSerializer,
        description="Create a new TVulneracion entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TVulneracionSerializer,
        responses=TVulneracionSerializer,
        description="Partially update an existing TVulneracion entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TVulneracionSerializer(many=True),
        description="Retrieve a list of TVulneracion entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TVulneracionSerializer,
        description="Retrieve a single TVulneracion entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
    
    @extend_schema(
        responses=None,
        description="Delete an existing TVulneracion entry"
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)

class TVulneracionHistoryViewSet(BaseViewSet):
    model = TVulneracionHistory
    serializer_class = TVulneracionHistorySerializer
    filterset_class = TVulneracionHistoryFilter

    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TVulneracionHistorySerializer(many=True),
        description="Retrieve a list of TVulneracionHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TVulneracionHistorySerializer,
        description="Retrieve a single TVulneracionHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
