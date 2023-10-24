class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descricao(self):
        return f"Este é um {self.marca} {self.modelo}"


meu_carro = Carro("Toyota", "Corolla")
print(meu_carro.descricao())

