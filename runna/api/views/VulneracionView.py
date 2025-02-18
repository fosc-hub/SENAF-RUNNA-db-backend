from drf_spectacular.utils import extend_schema

from .BaseView import BaseViewSet

from infrastructure.models import (
    TVulneracion,
    TVulneracionHistory,
)
from api.serializers import (
    TVulneracionSerializer,
    TVulneracionHistorySerializer,
)
from infrastructure.filters import (
    TVulneracionFilter,
    TVulneracionHistoryFilter,
)


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
