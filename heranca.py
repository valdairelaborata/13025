class Carro():

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f" Ano:{self.ano} marca:{self.marca} modelo:{self.modelo}"
    


class CarroEsportivo(Carro):

    def __init__(self, marca, modelo, ano, velocidadeMaxima):
       super().__init__(marca, modelo, ano)
       self.velocidadeMaxima = velocidadeMaxima
        
    def descricao(self):
        return super().descricao() + f" e tem velocidade máxima de {self.velocidadeMaxima}"
      

   


carro1 = CarroEsportivo("Honda", "Civic", "2003", "240")
print(carro1.descricao())

carro2 = CarroEsportivo("asd", "asd", "asd", "44")

print("Fim")