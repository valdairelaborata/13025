from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from services.cliente import atualizar, buscar_todos, incluir, buscar_por_id, remover
from services.infra import get_db
from views.cliente import ClienteView


app = FastAPI()
  

@app.get("/")
def root():
    return f"Root da aplicação."

@app.get("/clientes")
def listar(db: Session = Depends(get_db)):
    return buscar_todos(db)

@app.get("/clientes/{id}", response_model = ClienteView)
def listar(id, db: Session = Depends(get_db)):
    return buscar_por_id(id, db)

@app.post("/clientes")
def salvar(clienteView: ClienteView, db: Session = Depends(get_db)):
    incluir(clienteView.nome, clienteView.email, db)

    return f"Registro incluído com sucesso! Nome: {clienteView.nome} - email: {clienteView.email}"

@app.put("/clientes/{id}")
def alterar(id, clienteView: ClienteView, db: Session = Depends(get_db)):
    atualizar(id, clienteView, db)
    return f"Registro alterado com sucesso!"

@app.delete("/clientes/{id}")
def excluir(id, db: Session = Depends(get_db)):
    remover(id, db)
    return f"Registro excluído com sucesso! "