# Projeto de Cloud

## Nome: Beatriz Rodrigues de Freitas

### Projeto:

API desenvolvida utilizando FastAPI e conectada com o postgresql. Permite cadastro e login do usuário, e a consulta da temperatura máxima e mínima da cidade de São Paulo no dia. As informações da consulta foram obtidas através de um web scraping. A fonte foi a página do G1 de previsão de tempo da cidade de São Paulo (https://g1.globo.com/previsao-do-tempo/sp/sao-paulo.ghtml) e é atualizada diariamente.

### Publicação no Dockerhub:

Para a publicação da imagem da API no dockerhub, foi criado um repositório (api-image). Após isso, foi executado o comando abaixo dentro da pasta app, onde está localizado o arquivo Dockerfile. O comando utilizado realiza a criação e publicação da imagem tanto para Windows quando para Linux.

`docker buildx build --platform linux/arm64,linux/amd64 --push -t beatrizrodriguesf/api-image .`

Link da imagem no dockerhub: https://hub.docker.com/r/beatrizrodriguesf/api-image

### Execução da aplicação:

Para executar a aplicação basta clonar o repositório e executar o comando abaixo na raiz do repositório, onde está localizado o arquivo **compose.yaml**.

`docker compose up`

Como foi definido no compose.yaml, a conexão com a aplicação se dará pela porta 8000. Dessa forma, as requisições serão feitas partindo de localhost:8000.

### Endpoints da API:

- /registrar : post para criar usuário
- /login : post para fazer o login do usuário
- /consultar : get de informação do web scrapping