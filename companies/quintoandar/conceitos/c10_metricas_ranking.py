"""
CONCEITO 10: MÉTRICAS DE RANKING (NDCG, MRR)
==============================================
Cenário: Ranking de imóveis na busca do QuintoAndar.
Usuário pesquisou "apartamento 2 quartos em Pinheiros".

- NDCG: os MELHORES estão no TOPO? Penaliza resultados bons enterrados.
- MRR:  quão rápido o usuário encontra o PRIMEIRO resultado bom?

Offline: NDCG/MRR
Online:  CTR + taxa de agendamento (A/B test)
"""

import numpy as np
from sklearn.metrics import ndcg_score


def calcular_mrr(rankings):
    """MRR = em que posição está o PRIMEIRO resultado relevante?"""
    mrrs = []
    for ranking in rankings:
        for i, relevancia in enumerate(ranking):
            if relevancia >= 2:
                mrrs.append(1.0 / (i + 1))
                break
    return np.mean(mrrs)


def executar():
    # Relevância: 0=irrelevante, 1=ok, 2=bom, 3=perfeito
    ranking_bom = np.array([[3, 3, 2, 2, 1, 1, 0, 0, 0, 0]])
    ranking_ruim = np.array([[0, 0, 1, 0, 0, 2, 0, 3, 3, 0]])
    ranking_perfeito = np.array([[3, 3, 2, 2, 1, 1, 0, 0, 0, 0]])

    ndcg_bom = ndcg_score(ranking_perfeito, ranking_bom)
    ndcg_ruim = ndcg_score(ranking_perfeito, ranking_ruim)
    mrr_bom = calcular_mrr(ranking_bom)
    mrr_ruim = calcular_mrr(ranking_ruim)

    print("\n" + "=" * 70)
    print("CONCEITO 10: MÉTRICAS DE RANKING (NDCG, MRR)")
    print("=" * 70)

    print(f"\nBusca: 'apartamento 2 quartos Pinheiros' → 10 resultados")
    print(f"\nRanking BOM:  {ranking_bom[0].tolist()}")
    print(f"  NDCG: {ndcg_bom:.3f}  |  MRR: {mrr_bom:.3f}")
    print(f"\nRanking RUIM: {ranking_ruim[0].tolist()}")
    print(f"  NDCG: {ndcg_ruim:.3f}  |  MRR: {mrr_ruim:.3f}")

    print(f"\nNDCG → qualidade da lista INTEIRA")
    print(f"MRR  → quão rápido acha o PRIMEIRO bom")
    print(f"QuintoAndar: NDCG@10 offline + CTR/agendamento online")


if __name__ == "__main__":
    executar()
