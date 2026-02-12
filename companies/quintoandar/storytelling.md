# Roteiro de Storytelling - Tech Screening QuintoAndar

## Como usar este roteiro
- NÃO decore palavra por palavra - soa robótico
- Internalize os PONTOS-CHAVE de cada bloco
- Pratique em voz alta 3-4 vezes até fluir natural
- Tempo alvo: 2-3 minutos por história

---

## História 1: A Plataforma (técnica + hands-on)

**Use quando perguntarem:** "Me conta um projeto técnico", "Experiência com ML/dados", "Me fala sobre MLOps"

---

### CONTEXTO (30s)

> "Na empresa onde eu estava, tínhamos um cenário caótico de dados e ML. Existiam 5 plataformas diferentes espalhadas pelo mundo - cada país ou região tinha feito a sua. Não tinha padronização, não tinha governança, custos altos, e vários problemas de segurança.
>
> Pra dar um exemplo concreto: um time no México subiu um MongoDB pra servir os outputs dos modelos de ML. O time que fez isso saiu da empresa e ninguém mais conseguia dar manutenção. Esse tipo de coisa acontecia em vários lugares."

### PROBLEMA (30s)

> "A empresa precisava de uma plataforma centralizada onde mais de 600 engenheiros e cientistas de dados do mundo inteiro pudessem trabalhar com o mesmo padrão, com governança, e que permitisse escalar soluções rapidamente. Basicamente: construir a fundação de dados e ML da empresa do zero."

### O QUE EU FIZ (1.5min)

> "Eu comecei praticamente sozinho - mão no código e na infraestrutura. Fui o primeiro engenheiro do projeto.
>
> **Arquitetura:** Desenhei tudo em cima de Azure. Databricks com Spark no Kubernetes pra toda a parte de computação e processamento. Airflow pra orquestração dos pipelines offline. Kubernetes também pro model serving, com ArgoCD fazendo o deploy. Toda a infra provisionada via Terraform e Terragrunt. Observabilidade inteira no Datadog. Armazenamento no Azure Blob como data lake.
>
> **Padronização:** Criei um modelo de templates padronizados. O cientista de dados seguia uma estrutura pré-definida pra features, treinamento e predição - classes base que eram obrigatórias. Por baixo, a pipeline de CI/CD com GitHub Actions e ArgoCD levava o código pra produção automaticamente.
>
> **Processo:** Adotamos trunk-based development. O time conseguia levar código pra produção em 3 minutos. Tracking de modelos e experimentos via MLflow dentro do Databricks.
>
> Conforme a plataforma foi crescendo, montei um time de 9 engenheiros e 1 manager, e fui migrando mais pra gestão e arquitetura."

### RESULTADO (30s)

> "Hoje a plataforma roda mais de 70 mil execuções por dia, tem mais de 150 modelos de ML em produção em diversos países, e mais de 4 mil DAGs no Airflow. Descomissionamos as 5 plataformas legadas. É o padrão global da empresa."

---

## História 2: A Expansão Global (liderança + resiliência)

**Use quando perguntarem:** "Desafio de liderança", "Conflito/resistência", "Gestão de stakeholders", "Como equilibra técnico e gestão"

---

### CONTEXTO (30s)

> "Com a plataforma construída, o desafio mudou completamente. Agora era convencer o mundo inteiro a adotar. Tínhamos metas agressivas de migração: 60% dos dados da maior zona da empresa - cerca de 30 mil datasets -, 50% de outra zona com 5 mil datasets, e mais de 50 modelos de ML de várias regiões."

### PROBLEMA (30s)

> "Cada região tinha sua cultura, suas ferramentas, e principalmente - sua resistência. Pra muita gente, a plataforma deles funcionava. Convencer times de diferentes países e línguas a abandonar o que já tinham e migrar pra algo novo não era trivial. A resistência era real."

### O QUE EU FIZ (1.5min)

> "Primeiro, aprendi que resistência não era pessoal. Cada cultura reage diferente - algumas mais frias e diretas, outras mais abertas. Tive que desenvolver muito o meu lado político e de stakeholder management.
>
> A estratégia que funcionou: escolhi times early adopters, os que tinham mais dor. Entreguei resultado concreto rápido pra eles, e usei esses casos de sucesso pra convencer os próximos. Efeito dominó.
>
> Na gestão do time, aprendi a controlar a emoção da equipe. Era um projeto de alta pressão, com muita exposição. Quando necessário, abri exceções pontuais - tipo aceitar uma customização de um time específico - pra não perder a meta e manter a confiança.
>
> Também tive que equilibrar o hands-on técnico com a gestão. No começo eu codava. Depois fui formando o time, delegando a execução, e focando em arquitetura, alinhamento com stakeholders e direção técnica."

