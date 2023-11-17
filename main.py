from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from services.cliente import incluir, buscar_por_id


app = FastAPI()


class ClienteView(BaseModel):
    nome: str
    email: str
    

@app.get("/")
def root():
    return f"Root da aplicação."

@app.get("/clientes")
def listar():
    return f"Opa, chegou aqui!"

@app.get("/clientes/{id}", response_model = ClienteView)
def listar(id):
    return buscar_por_id(id)

@app.post("/clientes")
def salvar(clienteView: ClienteView):#, db: Session = Depends(get_db)):
    incluir(clienteView.nome, clienteView.email)

    return f"Registro incluído com sucesso! Nome: {clienteView.nome} - email: {clienteView.email}"

@app.put("/clientes")
def alterar():
    return f"Registro alterado com sucesso!"

@app.delete("/clientes")
def excluir():
    return f"Registro excluído com sucesso! "