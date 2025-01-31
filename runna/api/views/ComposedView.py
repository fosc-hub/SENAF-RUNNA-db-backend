from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework.views import APIView
from infrastructure.models import (
    TDemanda,
    TLocalizacion,
    TPersona,
    TNNyAEducacion,
    TOrigenDemanda,
    TSubOrigenDemanda,
    TCategoriaMotivo,
    TCategoriaSubmotivo,
    TBarrio,
    TLocalidad,
    TCPC,
    TVinculoPersona,
    TCondicionesVulnerabilidad,
    TInstitucionEducativa,
    TInstitucionSanitaria,
    TGravedadVulneracion,
    TUrgenciaVulneracion,
)
from api.serializers import (
    MesaDeEntradaSerializer,
    ChoiceFieldSerializer,
    NuevoRegistroFormDropdownsSerializer
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


class NuevoRegistroFormDropdownsView(APIView):
    def get(self, request):
        # Prepare choice fields data
        estado_demanda_choices = [{"key": key, "value": value} for key, value in TDemanda.estado_demanda_choices]
        ambito_vulneracion_choices = [{"key": key, "value": value} for key, value in TDemanda.ambito_vulneracion_choices]
        
        tipo_calle_choices = [{"key": key, "value": value} for key, value in TLocalizacion.tipo_calle_choices]

        situacion_dni_choices = [{"key": key, "value": value} for key, value in TPersona.situacion_dni_choices]
        genero_choices = [{"key": key, "value": value} for key, value in TPersona.genero_choices]

        nivel_choices = [{"key": key, "value": value} for key, value in TNNyAEducacion.nivel_choices]
        turno_choices = [{"key": key, "value": value} for key, value in TNNyAEducacion.turno_choices]

        # Query related models
        origenes = TOrigenDemanda.objects.all()
        sub_origenes = TSubOrigenDemanda.objects.all()
        motivos_ingreso = TCategoriaMotivo.objects.all()
        submotivos_ingreso = TCategoriaSubmotivo.objects.all()
        barrios = TBarrio.objects.all()
        localidades = TLocalidad.objects.all()
        cpcs = TCPC.objects.all()
        vinculos_choices = TVinculoPersona.objects.all()
        condiciones_vulnerabilidad = TCondicionesVulnerabilidad.objects.all()
        instituciones_educativas = TInstitucionEducativa.objects.all()
        instituciones_sanitarias = TInstitucionSanitaria.objects.all()
        gravedades_vulneracion = TGravedadVulneracion.objects.all()
        urgencias_vulneracion = TUrgenciaVulneracion.objects.all()

        # Serialize data
        serialized_data = NuevoRegistroFormDropdownsSerializer({
            "estado_demanda_choices": estado_demanda_choices,
            "ambito_vulneracion_choices": ambito_vulneracion_choices,
            "origenes": origenes,
            "sub_origenes": sub_origenes,
            "motivos_ingreso": motivos_ingreso,
            "submotivos_ingreso": submotivos_ingreso,
            "tipo_calle_choices": tipo_calle_choices,
            "barrios": barrios,
            "localidades": localidades,
            "cpcs": cpcs,
            "situacion_dni_choices": situacion_dni_choices,
            "genero_choices": genero_choices,
            "vinculos_choices": vinculos_choices,
            "condiciones_vulnerabilidad": condiciones_vulnerabilidad,
            "nivel_choices": nivel_choices,
            "turno_choices": turno_choices,
            "instituciones_educativas": instituciones_educativas,
            "instituciones_sanitarias": instituciones_sanitarias,
            "gravedades_vulneracion": gravedades_vulneracion,
            "urgencias_vulneracion": urgencias_vulneracion,
        })

        return Response(serialized_data.data)

