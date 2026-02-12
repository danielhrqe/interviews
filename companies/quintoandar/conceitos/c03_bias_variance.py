"""
CONCEITO 3: BIAS-VARIANCE TRADEOFF
====================================
Analogia: Jogadores de dardo.
- Alto Bias:     dardos agrupados, mas longe do centro (consistente, errado)
- Alta Variance: dardos espalhados, mas na média perto do centro (instável)

Conexão direta:
- Alto bias   = underfitting
- Alta variance = overfitting
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from conceitos.dados import gerar_dados_imoveis, FEATURES


def executar():
    df = gerar_dados_imoveis()
    X = df[FEATURES]
    y = df["alugou_30dias"]

    print("\n" + "=" * 70)
    print("CONCEITO 3: BIAS-VARIANCE TRADEOFF")
    print("=" * 70)
    print(f"\nTreinando o mesmo modelo em 5 amostras diferentes:\n")

    resultados_simples = []
    resultados_complexo = []

    for i in range(5):
        X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=i)

        m_simples = DecisionTreeClassifier(max_depth=1, random_state=42)
        m_simples.fit(X_tr, y_tr)
        acc_s = accuracy_score(y_te, m_simples.predict(X_te))
        resultados_simples.append(acc_s)

        m_complexo = DecisionTreeClassifier(max_depth=None, random_state=42)
        m_complexo.fit(X_tr, y_tr)
        acc_c = accuracy_score(y_te, m_complexo.predict(X_te))
        resultados_complexo.append(acc_c)

        print(f"  Amostra {i + 1}: Simples={acc_s:.3f}  |  Complexo={acc_c:.3f}")

    print(f"\n  {'Simples (depth=1):':<28} média={np.mean(resultados_simples):.3f}, variação={np.std(resultados_simples):.3f}")
    print(f"  {'Complexo (depth=∞):':<28} média={np.mean(resultados_complexo):.3f}, variação={np.std(resultados_complexo):.3f}")
    print(f"\nSimples: consistente mas baixo (ALTO BIAS)")
    print(f"Complexo: varia entre amostras (ALTA VARIANCE)")


if __name__ == "__main__":
    executar()
