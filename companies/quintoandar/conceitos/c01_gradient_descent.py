"""
CONCEITO 1: GRADIENT DESCENT
=============================
Analogia: Descer uma montanha no escuro. Sente a inclinação, dá um passo
na direção que desce. Repete até chegar no vale.

Learning rate = tamanho do passo
- Grande demais → pula o vale
- Pequeno demais → demora eternidade
"""

import numpy as np
from conceitos.dados import gerar_dados_imoveis


def gradient_descent(X, y, learning_rate=0.01, iteracoes=100, verbose=True):
    """
    Gradient descent manual para prever preço de aluguel.

    O modelo aprende: preco = peso * area + bias

    A cada iteração:
    1. Faz previsão com os pesos atuais
    2. Calcula o erro (quão longe ficou)
    3. Calcula o gradiente (pra onde o erro diminui)
    4. Ajusta os pesos na direção que DIMINUI o erro
    """
    peso = 0.0
    bias = 0.0
    n = len(X)
    historico_erro = []

    for i in range(iteracoes):
        previsao = peso * X + bias
        erro = np.mean((previsao - y) ** 2)
        historico_erro.append(erro)

        gradiente_peso = (2 / n) * np.sum((previsao - y) * X)
        gradiente_bias = (2 / n) * np.sum(previsao - y)

        peso -= learning_rate * gradiente_peso
        bias -= learning_rate * gradiente_bias

        if verbose and i % 20 == 0:
            print(f"  Iteração {i:3d}: erro = {erro:.4f} | peso = {peso:.4f} | lr = {learning_rate}")

    return peso, bias, historico_erro


def executar():
    df = gerar_dados_imoveis()

    X_area = df["area_m2"].values
    y_preco = df["preco_ideal"].values

    # Normalizar
    X_norm = (X_area - X_area.mean()) / X_area.std()
    y_norm = (y_preco - y_preco.mean()) / y_preco.std()

    print("\n" + "=" * 70)
    print("CONCEITO 1: GRADIENT DESCENT")
    print("=" * 70)

    print("\n--- Learning rate BOM (0.01) - Desce suave ---")
    _, _, erros_bom = gradient_descent(X_norm, y_norm, learning_rate=0.01)

    print("\n--- Learning rate PEQUENO (0.001) - Demora muito ---")
    _, _, erros_lento = gradient_descent(X_norm, y_norm, learning_rate=0.001)

    print(f"\n→ Com lr=0.01, erro final: {erros_bom[-1]:.4f}")
    print(f"→ Com lr=0.001, erro final: {erros_lento[-1]:.4f} (precisaria de mais iterações)")
    print(f"\nConclusão: learning rate é o tamanho do passo.")


if __name__ == "__main__":
    executar()
