from rest_framework import status, viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import NotFound
from django_filters.rest_framework import DjangoFilterBackend


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

class TInstitucionUsuarioExternoViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TInstitucionUsuarioExternoFilter

    @extend_schema(
        responses=TInstitucionUsuarioExternoSerializer(many=True),
        description="Retrieve a list of all TInstitucionUsuarioExterno entries with optional filtering."
    )
    def list(self, request):
        """List all TInstitucionUsuarioExterno."""
        queryset = TInstitucionUsuarioExterno.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = TInstitucionUsuarioExternoSerializer(filtered_queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        responses=TInstitucionUsuarioExternoSerializer,
        description="Retrieve a single TInstitucionUsuarioExterno"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TInstitucionUsuarioExterno."""
        try:
            obj = TInstitucionUsuarioExterno.objects.get(pk=pk)
        except TInstitucionUsuarioExterno.DoesNotExist:
            raise NotFound(f"TInstitucionUsuarioExterno with ID {pk} not found.")
        serializer = TInstitucionUsuarioExternoSerializer(obj)
        return Response(serializer.data)

    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)


class TVinculoUsuarioExternoViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TVinculoUsuarioExternoFilter

    @extend_schema(
        responses=TVinculoUsuarioExternoSerializer(many=True),
        description="Retrieve a list of all TVinculoUsuarioExterno entries with optional filtering."
    )
    def list(self, request):
        """List all TVinculoUsuarioExterno."""
        queryset = TVinculoUsuarioExterno.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = TVinculoUsuarioExternoSerializer(filtered_queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        responses=TVinculoUsuarioExternoSerializer,
        description="Retrieve a single TVinculoUsuarioExterno"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TVinculoUsuarioExterno."""
        try:
            obj = TVinculoUsuarioExterno.objects.get(pk=pk)
        except TVinculoUsuarioExterno.DoesNotExist:
            raise NotFound(f"TVinculoUsuarioExterno with ID {pk} not found.")
        serializer = TVinculoUsuarioExternoSerializer(obj)
        return Response(serializer.data)

    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)


class TCargoExternoViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TCargoExternoFilter

    @extend_schema(
        responses=TCargoExternoSerializer(many=True),
        description="Retrieve a list of all TCargoExterno entries with optional filtering."
    )
    def list(self, request):
        """List all TCargoExterno."""
        queryset = TCargoExterno.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = TCargoExternoSerializer(filtered_queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        responses=TCargoExternoSerializer,
        description="Retrieve a single TCargoExterno"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TCargoExterno."""
        try:
            obj = TCargoExterno.objects.get(pk=pk)
        except TCargoExterno.DoesNotExist:
            raise NotFound(f"TCargoExterno with ID {pk} not found.")
        serializer = TCargoExternoSerializer(obj)
        return Response(serializer.data)

    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)


class TResponsableExternoViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TResponsableExternoFilter

    @extend_schema(
        responses=TResponsableExternoSerializer(many=True),
        description="Retrieve a list of all TResponsableExterno entries with optional filtering."
    )
    def list(self, request):
        """List all TResponsableExterno."""
        queryset = TResponsableExterno.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = TResponsableExternoSerializer(filtered_queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        responses=TResponsableExternoSerializer,
        description="Retrieve a single TResponsableExterno"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TResponsableExterno."""
        try:
            obj = TResponsableExterno.objects.get(pk=pk)
        except TResponsableExterno.DoesNotExist:
            raise NotFound(f"TResponsableExterno with ID {pk} not found.")
        serializer = TResponsableExternoSerializer(obj)
        return Response(serializer.data)
    
    @extend_schema(
        request=TResponsableExternoSerializer,
        responses=TResponsableExternoSerializer,
        description="Create a new TResponsableExterno"
    )
    def create(self, request):
        """Create a new TResponsableExterno."""
        serializer = TResponsableExternoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        request=TResponsableExternoSerializer,
        responses=TResponsableExternoSerializer,
        description="Partially update an existing TResponsableExterno"
    )
    def partial_update(self, request, pk=None):
        """Partially update an existing TResponsableExterno."""
        try:
            obj = TResponsableExterno.objects.get(pk=pk)
        except TResponsableExterno.DoesNotExist:
            raise NotFound(f"TResponsableExterno with ID {pk} not found.")
        serializer = TResponsableExternoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)


class TUsuarioExternoViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TUsuarioExternoFilter

    @extend_schema(
        responses=TUsuarioExternoSerializer(many=True),
        description="Retrieve a list of all TUsuarioExterno entries with optional filtering."
    )
    def list(self, request):
        """List all TUsuarioExterno."""
        queryset = TUsuarioExterno.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = TUsuarioExternoSerializer(filtered_queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        responses=TUsuarioExternoSerializer,
        description="Retrieve a single TUsuarioExterno"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TUsuarioExterno."""
        try:
            obj = TUsuarioExterno.objects.get(pk=pk)
        except TUsuarioExterno.DoesNotExist:
            raise NotFound(f"TUsuarioExterno with ID {pk} not found.")
        serializer = TUsuarioExternoSerializer(obj)
        return Response(serializer.data)

    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)

class TUsuarioExternoViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TUsuarioExternoFilter

    @extend_schema(
        responses=TUsuarioExternoSerializer(many=True),
        description="Retrieve a list of all TUsuarioExterno entries with optional filtering."
    )
    def list(self, request):
        """List all TUsuarioExterno."""
        queryset = TUsuarioExterno.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = TUsuarioExternoSerializer(filtered_queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        responses=TUsuarioExternoSerializer,
        description="Retrieve a single TUsuarioExterno"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TUsuarioExterno."""
        try:
            obj = TUsuarioExterno.objects.get(pk=pk)
        except TUsuarioExterno.DoesNotExist:
            raise NotFound(f"TUsuarioExterno with ID {pk} not found.")
        serializer = TUsuarioExternoSerializer(obj)
        return Response(serializer.data)

    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)


class TDemandaViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TDemandaFilter

    @extend_schema(
        responses=TDemandaSerializer(many=True),
        description="Retrieve a list of all TDemanda entries with optional filtering."
    )
    def list(self, request):
        """List all TDemanda."""
        queryset = TDemanda.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = TDemandaSerializer(filtered_queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        responses=TDemandaSerializer,
        description="Retrieve a single TDemanda"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TDemanda."""
        try:
            obj = TDemanda.objects.get(pk=pk)
        except TDemanda.DoesNotExist:
            raise NotFound(f"TDemanda with ID {pk} not found.")
        serializer = TDemandaSerializer(obj)
        return Response(serializer.data)

    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)


class TPrecalificacionDemandaViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TPrecalificacionDemandaFilter

    @extend_schema(
        responses=TPrecalificacionDemandaSerializer(many=True),
        description="Retrieve a list of all TPrecalificacionDemanda entries with optional filtering."
    )
    def list(self, request):
        """List all TPrecalificacionDemanda."""
        queryset = TPrecalificacionDemanda.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = TPrecalificacionDemandaSerializer(filtered_queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        responses=TPrecalificacionDemandaSerializer,
        description="Retrieve a single TPrecalificacionDemanda"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TPrecalificacionDemanda."""
        try:
            obj = TPrecalificacionDemanda.objects.get(pk=pk)
        except TPrecalificacionDemanda.DoesNotExist:
            raise NotFound(f"TPrecalificacionDemanda with ID {pk} not found.")
        serializer = TPrecalificacionDemandaSerializer(obj)
        return Response(serializer.data)

    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)


class TScoreDemandaViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TScoreDemandaFilter

    @extend_schema(
        responses=TScoreDemandaSerializer(many=True),
        description="Retrieve a list of all TScoreDemanda entries with optional filtering."
    )
    def list(self, request):
        """List all TScoreDemanda."""
        queryset = TScoreDemanda.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = TScoreDemandaSerializer(filtered_queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        responses=TScoreDemandaSerializer,
        description="Retrieve a single TScoreDemanda"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single TScoreDemanda."""
        try:
            obj = TScoreDemanda.objects.get(pk=pk)
        except TScoreDemanda.DoesNotExist:
            raise NotFound(f"TScoreDemanda with ID {pk} not found.")
        serializer = TScoreDemandaSerializer(obj)
        return Response(serializer.data)

    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)

