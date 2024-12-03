from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from core.use_cases import TDecisionUseCase
from infrastructure.models import TNNyAScore, TDemandaScore
from api.serializers import TPersonaSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
class SuggestDecisionView(APIView):
    permission_classes = [AllowAny]
    """
    API endpoint to suggest a decision for a given NNyA.
    """
    @extend_schema(
        responses={
            200: dict,
        },
        description="Suggest a decision based on NNyA and related Demanda scores."
    )
    def get(self, request, nnya_id, demanda_id):
        try:
            # Fetch the NNyA object
            nnya_score = TNNyAScore.objects.get(nnya=nnya_id)
            demanda_score = TDemandaScore.objects.get(demanda=demanda_id)
        except TNNyAScore.DoesNotExist:
            return Response(
                {"error": "NNyA with the given ID does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        except TDemandaScore.DoesNotExist:
            return Response(
                {"error": "Demanda with the given ID does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Use case logic
        decision_use_case = TDecisionUseCase()
        suggestion = decision_use_case.suggest_decision(nnya_score, demanda_score)

        return Response(suggestion, status=status.HTTP_200_OK)
