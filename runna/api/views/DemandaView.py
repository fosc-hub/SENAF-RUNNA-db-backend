from drf_spectacular.utils import extend_schema

from .BaseView import BaseViewSet

from infrastructure.models import (
    TInstitucionUsuarioExterno, TVinculoUsuarioExterno, TCargoExterno,
    TResponsableExterno, TUsuarioExterno, TDemanda, TPrecalificacionDemanda, TScoreDemanda
)
from api.serializers import (
    TInstitucionUsuarioExternoSerializer, TVinculoUsuarioExternoSerializer,
    TCargoExternoSerializer, TResponsableExternoSerializer,
    TUsuarioExternoSerializer, TDemandaSerializer,
    TPrecalificacionDemandaSerializer, TScoreDemandaSerializer
)
from infrastructure.filters import (
    TInstitucionUsuarioExternoFilter, TVinculoUsuarioExternoFilter,
    TCargoExternoFilter, TResponsableExternoFilter,
    TUsuarioExternoFilter, TDemandaFilter,
    TPrecalificacionDemandaFilter, TScoreDemandaFilter
)


class TInstitucionUsuarioExternoViewSet(BaseViewSet):
    model = TInstitucionUsuarioExterno
    serializer_class = TInstitucionUsuarioExternoSerializer
    filterset_class = TInstitucionUsuarioExternoFilter
    
    http_method_names = ['get']  # Excludes POST, PUT, PATCH, DELETE

    @extend_schema(
        responses=TInstitucionUsuarioExternoSerializer(many=True),
        description="Retrieve a list of TInstitucionUsuarioExterno entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TInstitucionUsuarioExternoSerializer,
        description="Retrieve a single TInstitucionUsuarioExterno entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TVinculoUsuarioExternoViewSet(BaseViewSet):
    model = TVinculoUsuarioExterno
    serializer_class = TVinculoUsuarioExternoSerializer
    filterset_class = TVinculoUsuarioExternoFilter
    
    http_method_names = ['get']  # Excludes POST, PUT, PATCH, DELETE

    @extend_schema(
        responses=TVinculoUsuarioExternoSerializer(many=True),
        description="Retrieve a list of TVinculoUsuarioExterno entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TVinculoUsuarioExternoSerializer,
        description="Retrieve a single TVinculoUsuarioExterno entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TCargoExternoViewSet(BaseViewSet):
    model = TCargoExterno
    serializer_class = TCargoExternoSerializer
    filterset_class = TCargoExternoFilter
    
    http_method_names = ['get']  # Excludes POST, PUT, PATCH, DELETE

    @extend_schema(
        responses=TCargoExternoSerializer(many=True),
        description="Retrieve a list of TCargoExterno entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TCargoExternoSerializer,
        description="Retrieve a single TCargoExterno entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TResponsableExternoViewSet(BaseViewSet):
    model = TResponsableExterno
    serializer_class = TResponsableExternoSerializer
    filterset_class = TResponsableExternoFilter

    @extend_schema(
        request=TResponsableExternoSerializer,
        responses=TResponsableExternoSerializer,
        description="Create a new TResponsableExterno entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TResponsableExternoSerializer,
        responses=TResponsableExternoSerializer,
        description="Partially update an existing TResponsableExterno entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TResponsableExternoSerializer(many=True),
        description="Retrieve a list of TResponsableExterno entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TResponsableExternoSerializer,
        description="Retrieve a single TResponsableExterno entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TUsuarioExternoViewSet(BaseViewSet):
    model = TUsuarioExterno
    serializer_class = TUsuarioExternoSerializer
    filterset_class = TUsuarioExternoFilter

    @extend_schema(
        request=TUsuarioExternoSerializer,
        responses=TUsuarioExternoSerializer,
        description="Create a new TUsuarioExterno entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TUsuarioExternoSerializer,
        responses=TUsuarioExternoSerializer,
        description="Partially update an existing TUsuarioExterno entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TUsuarioExternoSerializer(many=True),
        description="Retrieve a list of TUsuarioExterno entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TUsuarioExternoSerializer,
        description="Retrieve a single TUsuarioExterno entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TDemandaViewSet(BaseViewSet):
    model = TDemanda
    serializer_class = TDemandaSerializer
    filterset_class = TDemandaFilter

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


class TPrecalificacionDemandaViewSet(BaseViewSet):
    model = TPrecalificacionDemanda
    serializer_class = TPrecalificacionDemandaSerializer
    filterset_class = TPrecalificacionDemandaFilter

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


class TScoreDemandaViewSet(BaseViewSet):
    model = TScoreDemanda
    serializer_class = TScoreDemandaSerializer
    filterset_class = TScoreDemandaFilter
    
    http_method_names = ['get']  # Excludes POST, PUT, PATCH, DELETE

    @extend_schema(
        responses=TScoreDemandaSerializer(many=True),
        description="Retrieve a list of TScoreDemanda entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TScoreDemandaSerializer,
        description="Retrieve a single TScoreDemanda entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
