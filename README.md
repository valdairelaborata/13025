1 - Cria o ambiente virtual
python -m venv api

2 - Ativar o ambiente virtual
Acionar o script [.\Scripts\activate] que está dentro do ambiente virtual

3 - Instalar dependências
pip install sqlalchemy
pip install fastapi
pip install uvicorn

4 - Iniciar api
uvicorn main:app --reload

5 - Acessar documentação da api
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc