"""
CONCEITO 2: OVERFITTING vs UNDERFITTING
========================================
Analogia: Estudar pra prova.
- Overfitting  = decorou a prova anterior. Tira 10 nela, 2 na nova.
- Underfitting = leu só o título do livro. Tira 3 em qualquer prova.
- Ideal        = entendeu a matéria. Tira 8 em qualquer prova.

COMO DETECTAR:
- Overfitting:  treino 99%, teste 60%
- Underfitting: treino 55%, teste 50%
- Ideal:        treino 90%, teste 87%
"""

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from conceitos.dados import gerar_dados_imoveis, FEATURES


def executar():
    df = gerar_dados_imoveis()
    X = df[FEATURES]
    y = df["alugou_30dias"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelos = {
        "Árvore depth=1 (simples)": DecisionTreeClassifier(max_depth=1, random_state=42),
        "Árvore depth=∞ (complexa)": DecisionTreeClassifier(max_depth=None, random_state=42),
        "Árvore depth=5 (equilibrada)": DecisionTreeClassifier(max_depth=5, random_state=42),
    }

    diagnosticos = {
        "Árvore depth=1 (simples)": "UNDERFITTING (não aprendeu)",
        "Árvore depth=∞ (complexa)": "OVERFITTING (decorou)",
        "Árvore depth=5 (equilibrada)": "IDEAL (generalizou)",
    }

    print("\n" + "=" * 70)
    print("CONCEITO 2: OVERFITTING vs UNDERFITTING")
    print("=" * 70)
    print(f"\n{'Modelo':<30} {'Treino':>8} {'Teste':>8}  Diagnóstico")
    print("-" * 75)

    for nome, modelo in modelos.items():
        modelo.fit(X_train, y_train)
        acc_train = accuracy_score(y_train, modelo.predict(X_train))
        acc_test = accuracy_score(y_test, modelo.predict(X_test))
        print(f"{nome:<30} {acc_train:>7.0%} {acc_test:>7.0%}  ← {diagnosticos[nome]}")

    print(f"\nmax_depth é um HIPERPARÂMETRO - definido pelo engenheiro, não pelo modelo.")


if __name__ == "__main__":
    executar()
