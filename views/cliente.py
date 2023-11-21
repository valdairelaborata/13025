from pydantic import BaseModel

class ClienteView(BaseModel):
    nome: str
    email: str