"""
13 Conceitos de ML - Contexto QuintoAndar
==========================================
Rode todos os conceitos ou um específico:

  uv run main.py              → roda todos
  uv run main.py 1            → gradient descent
  uv run main.py 6            → data drift vs concept drift
  uv run main.py 1 2 3        → múltiplos conceitos
"""

import sys
import warnings

from conceitos import (
    c01_gradient_descent,
    c02_overfitting_underfitting,
    c03_bias_variance,
    c04_cross_validation,
    c05_regularizacao,
    c06_drift,
    c07_classificacao_regressao,
    c08_metricas_classificacao,
    c09_metricas_regressao,
    c10_metricas_ranking,
    c11_tipos_aprendizado,
    c12_deep_learning_genai,
)
from conceitos.dados import gerar_dados_imoveis, exibir_resumo

warnings.filterwarnings("ignore")

CONCEITOS = {
    1: ("Gradient Descent", c01_gradient_descent),
    2: ("Overfitting vs Underfitting", c02_overfitting_underfitting),
    3: ("Bias-Variance Tradeoff", c03_bias_variance),
    4: ("Cross-Validation (K-Fold)", c04_cross_validation),
    5: ("L1 vs L2 Regularization", c05_regularizacao),
    6: ("Data Drift vs Concept Drift", c06_drift),
    7: ("Classificação vs Regressão", c07_classificacao_regressao),
    8: ("Métricas de Classificação", c08_metricas_classificacao),
    9: ("Métricas de Regressão", c09_metricas_regressao),
    10: ("Métricas de Ranking (NDCG, MRR)", c10_metricas_ranking),
    11: ("Supervised vs Unsupervised vs Reinforcement", c11_tipos_aprendizado),
    12: ("Deep Learning + GenAI", c12_deep_learning_genai),
}


def listar_conceitos():
    print("\nConceitos disponíveis:")
    for num, (nome, _) in CONCEITOS.items():
        print(f"  {num:>2}. {nome}")
    print(f"\nUso: uv run main.py [número(s)]")


def _exibir_resumo_final():
    print("\n" + "=" * 70)
    print("RESUMO FINAL - COLA PRA ENTREVISTA")
    print("=" * 70)
    print("""
┌──────────────────────┬──────────────────────────────────────────────┐
│ Conceito             │ Frase de entrevista                          │
├──────────────────────┼──────────────────────────────────────────────┤
│ Gradient Descent     │ Minimiza erro iterativamente.                │
│                      │ Learning rate = tamanho do passo.            │
├──────────────────────┼──────────────────────────────────────────────┤
│ Overfitting          │ Decorou treino. Treino 99%, teste 60%.       │
│                      │ Resolver: regularização, reduzir complexidade│
├──────────────────────┼──────────────────────────────────────────────┤
│ Underfitting         │ Simples demais. Treino e teste ruins.        │
├──────────────────────┼──────────────────────────────────────────────┤
│ Bias-Variance        │ Bias=underfitting, Variance=overfitting.     │
│                      │ Equilibrar os dois é o objetivo.             │
├──────────────────────┼──────────────────────────────────────────────┤
│ Cross-Validation     │ K-Fold: múltiplas divisões, score = média.   │
├──────────────────────┼──────────────────────────────────────────────┤
│ L1 (Lasso)           │ Zera features inúteis = seleção automática.  │
│ L2 (Ridge)           │ Reduz pesos sem zerar.                       │
├──────────────────────┼──────────────────────────────────────────────┤
│ Data Drift           │ INPUTS mudaram (novos perfis).               │
│ Concept Drift        │ Relação INPUT→OUTPUT mudou.                  │
├──────────────────────┼──────────────────────────────────────────────┤
│ Classificação        │ Prevê CATEGORIA. Métricas: P/R/F1/AUC.      │
│ Regressão            │ Prevê NÚMERO. Métricas: MAE/RMSE/R².        │
├──────────────────────┼──────────────────────────────────────────────┤
│ NDCG/MRR             │ Qualidade do ranking. NDCG=lista, MRR=1º bom│
├──────────────────────┼──────────────────────────────────────────────┤
│ Supervised           │ Com labels. Unsupervised: sem. RL: recompensa│
├──────────────────────┼──────────────────────────────────────────────┤
│ CNN/RNN/Transformer  │ Imagens / Sequências / Atenção (base LLMs)  │
├──────────────────────┼──────────────────────────────────────────────┤
│ RAG                  │ LLM + busca em docs. Reduz alucinação.       │
│ Embeddings           │ Texto → vetor. Similares ficam próximos.     │
└──────────────────────┴──────────────────────────────────────────────┘
""")


def main():
    args = sys.argv[1:]

    if args and args[0] in ("--help", "-h", "help"):
        listar_conceitos()
        return

    if args:
        nums = [int(a) for a in args if a.isdigit()]
    else:
        nums = list(CONCEITOS.keys())

    df = gerar_dados_imoveis()
    exibir_resumo(df)

    for num in nums:
        if num in CONCEITOS:
            CONCEITOS[num][1].executar()
        else:
            print(f"\nConceito {num} não encontrado.")
            listar_conceitos()

    if len(nums) == len(CONCEITOS):
        _exibir_resumo_final()


if __name__ == "__main__":
    main()
