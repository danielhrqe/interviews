"""
Dados simulados do QuintoAndar.
Compartilhados por todos os conceitos.
"""

import numpy as np
import pandas as pd


FEATURES = [
    "area_m2", "quartos", "vagas_garagem", "andar",
    "dist_metro_km", "nota_bairro", "fotos_qualidade",
]

SEED = 42
N_IMOVEIS = 1000


def gerar_dados_imoveis(n: int = N_IMOVEIS, seed: int = SEED) -> pd.DataFrame:
    """Gera dataset de imóveis simulando o contexto QuintoAndar."""
    np.random.seed(seed)

    df = pd.DataFrame({
        "area_m2": np.random.normal(70, 25, n).clip(20, 200),
        "quartos": np.random.choice([1, 2, 3, 4], n, p=[0.2, 0.4, 0.3, 0.1]),
        "vagas_garagem": np.random.choice([0, 1, 2], n, p=[0.3, 0.5, 0.2]),
        "andar": np.random.randint(1, 25, n),
        "dist_metro_km": np.random.exponential(2, n).clip(0, 15),
        "preco_aluguel": np.random.normal(3000, 1200, n).clip(800, 10000),
        "nota_bairro": np.random.uniform(3, 10, n),
        "fotos_qualidade": np.random.uniform(0, 1, n),
        "dias_anunciado": np.random.exponential(15, n).clip(1, 90),
        "cidade": np.random.choice(
            ["SP", "RJ", "BH", "Campinas", "Curitiba"],
            n,
            p=[0.4, 0.2, 0.15, 0.15, 0.1],
        ),
    })

    # Target CLASSIFICAÇÃO: alugou em 30 dias?
    score = (
        -0.3 * df["preco_aluguel"] / 1000
        + 0.5 * df["nota_bairro"]
        - 0.2 * df["dist_metro_km"]
        + 0.4 * df["fotos_qualidade"] * 10
        + 0.1 * df["quartos"]
        + np.random.normal(0, 1, n)
    )
    df["alugou_30dias"] = (score > score.median()).astype(int)

    # Target REGRESSÃO: preço ideal
    df["preco_ideal"] = (
        500
        + 35 * df["area_m2"]
        + 200 * df["quartos"]
        + 300 * df["vagas_garagem"]
        + 50 * df["nota_bairro"]
        - 30 * df["dist_metro_km"]
        + 15 * df["andar"]
        + np.random.normal(0, 300, n)
    )

    return df


def exibir_resumo(df: pd.DataFrame) -> None:
    """Exibe resumo do dataset."""
    print("=" * 70)
    print("DADOS DO QUINTOANDAR (simulados)")
    print("=" * 70)
    print(f"Total de imóveis: {len(df)}")
    print(f"Alugaram em 30 dias: {df['alugou_30dias'].sum()} ({df['alugou_30dias'].mean():.0%})")
    print(f"Preço médio de aluguel: R$ {df['preco_aluguel'].mean():,.0f}")
    print(f"\nPrimeiros registros:")
    print(df.head())
