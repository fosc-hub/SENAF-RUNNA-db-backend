from drf_spectacular.utils import extend_schema
import logging
logger = logging.getLogger(__name__)

from rest_framework.response import Response
from django.http import JsonResponse, Http404
from rest_framework import status
from django.db.models.signals import post_save
from django.db import transaction


from .BaseView import BaseViewSet

from infrastructure.models import (
    TActividadTipo, 
    TInstitucionActividad, 
    TActividad,
    TRespuestaEtiqueta,
    TRespuesta, 
    TIndicadoresValoracion, 
    TEvaluaciones, 
    TDecision, 
    TEvaluacionesHistory
)
from api.serializers import (
    TActividadTipoSerializer,
    TInstitucionActividadSerializer,
    TActividadSerializer,
    TRespuestaEtiquetaSerializer,
    TRespuestaSerializer,
    TIndicadoresValoracionSerializer,
    TEvaluacionesSerializer,
    TDecisionSerializer,
    TEvaluacionesHistorySerializer
)
from infrastructure.filters import (
    TActividadTipoFilter, 
    TInstitucionActividadFilter, 
    TActividadFilter, 
    TRespuestaFilter, 
    TIndicadoresValoracionFilter, 
    TEvaluacionesFilter, 
    TDecisionFilter, 
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

class TRespuestaEtiquetaViewSet(BaseViewSet):
    model = TRespuestaEtiqueta
    serializer_class = TRespuestaEtiquetaSerializer

    http_method_names = ['get'] # Only allow GET requests

    @extend_schema(
        responses=TRespuestaEtiquetaSerializer(many=True),
        description="Retrieve a list of TRespuestaEtiqueta entries."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TRespuestaEtiquetaSerializer,
        description="Retrieve a single TRespuestaEtiqueta entry."
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
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    # validated_data = serializer.validated_data
                    # adjuntos_data = validated_data.pop('adjuntos', [])
                    # print(f"adjuntos_data: {adjuntos_data}")
                    # instance = TRespuesta(**validated_data)
                    # instance._adjuntos = adjuntos_data
                    # instance.save()
                    # print(f"Serializer data: {serializer.validated_data}")
                    serializer._adjuntos = serializer.validated_data['adjuntos']
                    instance = serializer.save()  # _adjuntos is set on instance before saving.
                return Response(serializer.data, status=201)
            except Exception as e:
                return Response({"error": str(e)}, status=400)
            # instance = serializer.save()

            # # Capture signal response
            # responses = post_save.send(
            #     sender=TRespuesta,
            #     instance=instance,
            #     created=True,
            #     raw=False,
            #     using=None,
            # )
            # logger.info(f"Creation of TRespuesta instance: {instance}")
            # logger.info(f"Signal responses: {responses}")
            # # Collect the first valid response from signal receivers
            # signal_response = None
            # for receiver, response in responses:
            #     print(f'Receiver: {receiver}')
            #     print(f'Response: {response}')
            #     if response and 'email_status' in response and 'email_details' in response:
            #         signal_response = response
            #         logger.info(f"signal_response set to: {response}")
            #         break

            # # Prepare the API response
            # response_data = {
            #     "message": "TRespuesta instance created successfully",
            #     **serializer.data,  # Pass the serialized data
            #     "email_response": signal_response,  # Pass the captured signal response
            # }
            # return JsonResponse(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)


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