### RESULTADO (30s)

> "Batemos todas as metas de migração. A plataforma hoje é usada por mais de 600 pessoas globalmente. E pessoalmente, foi o maior aprendizado da minha carreira - saí um líder muito mais completo, tanto no técnico quanto no lado humano."

---

## Perguntas que o entrevistador pode fazer depois (prepare-se)

### Sobre a História 1
- "Por que Azure e não AWS/GCP?"
- "Como vocês garantiam qualidade dos dados?"
- "Como era o monitoramento dos modelos?"
- "O que você faria diferente hoje?"

### Sobre a História 2
- "Me dá um exemplo concreto de resistência e como resolveu"
- "Alguma meta que não bateu? O que aprendeu?"
- "Como priorizava o que migrar primeiro?"
- "Como media o sucesso da adoção?"

### Sobre as duas
- "Por que saiu/está saindo de lá?"
- "O que te atrai no QuintoAndar?"
- "Como essa experiência se aplica aqui?"

---

## História 3 (curta): Sistema de Recomendação - MBA + Zé Delivery

**Use quando perguntarem:** "Tem experiência direta com ML/modelos?", "Já trabalhou com recomendação?"

> "No meu MBA, trabalhei com sistemas de recomendação baseados em grafos, usando filtragem colaborativa e por conteúdo. Implementei um MVP no Zé Delivery em 2019 - basicamente recomendar produtos pro consumidor com base no perfil e no comportamento de usuários similares. Teve bons resultados, mas saí da empresa e o projeto não teve continuidade.
>
> Então tenho tanto a visão teórica de como um sistema de recomendação funciona quanto a experiência prática de ter implementado um. No meu papel mais recente, fiquei mais no lado de plataforma - garantindo que os cientistas de dados tivessem a infraestrutura pra construir e operar esses modelos em escala."

**Por que essa história importa:** Mostra que você não é só infra. Já colocou a mão em modelagem. E sistemas de recomendação são core do QuintoAndar (ranking de imóveis).

---

## Respostas Prontas para Perguntas-Chave

### "Por que saiu/está saindo da empresa?"

> "Fiquei 12 anos na empresa. Acredito que meu ciclo se encerrou de forma muito positiva - deixei um legado concreto com a plataforma rodando globalmente e um time treinado pra encarar os próximos desafios. Agora quero viver outros desafios, outras culturas, outros problemas. Sinto que é o momento certo pra isso."

**Dica:** Resposta curta, positiva, sem falar mal. Perfeita.

### "O que te atrai no QuintoAndar?"

> "Três coisas me atraíram. Primeiro, a cultura orientada ao cliente - eu acredito muito nisso. Segundo, ser uma empresa de tecnologia e inovação que é bem falada pelo ambiente colaborativo de trabalho. E terceiro, o desafio em si: o problema imobiliário é real e complexo, não só no Brasil mas na América Latina inteira.
>
> E quando olhei a vaga de MLOps especificamente, vi que o desafio técnico é muito parecido com o que eu vivi: construir e evoluir uma plataforma que empodera cientistas de dados a entregar valor. Li artigos do tech blog de vocês sobre o ML Pipeline, o monitoring com Kafka, o feature store - e me identifiquei muito com os problemas e a abordagem."

**Dica:** Conectar o "por que QuintoAndar" com o "o que eu já fiz" mostra que não é resposta genérica.

---

## Ponte com o QuintoAndar (use no final de qualquer história)

> "Quando eu vi a vaga de Tech Lead Manager de MLOps no QuintoAndar, me identifiquei muito. É um desafio parecido em essência: construir e evoluir uma plataforma de ML que empodera cientistas de dados a entregar valor. Li alguns artigos do tech blog de vocês - sobre o ML Pipeline, o monitoring com Kafka, o feature store - e vi que a stack e os desafios são muito próximos do que eu vivi. É exatamente o tipo de problema que me motiva."

---

## Dicas Finais

1. **Sempre comece pelo problema de negócio, não pela tecnologia**
2. **Use números** - 70K execuções, 150 modelos, 600 pessoas, 3 minutos de deploy
3. **Mostre evolução** - "comecei sozinho codando → montei o time → escala global"
4. **Conecte com o QuintoAndar** no final
5. **Se não souber algo, diga** - "não tenho profundidade nisso, mas minha abordagem seria..."
6. **A história do MBA/Zé Delivery** é o bridge entre "sou de infra" e "entendo ML na prática"
