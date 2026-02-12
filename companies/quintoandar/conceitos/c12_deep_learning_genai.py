"""
CONCEITOS 12-13: DEEP LEARNING + GenAI
========================================
CNN       = imagens (classificar fotos de imóveis)
RNN/LSTM  = sequências (analisar descrições)
Transformer = atenção seletiva (base dos LLMs)
LLM       = estagiário que leu todos os livros
RAG       = estagiário COM acesso à biblioteca da empresa
Embeddings = texto → coordenadas num mapa
"""


def executar():
    print("\n" + "=" * 70)
    print("CONCEITOS 12-13: DEEP LEARNING + GenAI")
    print("=" * 70)

    print("""
┌─────────────────────────────────────────────────────────────────┐
│  CNN (Convolutional Neural Network)                             │
│  Uso: Classificar qualidade das fotos de imóveis                │
│  Input: foto → Output: score 0-1                                │
│  Como: analisa pedaço por pedaço, detecta padrões visuais       │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  RNN/LSTM (Recurrent Neural Network)                            │
│  Uso: Analisar descrições de imóveis                            │
│  Input: texto → Output: sentimento, categorias                  │
│  Como: processa sequencialmente, lembra contexto anterior       │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  TRANSFORMER (base dos LLMs)                                    │
│  Diferencial: mecanismo de ATENÇÃO - foca no que importa        │
│  "apto perto do metrô em Pinheiros"                             │
│   → sabe que "Pinheiros" é mais importante que "em"             │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  EMBEDDINGS                                                     │
│  "Apartamento espaçoso em Pinheiros" → [0.82, -0.15, 0.94..]  │
│  "Amplo apto na Vila Madalena"       → [0.79, -0.12, 0.91..]  │
│  Textos PARECIDOS ficam PERTO no espaço vetorial                │
│  → Busca por SIGNIFICADO, não só palavras exatas                │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  RAG (Retrieval-Augmented Generation)                           │
│                                                                 │
│  SEM RAG: "Qual a política?" → LLM inventa (alucinação)        │
│                                                                 │
│  COM RAG:                                                       │
│    1. Pergunta chega                                            │
│    2. Busca docs relevantes na base do QuintoAndar              │
│    3. Passa docs + pergunta pro LLM                             │
│    4. Resposta baseada em docs REAIS                            │
│                                                                 │
│  Pipeline: Query → Embedding → Busca vetorial → LLM → Resposta │
└─────────────────────────────────────────────────────────────────┘
""")


if __name__ == "__main__":
    executar()
