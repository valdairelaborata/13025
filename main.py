# Configure a URL de conexão com o banco de dados
# Para SQLite (banco de dados em arquivo):


from sqlalchemy import create_engine


DATABASE_URL = "sqlite:///pedidos.db"

engine =  create_engine(DATABASE_URL)