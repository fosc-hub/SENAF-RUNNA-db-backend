from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from core.use_cases import TDecisionUseCase
from infrastructure.models import TNNyAScore, TDemandaScore, TDemandaPersona
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
    def get(self, request, demanda_id):
        try:
            demanda_score = TDemandaScore.objects.get(demanda=demanda_id)
            nnyas = TDemandaPersona.objects.filter(demanda=demanda_id, persona__nnya=True)
            print(f"NNyAs: {nnyas}")
            if not nnyas.exists():
                return Response(
                    {"error": "No NNyA associated with the given Demanda."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Find the NNyA with the highest score
            highest_score_nnya = None
            highest_score = -1
            for demanda_persona in nnyas:
                try:
                    nnya_score = TNNyAScore.objects.get(nnya=demanda_persona.persona)
                    if nnya_score.score > highest_score:
                        highest_score = nnya_score.score
                        highest_score_nnya = nnya_score
                except TNNyAScore.DoesNotExist:
                    continue

            if highest_score_nnya is None:
                return Response(
                    {"error": "No scores found for NNyAs associated with the given Demanda."},
                    status=status.HTTP_404_NOT_FOUND
                )
        except TDemandaScore.DoesNotExist:
            return Response(
                {"error": "Demanda with the given ID does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Use case logic
        decision_use_case = TDecisionUseCase()
        suggestion = decision_use_case.suggest_decision(highest_score_nnya, demanda_score)
        suggestion["NNyA"] = TPersonaSerializer(highest_score_nnya.nnya).data
        

        return Response(suggestion, status=status.HTTP_200_OK)
