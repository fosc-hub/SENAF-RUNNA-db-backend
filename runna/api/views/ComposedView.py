from django.http import Http404
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework.views import APIView

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from django.db import transaction

from .BaseView import BaseViewSet
from drf_spectacular.utils import extend_schema

from customAuth.models import (
    CustomUser,
    TZona,
    TCustomUserZona,
)
from customAuth.serializers import (
    CustomUserSerializer,
    TZonaSerializer,
    TCustomUserZonaSerializer,
)
from infrastructure.models import (
    TBloqueDatosRemitente,
    TTipoInstitucionDemanda,
    TAmbitoVulneracion,
    TTipoPresuntoDelito,
    TInstitucionDemanda,
    TDemanda,
    TTipoCodigoDemanda,
    TCodigoDemanda,
    TCalificacionDemanda,
    TDemandaScore,
    
    TLocalidad,
    TBarrio,
    TCPC,
    TLocalizacion,
    
    TPersona,
    TInstitucionEducativa,
    TEducacion,
    TInstitucionSanitaria,
    TSituacionSalud,
    TEnfermedad,
    TMedico,
    TCoberturaMedica,
    TPersonaEnfermedades,
    TNNyAScore,

    TDerechoAfectado,
    TCategoriaMotivo,
    TCategoriaSubmotivo,
    TGravedadVulneracion,
    TUrgenciaVulneracion,
    TCondicionesVulnerabilidad,
    TVulneracion,

    TLocalizacionPersona,
    TDemandaPersona,
    TDemandaZona,
    TDemandaVinculada,
    TPersonaCondicionesVulnerabilidad,
)
from api.serializers import (
    RegistroDemandaFormDropdownsSerializer,
    RegistroDemandaFormSerializer,
    MesaDeEntradaSerializer,
)

class MesaDeEntradaPagination(PageNumberPagination):
    page_size = 5  # Number of items per page
    page_size_query_param = 'page_size'  # Allow clients to override the page size
    max_page_size = 100  # Maximum limit


class MesaDeEntradaListView(generics.ListAPIView):
    queryset = TDemanda.objects.all()
    serializer_class = MesaDeEntradaSerializer
    pagination_class = MesaDeEntradaPagination

    # Enable filtering and ordering
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['fecha_creacion', 'estado_demanda']  # Fields allowed for sorting
    ordering = ['-fecha_creacion']  # Default sorting (descending)
    # filterset_fields = ['estado_demanda']  # Fields allowed for filtering

class RegistroDemandaFormDropdownsView(APIView):
    @method_decorator(cache_page(60*15), name='get')
    def get(self, request):

        # Query related models
        bloques_datos_remitente = TBloqueDatosRemitente.objects.all()
        tipo_institucion_demanda = TTipoInstitucionDemanda.objects.all()
        ambito_vulneracion = TAmbitoVulneracion.objects.all()
        tipo_presunto_delito = TTipoPresuntoDelito.objects.all()
        institucion_demanda = TInstitucionDemanda.objects.all()
        tipo_codigo_demanda = TTipoCodigoDemanda.objects.all()

        localidad = TLocalidad.objects.all()
        barrio = TBarrio.objects.all()
        cpc = TCPC.objects.all()

        institucion_educativa = TInstitucionEducativa.objects.all()
        institucion_sanitaria = TInstitucionSanitaria.objects.all()
        situacion_salud = TSituacionSalud.objects.all()
        enfermedad = TEnfermedad.objects.all()

        derecho_afectado = TDerechoAfectado.objects.all()
        categoria_motivo = TCategoriaMotivo.objects.all()
        categoria_submotivo = TCategoriaSubmotivo.objects.all()
        gravedad_vulneracion = TGravedadVulneracion.objects.all()
        urgencia_vulneracion = TUrgenciaVulneracion.objects.all()
        condiciones_vulnerabilidad = TCondicionesVulnerabilidad.objects.all()
        
        zonas = TZona.objects.all()

        # Serialize data
        serialized_data = RegistroDemandaFormDropdownsSerializer({
            "bloques_datos_remitente": bloques_datos_remitente,
            "tipo_institucion_demanda": tipo_institucion_demanda,
            "ambito_vulneracion": ambito_vulneracion,
            "tipo_presunto_delito": tipo_presunto_delito,
            "institucion_demanda": institucion_demanda,
            "tipo_codigo_demanda": tipo_codigo_demanda,

            "localidad": localidad,
            "barrio": barrio,
            "cpc": cpc,

            "institucion_educativa": institucion_educativa,
            "institucion_sanitaria": institucion_sanitaria,
            "situacion_salud": situacion_salud,
            "enfermedad": enfermedad,

            "derecho_afectado": derecho_afectado,
            "categoria_motivo": categoria_motivo,
            "categoria_submotivo": categoria_submotivo,
            "gravedad_vulneracion": gravedad_vulneracion,
            "urgencia_vulneracion": urgencia_vulneracion,
            "condiciones_vulnerabilidad": condiciones_vulnerabilidad,
            
            "zonas": zonas,
            
        })

        return Response(serialized_data.data)


class RegistroDemandaFormView(BaseViewSet):
    model = TDemanda
    serializer_class = RegistroDemandaFormSerializer
    
    http_method_names = ['post', 'patch', 'get']  # Excludes PUT, DELETE, HEAD, OPTIONS

    @extend_schema(
        request=RegistroDemandaFormSerializer,
        responses=RegistroDemandaFormSerializer,
        description="Create a new TDemanda entry"
    )
    def create(self, request):
        serializer = RegistroDemandaFormSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    serializer.save()
                return Response(serializer.data, status=201)
            except Exception as e:
                return Response({"error": str(e)}, status=400)
        return Response(serializer.errors, status=400)

    @extend_schema(
        request=RegistroDemandaFormSerializer,
        responses=RegistroDemandaFormSerializer,
        description="Partially update an existing TDemanda entry"
    )
    def partial_update(self, request, pk=None):
        try:
            instance = self.get_object(pk)
            serializer = RegistroDemandaFormSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                with transaction.atomic():
                    serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

    @extend_schema(
        responses=RegistroDemandaFormSerializer,
        description="Demanda Detalle info."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)

    def get_object(self, pk):
        try:
            return TDemanda.objects.get(pk=pk)
        except TDemanda.DoesNotExist:
            raise Http404


