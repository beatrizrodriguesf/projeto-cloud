from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel

class User(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key=True) 
    name: str
    email: str
    senha: str

class Login(SQLModel):
    email: str
    senha: str

class CommonHeaders(BaseModel):
    jwt: str