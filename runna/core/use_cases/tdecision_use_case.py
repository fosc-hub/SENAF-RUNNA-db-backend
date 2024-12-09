from core.entities import NNyAScore, DemandaScore, Persona, Demanda

class TDecisionUseCase:
    """
    Logic to suggest a decision based on scores.
    """
    DECISION_CHOICES = [
        ('APERTURA DE LEGAJO', 'Apertura de Legajo'),
        ('RECHAZAR CASO', 'Rechazar Caso'),
    ]

    def suggest_decision(self, nnya: NNyAScore, demanda: DemandaScore) -> dict:
        """
        Suggest a decision based on the NNyA's score and related TDemanda scores.
        """
        nnya_score = nnya.score if hasattr(nnya, 'score') else 0
        # print(nnya.__dict__)

        demanda_score = demanda.score if hasattr(demanda, 'score') else 0
        # print(demanda.__dict__)

        # Collect scores from all related TDemandas
        # demanda_scores = [demanda.score for demanda in nnya.tdemanda_set.all()]
        # max_demanda_score = max(demanda_scores, default=0)

        # Logic for suggesting a decision
        if nnya_score > 10 and demanda_score > 10:
            return {
                "decision": "APERTURA DE LEGAJO",
                "reason": f"Dado el alto score del nnya ({nnya_score}), y el alto score de la demanda ({demanda_score}), la decision sugerida es APERTURA DE LEGAJO.",
                "Demanda Scores": {
                    "score": getattr(demanda, 'score', None),
                    "score_condiciones_vulnerabilidad": getattr(demanda, 'score_condiciones_vulnerabilidad', None),
                    "score_vulneracion": getattr(demanda, 'score_vulneracion', None),
                    "score_motivos_intervencion": getattr(demanda, 'score_motivos_intervencion', None),
                    "score_indicadores_valoracion": getattr(demanda, 'score_indicadores_valoracion', None)
                },
                "NNyA Scores": {
                    "score": getattr(nnya, 'score', None),
                    "score_condiciones_vulnerabilidad": getattr(nnya, 'score_condiciones_vulnerabilidad', None),
                    "score_vulneracion": getattr(nnya, 'score_vulneracion', None),
                    "score_motivos_intervencion": getattr(nnya, 'score_motivos_intervencion', None)
                }
            }
        else:
            return {
                "decision": "RECHAZAR CASO",
                "reason": f"El score del nnya ({nnya_score}), y el score de la demanda ({demanda_score}), no suponen un riesgo, por lo tanto la sugerencia es RECHAZAR CASO.",
                "Demanda Scores": {
                    "score": getattr(demanda, 'score', None),
                    "score_condiciones_vulnerabilidad": getattr(demanda, 'score_condiciones_vulnerabilidad', None),
                    "score_vulneracion": getattr(demanda, 'score_vulneracion', None),
                    "score_motivos_intervencion": getattr(demanda, 'score_motivos_intervencion', None),
                    "score_indicadores_valoracion": getattr(demanda, 'score_indicadores_valoracion', None)
                },
                "NNyA Scores": {
                    "score": getattr(nnya, 'score', None),
                    "score_condiciones_vulnerabilidad": getattr(nnya, 'score_condiciones_vulnerabilidad', None),
                    "score_vulneracion": getattr(nnya, 'score_vulneracion', None),
                }
            }
