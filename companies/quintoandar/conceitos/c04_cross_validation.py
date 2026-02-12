"""
CONCEITO 4: CROSS-VALIDATION (K-Fold)
======================================
Analogia: Professor aplica 5 provas diferentes ao invés de 1.
Nota final = média das 5. Muito mais confiável.

K-Fold com K=5:
- Divide dados em 5 partes
- Treina em 4, testa em 1
- Repete 5 vezes, cada parte sendo teste uma vez
- Score final = média
"""

from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from conceitos.dados import gerar_dados_imoveis, FEATURES


def executar():
    df = gerar_dados_imoveis()
    X = df[FEATURES]
    y = df["alugou_30dias"]

    modelo = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)

    # Train/Test simples
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo.fit(X_tr, y_tr)
    score_simples = accuracy_score(y_te, modelo.predict(X_te))

    # Cross-validation K=5
    scores_cv = cross_val_score(modelo, X, y, cv=5, scoring="accuracy")

    print("\n" + "=" * 70)
    print("CONCEITO 4: CROSS-VALIDATION (K-Fold)")
    print("=" * 70)

    print(f"\nTrain/Test simples (1 divisão):")
    print(f"  Score: {score_simples:.3f}")
    print(f"  Problema: pode ter tido 'sorte' na divisão\n")

    print(f"Cross-Validation K=5 (5 divisões):")
    for i, score in enumerate(scores_cv):
        print(f"  Fold {i + 1}: {score:.3f}")
    print(f"  Média: {scores_cv.mean():.3f} ± {scores_cv.std():.3f}")

    print(f"\n--- Como o K-Fold divide os dados ---")
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    for i, (train_idx, test_idx) in enumerate(kf.split(X)):
        print(f"  Fold {i + 1}: treina com {len(train_idx)}, testa com {len(test_idx)}")


if __name__ == "__main__":
    executar()
