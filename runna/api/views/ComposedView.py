from rest_framework.response import Response
from rest_framework.views import APIView
from infrastructure.models import (
    TDemanda,
)
from api.serializers import (
    MesaDeEntradaSerializer
)

class MesaDeEntradaView(APIView):
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
            serializer = MesaDeEntradaSerializer(demandas, many=True)
            return Response(serializer.data)
    
