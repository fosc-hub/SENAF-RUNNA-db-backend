from drf_spectacular.utils import extend_schema

from .BaseView import BaseViewSet

from infrastructure.models import (
    TPersona,
    TPersonaHistory,
    TEducacion,
    TEducacionHistory,
    TMedico,
    TCoberturaMedica,
    TCoberturaMedicaHistory,
    TPersonaEnfermedades,
    TPersonaEnfermedadesHistory,
    TNNyAScore,
    TNNyAScoreHistory,
    TLegajo,
    TLegajoHistory,
)
from api.serializers import (
    TPersonaSerializer,
    TPersonaHistorySerializer,
    TEducacionSerializer,
    TEducacionHistorySerializer,
    TMedicoSerializer,
    TCoberturaMedicaSerializer,
    TCoberturaMedicaHistorySerializer,
    TPersonaEnfermedadesSerializer,
    TPersonaEnfermedadesHistorySerializer,
    TNNyAScoreSerializer,
    TNNyAScoreHistorySerializer,
    TLegajoSerializer,
    TLegajoHistorySerializer,
)
from infrastructure.filters import (
    TPersonaFilter,
    TPersonaHistoryFilter,
    TEducacionFilter,
    TEducacionHistoryFilter,
    TMedicoFilter,
    TCoberturaMedicaFilter,
    TCoberturaMedicaHistoryFilter,
    TPersonaEnfermedadesFilter,
    TPersonaEnfermedadesHistoryFilter,
    TNNyAScoreFilter,
    TNNyAScoreHistoryFilter,
    TLegajoFilter,
    TLegajoHistoryFilter,
)

