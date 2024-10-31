import jwt
from fastapi import FastAPI, Header, HTTPException, Depends, Security
from fastapi.security.api_key import APIKeyHeader
from classes import *
from typing import Annotated
from sqlmodel import Session, select
from database import get_session
from hashfunctions import get_password_hash, verify_password
from consulta import get_day_temp_sp

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()
key = "CL@ud0"

@app.post("/registrar", status_code=201)
def create_user(user: User, session: SessionDep):

    # Verifica se o email já está no banco de dados
    select_user = select(User).where(User.email == user.email)
    existent_user = session.exec(select_user).all()

    if not existent_user:
        hashed_password = get_password_hash(user.senha) # Faz hash da senha
        new_user = User(
            email=user.email,
            name=user.name,
            senha=hashed_password,
        )
        session.add(new_user) # cria novo user
        session.commit()
        session.refresh(new_user)

        # Cria jwt
        payload = {"email": new_user.email}
        encoded_jwt = jwt.encode(payload, key, algorithm="HS256")
        json_jwt = {"jwt": f"{encoded_jwt}"}
        return json_jwt
    else:
        # Se o email já está cadastrado, retorna um erro
        raise HTTPException(status_code=409, detail=f"Email já cadastrado")

@app.post("/login", status_code=200)
def login(login: Login, session: SessionDep):
    # Busca usuário no banco de dados
    existent_user = session.scalar(select(User).where(User.email == login.email))

    if existent_user:
        hashed_password = existent_user.senha
        if (verify_password(login.senha, hashed_password)):
            payload = {"email" : existent_user.email}
            encoded_jwt = jwt.encode(payload, key, algorithm="HS256")
            json_jwt = {"jwt": f"{encoded_jwt}"}
            return json_jwt
        else:
            raise HTTPException(status_code=401, detail=f"Senha incorreta")
    else:
        raise HTTPException(status_code=401, detail=f"Email não encontrado")


@app.get("/consultar", status_code = 200)
def consultar(Authorization: str=Security(APIKeyHeader(name="Authorization"))):
    bearer_token = Authorization.split(' ')
    if len(bearer_token) < 2:
        raise HTTPException(status_code=403, detail=f"Formato do authorization deve ser: Bearer token")
    try:
        token = bearer_token[1]
        jwt.decode(token, key, algorithms=["HS256"])
        info_json = {"info": f"{get_day_temp_sp()}"}
        return info_json
    except:
        raise HTTPException(status_code=403, detail=f"Token inválido")