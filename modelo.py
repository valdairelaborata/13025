from sqlalchemy import Integer, String, column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    id = column(Integer, primary_key=True, index=True)
    nome = column(String, index=True)
    email = column(String, unique=True, index=True)






