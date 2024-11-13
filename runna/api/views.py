from django.shortcuts import render

# Create your views here.

'''
view example:

from rest_framework import status, viewsets
from rest_framework.response import Response

from core.use_cases import ProductUseCase
from api.serializers import ProductSerializer
from infrastructure.repositories import ProductRepository

class ProductViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_use_case = ProductUseCase()
        self.product_repo = ProductRepository()

    def list(self, request):
        """List all products."""
        products = self.product_repo.get_all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new product."""
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = self.product_use_case.create_product(**serializer.validated_data)
            self.product_repo.create(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
'''

from rest_framework import status, viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from core.use_cases import LocalizacionUseCase, UsuarioLineaUseCase, DemandaUseCase, PersonaUseCase, VulneracionUseCase #, PrecalificacionDemandaUseCase, DecisionUseCase
from api.serializers import LocalizacionModelSerializer, UsuarioLineaModelSerializer, DemandaModelSerializer, PersonaModelSerializer, VulneracionModelSerializer #, PrecalificacionDemandaModelSerializer, DecisionSerializer
from infrastructure.repositories import LocalizacionRepository, UsuarioLineaRepository, DemandaRepository, PersonaRepository, VulneracionRepository #, PrecalificacionDemandaRepository, DecisionRepository

class LocalizacionViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.localizacion_use_case = LocalizacionUseCase()
        self.localizacion_repo = LocalizacionRepository()

    @extend_schema(
        responses=LocalizacionModelSerializer(many=True),
        description="Retrieve a list of all Localizacion entries."
    )
    def list(self, request):
        """List all Localizacion."""
        localizaciones = self.localizacion_repo.get_all()
        serializer = LocalizacionModelSerializer(localizaciones, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=LocalizacionModelSerializer,
        responses=LocalizacionModelSerializer,
        description="Create a new Localizacion entry."
    )
    def create(self, request):
        """Create a new Localizacion."""
        serializer = LocalizacionModelSerializer(data=request.data)
        if serializer.is_valid():
            localizacion = self.localizacion_use_case.create_localizacion(**serializer.validated_data)
            self.localizacion_repo.create(localizacion)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioLineaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.usuario_use_case = UsuarioLineaUseCase()
        self.usuario_repo = UsuarioLineaRepository()

    def list(self, request):
        """List all UsuarioLinea."""
        usuarios = self.usuario_repo.get_all()
        serializer = UsuarioLineaModelSerializer(usuarios, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new UsuarioLinea."""
        serializer = UsuarioLineaModelSerializer(data=request.data)
        if serializer.is_valid():
            usuario = self.usuario_use_case.create_usuario_linea(**serializer.validated_data)
            self.usuario_repo.create(usuario)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DemandaViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.demanda_use_case = DemandaUseCase()
        self.demanda_repo = DemandaRepository()

    def list(self, request):
        """List all Demanda instances."""
        demandas = self.demanda_repo.get_all()
        serializer = DemandaModelSerializer(demandas, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new Demanda."""
        serializer = DemandaModelSerializer(data=request.data)
        if serializer.is_valid():
            demanda = self.demanda_use_case.create_demanda(**serializer.validated_data)
            self.demanda_repo.create(demanda)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonaViewSet(viewsets.ViewSet):
    """
    API view for listing all `Tecnico` instances with support for filtering and ordering.
    Inherits from Django REST Framework's ListAPIView to provide GET requests for the list of technicians.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.persona_use_case = PersonaUseCase()
        self.persona_repo = PersonaRepository()

    @extend_schema(
        responses=PersonaModelSerializer(many=True),
        description="Retrieve a list of all Localizacion entries."
    )
    def list(self, request):
        """List all Persona instances."""
        personas = self.persona_repo.get_all()
        serializer = PersonaModelSerializer(personas, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=PersonaModelSerializer,
        responses=PersonaModelSerializer,
        description="Create a new Localizacion entry."
    )
    def create(self, request):
        """Create a new Persona."""
        serializer = PersonaModelSerializer(data=request.data)
        if serializer.is_valid():
            persona = self.persona_use_case.create_persona(**serializer.validated_data)
            self.persona_repo.create(persona)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VulneracionViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vulneracion_use_case = VulneracionUseCase()
        self.vulneracion_repo = VulneracionRepository()

    def list(self, request):
        """List all Vulneracion instances."""
        vulneraciones = self.vulneracion_repo.get_all()
        serializer = VulneracionModelSerializer(vulneraciones, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new Vulneracion."""
        serializer = VulneracionModelSerializer(data=request.data)
        if serializer.is_valid():
            vulneracion = self.vulneracion_use_case.create_vulneracion(**serializer.validated_data)
            self.vulneracion_repo.create(vulneracion)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PrecalificacionDemandaViewSet(viewsets.ViewSet):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.precalificacion_use_case = PrecalificacionDemandaUseCase()
#         self.precalificacion_repo = PrecalificacionDemandaRepository()

#     def list(self, request):
#         """List all PrecalificacionDemanda instances."""
#         precalificaciones = self.precalificacion_repo.get_all()
#         serializer = PrecalificacionDemandaModelSerializer(precalificaciones, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         """Create a new PrecalificacionDemanda."""
#         serializer = PrecalificacionDemandaModelSerializer(data=request.data)
#         if serializer.is_valid():
#             precalificacion = self.precalificacion_use_case.create_precalificacion_demanda(**serializer.validated_data)
#             self.precalificacion_repo.create(precalificacion)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class DecisionViewSet(viewsets.ViewSet):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.decision_use_case = DecisionUseCase()
#         self.decision_repo = DecisionRepository()

#     def list(self, request):
#         """List all Decision instances."""
#         decisions = self.decision_repo.get_all()
#         serializer = DecisionSerializer(decisions, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         """Create a new Decision."""
#         serializer = DecisionSerializer(data=request.data)
#         if serializer.is_valid():
#             decision = self.decision_use_case.make_decision(**serializer.validated_data)
#             self.decision_repo.create(decision)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

