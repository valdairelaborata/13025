from fastapi import FastAPI
from pydantic import BaseModel


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

@app.get("/clientes/{id}")
def listar(id):
    return f"Opa, chegou aqui! {id}"

@app.post("/clientes")
def incluir(clienteView: ClienteView):
    # consumir um service
    return f"Registro incluído com sucesso! Nome: {clienteView.nome} - email: {clienteView.email}"

@app.put("/clientes")
def alterar():
    return f"Registro alterado com sucesso!"

@app.delete("/clientes")
def excluir():
    return f"Registro excluído com sucesso! "