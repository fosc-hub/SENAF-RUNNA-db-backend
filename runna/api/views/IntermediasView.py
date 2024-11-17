from drf_spectacular.utils import extend_schema

from .BaseView import BaseViewSet

from infrastructure.models import (
    TLocalizacionPersona, TDemandaPersona, TDemandaAsignado, TDemandaVinculada, TLegajoAsignado, TVinculoPersona, TVinculoPersonaPersona, TDemandaMotivoIntervencion, TPersonaCondicionesVulnerabilidad
)
from api.serializers import (
    TLocalizacionPersonaSerializer, TDemandaPersonaSerializer, TDemandaAsignadoSerializer, TDemandaVinculadaSerializer, TLegajoAsignadoSerializer, TVinculoPersonaSerializer, TVinculoPersonaPersonaSerializer, TDemandaMotivoIntervencionSerializer, TPersonaCondicionesVulnerabilidadSerializer
)
from infrastructure.filters import (
    TLocalizacionPersonaFilter, TDemandaPersonaFilter, TDemandaAsignadoFilter, TDemandaVinculadaFilter, TLegajoAsignadoFilter, TVinculoPersonaFilter, TVinculoPersonaPersonaFilter, TDemandaMotivoIntervencionFilter, TPersonaCondicionesVulnerabilidadFilter
)

