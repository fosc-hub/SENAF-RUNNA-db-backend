from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
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
from rest_framework.exceptions import NotFound
from customAuth.filters import CustomUserFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class TZonaViewSet(viewsets.ModelViewSet):
    queryset = TZona.objects.all()
    serializer_class = TZonaSerializer
    
    http_method_names = ['get']


class TCustomUserZonaViewSet(viewsets.ModelViewSet):
    queryset = TCustomUserZona.objects.all()
    serializer_class = TCustomUserZonaSerializer

    http_method_names = ['get']


class CustomUserViewSet(viewsets.ViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = CustomUserFilter

    @extend_schema(
        responses=CustomUserSerializer(many=True),
        description="Retrieve a list of all users and their related information."
    )
    def list(self, request):
        """List all users with related information."""
        # queryset = CustomUser.objects.prefetch_related('groups__permissions', 'user_permissions').all()
        queryset = CustomUser.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = CustomUserSerializer(filtered_queryset, many=True)

        return Response(serializer.data)
    
    @extend_schema(
        responses=CustomUserSerializer,
        description="Retrieve a single user by ID, including their related information."
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single user by ID."""
        try:
            # user = CustomUser.objects.prefetch_related('groups__permissions', 'user_permissions').get(pk=pk)
            user = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise NotFound(f"User with ID {pk} not found.")
        
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

class CurrentUserView(APIView):
    """
    Retrieve the details of the currently authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # This is the currently authenticated user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
