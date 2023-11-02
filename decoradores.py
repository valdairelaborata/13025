class ContaBancaria:

    def __init__(self, numero):
        self.__numero = numero

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero


conta = ContaBancaria('321321')
conta.numero = '64645'

print(conta.numero)