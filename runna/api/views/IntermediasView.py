from drf_spectacular.utils import extend_schema
# from requests import Response
from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework import status
import logging
logger = logging.getLogger(__name__)

from .BaseView import BaseViewSet
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from services.email_service import EmailService
# from infrastructure.signals import send_mail_to_user_asignado
from django.http import JsonResponse

from infrastructure.models import (
    TLocalizacionPersona,
    TLocalizacionPersonaHistory,
    TDemandaPersona,
    TDemandaPersonaHistory,
    TDemandaZona,
    TDemandaZonaHistory,
    TDemandaVinculada,
    TDemandaVinculadaHistory,
    TPersonaCondicionesVulnerabilidad,
    TPersonaCondicionesVulnerabilidadHistory,
)
from api.serializers import (
    TLocalizacionPersonaSerializer,
    TLocalizacionPersonaHistorySerializer,
    TDemandaPersonaSerializer,
    TDemandaPersonaHistorySerializer,
    TDemandaZonaSerializer,
    TDemandaZonaHistorySerializer,
    TDemandaVinculadaSerializer,
    TDemandaVinculadaHistorySerializer,
    TPersonaCondicionesVulnerabilidadSerializer,
    TPersonaCondicionesVulnerabilidadHistorySerializer,
)
from infrastructure.filters import (
    TLocalizacionPersonaFilter,
    TLocalizacionPersonaHistoryFilter,
    TDemandaPersonaFilter,
    TDemandaPersonaHistoryFilter,
    TDemandaZonaFilter,
    TDemandaZonaHistoryFilter,
    TDemandaVinculadaFilter,
    TDemandaVinculadaHistoryFilter,
    TPersonaCondicionesVulnerabilidadFilter,
    TPersonaCondicionesVulnerabilidadHistoryFilter,
)

class TLocalizacionPersonaViewSet(BaseViewSet):
    model = TLocalizacionPersona
    serializer_class = TLocalizacionPersonaSerializer
    filterset_class = TLocalizacionPersonaFilter
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

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
    
    @extend_schema(
        responses=None,
        description="Delete an existing TLocalizacionPersona entry"
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)


class TDemandaPersonaViewSet(BaseViewSet):
    model = TDemandaPersona
    serializer_class = TDemandaPersonaSerializer
    filterset_class = TDemandaPersonaFilter
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

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
    
    @extend_schema(
        responses=None,
        description="Delete an existing TDemandaPersona entry"
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)


