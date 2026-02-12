"""
CONCEITO 8: MÉTRICAS DE CLASSIFICAÇÃO
=======================================
Cenário: Modelo prevê se imóvel vai alugar em 30 dias.

- PRECISION: "quando diz sim, acerta?"
- RECALL:    "pega todos os sins?"
- F1:        equilíbrio entre os dois
- AUC-ROC:   capacidade de separar classes (0.5=chute, 1.0=perfeito)
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    precision_score, recall_score, f1_score,
    roc_auc_score, classification_report,
)

from conceitos.dados import gerar_dados_imoveis, FEATURES


def executar():
    df = gerar_dados_imoveis()
    X = df[FEATURES]
    y = df["alugou_30dias"]

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = LogisticRegression(random_state=42, max_iter=1000).fit(X_tr, y_tr)
    y_pred = modelo.predict(X_te)

    precision = precision_score(y_te, y_pred)
    recall = recall_score(y_te, y_pred)
    f1 = f1_score(y_te, y_pred)
    auc = roc_auc_score(y_te, modelo.predict_proba(X_te)[:, 1])

    print("\n" + "=" * 70)
    print("CONCEITO 8: MÉTRICAS DE CLASSIFICAÇÃO")
    print("=" * 70)

    print(f"\n{'Precision:':<12} {precision:.3f}  → Quando diz 'vai alugar', acerta {precision:.0%}")
    print(f"{'Recall:':<12} {recall:.3f}  → Dos que realmente alugaram, pegou {recall:.0%}")
    print(f"{'F1 Score:':<12} {f1:.3f}  → Equilíbrio entre precision e recall")
    print(f"{'AUC-ROC:':<12} {auc:.3f}  → Separação de classes (0.5=chute, 1.0=perfeito)")

    print(f"\n{classification_report(y_te, y_pred, target_names=['Não alugou', 'Alugou'])}")

    # Impacto no negócio
    fp = ((y_pred == 1) & (y_te == 0)).sum()
    fn = ((y_pred == 0) & (y_te == 1)).sum()
    print(f"--- Impacto no negócio ---")
    print(f"Falsos positivos: {fp} → financeiro planejou errado")
    print(f"Falsos negativos: {fn} → perdeu oportunidades de destaque")


if __name__ == "__main__":
    executar()
