class ContaBancaria:

    def __init__(self, saldo, titular) :
        self.__saldo = saldo
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo
    

    # @saldo.setter
    # def saldo(self, valor):
    #     self.__saldo = valor
    

    def depositar(self, valor):
        self.__saldo += valor


    def sacar(self, valor):
        self.__saldo -= valor


    def trocarTitular(self, titular):
        self.__titular = titular

    
    def detalhes(self):
        return f'Conta do titular:{self.__titular}, com  saldo de:{self.__saldo}'


conta01 = ContaBancaria(0, 'Valdair')
print(conta01.detalhes())

conta01.depositar(20)
conta01.sacar(15)
print(conta01.detalhes())

conta01.trocarTitular('João')
print(conta01.detalhes())

conta01.depositar(200)
conta01.sacar(150)
print(conta01.detalhes())



