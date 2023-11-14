from sqlalchemy import create_engine
from models.cliente import Base, Cliente
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///pedidos.db"

engine =  create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def incluir(nome, email):
    db = SessionLocal()
    novo_cliente = Cliente(nome=nome, email=email)
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    db.close()

def buscar_por_nome(nome):
    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.nome == nome).first()
    if cliente:
        print(f'Olá, eu sou o cliente {cliente.id} - {cliente.nome} - {cliente.email}')
    else:
        print(f"Cliente não encontrado com o nome - {nome}")
    db.close()

def excluir(id):
    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    db.delete(cliente)
    db.commit()
    db.close()


def alterar(id, nome, email):
    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    cliente.nome = nome
    cliente.email = email
    db.commit()
    db.close()
