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

from infrastructure.models import (
    TDemanda,
    TInformante,
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
    TDemandaPersona,
    TInstitucionEducativa,
    TInstitucionSanitaria,
    TGravedadVulneracion,
    TUrgenciaVulneracion,
)
from api.serializers import (
    MesaDeEntradaSerializer,
    NuevoRegistroFormDropdownsSerializer,
    RegistroCasoFormSerializer
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
    @method_decorator(cache_page(60*15), name='get')
    def get(self, request):

        # Query related models
        informantes = TInformante.objects.all()
        origenes = TOrigenDemanda.objects.all()
        sub_origenes = TSubOrigenDemanda.objects.all()
        categoria_motivos = TCategoriaMotivo.objects.all()
        categoria_submotivos = TCategoriaSubmotivo.objects.all()
        barrios = TBarrio.objects.all()
        localidades = TLocalidad.objects.all()
        cpcs = TCPC.objects.all()
        vinculos = TVinculoPersona.objects.all()
        condiciones_vulnerabilidad = TCondicionesVulnerabilidad.objects.all()
        instituciones_educativas = TInstitucionEducativa.objects.all()
        instituciones_sanitarias = TInstitucionSanitaria.objects.all()
        gravedades_vulneracion = TGravedadVulneracion.objects.all()
        urgencias_vulneracion = TUrgenciaVulneracion.objects.all()

        # Serialize data
        serialized_data = NuevoRegistroFormDropdownsSerializer({
            "informantes": informantes,
            "origenes": origenes,
            "sub_origenes": sub_origenes,
            "categoria_motivos": categoria_motivos,
            "categoria_submotivos": categoria_submotivos,
            "barrios": barrios,
            "localidades": localidades,
            "cpcs": cpcs,
            "condiciones_vulnerabilidad": condiciones_vulnerabilidad,
            "vinculos": vinculos,
            "instituciones_educativas": instituciones_educativas,
            "instituciones_sanitarias": instituciones_sanitarias,
            "gravedades_vulneracion": gravedades_vulneracion,
            "urgencias_vulneracion": urgencias_vulneracion,
        })

        return Response(serialized_data.data)


class RegistroCasoFormView(BaseViewSet):
    model = TDemanda
    serializer_class = RegistroCasoFormSerializer
    
    http_method_names = ['post', 'patch', 'get']  # Excludes PUT, DELETE, HEAD, OPTIONS

    @extend_schema(
        request=RegistroCasoFormSerializer,
        responses=RegistroCasoFormSerializer,
        description="Create a new TDemanda entry"
    )
    def create(self, request):
        serializer = RegistroCasoFormSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    serializer.save()
                return Response(serializer.data, status=201)
            except Exception as e:
                return Response({"error": str(e)}, status=400)
        return Response(serializer.errors, status=400)

    @extend_schema(
        request=RegistroCasoFormSerializer,
        responses=RegistroCasoFormSerializer,
        description="Partially update an existing TDemanda entry"
    )
    def partial_update(self, request, pk=None):
        try:
            instance = self.get_object(pk)
            serializer = RegistroCasoFormSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                with transaction.atomic():
                    serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

    @extend_schema(
        responses=RegistroCasoFormSerializer,
        description="Demanda Detalle info."
    )
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)

    def get_object(self, pk):
        try:
            return TDemanda.objects.get(pk=pk)
        except TDemanda.DoesNotExist:
            raise Http404

