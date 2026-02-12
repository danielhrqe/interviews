"""
CONCEITO 9: MÉTRICAS DE REGRESSÃO
===================================
Cenário: Modelo prevê preço ideal de aluguel.

- MAE:  erro médio em reais ("em média, erro por R$ 200")
- MSE:  erro ao quadrado (penaliza erros grandes MUITO mais)
- RMSE: raiz do MSE (volta pra reais)
- R²:   quanto o modelo explica (0.85 = explica 85%)
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from conceitos.dados import gerar_dados_imoveis, FEATURES


def executar():
    df = gerar_dados_imoveis()
    X = df[FEATURES]
    y = df["preco_ideal"]

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = LinearRegression().fit(X_tr, y_tr)
    y_pred = modelo.predict(X_te)

    mae = mean_absolute_error(y_te, y_pred)
    mse = mean_squared_error(y_te, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_te, y_pred)

    print("\n" + "=" * 70)
    print("CONCEITO 9: MÉTRICAS DE REGRESSÃO")
    print("=" * 70)

    print(f"\n{'MAE:':<8} R$ {mae:,.0f}   → Em média, erra R$ {mae:,.0f}")
    print(f"{'MSE:':<8} {mse:,.0f}  → Penaliza erros grandes")
    print(f"{'RMSE:':<8} R$ {rmse:,.0f}   → Raiz do MSE")
    print(f"{'R²:':<8} {r2:.3f}     → Explica {r2:.0%} da variação")

    print(f"\n--- Exemplos ---")
    for i in range(5):
        real = y_te.iloc[i]
        pred = y_pred[i]
        print(f"Imóvel {i + 1}: Real R$ {real:,.0f} | Previsto R$ {pred:,.0f} | Erro R$ {abs(real - pred):,.0f}")


if __name__ == "__main__":
    executar()
