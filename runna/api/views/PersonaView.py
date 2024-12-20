from drf_spectacular.utils import extend_schema

from .BaseView import BaseViewSet

from infrastructure.models import (
    TPersona,
    TInstitucionEducativa,
    TNNyAEducacion,
    TInstitucionSanitaria,
    TNNyASalud,
    TNNyAScore,
    TLegajo,
    TPersonaHistory,
    TNNyAEducacionHistory,
    TNNyASaludHistory,
    TLegajoHistory,
    TNNyAScoreHistory
)
from api.serializers import (
    TPersonaSerializer,
    TInstitucionEducativaSerializer,
    TNNyAEducacionSerializer,
    TInstitucionSanitariaSerializer,
    TNNyASaludSerializer,
    TNNyAScoreSerializer,
    TLegajoSerializer,
    TPersonaHistorySerializer,
    TNNyAEducacionHistorySerializer,
    TNNyASaludHistorySerializer,
    TLegajoHistorySerializer,
    TNNyAScoreHistorySerializer
)
from infrastructure.filters import (
    TPersonaFilter, 
    TInstitucionEducativaFilter, 
    TNNyAEducacionFilter, 
    TInstitucionSanitariaFilter, 
    TNNyASaludFilter, 
    TNNyAScoreFilter, 
    TLegajoFilter, 
    TPersonaHistoryFilter, 
    TNNyAEducacionHistoryFilter, 
    TNNyASaludHistoryFilter,
    TLegajoHistoryFilter,
    TNNyAScoreHistoryFilter
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


class TInstitucionEducativaViewSet(BaseViewSet):
    model = TInstitucionEducativa
    serializer_class = TInstitucionEducativaSerializer
    filterset_class = TInstitucionEducativaFilter
    
    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TInstitucionEducativaSerializer(many=True),
        description="Retrieve a list of TInstitucionEducativa entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TInstitucionEducativaSerializer,
        description="Retrieve a single TInstitucionEducativa entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TNNyAEducacionViewSet(BaseViewSet):
    model = TNNyAEducacion
    serializer_class = TNNyAEducacionSerializer
    filterset_class = TNNyAEducacionFilter
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    @extend_schema(
        request=TNNyAEducacionSerializer,
        responses=TNNyAEducacionSerializer,
        description="Create a new TNNyAEducacion entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TNNyAEducacionSerializer,
        responses=TNNyAEducacionSerializer,
        description="Partially update an existing TNNyAEducacion entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TNNyAEducacionSerializer(many=True),
        description="Retrieve a list of TNNyAEducacion entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TNNyAEducacionSerializer,
        description="Retrieve a single TNNyAEducacion entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
    
    @extend_schema(
        responses=None,
        description="Delete an existing TNNyAEducacion entry"
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)


class TInstitucionSanitariaViewSet(BaseViewSet):
    model = TInstitucionSanitaria
    serializer_class = TInstitucionSanitariaSerializer
    filterset_class = TInstitucionSanitariaFilter

    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TInstitucionSanitariaSerializer(many=True),
        description="Retrieve a list of TInstitucionSanitaria entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TInstitucionSanitariaSerializer,
        description="Retrieve a single TInstitucionSanitaria entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TNNyASaludViewSet(BaseViewSet):
    model = TNNyASalud
    serializer_class = TNNyASaludSerializer
    filterset_class = TNNyASaludFilter
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    @extend_schema(
        request=TNNyASaludSerializer,
        responses=TNNyASaludSerializer,
        description="Create a new TNNyASalud entry"
    )
    def create(self, request):
        return super().create(request)

    @extend_schema(
        request=TNNyASaludSerializer,
        responses=TNNyASaludSerializer,
        description="Partially update an existing TNNyASalud entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TNNyASaludSerializer(many=True),
        description="Retrieve a list of TNNyASalud entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TNNyASaludSerializer,
        description="Retrieve a single TNNyASalud entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
    
    @extend_schema(
        responses=None,
        description="Delete an existing TNNyASalud entry"
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)


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


class TPersonaHistoryViewSet(BaseViewSet):
    model = TPersonaHistory
    serializer_class = TPersonaHistorySerializer
    filterset_class = TPersonaHistoryFilter
    
    http_method_names = ['get'] # Only allow GET requests

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


class TNNyAEducacionHistoryViewSet(BaseViewSet):
    model = TNNyAEducacionHistory
    serializer_class = TNNyAEducacionHistorySerializer
    filterset_class = TNNyAEducacionHistoryFilter
    
    http_method_names = ['get'] # Only allow GET requests
    
    @extend_schema(
        responses=TNNyAEducacionHistorySerializer(many=True),
        description="Retrieve a list of TNNyAEducacionHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)
    
    @extend_schema(
        responses=TNNyAEducacionHistorySerializer,
        description="Retrieve a single TNNyAEducacionHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
    

class TNNyASaludHistoryViewSet(BaseViewSet):
    model = TNNyASaludHistory
    serializer_class = TNNyASaludHistorySerializer
    filterset_class = TNNyASaludHistoryFilter
    
    http_method_names = ['get'] # Only allow GET requests
    
    @extend_schema(
        responses=TNNyASaludHistorySerializer(many=True),
        description="Retrieve a list of TNNyASaludHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)
    
    @extend_schema(
        responses=TNNyASaludHistorySerializer,
        description="Retrieve a single TNNyASaludHistory entry."
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
