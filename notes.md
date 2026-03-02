Problema:       

  O QuintoAndar quer criar um sistema de ranking de imóveis para usuários não logados. Quando alguém acessa o site sem conta, busca
  "apartamento 2 quartos Pinheiros", o sistema precisa ordenar os resultados de forma inteligente — não só por data de publicação.

  Você não tem histórico do usuário. Não tem login. Só tem a query de busca e os dados dos imóveis.

  Requisitos:
  - ~500K imóveis ativos
  - ~2M buscas/dia
  - Latência < 200ms

  Desenhe o sistema end-to-end: dados, features, modelo, serving, monitoramento.


req func
usuario pode ser capaz de entrar no site sem login
usuarios nao logados podem fazer uma busca de apartamentos por filtros pre determinados

req non func
availability > consistencia
low latency: latencia < 200ms
read > write
zero loos data

napkin math
read qps = 2m / 100k = 20
storage = 500k imoveis * ~1kb cada imovel = 0.5gb total

a leitura vai atingir uma taxa de 20 queries por segundos, o que um banco relacional como postgres
consegue lidar bem. o grande ponto é que mesmo sendo 20 queries por segundos, sao queries orientadas a busca de dados
com multiplos filtros, entao um banco de dados como um postgres nao deveria ser capaz de lidar com isso em larga escala
mesmo tendo mecanismos para isso, e por isso o melhor cenario aqui é ir para um banco de dados orietado a busca(elastic search)
entities

real_state (name, description, price, neighborhood, city, state, rooms)
non_logged_user (temporary_id, latitude, longitude)
search_events (temporary_id, latitude, longitude, price, neighborhood, city, state, rooms)
real_state_ranking()

apis
get -> /real-state/search?user_location=xx&rooms=x&price=xx&neighborhood=x&city=xx&state=xxx
result = {
    total = xx,
    items = [{
        name=xx,
        price=xx,
        description=xxm
        rooms=xx,
        city=xx,
        neighborhood=xx
}]  
}

post -> /real-state
requests = {
        name=xx,
        price=xx,
        description=xxm
        rooms=xx,
        city=xx,
        neighborhood=xx,
        owner=xx,
}

result = {
    "ok"
}

high level design
web app: aplicacao onde o usuario acessar e consegue fazer as buscas dos imoveis que ele deseja
cnd: imagens dos imoveis cacheadas
api gateway: entrypoint unico para todas as requisicoes e roteamento para os servicos de backend
loadbalancer: distribui cargas pegadas para multiplos servicos de backend
postgresql: banco transacional para armazenar as informacoes de real state
redis: banco in memory para armazenarmos a informacao dos usuarios com um TTL estabelecido. pode ser gerado uma chave com 
base na lat/long ou cookie. responsavel tambem por armazenar todas as features
search_service: servico de backend utilizado para se conectar com redis para pegar as infos do usuario nao loggado
e encaminhar requisicao para o elastiserach, a fim de retornar para o usuario o ranking de imoveis

elasticsearch: banco de dado de busca, onde o modelo ira pre armazenar todo rankeamento dos imoveis com base em scores pre 
definido. é ideia aqui é que com base na localizacao do usuario nao logado, o ranking consiga retornar os melhores imoveis com uma latencia baixa

ranking pipeline:
    ingestion-service: responsavel por ingerir todos os dados do transacionais(real state, user, cities, e etc) e armazenar em um datalake(s3). dados os requisitos
    inicialmente sera uma ingestao em batch, triggada regularmente por um servico de scheduler
    features-service: responsavel por gerar todas as features necessarias para o treinamento do modelo
    train-service: responsavel por 
    serving:
    observability:

Perguntas → Métricas → Dados e labels → Features → Modelo → Serving →  Monitoramento

Perguntas:
Quantas imoveis temos cadastrados na base?
Qual problema de negocio queremos resolver quais metricas queremos olhar?
Qual é a volumetria de acesso para esses casos?
Qual a latencia ideial que precisamos retornar os anuncio para os usuarios?

500k imoveis na base
2m buscas por dia
200ms de latencia por busca
taxa de agendamento de visitas
CTR

Metricas:
Entendi, entao o problema é rankear os imoveis com maior relevancia para os usuarios nao logados, entao
logicamente usaremos aqui um modelo de ranking.

Acho que algumas metricas de evaluation que podemos medir para ver a qualidade seria o NDGC, 
onde a gente consegue medir quais se os top K itens retornados realmente sao os itens mais relavantes

Dados:
Ai a gente comeca a falar de montar todo o material offline para o treinamento do modelo em si.
Para isso, acredito que a gente pode quebrar isso em 3-4 grupos:
imoveis(endereco, quartos, preco, banheiro, tamanho, foto etc)
usuari


Features:

Modelo:

Serving:

Monitoramento
