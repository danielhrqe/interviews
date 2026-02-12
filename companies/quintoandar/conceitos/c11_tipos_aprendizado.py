"""
CONCEITO 11: SUPERVISED vs UNSUPERVISED vs REINFORCEMENT
==========================================================
Analogia: Três formas de ensinar uma criança.
- Supervised:    mostra fotos COM etiqueta. Tem professor.
- Unsupervised:  mostra fotos SEM etiqueta. Agrupa sozinha.
- Reinforcement: aprende jogando. Ganha ponto ou perde vida.
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from conceitos.dados import gerar_dados_imoveis, FEATURES


def executar():
    df = gerar_dados_imoveis()
    X = df[FEATURES]
    y = df["alugou_30dias"]

    print("\n" + "=" * 70)
    print("CONCEITO 11: SUPERVISED vs UNSUPERVISED vs REINFORCEMENT")
    print("=" * 70)

    # SUPERVISED
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = LogisticRegression(random_state=42, max_iter=1000).fit(X_tr, y_tr)

    print(f"\n--- SUPERVISED: Prever se aluga em 30 dias ---")
    print(f"Temos LABELS (resposta certa)")
    print(f"Accuracy: {accuracy_score(y_te, modelo.predict(X_te)):.3f}")

    # UNSUPERVISED
    features_cluster = ["area_m2", "quartos", "preco_aluguel", "dist_metro_km"]
    X_cluster = StandardScaler().fit_transform(df[features_cluster])
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(X_cluster)

    print(f"\n--- UNSUPERVISED: Agrupar imóveis similares ---")
    print(f"SEM labels - descobre padrões sozinho\n")
    for c in range(4):
        g = df[df["cluster"] == c]
        print(f"  Grupo {c}: {len(g)} imóveis | {g['area_m2'].mean():.0f}m² | R$ {g['preco_aluguel'].mean():,.0f}")

    # REINFORCEMENT
    print(f"\n--- REINFORCEMENT LEARNING (conceitual) ---")
    print(f"QuintoAndar: otimizar preço de aluguel em tempo real")
    print(f"  Aluga rápido = recompensa positiva")
    print(f"  Demora = recompensa negativa")
    print(f"  Também usado em LLMs (RLHF)")


if __name__ == "__main__":
    executar()
