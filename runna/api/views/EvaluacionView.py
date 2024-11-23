from drf_spectacular.utils import extend_schema

from .BaseView import BaseViewSet

from infrastructure.models import (
    TActividadTipo, TInstitucionActividad, TActividad, TInstitucionRespuesta, TRespuesta, TIndicadoresValoracion, TEvaluaciones, TDecision
)
from api.serializers import (
    TActividadTipoSerializer, TInstitucionActividadSerializer, TActividadSerializer, TInstitucionRespuestaSerializer, TRespuestaSerializer, TIndicadoresValoracionSerializer, TEvaluacionesSerializer, TDecisionSerializer
)
from infrastructure.filters import (
    TActividadTipoFilter, TInstitucionActividadFilter, TActividadFilter, TInstitucionRespuestaFilter, TRespuestaFilter, TIndicadoresValoracionFilter, TEvaluacionesFilter, TDecisionFilter
)


class TActividadTipoViewSet(BaseViewSet):
    model = TActividadTipo
    serializer_class = TActividadTipoSerializer
    filterset_class = TActividadTipoFilter

    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TActividadTipoSerializer(many=True),
        description="Retrieve a list of TActividadTipo entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TActividadTipoSerializer,
        description="Retrieve a single TActividadTipo entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TInstitucionActividadViewSet(BaseViewSet):
    model = TInstitucionActividad
    serializer_class = TInstitucionActividadSerializer
    filterset_class = TInstitucionActividadFilter

    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TInstitucionActividadSerializer(many=True),
        description="Retrieve a list of TInstitucionActividad entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TInstitucionActividadSerializer,
        description="Retrieve a single TInstitucionActividad entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TActividadViewSet(BaseViewSet):
    model = TActividad
    serializer_class = TActividadSerializer
    filterset_class = TActividadFilter
    
    http_method_names = ['get', 'post', 'put', 'patch']

    @extend_schema(
        request=TActividadSerializer,
        responses=TActividadSerializer,
        description="Create a new TActividad entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TActividadSerializer,
        responses=TActividadSerializer,
        description="Partially update an existing TActividad entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TActividadSerializer(many=True),
        description="Retrieve a list of TActividad entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TActividadSerializer,
        description="Retrieve a single TActividad entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TInstitucionRespuestaViewSet(BaseViewSet):
    model = TInstitucionRespuesta
    serializer_class = TInstitucionRespuestaSerializer
    filterset_class = TInstitucionRespuestaFilter

    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TInstitucionRespuestaSerializer(many=True),
        description="Retrieve a list of TInstitucionRespuesta entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TInstitucionRespuestaSerializer,
        description="Retrieve a single TInstitucionRespuesta entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TRespuestaViewSet(BaseViewSet):
    model = TRespuesta
    serializer_class = TRespuestaSerializer
    filterset_class = TRespuestaFilter
    
    http_method_names = ['get', 'post'] # Only allow GET and POST requests

    @extend_schema(
        request=TRespuestaSerializer,
        responses=TRespuestaSerializer,
        description="Create a new TRespuesta entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        responses=TRespuestaSerializer(many=True),
        description="Retrieve a list of TRespuesta entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TRespuestaSerializer,
        description="Retrieve a single TRespuesta entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TIndicadoresValoracionViewSet(BaseViewSet):
    model = TIndicadoresValoracion
    serializer_class = TIndicadoresValoracionSerializer
    filterset_class = TIndicadoresValoracionFilter

    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TIndicadoresValoracionSerializer(many=True),
        description="Retrieve a list of TIndicadoresValoracion entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TIndicadoresValoracionSerializer,
        description="Retrieve a single TIndicadoresValoracion entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TEvaluacionesViewSet(BaseViewSet):
    model = TEvaluaciones
    serializer_class = TEvaluacionesSerializer
    filterset_class = TEvaluacionesFilter
    
    http_method_names = ['get', 'post', 'put', 'patch']

    @extend_schema(
        request=TEvaluacionesSerializer,
        responses=TEvaluacionesSerializer,
        description="Create a new TEvaluaciones entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TEvaluacionesSerializer,
        responses=TEvaluacionesSerializer,
        description="Partially update an existing TEvaluaciones entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TEvaluacionesSerializer(many=True),
        description="Retrieve a list of TEvaluaciones entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TEvaluacionesSerializer,
        description="Retrieve a single TEvaluaciones entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TDecisionViewSet(BaseViewSet):
    model = TDecision
    serializer_class = TDecisionSerializer
    filterset_class = TDecisionFilter
    
    http_method_names = ['get', 'post'] # Only allow GET and POST requests

    @extend_schema(
        request=TDecisionSerializer,
        responses=TDecisionSerializer,
        description="Create a new TDecision entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        responses=TDecisionSerializer(many=True),
        description="Retrieve a list of TDecision entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TDecisionSerializer,
        description="Retrieve a single TDecision entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
