from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class BaseViewSet(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    model = None
    serializer_class = None
    filterset_class = None

    @extend_schema(
        responses=None,  # To be overridden in subclasses
        description="Retrieve a list of entries with optional filtering."
    )
    def list(self, request):
        """List all entries."""
        queryset = self.model.objects.all()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filtered_queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        responses=None,  # To be overridden in subclasses
        description="Retrieve a single entry"
    )
    def retrieve(self, request, pk=None):
        """Retrieve a single entry."""
        try:
            obj = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise NotFound(f"{self.model.__name__} with ID {pk} not found.")
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    @extend_schema(
        request=None,  # To be overridden in subclasses
        responses=None,  # To be overridden in subclasses
        description="Create a new entry"
    )
    def create(self, request):
        """Create a new entry."""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=None,  # To be overridden in subclasses
        responses=None,  # To be overridden in subclasses
        description="Partially update an existing entry"
    )
    def partial_update(self, request, pk=None):
        """Partially update an existing entry."""
        try:
            obj = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise NotFound(f"{self.model.__name__} with ID {pk} not found.")
        
        serializer = self.serializer_class(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)
