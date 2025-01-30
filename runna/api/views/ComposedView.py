from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework.views import APIView
from infrastructure.models import (
    TDemanda,
)
from api.serializers import (
    MesaDeEntradaSerializer
)

class MesaDeEntradaPagination(PageNumberPagination):
    page_size = 5  # Number of items per page
    page_size_query_param = 'page_size'  # Allow clients to override the page size
    max_page_size = 100  # Maximum limit


class MesaDeEntradaView(APIView):
    pagination_class = MesaDeEntradaPagination

    def get(self, request, *args, **kwargs):
        demanda_id = self.kwargs.get("pk")

        if demanda_id:
            # Fetch a single demanda by ID
            try:
                demanda = TDemanda.objects.get(pk=demanda_id)
                serializer = MesaDeEntradaSerializer(demanda)
                return Response(serializer.data)
            except TDemanda.DoesNotExist:
                return Response({"error": "Demanda not found"}, status=404)
        else:
            # Fetch all demand instances
            demandas = TDemanda.objects.all()
            
            # Apply pagination
            paginator = MesaDeEntradaPagination()
            paginated_demandas = paginator.paginate_queryset(demandas, request)
            serializer = MesaDeEntradaSerializer(paginated_demandas, many=True)
            return paginator.get_paginated_response(serializer.data)
    