class TLocalizacionPersonaViewSet(BaseViewSet):
    model = TLocalizacionPersona
    serializer_class = TLocalizacionPersonaSerializer
    filterset_class = TLocalizacionPersonaFilter

    @extend_schema(
        request=TLocalizacionPersonaSerializer,
        responses=TLocalizacionPersonaSerializer,
        description="Create a new TLocalizacionPersona entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TLocalizacionPersonaSerializer,
        responses=TLocalizacionPersonaSerializer,
        description="Partially update an existing TLocalizacionPersona entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TLocalizacionPersonaSerializer(many=True),
        description="Retrieve a list of TLocalizacionPersona entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TLocalizacionPersonaSerializer,
        description="Retrieve a single TLocalizacionPersona entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TDemandaPersonaViewSet(BaseViewSet):
    model = TDemandaPersona
    serializer_class = TDemandaPersonaSerializer
    filterset_class = TDemandaPersonaFilter

    @extend_schema(
        request=TDemandaPersonaSerializer,
        responses=TDemandaPersonaSerializer,
        description="Create a new TDemandaPersona entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TDemandaPersonaSerializer,
        responses=TDemandaPersonaSerializer,
        description="Partially update an existing TDemandaPersona entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TDemandaPersonaSerializer(many=True),
        description="Retrieve a list of TDemandaPersona entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TDemandaPersonaSerializer,
        description="Retrieve a single TDemandaPersona entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TDemandaAsignadoViewSet(BaseViewSet):
    model = TDemandaAsignado
    serializer_class = TDemandaAsignadoSerializer
    filterset_class = TDemandaAsignadoFilter

    @extend_schema(
        request=TDemandaAsignadoSerializer,
        responses=TDemandaAsignadoSerializer,
        description="Create a new TDemandaAsignado entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TDemandaAsignadoSerializer,
        responses=TDemandaAsignadoSerializer,
        description="Partially update an existing TDemandaAsignado entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TDemandaAsignadoSerializer(many=True),
        description="Retrieve a list of TDemandaAsignado entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TDemandaAsignadoSerializer,
        description="Retrieve a single TDemandaAsignado entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TDemandaVinculadaViewSet(BaseViewSet):
    model = TDemandaVinculada
    serializer_class = TDemandaVinculadaSerializer
    filterset_class = TDemandaVinculadaFilter

    @extend_schema(
        request=TDemandaVinculadaSerializer,
        responses=TDemandaVinculadaSerializer,
        description="Create a new TDemandaVinculada entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TDemandaVinculadaSerializer,
        responses=TDemandaVinculadaSerializer,
        description="Partially update an existing TDemandaVinculada entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TDemandaVinculadaSerializer(many=True),
        description="Retrieve a list of TDemandaVinculada entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TDemandaVinculadaSerializer,
        description="Retrieve a single TDemandaVinculada entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TLegajoAsignadoViewSet(BaseViewSet):
    model = TLegajoAsignado
    serializer_class = TLegajoAsignadoSerializer
    filterset_class = TLegajoAsignadoFilter

    @extend_schema(
        request=TLegajoAsignadoSerializer,
        responses=TLegajoAsignadoSerializer,
        description="Create a new TLegajoAsignado entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TLegajoAsignadoSerializer,
        responses=TLegajoAsignadoSerializer,
        description="Partially update an existing TLegajoAsignado entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TLegajoAsignadoSerializer(many=True),
        description="Retrieve a list of TLegajoAsignado entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TLegajoAsignadoSerializer,
        description="Retrieve a single TLegajoAsignado entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TVinculoPersonaViewSet(BaseViewSet):
    model = TVinculoPersona
    serializer_class = TVinculoPersonaSerializer
    filterset_class = TVinculoPersonaFilter
    
    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TVinculoPersonaSerializer(many=True),
        description="Retrieve a list of TVinculoPersona entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TVinculoPersonaSerializer,
        description="Retrieve a single TVinculoPersona entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TVinculoPersonaPersonaViewSet(BaseViewSet):
    model = TVinculoPersonaPersona
    serializer_class = TVinculoPersonaPersonaSerializer
    filterset_class = TVinculoPersonaPersonaFilter

    @extend_schema(
        request=TVinculoPersonaPersonaSerializer,
        responses=TVinculoPersonaPersonaSerializer,
        description="Create a new TVinculoPersonaPersona entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TVinculoPersonaPersonaSerializer,
        responses=TVinculoPersonaPersonaSerializer,
        description="Partially update an existing TVinculoPersonaPersona entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TVinculoPersonaPersonaSerializer(many=True),
        description="Retrieve a list of TVinculoPersonaPersona entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TVinculoPersonaPersonaSerializer,
        description="Retrieve a single TVinculoPersonaPersona entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TDemandaMotivoIntervencionViewSet(BaseViewSet):
    model = TDemandaMotivoIntervencion
    serializer_class = TDemandaMotivoIntervencionSerializer
    filterset_class = TDemandaMotivoIntervencionFilter

    @extend_schema(
        request=TDemandaMotivoIntervencionSerializer,
        responses=TDemandaMotivoIntervencionSerializer,
        description="Create a new TDemandaMotivoIntervencion entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TDemandaMotivoIntervencionSerializer,
        responses=TDemandaMotivoIntervencionSerializer,
        description="Partially update an existing TDemandaMotivoIntervencion entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TDemandaMotivoIntervencionSerializer(many=True),
        description="Retrieve a list of TDemandaMotivoIntervencion entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TDemandaMotivoIntervencionSerializer,
        description="Retrieve a single TDemandaMotivoIntervencion entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TPersonaCondicionesVulnerabilidadViewSet(BaseViewSet):
    model = TPersonaCondicionesVulnerabilidad
    serializer_class = TPersonaCondicionesVulnerabilidadSerializer
    filterset_class = TPersonaCondicionesVulnerabilidadFilter

    @extend_schema(
        request=TPersonaCondicionesVulnerabilidadSerializer,
        responses=TPersonaCondicionesVulnerabilidadSerializer,
        description="Create a new TPersonaCondicionesVulnerabilidad entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TPersonaCondicionesVulnerabilidadSerializer,
        responses=TPersonaCondicionesVulnerabilidadSerializer,
        description="Partially update an existing TPersonaCondicionesVulnerabilidad entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TPersonaCondicionesVulnerabilidadSerializer(many=True),
        description="Retrieve a list of TPersonaCondicionesVulnerabilidad entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TPersonaCondicionesVulnerabilidadSerializer,
        description="Retrieve a single TPersonaCondicionesVulnerabilidad entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
