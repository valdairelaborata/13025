class Veiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):    
        self.__marca = marca

    @marca.getter
    def marca(self):    
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
    
    @modelo.getter
    def modelo(self):
        return self.__modelo


    def descricao(self):
        return f"Esse é um {self.__marca} do modelo {self.__modelo}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, portaMalas):
        super().__init__(marca, modelo)
        self.__portaMalas = portaMalas

    @property
    def portaMalas(self):
        return self.__portaMalas
    
    @portaMalas.getter
    def portaMalas(self):
        return self.__portaMalas
    
    @portaMalas.setter
    def portaMalas(self, volume):
        self.__portaMalas = volume

    def descricao(self):
        print(f"{super().descricao()} com capacidade de {self.portaMalas} litros" )



class Moto(Veiculo):    
    def __init__(self, marca, modelo, guidao):
        super().__init__(marca, modelo)
        self.__guidao = guidao


    @property
    def guidao(self):
        return self.__guidao
    
    @guidao.getter
    def guidao(self):
        return self.__guidao

    def descricao(self):
        print(f"{super().descricao()} com guidão {self.guidao}" )


class Caminhao(Veiculo):    
    def __init__(self, marca, modelo, engate):
        super().__init__(marca, modelo)
        self.__engate = engate

    @property
    def engate(self):
        return self.__engate
    
    @engate.getter
    def engate(self):
        return self.__engate

    def descricao(self):
       print(f"{super().descricao()} com engate {self.engate}" )


meu_carro = Carro("Honda", "Civic", 350)
meu_carro.marca = "VW"
meu_carro.descricao()

minha_moto = Moto("Honda", "125", "curvo médio")
minha_moto.marca = "xptoAlterado"
minha_moto.descricao()

meu_caminhao = Caminhao("Scania", "xpto0150", "Engate 0500")
meu_caminhao.marca = "Scania alterado a marca"
meu_caminhao.descricao()

print("Fim!")