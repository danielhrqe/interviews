# Pesquisa Completa: Entrevista QuintoAndar - Lider de Engenharia MLOps

**Data da pesquisa:** 09/fev/2026
**Vaga:** Tech Lead Manager - MLOps
**Fontes:** Glassdoor, Medium (QuintoAndar Tech Blog), site oficial de carreiras, LinkedIn, job postings

---

## 1. Visao Geral da Empresa

O QuintoAndar e o maior ecossistema de moradia da America Latina, uma empresa de tecnologia que nasceu para simplificar a vida de quem busca um novo lar, revolucionando o mercado imobiliario com um modelo de negocio pioneiro.

### Valores Fundamentais
- **Jogamos limpo** - Transparencia e etica
- **Existimos pelo cliente** - Foco no usuario
- **Temos coragem para fazer o novo** - Inovacao e ousadia
- **Entregamos** - Orientacao a resultados
- **Juntos vamos mais longe** - Colaboracao e trabalho em equipe

### Modelo de Trabalho
- **Remote-first**: Trabalho de qualquer lugar do Brasil
- Opcao de usar escritorios em Sao Paulo e Campinas ou coworkings parceiros ate 2x por semana
- Escritorio de tecnologia tambem em Lisboa, Portugal

### Estrutura de Times
- Organizado em **squads** multidisciplinares (Product Primitives)
- Cada squad tem: Software Engineers, Product Designers, Product Managers e Data Scientists
- Areas: engenharia de software, data engineering, data science, infraestrutura, SRE, seguranca da informacao, product management, product design

---

## 2. Tech Stack do QuintoAndar

### Linguagens e Frameworks
- Python, Django
- Java, Spring
- Kotlin, Micronaut
- Node.js, JavaScript/TypeScript
- Dart (Flutter)
- Go, C++, C#

### Infraestrutura e Cloud
- AWS (EC2, S3, RDS, Redshift, Lambda, CloudFront)
- Google Cloud Platform (Cloud Composer)
- Kubernetes, Docker
- Elastic Stack

### Dados e ML
- Apache Kafka (inclusive com lib propria: quintoandar-kafka)
- Apache Airflow (via Google Cloud Composer)
- Spark (via Databricks)
- Feature Store proprio
- MLflow, Kubeflow
- Metabase (dashboards)
- Kibana (logs)

### Messaging
- Kafka, RabbitMQ, SQS

---

## 3. Plataforma de MLOps do QuintoAndar (Contexto para a Vaga)

### Visao Geral
O time de MLOps e responsavel por criar uma plataforma que empodera todo o capitulo de Data Science a realizar o ciclo completo de desenvolvimento de modelos de forma eficiente: do gerenciamento do feature store ao serving e monitoramento de predicoes em tempo real.

### Arquitetura do ML Pipeline
1. **Orquestracao**: Apache Airflow (Google Cloud Composer)
2. **Processamento**: Spark via Databricks (com DatabricksOperator customizado)
3. **Feature Store**: Camada centralizada de dados com features pre-computadas para treino e serving
4. **Model Serving**: Deploy em cluster Kubernetes para predicoes near-real-time
5. **Monitoramento**: Sistema escalavel com produtores async que enviam logs via Kafka
   - ~8 milhoes de registros/dia em media
   - Deteccao de data drift e concept drift
   - Consumidor centralizado que estrutura schema e armazena os dados
   - Integracao com ferramentas de visualizacao

### Template de ML
- Template padrao que cuida do boilerplate code
- Permite que data scientists foquem no desenvolvimento do modelo

### Desafios Atuais
- Escalar sistemas de ML para producao
- Manter monitoramento modular e independente
- Feature store com baixa latencia e alto throughput (centenas de operacoes por segundo)

---

## 4. A Vaga: Tech Lead Manager - MLOps

### Responsabilidades
- **Lideranca de equipe**: Gerenciar Machine Learning Engineers focados na plataforma de ML
- **Colaboracao cross-funcional**: Trabalhar com times de Data Science e AI
- **Gestao de modelos**: Garantir deploy suave, monitoramento e tratar model drift
- **Padroes e excelencia**: Promover padroes de infraestrutura e codigo alinhados com necessidades de ML
- **Melhoria de processos**: Automatizar workflows, integrar ferramentas, otimizar pipelines
- **Desenvolvimento de carreira**: Gerenciar crescimento profissional dos membros do time

