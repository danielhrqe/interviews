"""
CONCEITO 6: DATA DRIFT vs CONCEPT DRIFT
=========================================
Analogia da Pizzaria:
- Data drift    = mudou o BAIRRO (perfil dos clientes mudou)
- Concept drift = mudou o COMPORTAMENTO (sexta não é mais dia de pizza)

QuintoAndar:
- Data drift    = expansão pra novas cidades → perfil dos imóveis mudou
- Concept drift = home office → "perto do metrô" perdeu importância

Cola mental:
- Mudou QUEM ENTRA no modelo     → data drift
- Mudou O QUE SIGNIFICA          → concept drift
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from conceitos.dados import gerar_dados_imoveis, FEATURES


def executar():
    df = gerar_dados_imoveis()

    # Treinar modelo só com SP (cenário original)
    dados_sp = df[df["cidade"] == "SP"].copy()
    X_sp = dados_sp[FEATURES]
    y_sp = dados_sp["alugou_30dias"]

    modelo = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    modelo.fit(X_sp, y_sp)
    score_sp = accuracy_score(y_sp, modelo.predict(X_sp))

    print("\n" + "=" * 70)
    print("CONCEITO 6: DATA DRIFT vs CONCEPT DRIFT")
    print("=" * 70)

    # --- DATA DRIFT ---
    dados_outras = df[df["cidade"] != "SP"].copy()
    X_outras = dados_outras[FEATURES]
    y_outras = dados_outras["alugou_30dias"]
    score_drift = accuracy_score(y_outras, modelo.predict(X_outras))

    print(f"\n--- DATA DRIFT: Expansão para novas cidades ---")
    print(f"Performance em SP:            {score_sp:.3f}")
    print(f"Performance novas cidades:    {score_drift:.3f} (queda: {score_sp - score_drift:.3f})")
    print(f"→ Os INPUTS mudaram (perfil diferente) = DATA DRIFT")

    # --- CONCEPT DRIFT ---
    dados_pandemia = dados_sp.copy()
    score_sem_metro = (
        -0.3 * dados_pandemia["preco_aluguel"] / 1000
        + 0.5 * dados_pandemia["nota_bairro"]
        + 0.4 * dados_pandemia["fotos_qualidade"] * 10
        + 0.1 * dados_pandemia["quartos"]
        + np.random.normal(0, 1, len(dados_pandemia))
        # dist_metro REMOVIDO - não importa mais
    )
    y_novo = (score_sem_metro > score_sem_metro.median()).astype(int)
    score_concept = accuracy_score(y_novo, modelo.predict(X_sp))

    print(f"\n--- CONCEPT DRIFT: Home office pós-pandemia ---")
    print(f"Performance no mundo novo:    {score_concept:.3f} (queda: {score_sp - score_concept:.3f})")
    print(f"→ A RELAÇÃO input→output mudou = CONCEPT DRIFT")
    print(f"  (mesmos imóveis, mas 'perto do metrô' perdeu relevância)")

    print(f"\n{'='*50}")
    print(f"RESUMO:")
    print(f"  Data drift    = inputs mudaram")
    print(f"  Concept drift = relação input→output mudou")
    print(f"  Ambos exigem RETREINAMENTO")
    print(f"{'='*50}")


if __name__ == "__main__":
    executar()
