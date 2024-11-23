# API Restfull com Postgres

API com endpoints para cadastro de um novo usuário, login e consulta. A consulta é da informação da temperatura máxima e mínima da cidade de São Paulo no dia, para realizá-la o usuário deverá estar autenticado. O token para autenticação pode ser obtido na requisição de cadastro ou login. 

## Publicação no Docker Hub

Foi feita a publicação da imagem da API no docker hub. Dessa forma, a aplicação pode ser executada por meio do comando `docker compose up`. Os passos utilizados estão descritos na sessão.

## Disponibilização na AWS

A aplicação foi publicada na AWS e está disponível em : `http://a2bba3ecd5f6445868ac3407a8fdc70d-132096921.us-east-1.elb.amazonaws.com`. Os endpoints também podem ser testados por meio da interface do FastAPI. Os passos utilizados estão descritos na sessão.