### Requisitos Obrigatorios
- Experiencia comprovada em lideranca de equipe e gestao de carreira
- Entendimento geral de conceitos de ML (regressao, classificacao, clustering, redes neurais)
- Conhecimento de desafios de deploy de sistemas ML em producao
- Proficiencia em Python ou outra linguagem principal
- Experiencia com servicos de cloud
- Excelente comunicacao escrita e verbal
- Mentalidade de produto para guiar roadmap de longo prazo
- Conhecimento atual de avancos em ML Engineering

### Diferenciais
- Mestrado em Ciencia da Computacao, Engenharia, Estatistica ou area relacionada
- Experiencia construindo plataformas de ML
- Experiencia com monorepos grandes
- Expertise com ferramentas MLOps (Kubeflow, MLflow, AWS SageMaker, Google AI Platform, Databricks)
- Conhecimento de solucoes AWS

---

## 5. Processo Seletivo - Etapas (CONFIRMADO VIA PDF OFICIAL DO RH)

### Duracao Media
- **30-40 dias** do inicio ao fim (media oficial)
- **~24 dias** segundo dados do Glassdoor

### Etapas CONFIRMADAS para a Vaga (PDF do RH)

1. **Application & Screening** - Candidatura e triagem pelos times de People e Engenharia
2. **People Interview** - Entrevista com o time de People sobre carreira. Oportunidade de conhecer o QuintoAndar
3. **Tech Screening (1h)** - Primeira entrevista tecnica. Discussao de experiencia + conceitos de data science + possivelmente caso simplificado. Se aprovado, avanca para Coding e ML
4. **Coding Interview (1h)** - Algoritmos e estruturas de dados na plataforma **Codility**. 40 minutos para implementar solucao. Entrevistador presente ao vivo
5. **Machine Learning Interview (1h)** - Perguntas tecnicas diretas sobre ML, Deep Learning e GenAI + caso de negocio. SEM CODIGO nesta etapa
6. **Oferta**

### Dicas Oficiais do Guia (PDF do RH)

**Gerais:**
- Entrar no Google Meet alguns minutos antes
- **Desabilitar ferramentas de anotacao com IA** antes da call
- Pesquisar sobre o QuintoAndar e fazer perguntas relevantes
- Explicar o raciocinio - valorizam o PROCESSO mais que o resultado
- Nao hesitar em pedir ajuda - esperam colaboracao com o entrevistador

**System Design:**
- Quebrar o problema em problemas menores
- Discutir trade-offs de multiplas abordagens
- Napkin Math para dimensionar componentes
- Evitar over-engineering - comecar simples, melhorar iterativamente

**Coding:**
- Dominar pelo menos uma linguagem de programacao
- Saber OOP e como testar codigo
- Estruturas: arrays, linked lists, stacks, queues, sets, maps, trees, graphs
- Complexidade: Big-O tempo e espaco
- Sorting: insertion sort, quicksort, mergesort
- Recursao: muitos problemas sao resolvidos mais facilmente com recursao
- Plataforma: **Codility** (fazer o demo test antes!)
- Linguagens suportadas: ver lista no Codility (Python suportado)

### Processo Geral para Engenharia (referencia - pesquisa)

1. **Candidatura e Triagem** - Analise de CV
2. **Teste Online (Codility)** - Desafio de codigo com prazo (7 dias para completar)
3. **Entrevista com Recrutador** - Fit cultural, motivacoes, experiencias
4. **Entrevista com Lideranca** - Confirmacao de achados anteriores, detalhes da vaga
5. **Entrevista com Stakeholder** - Alguem de fora do time contratante
6. **Oferta**

---

## 6. Detalhes das Entrevistas Tecnicas

### 6.1. Tech Screening (Machine Learning)

**Formato**: Conversa tecnica explorando background profissional e conceitos de ML com cenarios simplificados.

**O que avaliam**:
- Como voce PENSA nos problemas (nao esperam respostas perfeitas)
- Discussao detalhada dos seus projetos de ML/dados com profundidade tecnica
- Traducao de necessidades de negocio em solucoes tecnicas
- Tipos de dados e abordagens de modelagem (estruturados e nao-estruturados)
- Desafios tecnicos: MLOps, context engineering, search, sistemas de recomendacao