class TPersonaViewSet(BaseViewSet):
    model = TPersona
    serializer_class = TPersonaSerializer
    filterset_class = TPersonaFilter
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    @extend_schema(
        request=TPersonaSerializer,
        responses=TPersonaSerializer,
        description="Create a new TPersona entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TPersonaSerializer,
        responses=TPersonaSerializer,
        description="Partially update an existing TPersona entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TPersonaSerializer(many=True),
        description="Retrieve a list of TPersona entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TPersonaSerializer,
        description="Retrieve a single TPersona entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
    
    @extend_schema(
        responses=None,
        description="Delete an existing TPersona entry"
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)


class TPersonaHistoryViewSet(BaseViewSet):
    model = TPersonaHistory
    serializer_class = TPersonaHistorySerializer
    filterset_class = TPersonaHistoryFilter
    
    http_method_names = ['get']  # Only allow GET requests

    @extend_schema(
        responses=TPersonaHistorySerializer(many=True),
        description="Retrieve a list of TPersonaHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TPersonaHistorySerializer,
        description="Retrieve a single TPersonaHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TEducacionViewSet(BaseViewSet):
    model = TEducacion
    serializer_class = TEducacionSerializer
    filterset_class = TEducacionFilter
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    @extend_schema(
        request=TEducacionSerializer,
        responses=TEducacionSerializer,
        description="Create a new TEducacion entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TEducacionSerializer,
        responses=TEducacionSerializer,
        description="Partially update an existing TEducacion entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TEducacionSerializer(many=True),
        description="Retrieve a list of TEducacion entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TEducacionSerializer,
        description="Retrieve a single TEducacion entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
    
    @extend_schema(
        responses=None,
        description="Delete an existing TEducacion entry"
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)


class TEducacionHistoryViewSet(BaseViewSet):
    model = TEducacionHistory
    serializer_class = TEducacionHistorySerializer
    filterset_class = TEducacionHistoryFilter
    
    http_method_names = ['get'] # Only allow GET requests
    
    @extend_schema(
        responses=TEducacionHistorySerializer(many=True),
        description="Retrieve a list of TEducacionHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)
    
    @extend_schema(
        responses=TEducacionHistorySerializer,
        description="Retrieve a single TEducacionHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TMedicoViewSet(BaseViewSet):
    model = TMedico
    serializer_class = TMedicoSerializer
    filterset_class = TMedicoFilter
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    @extend_schema(
        request=TMedicoSerializer,
        responses=TMedicoSerializer,
        description="Create a new TMedico entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TMedicoSerializer,
        responses=TMedicoSerializer,
        description="Partially update an existing TMedico entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TMedicoSerializer(many=True),
        description="Retrieve a list of TMedico entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TMedicoSerializer,
        description="Retrieve a single TMedico entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
    
    @extend_schema(
        responses=None,
        description="Delete an existing TMedico entry"
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)


class TCoberturaMedicaViewSet(BaseViewSet):
    model = TCoberturaMedica
    serializer_class = TCoberturaMedicaSerializer
    filterset_class = TCoberturaMedicaFilter
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    @extend_schema(
        request=TCoberturaMedicaSerializer,
        responses=TCoberturaMedicaSerializer,
        description="Create a new TCoberturaMedica entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TCoberturaMedicaSerializer,
        responses=TCoberturaMedicaSerializer,
        description="Partially update an existing TCoberturaMedica entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TCoberturaMedicaSerializer(many=True),
        description="Retrieve a list of TCoberturaMedica entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TCoberturaMedicaSerializer,
        description="Retrieve a single TCoberturaMedica entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
    
    @extend_schema(
        responses=None,
        description="Delete an existing TCoberturaMedica entry"
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)


class TCoberturaMedicaHistoryViewSet(BaseViewSet):
    model = TCoberturaMedicaHistory
    serializer_class = TCoberturaMedicaHistorySerializer
    filterset_class = TCoberturaMedicaHistoryFilter
    
    http_method_names = ['get'] # Only allow GET requests
    
    @extend_schema(
        responses=TCoberturaMedicaHistorySerializer(many=True),
        description="Retrieve a list of TCoberturaMedicaHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)
    
    @extend_schema(
        responses=TCoberturaMedicaHistorySerializer,
        description="Retrieve a single TCoberturaMedicaHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TPersonaEnfermedadesViewSet(BaseViewSet):
    model = TPersonaEnfermedades
    serializer_class = TPersonaEnfermedadesSerializer
    filterset_class = TPersonaEnfermedadesFilter
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    @extend_schema(
        request=TPersonaEnfermedadesSerializer,
        responses=TPersonaEnfermedadesSerializer,
        description="Create a new TPersonaEnfermedades entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TPersonaEnfermedadesSerializer,
        responses=TPersonaEnfermedadesSerializer,
        description="Partially update an existing TPersonaEnfermedades entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TPersonaEnfermedadesSerializer(many=True),
        description="Retrieve a list of TPersonaEnfermedades entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TPersonaEnfermedadesSerializer,
        description="Retrieve a single TPersonaEnfermedades entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
    
    @extend_schema(
        responses=None,
        description="Delete an existing TPersonaEnfermedades entry"
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)


class TPersonaEnfermedadesHistoryViewSet(BaseViewSet):
    model = TPersonaEnfermedadesHistory
    serializer_class = TPersonaEnfermedadesHistorySerializer
    filterset_class = TPersonaEnfermedadesHistoryFilter
    
    http_method_names = ['get'] # Only allow GET requests
    
    @extend_schema(
        responses=TPersonaEnfermedadesHistorySerializer(many=True),
        description="Retrieve a list of TPersonaEnfermedadesHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)
    
    @extend_schema(
        responses=TPersonaEnfermedadesHistorySerializer,
        description="Retrieve a single TPersonaEnfermedadesHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TNNyAScoreViewSet(BaseViewSet):
    model = TNNyAScore
    serializer_class = TNNyAScoreSerializer
    filterset_class = TNNyAScoreFilter
    
    http_method_names = ['get'] # Only allow GET requests
    
    @extend_schema(
        responses=TNNyAScoreSerializer(many=True),
        description="Retrieve a list of TNNyAScore entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TNNyAScoreSerializer,
        description="Retrieve a single TNNyAScore entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TNNyAScoreHistoryViewSet(BaseViewSet):
    model = TNNyAScoreHistory
    serializer_class = TNNyAScoreHistorySerializer
    filterset_class = TNNyAScoreHistoryFilter
    
    http_method_names = ['get'] # Only allow GET requests
    
    @extend_schema(
        responses=TNNyAScoreHistorySerializer(many=True),
        description="Retrieve a list of TNNyAScoreHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)
    
    @extend_schema(
        responses=TNNyAScoreHistorySerializer,
        description="Retrieve a single TNNyAScoreHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TLegajoViewSet(BaseViewSet):
    model = TLegajo
    serializer_class = TLegajoSerializer
    filterset_class = TLegajoFilter
    
    http_method_names = ['get', 'patch' ] # Only allow GET and PATCH requests

    @extend_schema(
        request=TLegajoSerializer,
        responses=TLegajoSerializer,
        description="Partially update an existing TLegajo entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TLegajoSerializer(many=True),
        description="Retrieve a list of TLegajo entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TLegajoSerializer,
        description="Retrieve a single TLegajo entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TLegajoHistoryViewSet(BaseViewSet):
    model = TLegajoHistory
    serializer_class = TLegajoHistorySerializer
    filterset_class = TLegajoHistoryFilter
    
    http_method_names = ['get'] # Only allow GET requests
    
    @extend_schema(
        responses=TLegajoHistorySerializer(many=True),
        description="Retrieve a list of TLegajoHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)
    
    @extend_schema(
        responses=TLegajoHistorySerializer,
        description="Retrieve a single TLegajoHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)

