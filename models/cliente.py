from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)    
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)