**Material de preparacao recomendado pelo QuintoAndar**:
- "Building Multimodal Search and RAG" (DeepLearning.AI)
- "Machine Learning in Production" course

### 6.2. Coding Interview

**Formato**: Plataforma Codility, ao vivo com entrevistador.

**O que cobram**:
- Algoritmos e SQL em contexto de ML
- Logica de loops, condicionais e recursao
- Estruturacao de codigo com boas praticas
- SQL: JOINs e Window Functions (MUITO IMPORTANTE)
- Proficiencia em pelo menos uma linguagem com OOP

**Estruturas de dados essenciais**:
- Arrays, Linked Lists, Stacks, Queues
- Sets, HashMaps
- Trees (BST, AVL, Heaps), Graphs

**Algoritmos essenciais**:
- Busca Linear e Binaria
- Ordenacao (bubble, insertion, merge, quicksort)
- Recursao e Backtracking
- Dynamic Programming basico
- Analise de complexidade Big-O

**Linguagens suportadas**: Java, Kotlin, Python, JavaScript/TypeScript, Dart, Go, C++, C#

**Dicas oficiais**:
- Validar o problema com o entrevistador ANTES de codar
- Comecar simples, depois otimizar
- Testar o codigo com varios inputs
- Usar nomes claros de variaveis
- Pedir tempo para pensar quando necessario
- Explicar o raciocinio em voz alta DURANTE a codificacao

### 6.3. Machine Learning System Design

**Formato**: Perguntas tecnicas abertas e analise de caso de negocio. SEM CODIGO.

**O que avaliam**:
- **Decomposicao de problemas**: Quebrar problemas complexos em componentes gerenciaveis
- **Analise de trade-offs**: Justificar escolhas com pros/contras
- **Escalabilidade e dimensionamento**: "Napkin Math" para estimar storage, throughput, servidores
- **Design iterativo**: Comecar com solucao minima viavel, adicionar complexidade conforme necessario
- **Conhecimento de fundamentos**: Hash tables para caching, B-trees em bancos de dados

**Conceitos-chave para System Design**:
- Load Balancing (round-robin, least connections, health checks)
- Caching (Redis, CDN, TTL, cache stampede)
- Sharding e Partitioning
- Messaging (Kafka, RabbitMQ, SQS)
- Teorema CAP
- Escalabilidade (vertical vs horizontal)
- Tolerancia a falhas (fallback, retry, timeout, circuit breaker)
- Observabilidade (metricas, logs estruturados, distributed tracing)

**Abordagem recomendada**:
1. Entender o problema e alinhar escopo com entrevistador
2. Comecar com arquitetura de alto nivel
3. Identificar componentes-chave
4. Detalhar interacoes e protocolos
5. Fazer estimativas de capacidade
6. Explorar alternativas e trade-offs
7. Considerar cenarios de falha

### 6.4. Entrevista Comportamental / Fit Cultural

**Perguntas reportadas no Glassdoor**:
- "Conte sobre uma vez que voce teve um conflito com um colega e como lidou com isso"
- "Voce ja teve que assumir o papel de lider para resolver um problema no trabalho?"
- Perguntas sobre experiencias anteriores, resultados e impacto
- Alinhamento de expectativas salariais

**O que buscam em atitudes**:
- **Mostrar raciocinio**: Pensar em voz alta, explicar escolhas, compartilhar incertezas
- **Comunicar com clareza**: Resumir em blocos, validar requisitos, recapitular pensamento
- **Colaborar**: Estar aberto a feedback, ouvir, ver a entrevista como construcao conjunta
- **Demonstrar autoconhecimento**: Compartilhar aprendizados recentes, reconhecer gaps de forma construtiva
- **Conectar com o QuintoAndar**: Pesquisar cultura, referenciar artigos tecnicos, alinhar objetivos de carreira

---

## 7. Perguntas Especificas Reportadas (Glassdoor)

### Coding
- Implementar o comando Unix `cd` e depois fazer output do `pwd` apos um `cd`
- Problemas de linked list contextualizados com cenarios de negocios do QuintoAndar
- Problemas estilo LeetCode easy/medium (2 problemas na primeira etapa de live coding)

