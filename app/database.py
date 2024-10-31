from classes import User, Login
from sqlmodel import SQLModel, Session, select, create_engine
from dotenv import load_dotenv
import os

# Configurações contidas no .env
load_dotenv()
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
database = os.getenv("POSTGRES_DB")
host = "db:5432"

# Configurações
# user = "projeto"
# password = "projeto"
# host = "db:5430"
# atabase = "projeto"

sqlite_url = f"postgresql+psycopg2://{user}:{password}@{host}/{database}"

engine = create_engine(sqlite_url)
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session