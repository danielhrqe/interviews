"""
CONCEITO 5: L1 vs L2 REGULARIZATION
=====================================
Analogia: CEO cortando custos.
- L1 (Lasso) = DEMITE funcionários que não produzem (zera features inúteis)
- L2 (Ridge) = REDUZ SALÁRIO de todo mundo (diminui todos os pesos)

Ambos combatem overfitting penalizando modelos complexos.
"""

import numpy as np
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.preprocessing import StandardScaler

from conceitos.dados import gerar_dados_imoveis, FEATURES


def executar():
    df = gerar_dados_imoveis()

    X_reg = df[FEATURES].copy()
    # Features INÚTEIS (ruído puro)
    X_reg["ruido_1"] = np.random.normal(0, 1, len(df))
    X_reg["ruido_2"] = np.random.normal(0, 1, len(df))
    X_reg["ruido_3"] = np.random.normal(0, 1, len(df))

    y = df["preco_ideal"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_reg)

    modelo_normal = LinearRegression().fit(X_scaled, y)
    modelo_l1 = Lasso(alpha=100, random_state=42).fit(X_scaled, y)
    modelo_l2 = Ridge(alpha=100, random_state=42).fit(X_scaled, y)

    print("\n" + "=" * 70)
    print("CONCEITO 5: L1 vs L2 REGULARIZATION")
    print("=" * 70)

    print(f"\n{'Feature':<20} {'Sem Reg':>10} {'L1 (Lasso)':>12} {'L2 (Ridge)':>12}")
    print("-" * 56)

    for i, feat in enumerate(X_reg.columns):
        p_normal = modelo_normal.coef_[i]
        p_l1 = modelo_l1.coef_[i]
        p_l2 = modelo_l2.coef_[i]
        marca = ""
        if feat.startswith("ruido"):
            marca = " ← RUÍDO"
        if p_l1 == 0:
            marca += " [L1 ZEROU!]"
        print(f"{feat:<20} {p_normal:>10.1f} {p_l1:>12.1f} {p_l2:>12.1f}{marca}")

    print(f"\nL1 (Lasso) ZEROU features de ruído → seleção automática!")
    print(f"L2 (Ridge) REDUZIU tudo, mas não zerou nada")


if __name__ == "__main__":
    executar()