### System Design
- **System Design 1**: Implementar a funcao de busca (com filtros) de um app imobiliario
- **System Design 2**: Sistema de notificacoes com capacidade de enviar notificacoes baseadas em eventos e agendar notificacoes
- Projetar um sistema para motoristas de aplicativos (com code review de trechos fornecidos)

### Machine Learning (inferido do guia e blog)
- Cenarios de MLOps e deploy de modelos
- Discussao sobre feature store e model serving
- Monitoramento de modelos em producao
- Data drift e concept drift

---

## 8. Nivel de Dificuldade e Experiencia dos Candidatos

### Estatisticas do Glassdoor
- **56% experiencia positiva** (44% neutra/negativa)
- **Dificuldade: 3.1-3.26 de 5** (moderada-alta)
- Entrevistas para **Sr. Software Engineer e Machine Learning Engineer** foram classificadas como as **mais dificeis**
- 630+ perguntas e 580+ reviews de entrevistas

### Feedback Positivo
- Recrutadores explicam todas as etapas e fornecem material de estudo
- Feedback consistente para candidatos
- Processo geralmente transparente
- Problemas contextualizados com o negocio (nao so algoritmos abstratos)

### Feedback Negativo
- Alguns candidatos reportaram entrevistadores com atitude fria e pouco espaco para dialogo
- Processo as vezes lento com comunicacao confusa
- Em alguns casos, falta de clareza sobre detalhes das posicoes
- Analista de RH parecendo fazer triagem em volume

---

## 9. Dicas de Preparacao Especificas

### Para a Entrevista com Recrutador
1. Documentar experiencias de projetos com descricao de tarefas, resultados e impacto
2. Preparar exemplos demonstrando alinhamento com os 5 valores do QuintoAndar
3. Ter claro: expectativa salarial, motivacao para sair do emprego atual, por que QuintoAndar
4. Pesquisar a empresa a fundo (ler o tech blog!)

### Para o Tech Screening (ML)
1. Preparar 2-3 historias detalhadas de projetos ML/dados com profundidade tecnica
2. Saber explicar como traduziu necessidade de negocio em solucao tecnica
3. Estudar conceitos de MLOps, pipelines, deploy de modelos
4. Conhecer desafios de search e sistemas de recomendacao (relevante para real estate)

### Para o Coding
1. Praticar no LeetCode (easy/medium) e Codility
2. Foco em: arrays, hash maps, trees, e SQL (JOINs + Window Functions)
3. SEMPRE explicar o raciocinio em voz alta
4. Comecar com solucao bruta, depois otimizar
5. Testar com edge cases
6. Usar Python (alinhado com o stack deles)

### Para System Design (ML)
1. Ler "Designing Machine Learning Systems" (Chip Huyen)
2. Ler "Designing Data-Intensive Applications" (Martin Kleppmann)
3. Praticar "Napkin Math" (estimativas de capacidade)
4. Conhecer arquitetura de ML pipelines end-to-end
5. Saber discutir trade-offs de diferentes abordagens
6. Usar FigJam ou Excalidraw para diagramas

### Para Lideranca (especifico para Tech Lead Manager)
1. Preparar exemplos de gestao de equipe e desenvolvimento de carreira
2. Ter historias de colaboracao cross-funcional (DS + Eng + Produto)
3. Demonstrar mentalidade de produto (roadmap, priorizacao)
4. Mostrar como equilibra hands-on tecnico com gestao de pessoas
5. Falar sobre como promove padroes de qualidade e boas praticas

---

## 10. Recursos Recomendados pelo Proprio QuintoAndar

### Livros
- "Cracking the Coding Interview" (geral)
- "System Design Interview" por Alex Xu
- "Designing Data-Intensive Applications" por Martin Kleppmann
- "Designing Machine Learning Systems" por Chip Huyen
- "The Data Warehouse Toolkit" por Ralph Kimball
- "Fundamentals of Data Engineering" por Joe Reis e Matt Housley

### Plataformas de Pratica
- LeetCode
- NeetCode
- Advent of Code
- HackerRank (para SQL)
- Codility (plataforma usada nas entrevistas!)

### Cursos
- "Building Multimodal Search and RAG" (DeepLearning.AI)
- "Machine Learning in Production"

### Blogs e Referencias
- **QuintoAndar Tech Blog** (Medium) - LEITURA OBRIGATORIA
- System Design Primer (GitHub)
- NeetCode System Design
- High Scalability blog

