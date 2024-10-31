# Projeto de Cloud

## Nome: Beatriz Rodrigues de Freitas

### Projeto:

API desenvolvida utilizando FastAPI e conectada com o postgresql. A imagem da API está publicada no docker hub, o projeto final, API + banco de dados foi dockerizado.

### Endpoints da API:

- /registrar : post para criar usuário
- /login : post para fazer o login do usuário
- /consultar : get de informação do web scrapping

### Web scrapping:

Foi feito um scrapping da página do g1 contendo a previsão do tempo de são paulo. A informação retornada pelo endpoint de consulta terá a temperatura máxima e mínima de São Paulo.

### Execução da aplicação:

Para executar a aplicação basta clonar o repositório e executar o comando:

`docker compose up`

O arquivo compose.yaml está na raiz do repositório, logo, o comando acima deve ser executado na raiz do repositório.

A conexão com a aplicação se dará pela porta 8000.
