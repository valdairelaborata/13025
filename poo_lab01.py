class Carro:

    def __init__(self, marca, modelo) :
        self.marca = marca
        self.modelo = modelo

    def descricao(self):
        return f"Marca {self.marca}, modelo {self.modelo}"
        


meuCarro = Carro("Honda", "Civic 2003")
print(meuCarro.descricao())