### Artigos do QuintoAndar Tech Blog Relevantes
- "What to expect when interviewing for Engineering @ QuintoAndar" (Guilherme Salerno)
- "Succeeding in Your System Design Interview" (Mikael Mello)
- "How to be Fully Prepared for a Coding Interview" (Clarice Abreu)
- "How to be Effective During a Code Interview" (Clarice Abreu)
- "From the notebooks to the user: ML Platform at QuintoAndar" (Lucas Cardozo)
- "Scaling machine learning monitoring" (Ralph Rassweiler)
- "Machine Learning Pipeline at QuintoAndar" (Andre Barbosa)
- "How Apache Airflow is helping us evolve our data pipeline" (LF)

---

## 11. Filosofia de Entrevista do QuintoAndar

> "A entrevista e uma troca. Nao esperamos respostas perfeitas, mas sim clareza de raciocinio, boas escolhas e uma atitude construtiva."

Pontos-chave:
- Valorizam o PROCESSO de pensamento mais que a resposta final
- Querem ver como voce COLABORA (a entrevista e uma construcao conjunta)
- Buscam pessoas que entregam a melhor solucao possivel e estao sempre aprendendo
- Acreditam que time e mais que a soma das partes
- Esperam que voce peca tempo para pensar quando necessario
- Querem candidatos que reconhecem gaps de forma construtiva

---

## 12. Fontes Consultadas

- [Guia de Entrevistas Tecnicas - Engenharia](https://carreiras.quintoandar.com.br/guia-de-entrevistas-tecnicas/engenharia/)
- [Guia de Entrevistas Tecnicas - Machine Learning](https://carreiras.quintoandar.com.br/guia-de-entrevistas-tecnicas/machine-learning/)
- [Processo Seletivo QuintoAndar](https://carreiras.quintoandar.com.br/nosso-processo-seletivo/)
- [What to expect when interviewing for Engineering @ QuintoAndar](https://medium.com/quintoandar-tech-blog/what-to-expect-when-interviewing-for-engineering-quintoandar-32e8e2e92b0c)
- [How to be Fully Prepared for a Coding Interview](https://medium.com/quintoandar-tech-blog/how-to-be-fully-prepared-for-a-coding-interview-48b5eda4f440)
- [How to be Effective During a Code Interview](https://medium.com/quintoandar-tech-blog/how-to-be-effective-during-a-code-interview-ddc790243d70)
- [Succeeding in Your System Design Interview](https://medium.com/quintoandar-tech-blog/succeeding-in-your-system-design-interview-3817494df3af)
- [Scaling Machine Learning Monitoring](https://medium.com/quintoandar-tech-blog/scaling-machine-learning-monitoring-b6aa917adab0)
- [Machine Learning Pipeline at QuintoAndar](https://medium.com/quintoandar-tech-blog/machine-learning-pipeline-at-quintoandar-e2f24136006b)
- [From the notebooks to the user: ML Platform at QuintoAndar](https://medium.com/quintoandar-tech-blog/from-the-notebooks-to-the-user-ml-platform-at-quintoandar-61a57f635870)
- [QuintoAndar Glassdoor Interviews](https://www.glassdoor.com/Interview/QuintoAndar-Interview-Questions-E1161693.htm)
- [Glassdoor Software Engineer Questions](https://www.glassdoor.com.br/Entrevista/QuintoAndar-Software-Engineer-Perguntas-entrevista-EI_IE1161693.0,11_KO12,29.htm)
- [Tech Lead Manager MLOps - Job Posting](https://job-boards.greenhouse.io/quintoandar/jobs/4092012009)
- [QuintoAndar Tech Stack (StackShare)](https://stackshare.io/quintoandar/quintoandar)
- [QuintoAndar Tech Stack (Himalayas)](https://himalayas.app/companies/quintoandar/tech-stack)
- [QuintoAndar Cultura (LinkedIn)](https://br.linkedin.com/company/quintoandar-com-br/life)
- [Experiencia Micael Cid (Medium)](https://medium.com/@micaelcid/minha-experi%C3%AAncia-no-processo-seletivo-de-est%C3%A1gio-de-engenharia-de-software-no-quintoandar-c5648cd4b872)
