# Cola Rápida - Tech Screening QuintoAndar

## 1. Gradient Descent
- **O que é:** Algoritmo que minimiza o erro do modelo iterativamente
- **Learning rate:** Tamanho do passo (hiperparâmetro definido pelo engenheiro)
- **LR alto:** erro pula, nunca converge → diminuir LR
- **LR baixo:** demora eternidade → aumentar LR
- **Analogia:** Descer montanha no escuro sentindo a inclinação com o pé

## 2. Overfitting vs Underfitting
- **Overfitting:** Decorou o treino. Treino 99%, teste 60% (gap grande)
- **Underfitting:** Não aprendeu. Treino 55%, teste 50% (ambos ruins)
- **Ideal:** Treino 90%, teste 87% (gap pequeno, ambos altos)
- **Resolver overfitting:** Regularização (L1/L2), reduzir complexidade
- **Resolver underfitting:** Modelo mais complexo, mais features
- **NUNCA:** "novos dados" resolve overfitting. Novos dados → resolve drift
- **Analogia:** Estudar pra prova. Decorar vs entender vs nem ler

## 3. Bias-Variance Tradeoff
- **Alto Bias = Underfitting** (modelo simples demais, erra sistematicamente)
- **Alta Variance = Overfitting** (modelo complexo demais, instável)
- **Objetivo:** Equilibrar os dois
- **Analogia:** Jogador de dardo. Bias=agrupado longe do centro. Variance=espalhado

## 4. Cross-Validation (K-Fold)
- **Por quê:** Train/test simples pode ter sorte/azar na divisão
- **Como:** Divide em K partes, treina em K-1, testa em 1, repete K vezes
- **Score final:** Média das K rodadas
- **K=10 mais confiável** que K=5 (mais combinações, mais dados por treino)
- **Analogia:** Professor que aplica 5 provas diferentes, nota = média

## 5. L1 vs L2 Regularização
- **L1 (Lasso):** ZERA features inúteis → seleção automática
- **L2 (Ridge):** REDUZ todos os pesos sem zerar
- **Quando usar L1:** Muitas features, maioria é lixo
- **Quando usar L2:** Todas contribuem um pouco
- **Ambos:** Combatem overfitting penalizando complexidade
- **Analogia:** L1=demitir improdutivos. L2=reduzir salário de todos

## 6. Data Drift vs Concept Drift
- **Data Drift:** Os INPUTS mudaram (perfil diferente)
  - Ex: Expansão pra novas cidades → imóveis diferentes
- **Concept Drift:** A RELAÇÃO input→output mudou (comportamento mudou)
  - Ex: Home office → "perto do metrô" perdeu relevância
- **Cola:** Mudou QUEM ENTRA → data drift. Mudou O QUE SIGNIFICA → concept drift
- **Ambos:** Solução é RETREINAR o modelo com dados recentes
- **Analogia:** Pizzaria. Data drift=mudou o bairro. Concept drift=sexta virou dia de salada

## 7. Classificação vs Regressão
- **Classificação:** Prevê CATEGORIA (sim/não, A/B/C)
- **Regressão:** Prevê NÚMERO contínuo (preço, temperatura)
- **PEGADINHA:** Regressão Logística é CLASSIFICAÇÃO!
- **Regra:** "Vai alugar?" → classificação. "Qual o preço?" → regressão

## 8. Métricas de Classificação
- **Precision:** Dos que ACUSOU, quantos ACERTOU? (confiança na acusação)
- **Recall:** Dos que EXISTIAM, quantos PEGOU? (capacidade de captura)
- **F1:** Média harmônica de precision e recall
- **AUC-ROC:** Capacidade de separar classes (0.5=chute, 1.0=perfeito)
- **Fraude/Golpe:** Recall alto é prioridade (não deixar escapar)
- **Planejamento financeiro:** Precision alta é prioridade (confiar na previsão)
- **SEMPRE perguntar:** "Como o output é usado?" antes de escolher

## 9. Métricas de Regressão
- **MAE:** Erro médio em reais → "erra R$ 200 em média" (mais intuitivo)
- **RMSE:** Penaliza erros grandes muito mais que pequenos
- **R²:** Quanto o modelo explica (0 a 1, mais perto de 1 = melhor)
- **NUNCA usar acurácia pra regressão**

## 10. Métricas de Ranking (NDCG, MRR)
- **NDCG:** Qualidade da ordenação inteira. Melhores no topo = NDCG alto
- **MRR:** Posição do primeiro resultado bom. Posição 1 = MRR 1.0, posição 5 = MRR 0.2
- **Offline:** NDCG/MRR pra avaliar antes do deploy
- **Online:** CTR + taxa de agendamento via A/B test
- **QuintoAndar:** NDCG@10 = "dos 10 primeiros, os melhores estão no topo?"

## 11. Supervised vs Unsupervised vs Reinforcement
- **Supervised:** Tem labels (resposta certa). Ex: prever se aluga (sim/não)
- **Unsupervised:** Sem labels. Descobre padrões. Ex: agrupar imóveis (K-Means)
- **Reinforcement:** Aprende por recompensa. Ex: otimizar preço em tempo real
- **Anomalia sem labels:** Unsupervised (Isolation Forest, DBSCAN)
- **Analogia:** Criança com professor / sem professor / jogando videogame

## 12. Deep Learning
- **CNN:** Imagens (fotos de imóveis, classificar cômodos)
- **RNN/LSTM:** Sequências (descrições de imóveis, texto em ordem)
- **Transformer:** Mecanismo de ATENÇÃO, foca no relevante. Base dos LLMs
- **Não confundir:** Transformer não é só "prever próxima palavra" - é a arquitetura

## 13. RAG e Embeddings
- **Embeddings:** Texto → vetor numérico. Textos parecidos ficam perto no espaço
- **RAG:** LLM + busca em documentos reais da empresa → reduz alucinação
- **Pipeline RAG:** Query → Embedding → Busca vetorial → Top K docs → LLM → Resposta
- **Tokenização:** Quebra texto em tokens (vem ANTES do embedding)

---

## Termos Importantes
- **Hiperparâmetro:** Configuração definida pelo ENGENHEIRO antes do treino (learning rate, max_depth)
- **Parâmetro:** O que o MODELO aprende sozinho (pesos, coeficientes)
- **Feature:** Variável de entrada do modelo
- **Label/Target:** Resposta certa (o que queremos prever)
- **Threshold:** Ponto de corte pra classificar (ex: >0.5 = sim)
- **Epoch:** Uma passada completa pelos dados de treino

---

## Respostas Rápidas QuintoAndar

**"Como monitorar modelo em produção?"**
→ Precision/Recall do modelo, distribuição dos inputs (detectar drift), métricas de infra (latência), alertas com threshold pra retreinar

**"Modelo degradou, o que fazer?"**
→ Investigar: data quality → data drift → concept drift → retreinar com dados recentes → validar → deploy canary

**"Como levar notebook pra produção?"**
→ Templates padronizados (classes base) → PR review → CI/CD automático → deploy → monitoring. Trunk-based, 3 min pra produção

**"Diferença entre data drift e concept drift?"**
→ Data drift = inputs mudaram. Concept drift = relação mudou. Ambos precisam de retreinamento