class TDemandaZonaViewSet(BaseViewSet):
    model = TDemandaZona
    serializer_class = TDemandaZonaSerializer
    filterset_class = TDemandaZonaFilter
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    @extend_schema(
        request=TDemandaZonaSerializer,
        responses=TDemandaZonaSerializer,
        description="Create a new TDemandaZona entry"
    )
    def create(self, request):
        # Create the object using the serializer
        try:
            serializer = TDemandaZonaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Capture signal response
        # responses = post_save.send(
        #     sender=TDemandaZona,
        #     instance=instance,
        #     created=True,
        #     raw=False,
        #     using=None,
        # )
        # logger.info(f"Creation of TDemandAsignado instance: {instance}")
        # logger.info(f"Signal responses: {responses}")
        # Collect the first valid response from signal receivers
        signal_response = None
        # for receiver, response in responses:
        #     print(f'Receiver: {receiver}')
        #     print(f'Response: {response}')
        #     if response and 'email_status' in response and 'email_details' in response:
        #         signal_response = response
        #         logger.info(f"signal_response set to: {response}")
        #         break

        # Prepare the API response
        response_data = {
            "message": "TDemandaZona instance created successfully",
            **serializer.data,  # Pass the serialized data
            "email_response": signal_response,  # Pass the captured signal response
        }
        return JsonResponse(response_data, status=status.HTTP_201_CREATED)

    @extend_schema(
        request=TDemandaZonaSerializer,
        responses=TDemandaZonaSerializer,
        description="Partially update an existing TDemandaZona entry"
    )
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk=pk)

    @extend_schema(
        responses=TDemandaZonaSerializer(many=True),
        description="Retrieve a list of TDemandaZona entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TDemandaZonaSerializer,
        description="Retrieve a single TDemandaZona entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
    
    @extend_schema(
        responses=None,
        description="Delete an existing TDemandaZona entry"
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)



class TDemandaVinculadaViewSet(BaseViewSet):
    model = TDemandaVinculada
    serializer_class = TDemandaVinculadaSerializer
    filterset_class = TDemandaVinculadaFilter
    
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

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
    
    @extend_schema(
        responses=None,
        description="Delete an existing TDemandaVinculada entry"
    )
    def destroy(self, request, pk=None):
        return super().destroy(request, pk=pk)


class TPersonaCondicionesVulnerabilidadViewSet(BaseViewSet):
    model = TPersonaCondicionesVulnerabilidad
    serializer_class = TPersonaCondicionesVulnerabilidadSerializer
    filterset_class = TPersonaCondicionesVulnerabilidadFilter
    
    http_method_names = ['get', 'post', 'put', 'patch']

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

class TLocalizacionPersonaHistoryViewSet(BaseViewSet):
    model = TLocalizacionPersonaHistory
    serializer_class = TLocalizacionPersonaHistorySerializer
    filterset_class = TLocalizacionPersonaHistoryFilter
    
    http_method_names = ['get']

    @extend_schema(
        responses=TLocalizacionPersonaHistorySerializer(many=True),
        description="Retrieve a list of TLocalizacionPersonaHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TLocalizacionPersonaHistorySerializer,
        description="Retrieve a single TLocalizacionPersonaHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TDemandaPersonaHistoryViewSet(BaseViewSet):
    model = TDemandaPersonaHistory
    serializer_class = TDemandaPersonaHistorySerializer
    filterset_class = TDemandaPersonaHistoryFilter
    
    http_method_names = ['get']

    @extend_schema(
        responses=TDemandaPersonaHistorySerializer(many=True),
        description="Retrieve a list of TDemandaPersonaHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TDemandaPersonaHistorySerializer,
        description="Retrieve a single TDemandaPersonaHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class TDemandaZonaHistoryViewSet(BaseViewSet):
    model = TDemandaZonaHistory
    serializer_class = TDemandaZonaHistorySerializer
    filterset_class = TDemandaZonaHistoryFilter
    
    http_method_names = ['get']

    @extend_schema(
        responses=TDemandaZonaHistorySerializer(many=True),
        description="Retrieve a list of TDemandaZonaHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TDemandaZonaHistorySerializer,
        description="Retrieve a single TDemandaZonaHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class AuditoriaDemandaZonaZonaView(APIView):
    def get(self, request, pk):
        objects = TDemandaZonaHistory.objects.filter(parent=pk)
        serializer_data = TDemandaZonaHistorySerializer(objects, many=True).data

        return Response(serializer_data, status=status.HTTP_200_OK)

class TDemandaVinculadaHistoryViewSet(BaseViewSet):
    model = TDemandaVinculadaHistory
    serializer_class = TDemandaVinculadaHistorySerializer
    filterset_class = TDemandaVinculadaHistoryFilter
    
    http_method_names = ['get']

    @extend_schema(
        responses=TDemandaVinculadaHistorySerializer(many=True),
        description="Retrieve a list of TDemandaVinculadaHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TDemandaVinculadaHistorySerializer,
        description="Retrieve a single TDemandaVinculadaHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)


class GestionDemandaZonaZonaView(APIView):
    def get(self, request, pk):

        objects = TDemandaZonaHistory.objects.filter(parent=pk)
        
        serializer_data = TDemandaZonaHistorySerializer(objects, many=True).data

        return JsonResponse(serializer_data, status=status.HTTP_200_OK)


class TPersonaCondicionesVulnerabilidadHistoryViewSet(BaseViewSet):
    model = TPersonaCondicionesVulnerabilidadHistory
    serializer_class = TPersonaCondicionesVulnerabilidadHistorySerializer
    filterset_class = TPersonaCondicionesVulnerabilidadHistoryFilter
    
    http_method_names = ['get']

    @extend_schema(
        responses=TPersonaCondicionesVulnerabilidadHistorySerializer(many=True),
        description="Retrieve a list of TPersonaCondicionesVulnerabilidadHistory entries with optional filtering."
    )
    def list(self, request):
        return super().list(request)

    @extend_schema(
        responses=TPersonaCondicionesVulnerabilidadHistorySerializer,
        description="Retrieve a single TPersonaCondicionesVulnerabilidadHistory entry."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)

