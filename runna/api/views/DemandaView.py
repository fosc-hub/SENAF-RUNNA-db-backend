from drf_spectacular.utils import extend_schema

from .BaseView import BaseViewSet

from infrastructure.models import (
    TDemanda,
    TDemandaHistory,
    TCalificacionDemanda,
    TCalificacionDemandaHistory,
    TDemandaScore, 
    TDemandaScoreHistory,
)
from api.serializers import (
    TDemandaSerializer,
    TDemandaHistorySerializer,
    TCalificacionDemandaSerializer,
    TCalificacionDemandaHistorySerializer,
    TDemandaScoreSerializer,
    TDemandaScoreHistorySerializer,
)
from infrastructure.filters import (
    TDemandaFilter,
    TDemandaHistoryFilter,
    TCalificacionDemandaFilter,
    TCalificacionDemandaHistoryFilter,
    TDemandaScoreFilter,
    TDemandaScoreHistoryFilter,
)


class TDemandaViewSet(BaseViewSet):
    model = TDemanda
    serializer_class = TDemandaSerializer
    filterset_class = TDemandaFilter

    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    @extend_schema(
        request=TDemandaSerializer,
        responses=TDemandaSerializer,
        description="Create a new TDemanda entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TDemandaSerializer,
        responses=TDemandaSerializer,
        description="Partially update an existing TDemanda entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TDemandaSerializer(many=True),
        description="Retrieve a list of TDemanda entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TDemandaSerializer,
        description="Retrieve a single TDemanda entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
    
    @extend_schema(
        responses=None,
        description="Delete an existing TDemanda entry"
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)

class TDemandaHistoryViewSet(BaseViewSet):
    model = TDemandaHistory
    serializer_class = TDemandaHistorySerializer
    filterset_class = TDemandaHistoryFilter
    
    http_method_names = ['get']  # Excludes POST, PUT, PATCH, DELETE

    @extend_schema(
        responses=TDemandaHistorySerializer(many=True),
        description="Retrieve a list of TDemandaHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TDemandaHistorySerializer,
        description="Retrieve a single TDemandaHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)

class TCalificacionDemandaViewSet(BaseViewSet):
    model = TCalificacionDemanda
    serializer_class = TCalificacionDemandaSerializer
    filterset_class = TCalificacionDemandaFilter
    
    http_method_names = ['get', 'post', 'put', 'patch']

    @extend_schema(
        request=TCalificacionDemandaSerializer,
        responses=TCalificacionDemandaSerializer,
        description="Create a new TCalificacionDemanda entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TCalificacionDemandaSerializer,
        responses=TCalificacionDemandaSerializer,
        description="Partially update an existing TCalificacionDemanda entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TCalificacionDemandaSerializer(many=True),
        description="Retrieve a list of TCalificacionDemanda entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TCalificacionDemandaSerializer,
        description="Retrieve a single TCalificacionDemanda entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)

class TCalificacionDemandaHistoryViewSet(BaseViewSet):
    model = TCalificacionDemandaHistory
    serializer_class = TCalificacionDemandaHistorySerializer
    filterset_class = TCalificacionDemandaHistoryFilter
    
    http_method_names = ['get']  # Excludes POST, PUT, PATCH, DELETE

    @extend_schema(
        responses=TCalificacionDemandaHistorySerializer(many=True),
        description="Retrieve a list of TCalificacionDemandaHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TCalificacionDemandaHistorySerializer,
        description="Retrieve a single TCalificacionDemandaHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)

class TDemandaScoreViewSet(BaseViewSet):
    model = TDemandaScore
    serializer_class = TDemandaScoreSerializer
    filterset_class = TDemandaScoreFilter
    
    http_method_names = ['get']  # Excludes POST, PUT, PATCH, DELETE

    @extend_schema(
        responses=TDemandaScoreSerializer(many=True),
        description="Retrieve a list of TDemandaScore entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TDemandaScoreSerializer,
        description="Retrieve a single TDemandaScore entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)

class TDemandaScoreHistoryViewSet(BaseViewSet):
    model = TDemandaScoreHistory
    serializer_class = TDemandaScoreHistorySerializer
    filterset_class = TDemandaScoreHistoryFilter
    
    http_method_names = ['get']  # Excludes POST, PUT, PATCH, DELETE

    @extend_schema(
        responses=TDemandaScoreHistorySerializer(many=True),
        description="Retrieve a list of TDemandaScoreHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TDemandaScoreHistorySerializer,
        description="Retrieve a single TDemandaScoreHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)

