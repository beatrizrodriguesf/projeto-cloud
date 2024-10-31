import jwt
from fastapi import FastAPI, Header, HTTPException, Depends
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
        hashed_password = get_password_hash(user.password) # Faz hash da senha
        new_user = User(
            email=user.email,
            name=user.name,
            password=hashed_password,
        )
        session.add(new_user) # cria novo user
        session.commit()
        session.refresh(new_user)

        # Cria jwt
        payload = {"email": new_user.email}
        encoded_jwt = jwt.encode(payload, key, algorithm="HS256")
        return encoded_jwt
    else:
        # Se o email já está cadastrado, retorna um erro
        raise HTTPException(status_code=409, detail=f"Email já cadastrado")

@app.post("/login", status_code=200)
def login(login: Login, session: SessionDep):
    # Busca usuário no banco de dados
    existent_user = session.scalar(select(User).where(User.email == login.email))

    if existent_user:
        hashed_password = existent_user.password
        if (verify_password(login.password, hashed_password)):
            payload = {"email" : existent_user.email}
            encoded_jwt = jwt.encode(payload, key, algorithm="HS256")
            return encoded_jwt
        else:
            raise HTTPException(status_code=401, detail=f"Senha não confere")
    else:
        raise HTTPException(status_code=401, detail=f"Email não encontrado")


@app.get("/consultar", status_code = 200)
def consultar(headers: Annotated[CommonHeaders, Header()]):
    try:
        jwt.decode(headers.jwt, key, algorithms=["HS256"])
        return(get_day_temp_sp())
    except:
        raise HTTPException(status_code=401, detail=f"Token inválido")