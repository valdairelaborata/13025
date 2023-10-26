class Carro:
    def __init__(self, cor, tanque = 0):
        self.__cor = cor
        self.__tanque = tanque

    
    # def set_cor(self, cor):
    #     self.__cor = cor

    # def get_cor(self):
    #     return self.__cor
    

    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @cor.getter
    def cor(self):
         return self.__cor

    @property
    def tanque(self):
        return self.__tanque
      
    @tanque.getter
    def tanque(self):
         return self.__tanque  

    def abastecer(self, volume):
        self.__tanque += volume


meu_carro = Carro("Preta")
meu_carro.abastecer(50)
print(meu_carro.tanque)

meu_carro.set_cor("Azul")

meu_carro.cor = "Azul"

print(meu_carro.cor)


print(meu_carro.get_tanque())
meu_carro.abastecer(60)
print(meu_carro.get_tanque())

print("Fim!")




# meu_carro = Carro("Preta")
# print(meu_carro.get_cor())
# meu_carro.set_cor("Azul")

# meu_carro.abastecer(50)

# print(meu_carro.get_cor())
# print(meu_carro.get_tanque())

# meu_carro.abastecer(500)

# print(meu_carro.get_tanque())