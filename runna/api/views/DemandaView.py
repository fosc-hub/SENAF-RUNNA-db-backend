from drf_spectacular.utils import extend_schema

from .BaseView import BaseViewSet

from infrastructure.models import ( 
    TOrigenDemanda,
    TSubOrigenDemanda, 
    TInformante, 
    TDemanda, 
    TPrecalificacionDemanda, 
    TDemandaScore, 
    TDemandaHistory,
    TInforme101,
    TPrecalificacionDemandaHistory,
    TCalificacionDemanda,
    TCalificacionDemandaHistory,
    TDemandaScoreHistory
)
from api.serializers import (
    TOrigenDemandaSerializer,
    TSubOrigenDemandaSerializer,
    TInformanteSerializer,
    TDemandaSerializer,
    TPrecalificacionDemandaSerializer,
    TDemandaScoreSerializer,
    TDemandaHistorySerializer,
    TInforme101Serializer,
    TPrecalificacionDemandaHistorySerializer,
    TCalificacionDemandaSerializer,
    TCalificacionDemandaHistorySerializer,
    TDemandaScoreHistorySerializer
)
from infrastructure.filters import (
    TOrigenDemandaFilter,
    TSubOrigenDemandaFilter,
    TInformanteFilter, 
    TDemandaFilter, 
    TPrecalificacionDemandaFilter, 
    TDemandaScoreFilter, 
    TDemandaHistoryFilter, 
    TInforme101Filter,
    TPrecalificacionDemandaHistoryFilter,
    TCalificacionDemandaFilter,
    TCalificacionDemandaHistoryFilter,
    TDemandaScoreHistoryFilter
)

class TOrigenDemandaViewSet(BaseViewSet):
    model = TOrigenDemanda
    serializer_class = TOrigenDemandaSerializer
    filterset_class = TOrigenDemandaFilter
    
    http_method_names = ['get']  # Excludes POST, PUT, PATCH, DELETE

    @extend_schema(
        responses=TOrigenDemandaSerializer(many=True),
        description="Retrieve a list of TOrigenDemanda entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TOrigenDemandaSerializer,
        description="Retrieve a single TOrigenDemanda entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)

class TSubOrigenDemandaViewSet(BaseViewSet):
    model = TSubOrigenDemanda
    serializer_class = TSubOrigenDemandaSerializer
    filterset_class = TSubOrigenDemandaFilter
    
    http_method_names = ['get']  # Excludes POST, PUT, PATCH, DELETE

    @extend_schema(
        responses=TSubOrigenDemandaSerializer(many=True),
        description="Retrieve a list of TSubOrigenDemanda entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TSubOrigenDemandaSerializer,
        description="Retrieve a single TSubOrigenDemanda entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TInformanteViewSet(BaseViewSet):
    model = TInformante
    serializer_class = TInformanteSerializer
    filterset_class = TInformanteFilter
    
    http_method_names = ['get', 'post', 'put', 'patch']  # Excludes  DELETE

    @extend_schema(
        request=TInformanteSerializer,
        responses=TInformanteSerializer,
        description="Create a new TInformante entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TInformanteSerializer,
        responses=TInformanteSerializer,
        description="Partially update an existing TInformante entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TInformanteSerializer(many=True),
        description="Retrieve a list of TInformante entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TInformanteSerializer,
        description="Retrieve a single TInformante entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


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


class TInforme101ViewSet(BaseViewSet):
    model = TInforme101
    serializer_class = TInforme101Serializer
    filterset_class = TInforme101Filter
    
    http_method_names = ['get']  # Excludes POST, PUT, PATCH, DELETE

    @extend_schema(
        responses=TInforme101Serializer(many=True),
        description="Retrieve a list of TInforme101 entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TInforme101Serializer,
        description="Retrieve a single TInforme101 entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)

class TPrecalificacionDemandaViewSet(BaseViewSet):
    model = TPrecalificacionDemanda
    serializer_class = TPrecalificacionDemandaSerializer
    filterset_class = TPrecalificacionDemandaFilter
    
    http_method_names = ['get', 'post', 'put', 'patch']

    @extend_schema(
        request=TPrecalificacionDemandaSerializer,
        responses=TPrecalificacionDemandaSerializer,
        description="Create a new TPrecalificacionDemanda entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TPrecalificacionDemandaSerializer,
        responses=TPrecalificacionDemandaSerializer,
        description="Partially update an existing TPrecalificacionDemanda entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TPrecalificacionDemandaSerializer(many=True),
        description="Retrieve a list of TPrecalificacionDemanda entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TPrecalificacionDemandaSerializer,
        description="Retrieve a single TPrecalificacionDemanda entry."
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


class TPrecalificacionDemandaHistoryViewSet(BaseViewSet):
    model = TPrecalificacionDemandaHistory
    serializer_class = TPrecalificacionDemandaHistorySerializer
    filterset_class = TPrecalificacionDemandaHistoryFilter
    
    http_method_names = ['get']  # Excludes POST, PUT, PATCH, DELETE

    @extend_schema(
        responses=TPrecalificacionDemandaHistorySerializer(many=True),
        description="Retrieve a list of TPrecalificacionDemandaHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TPrecalificacionDemandaHistorySerializer,
        description="Retrieve a single TPrecalificacionDemandaHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TCalificacionDemandaViewSet(BaseViewSet):
    model = TCalificacionDemanda
    serializer_class = TCalificacionDemandaSerializer
    filterset_class = TCalificacionDemandaFilter
    
    http_method_names = ['get', 'post']

    @extend_schema(
        request=TCalificacionDemandaSerializer,
        responses=TCalificacionDemandaSerializer,
        description="Create a new TCalificacionDemanda entry"
    )
    def create(self, request):
        return super().create(request)

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

