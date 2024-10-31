from classes import User, Login
from sqlmodel import SQLModel, Session, select, create_engine

# Configurações
user = "projeto"
password = "projeto"
host = "db:5432"
database = "projeto"

sqlite_url = f"postgresql://{user}:{password}@{host}/{database}"

engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session