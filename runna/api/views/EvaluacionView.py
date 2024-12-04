from drf_spectacular.utils import extend_schema
import logging
logger = logging.getLogger(__name__)

from django.http import JsonResponse
from rest_framework import status
from django.db.models.signals import post_save


from .BaseView import BaseViewSet

from infrastructure.models import (
    TActividadTipo, 
    TInstitucionActividad, 
    TActividad, 
    TInstitucionRespuesta, 
    TRespuesta, 
    TIndicadoresValoracion, 
    TEvaluaciones, 
    TDecision, 
    TActividadHistory, 
    TEvaluacionesHistory
)
from api.serializers import (
    TActividadTipoSerializer,
    TInstitucionActividadSerializer,
    TActividadSerializer,
    TInstitucionRespuestaSerializer,
    TRespuestaSerializer,
    TIndicadoresValoracionSerializer,
    TEvaluacionesSerializer,
    TDecisionSerializer,
    TActividadHistorySerializer,
    TEvaluacionesHistorySerializer
)
from infrastructure.filters import (
    TActividadTipoFilter, 
    TInstitucionActividadFilter, 
    TActividadFilter, 
    TInstitucionRespuestaFilter, 
    TRespuestaFilter, 
    TIndicadoresValoracionFilter, 
    TEvaluacionesFilter, 
    TDecisionFilter, 
    TActividadHistoryFilter,
    TEvaluacionesHistoryFilter
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
        # Create the object using the serializer
        serializer = TRespuestaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        # Capture signal response
        responses = post_save.send(
            sender=TRespuesta,
            instance=instance,
            created=True,
            raw=False,
            using=None,
        )
        logger.info(f"Creation of TRespuesta instance: {instance}")
        logger.info(f"Signal responses: {responses}")
        # Collect the first valid response from signal receivers
        signal_response = None
        for receiver, response in responses:
            print(f'Receiver: {receiver}')
            print(f'Response: {response}')
            if response and 'email_status' in response and 'email_details' in response:
                signal_response = response
                logger.info(f"signal_response set to: {response}")
                break

        # Prepare the API response
        response_data = {
            "message": "TRespuesta instance created successfully",
            **serializer.data,  # Pass the serialized data
            "email_response": signal_response,  # Pass the captured signal response
        }
        return JsonResponse(response_data, status=status.HTTP_201_CREATED)


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


class TActividadHistoryViewSet(BaseViewSet):
    model = TActividadHistory
    serializer_class = TActividadHistorySerializer
    filterset_class = TActividadHistoryFilter

    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TActividadHistorySerializer(many=True),
        description="Retrieve a list of TActividadHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TActividadHistorySerializer,
        description="Retrieve a single TActividadHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TEvaluacionesHistoryViewSet(BaseViewSet):
    model = TEvaluacionesHistory
    serializer_class = TEvaluacionesHistorySerializer
    filterset_class = TEvaluacionesHistoryFilter

    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TEvaluacionesHistorySerializer(many=True),
        description="Retrieve a list of TEvaluacionesHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TEvaluacionesHistorySerializer,
        description="Retrieve a single TEvaluacionesHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)



