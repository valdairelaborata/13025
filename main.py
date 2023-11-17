from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return f"Root da aplicação."

@app.get("/clientes")
def listar():
    return f"Opa, chegou aqui!"

@app.post("/clientes")
def incluir():
    return f"Registro incluído com sucesso!"

@app.put("/clientes")
def incluir():
    return f"Registro alterado com sucesso!"

@app.delete("/clientes")
def incluir():
    return f"Registro excluído com sucesso! "