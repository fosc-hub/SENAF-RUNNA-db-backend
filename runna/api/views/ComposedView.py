import re
from django.http import Http404
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from django.db import transaction
from rest_framework.parsers import MultiPartParser, FormParser

from .BaseView import BaseViewSet
from drf_spectacular.utils import extend_schema
from django.db.models import Q
import json

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
    
    TVinculoDePersonas,
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
    
    TActividadTipo,
    TInstitucionActividad,
)
from infrastructure.filters import (
    TDemandaFilter,
)
from api.serializers import (
    RegistroDemandaFormDropdownsSerializer,
    RegistroDemandaFormSerializer,
    MesaDeEntradaSerializer,
    GestionDemandaZonaSerializer,
    TActividadDropdownSerializer,
)

class MesaDeEntradaPagination(PageNumberPagination):
    page_size = 5  # Number of items per page
    page_size_query_param = 'page_size'  # Allow clients to override the page size
    max_page_size = 100  # Maximum limit


class MesaDeEntradaListView(generics.ListAPIView):
    serializer_class = MesaDeEntradaSerializer
    pagination_class = MesaDeEntradaPagination

    # Enable filtering and ordering
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['fecha_creacion', 'estado_demanda']  # Fields allowed for sorting
    ordering = ['-fecha_creacion']  # Default sorting (descending)
    filterset_fields = ['estado_demanda', 'objetivo_de_demanda', 'tipo_demanda']  # Fields allowed for filtering

    def get_queryset(self):
        # user = self.request.user

        # # 1. Get all TCustomUserZona objects for the current user
        # user_zonas = TCustomUserZona.objects.filter(user=user)

        # # 2. Split the zones into two sets:
        # #    (a) Zones where the user is jefe or director
        # #    (b) Zones where the user is neither jefe nor director
        # zone_ids_jefe_director = user_zonas.filter(
        #     Q(jefe=True) | Q(director=True)
        # ).values_list('zona_id', flat=True)

        # zone_ids_normal = user_zonas.filter(
        #     jefe=False, director=False
        # ).values_list('zona_id', flat=True)

        # # 3. Build Q objects to handle the OR conditions

        # # (i) For jefe/director zones, include:
        # #     - All TDemanda objects linked via TDemandaZona to those zones
        # #       (tdemandazona__zona__in=zone_ids_jefe_director)
        # #     - All TDemanda objects that have registrado_por_user_zona in those zones
        # q_jefe_director = (
        #     Q(tdemandazona__zona__in=zone_ids_jefe_director) |
        #     Q(registrado_por_user_zona__in=zone_ids_jefe_director)
        # )

        # # (ii) For non-jefe/director zones, include TDemanda objects linked 
        # #      via TDemandaZona and having esta_activo=True
        # q_normal = (
        #     Q(tdemandazona__zona__in=zone_ids_normal) &
        #     Q(tdemandazona__esta_activo=True)
        # )

        # # 4. Also include TDemanda objects registered directly by the user
        # #    (via registrado_por_user)
        # q_registered_by_user = Q(registrado_por_user=user)

        # # Combine all three conditions with OR
        # final_filter = q_jefe_director | q_normal | q_registered_by_user

        # # Return the distinct results so that the same TDemanda isn't repeated
        # return TDemanda.objects.filter(final_filter).distinct()
        return TDemanda.objects.all()

class RegistroDemandaFormDropdownsView(APIView):
    # @method_decorator(cache_page(60*15), name='get')
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

        vinculo_de_personas = TVinculoDePersonas.objects.all()
        institucion_educativa = TInstitucionEducativa.objects.all()
        institucion_sanitaria = TInstitucionSanitaria.objects.all()
        situacion_salud = TSituacionSalud.objects.all()
        enfermedad = TEnfermedad.objects.all()

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

            "vinculo_con_nnya_principal_choices": vinculo_de_personas,
            "institucion_educativa": institucion_educativa,
            "institucion_sanitaria": institucion_sanitaria,
            "situacion_salud": situacion_salud,
            "enfermedad": enfermedad,

            "categoria_motivo": categoria_motivo,
            "categoria_submotivo": categoria_submotivo,
            "gravedad_vulneracion": gravedad_vulneracion,
            "urgencia_vulneracion": urgencia_vulneracion,
            "condiciones_vulnerabilidad": condiciones_vulnerabilidad,
            
            "zonas": zonas,
            
        })

        return Response(serialized_data.data)

