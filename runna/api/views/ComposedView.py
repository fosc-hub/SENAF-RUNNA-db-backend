from rest_framework.response import Response
from rest_framework.views import APIView
from infrastructure.models import (
    TDemanda,
)
from api.serializers import (
    ComposedDemandaSerializer
)

class ComposedDemandaView(APIView):
    def get(self, request, *args, **kwargs):
        demanda_id = self.kwargs.get("pk")
        principal = self.request.query_params.get("principal", None)
        estado_demanda = self.request.query_params.get("estado_demanda", None)
        
        try:
            demanda = TDemanda.objects.get(pk=demanda_id, principal=principal, estado_demanda=estado_demanda)
            serializer = ComposedDemandaSerializer(demanda)
            return Response(serializer.data)
        except TDemanda.DoesNotExist:
            return Response({"error": "Demanda not found"}, status=404)
