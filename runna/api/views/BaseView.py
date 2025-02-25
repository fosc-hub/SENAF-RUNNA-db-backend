from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError as DRFValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny

class BaseViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
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

        try:
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()
            return Response(self.serializer_class(instance).data, status=status.HTTP_201_CREATED)
        except DRFValidationError as e:
            # Handles serializer validation errors
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        except DjangoValidationError as e:
            # Handles model-level validation errors
            return Response({"ValidationError": e.messages}, status=status.HTTP_400_BAD_REQUEST)

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

        try:
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()
            return Response(self.serializer_class(instance).data)
        except DRFValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        except DjangoValidationError as e:
            return Response({"ValidationError": e.messages}, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses=None,  # To be overridden in subclasses
        description="Delete an existing entry"
    )
    def destroy(self, request, pk=None):
        """Delete an existing entry."""
        try:
            obj = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise NotFound(f"{self.model.__name__} with ID {pk} not found.")
        
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def filter_queryset(self, queryset):
        """Applies filters to the queryset."""
        filter_backend = DjangoFilterBackend()
        return filter_backend.filter_queryset(self.request, queryset, self)
