class Carro():

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.__velocidade = 0

    def descricao(self):
        return f" Ano:{self.ano} marca:{self.marca} modelo:{self.modelo}"
    

    def acelerar(self, valor):
        self.__velocidade += valor


    @property
    def velocidade(self):
        return self.__velocidade
    
    
    @velocidade.setter
    def velocidade(self, valor):
        self.__velocidade = valor



class CarroEsportivo(Carro):

    def __init__(self, marca, modelo, ano, velocidadeMaxima):
       super().__init__(marca, modelo, ano)
       self.velocidadeMaxima = velocidadeMaxima
        
    def descricao(self):
        return super().descricao() + f" e tem velocidade máxima de {self.velocidadeMaxima}"
      


  
class CarroSedan(Carro):

    def __init__(self, marca, modelo, ano, tamanhoPortaMalas):
        super().__init__(marca, modelo, ano)
        self.tamanhoPortaMalas = tamanhoPortaMalas

    def descricao(self):
        return super().descricao() + f" e tem capacidade de {self.tamanhoPortaMalas} litros"
      


carro1 = CarroEsportivo("Honda", "Civic", "2003", "240")

carro1.acelerar(20)
carro1.acelerar(120)

carro1.velocidade = 250

print(carro1.velocidade)

# print(carro1.obterVelocidade())


# print(carro1.descricao())

carro2 = CarroSedan("VW", "Voyage", 2020, 380)
carro2.acelerar(20)

# print(carro2.descricao())

print("Fim")