def process_files(final_data, files_dict):
    for key in files_dict:
        files = files_dict.getlist(key)
        # Procesar archivos que siguen el patrón específico
        certificado_pattern = r'^personas\[(\d+)\]persona_enfermedades\[(\d+)\]certificado_adjunto\[(\d+)\]archivo$'
        match = re.match(certificado_pattern, key)
        if match:
            persona_index = int(match.group(1))
            enfermedad_index = int(match.group(2))
            # Inicializar la estructura si es necesario
            if "personas" not in final_data:
                final_data["personas"] = []
            while len(final_data["personas"]) <= persona_index:
                final_data["personas"].append({})
            if "persona_enfermedades" not in final_data["personas"][persona_index]:
                final_data["personas"][persona_index]["persona_enfermedades"] = []
            while len(final_data["personas"][persona_index]["persona_enfermedades"]) <= enfermedad_index:
                final_data["personas"][persona_index]["persona_enfermedades"].append({})
            if "certificado_adjunto" not in final_data["personas"][persona_index]["persona_enfermedades"][enfermedad_index]:
                final_data["personas"][persona_index]["persona_enfermedades"][enfermedad_index]["certificado_adjunto"] = []
            for f in files:
                final_data["personas"][persona_index]["persona_enfermedades"][enfermedad_index]["certificado_adjunto"].append({"archivo": f})
        else:
            # Procesar archivos generales
            if "adjuntos" not in final_data:
                final_data["adjuntos"] = []
            for f in files:
                final_data["adjuntos"].append({"archivo": f})
    return final_data

class RegistroDemandaFormView(BaseViewSet):
    model = TDemanda
    serializer_class = RegistroDemandaFormSerializer
    http_method_names = ['post', 'patch', 'get']

    @extend_schema(
        request=RegistroDemandaFormSerializer,
        responses=RegistroDemandaFormSerializer,
        description="Create a new TDemanda entry"
    )
    def create(self, request):
        data_field = request.data.get("data")
        if data_field:
            try:
                final_data = json.loads(data_field)
            except json.JSONDecodeError:
                return Response({"error": "JSON inválido en el campo 'data'."}, status=400)
        else:
            final_data = {}

        final_data = process_files(final_data, request.FILES)
        serializer = RegistroDemandaFormSerializer(data=final_data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    demanda = serializer.save()
                return Response({
                    "message_encrypted": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",  # Token de ejemplo
                    "demanda": demanda.pk
                }, status=201)
            except Exception as e:
                return Response({"error": str(e)}, status=400)
        return Response(serializer.errors, status=400)

    @extend_schema(
        request=RegistroDemandaFormSerializer,
        responses=RegistroDemandaFormSerializer,
        description="Partially update an existing TDemanda entry"
    )
    def partial_update(self, request, pk=None):
        data_field = request.data.get("data")
        if data_field:
            try:
                final_data = json.loads(data_field)
            except json.JSONDecodeError:
                return Response({"error": "JSON inválido en el campo 'data'."}, status=400)
        else:
            final_data = {}

        final_data = process_files(final_data, request.FILES)

        try:
            instance = self.get_object(pk)
            serializer = RegistroDemandaFormSerializer(instance, data=final_data, partial=True)
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
        
class GestionDemandaZonaZonaView(APIView):
    def get(self, request, pk):
        try:
            demanda = TDemanda.objects.get(pk=pk)
        except TDemanda.DoesNotExist:
            raise Http404

        demanda_zonas = TDemandaZona.objects.filter(demanda=demanda, esta_activo=True)
        zonas = TZona.objects.all()
        users = CustomUser.objects.all()
        serialized_data = GestionDemandaZonaSerializer({
            "demanda_zonas": demanda_zonas,
            "zonas": zonas,
            "users": users,
        })

        return Response(serialized_data.data)


class TActividadDropdownView(APIView):
    # @method_decorator(cache_page(60*15), name='get')
    def get(self, request):
        actividad_tipo = TActividadTipo.objects.all()
        institucion_actividad = TInstitucionActividad.objects.all()
        
        serialized_data = TActividadDropdownSerializer({
            "tipos_actividad": actividad_tipo,
            "instituciones_actividad": institucion_actividad,
        })

        return Response(serialized_data.data)