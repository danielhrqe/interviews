"""
CONCEITO 7: CLASSIFICAÇÃO vs REGRESSÃO
========================================
Duas perguntas sobre um imóvel:
- "Vai alugar em 30 dias?" → CLASSIFICAÇÃO (sim/não)
- "Qual o preço ideal?"    → REGRESSÃO (número)

Regra: resposta é categoria → classificação
       resposta é número   → regressão

PEGADINHA: Regressão Logística é CLASSIFICAÇÃO!
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression

from conceitos.dados import gerar_dados_imoveis, FEATURES


def executar():
    df = gerar_dados_imoveis()
    X = df[FEATURES]

    print("\n" + "=" * 70)
    print("CONCEITO 7: CLASSIFICAÇÃO vs REGRESSÃO")
    print("=" * 70)

    # --- CLASSIFICAÇÃO ---
    y_class = df["alugou_30dias"]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y_class, test_size=0.2, random_state=42)
    modelo_class = LogisticRegression(random_state=42, max_iter=1000).fit(X_tr, y_tr)

    print(f"\n--- CLASSIFICAÇÃO: Vai alugar em 30 dias? ---")
    print(f"Resposta: {modelo_class.predict(X_te)[:5]}  (0=não, 1=sim)")
    print(f"Tipo: CATEGORIA")

    # --- REGRESSÃO ---
    y_reg = df["preco_ideal"]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y_reg, test_size=0.2, random_state=42)
    modelo_reg = LinearRegression().fit(X_tr, y_tr)

    print(f"\n--- REGRESSÃO: Qual o preço ideal? ---")
    print(f"Resposta: {modelo_reg.predict(X_te)[:5].astype(int)}  (R$)")
    print(f"Tipo: NÚMERO CONTÍNUO")

    # PEGADINHA
    print(f"\n⚠️  PEGADINHA: LogisticRegression é CLASSIFICAÇÃO!")
    print(f"   Probabilidades: {modelo_class.predict_proba(X_te)[:3, 1].round(3)}")


if __name__ == "__main__":
    executar()
